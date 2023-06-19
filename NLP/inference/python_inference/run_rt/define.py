# encoding=utf-8
print('0. Entry Server**************')
import argparse
import json
# import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import os
os.environ["CUDA_VISIBLE_DEVICES"] = '1'
from infer import prepare, inference
# from infer import Engine

print('1. Imported Module**************')
# 请求:
# {
#     "opid"      : "2354546c0876aaeb2cf9f47c3a2957abcfd",
#     "engine"    : "sxs",
#     "texts"     : 
#     [
#         ["A","这我跟你说哈共产党没安好心眼只要跟着共产党就会走向火葬场"],
#         ["B","老公我已经偷渡到深圳了，正在吃宵夜"],
#         ["A","打倒中国帝国主义打倒东亚病夫"]
#     ]
# }
# 响应:
# {
#     "opid"      : "2354546c0876aaeb2cf9f47c3a2957abcfd",
#     "engine"    : "sxs",
#     "version"   : "classfy_v1.0",
#     "output"    : ["涉政", "走私偷渡", "涉政"]
# }


class RequestData(BaseModel):
    opid : str
    engine : str
    texts : List[List[str]]

print('2. Declare Class**************')

parser = argparse.ArgumentParser()
parser.add_argument('--host', type=str, default='0.0.0.0', help='the host of server for listening')
parser.add_argument('--port', type=int, default=2777, help='the port of server for listening')
parser.add_argument('--log_level', type=str, default='info', help='critical|error|warning|info|debug|trace')
parser.add_argument('--workers', type=int, default=1, help='number of worker processes')
parser.add_argument('--engine_model_path', type=str, default='/workspace/results/bert_static_64.trt', help='the path of model')
parser.add_argument('--premodel_path', type=str, default='/workspace/pre_model/chinese-xlnet-base', help='the path of pretrained model')
parser.add_argument('--batch_size', type=int, default=64, help='the batch size of model')
parser.add_argument('--max_length', type=int, default=1024, help='the max length of sentence')
opt = parser.parse_args()
print('3. Parsed Server Argument**************')
tokenizer, context, inputs, outputs, bindings, stream = prepare(opt.engine_model_path, opt.premodel_path, opt.batch_size, opt.max_length)
# engine = Engine()

app = FastAPI()
print('4. Instanced Engine**************')

# Service: VoiceClassify
# URL: /voice/model/classify
@app.post('/voice/model/classify')
def classify(data: RequestData):
# async def classify(data: RequestData):
    print("opid:{} texts_size:{}".format(data.opid, len(data.texts)))
    sentences = []
    for line in data.texts:
        if len(line) != 2:
            continue
        sentences.append(line[1])
        # text = line[1].encode('utf-8')
        # print("text:{}\n".format(text))
        # sentences.append(text)
    # classify_result = engine.infer(sentences)
    sentences += [''] * (opt.batch_size - len(sentences))
    # global tokenizer
    # global context
    # global inputs
    # global outputs
    # global bindings
    # global stream
    classify_result = inference(sentences, tokenizer, context, inputs, outputs, bindings, stream)
    # classify_result = ["涉政", "走私偷渡", "涉政"]
    return json.dumps({'opid': data.opid, 'engine': data.engine,
                       'version': 'classfy_v1.0', 'output': classify_result})

# def classify(data: RequestData):
# # async def classify(data: RequestData):
#     print("opid:{} texts_size:{}".format(data.opid, len(data.texts)))
#     sentences = []
#     for line in data.texts:
#         if len(line) != 2:
#             continue
#         sentences.append(line[1])
#         # text = line[1].encode('utf-8')
#         # print("text:{}\n".format(text))
#         # sentences.append(text)
#     classify_result = engine.infer(sentences)
#     # classify_result = ["涉政", "走私偷渡", "涉政"]
#     return json.dumps({'opid': data.opid, 'engine': data.engine,
#                        'version': 'classfy_v1.0', 'output': classify_result})
print('5. App instanced**************')


def server_run():
    print('Startup Server**************')
    # uvicorn.run(app='define:app', interface="wsgi", host=opt.host, port=opt.port, log_level=opt.log_level, workers=opt.workers)
    # uvicorn.run(__file__.split('.')[0]+':app', host=opt.host, port=opt.port, log_level=opt.log_level, workers=opt.workers)
