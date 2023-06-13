bs=64
./TensorRT-8.6.1.6/bin/trtexec \
  --onnx=./results/bert_static.onnx \
  --saveEngine=./results/bert_static_64.trt \
  --workspace=14000 \
  --fp16 \
#  --minShapes='input_ids':${bs}x3,'token_type_ids':16x3,'attention_mask':16x3 \
#  --optShapes='input_ids':64x1024,'token_type_ids':16x1024,'attention_mask':16x1024 \
#  --maxShapes='input_ids':64x1024,'token_type_ids':16x1024,'attention_mask':16x1024
