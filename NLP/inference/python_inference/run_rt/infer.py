import numpy as np
from transformers import AutoTokenizer
import tensorrt as trt
import common

"""
a、获取 engine，建立上下文
"""
TRT_LOGGER = trt.Logger(trt.Logger.WARNING)

def to_numpy(tensor):
    return tensor.detach().cpu().numpy() if tensor.requires_grad else tensor.cpu().numpy()

def get_engine(engine_file_path):
    print("Reading engine from file {}".format(engine_file_path))
    with open(engine_file_path, "rb") as f, trt.Runtime(TRT_LOGGER) as runtime:
        engine = runtime.deserialize_cuda_engine(f.read())
        return engine

def prepare(engine_model_path,premodel_path,batch_size,max_length=1024):
    # engine_model_path = "/workspace/results/bert_static_64.trt"
    # premodel_path = "/workspace/pre_model/chinese-xlnet-base"
    # Build a TensorRT engine.
    engine = get_engine(engine_model_path)

    # Contexts are used to perform inference.
    context = engine.create_execution_context()
    context.active_optimization_profile = 0
    origin_inputshape = context.get_binding_shape(0)  # (1,-1)
    origin_inputshape[0], origin_inputshape[1] = batch_size,max_length  # (batch_size, max_sequence_length)
    context.set_binding_shape(0, (origin_inputshape))
    context.set_binding_shape(1, (origin_inputshape))

    inputs, outputs, bindings, stream = common.allocate_buffers_v2(engine, context)
    tokenizer = AutoTokenizer.from_pretrained(premodel_path,use_fast=True)
    tokenizer.padding_side = 'right'
    return tokenizer, context, inputs, outputs, bindings, stream


def inference(sentence, tokenizer, context, inputs, outputs, bindings, stream):
    input = tokenizer.batch_encode_plus(sentence, return_tensors='pt', add_special_tokens=True, max_length=1024,
                                        padding='max_length', truncation=True)
    tokens_id = to_numpy(input['input_ids'].int())
    attention_mask = to_numpy(input['attention_mask'].int())
    token_type_ids = to_numpy(input['token_type_ids'].int())
    inputs[0].host = tokens_id
    inputs[1].host = token_type_ids
    inputs[2].host = attention_mask
    # import time
    # time1 = time.time()
    trt_outputs = common.do_inference_v2(context, bindings=bindings, inputs=inputs, outputs=outputs, stream=stream)
    preds = np.argmax(np.array(trt_outputs).reshape(-1, 4), axis=1)
    # time2 = time.time()
    # print("====sentence=:", sentence)
    # print("====preds====:", preds)
    # print("====use time:=", time2 - time1)
    return preds
