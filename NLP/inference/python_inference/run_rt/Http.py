# -*- coding: utf-8 -*-
import sys
import json
if sys.version_info < (3, 0):
    from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler  #导入HTTP处理相关的模块
else :
    from http.server import HTTPServer, BaseHTTPRequestHandler 
import requests
import os
os.environ["CUDA_VISIBLE_DEVICES"] = '1'
from infer import prepare, inference
# import pdb

# 参数设置，与打包的模型结构有关，模型不变不用改
engine_model_path = "/workspace/results/bert_static_64.trt"
premodel_path = "/workspace/pre_model/chinese-xlnet-base"
batch_size = 64
max_length = 1024
# 输出结果中数字和分类结果对应
digit2str = {
    0 : '诈骗',
    1 : '涉政',
    2 : '走私偷渡',
    3 : '宗教',
    4 : '其他'
}

# 获取推理所需的推理框架,只需要执行一次
tokenizer, context, inputs, outputs, bindings, stream = prepare(engine_model_path, premodel_path,
                                                                batch_size, max_length)

# 送入推理框架和输入到inference_function中，只要推理框架没有变动，可以反复执行，送入不同的输入，输出为list[int,int...,int]，长度和输入等长（64）
# pred = inference(sentence1, tokenizer, context, inputs, outputs, bindings, stream)

def infer(sentences):
    sentences_size = len(sentences)
    print("input engine sentences_size[{}]".format(sentences_size))
    results = []
    # do inference
    if sentences_size < 0:
        return []
    elif sentences_size < batch_size and sentences_size > 0:
        sentences += [''] * (batch_size - sentences_size)
        # pdb.set_trace()
        results = inference(sentences, tokenizer, context, inputs, outputs, bindings, stream)
    elif sentences_size == batch_size:
        results = inference(sentences, tokenizer, context, inputs, outputs, bindings, stream)
    else:
        for i in range((sentences_size / batch_size)):
            begin = batch_size * i
            end = batch_size * (i + 1)
            results.extend(inference(sentences[begin:end], tokenizer, context, inputs, outputs, bindings, stream))
        residue = sentences_size % batch_size
        results.extend(inference(sentences[-residue:], tokenizer, context, inputs, outputs, bindings, stream))

    print("engine output results_size[{}]".format(len(results)))
    str_results = []
    # 不足一个batch_size时，只取前sentances_size个推理结果返回
    for res in results[:sentences_size]:
        if res > 4 or res < 0:
            str_results.append('其他')
        else:
            str_results.append(digit2str[res])
    print("output str_results_size[{}]".format(len(str_results)))
    return str_results

#自定义处理程序，用于处理HTTP请求  
class HTTPHandler(BaseHTTPRequestHandler):

    def do_Reqt(self):
        request = dict()
        # 获取http data
        data = self.rfile.read(int(self.headers['content-length']))
        print("got data:" + data.decode('utf-8'))
        if data:
            request['data'] = data.decode("utf-8", 'ignore')
            '''
            "phone": ["139123456789","139123456789","139123456789"]
            "process": "导航测试流程",
            "taskId ": "sewrwer1234",
            "token": "xxxxxxx"
            '''
            return json.loads(request["data"])
            # return request['data'].json()
        else:
            return None

    def do_Resp(self, json_str):
        self.protocal_version = 'HTTP/1.1'  #设置协议版本  
        self.send_response(200) #设置响应状态码
        self.send_header("Content-Type", "application/json")  #设置响应头  
        self.end_headers()
        if sys.version_info >= (3, 0):  
            json_str = json_str.encode('utf-8')
        # html = json.dumps(html).encode(encoding='utf-8')
        self.wfile.write(json_str)   #输出响应内容

    #处理GET请求  
    def do_GET(self):
        # self.doIndexHtml()
        #获取URL
        print('URL=' + self.path)
        #页面输出模板字符串  
        templateStr = '''
        <html>   
        <head>   
        <title>QR Link Generator</title>   
        </head>   
        <body>   
        hello Client!
        </body>   
        </html>
        '''
        self.do_Resp(templateStr)

    #处理POST请求, 返回reuqest body data of json
    def do_POST(self):
        print('URL=' + self.path)
        data = self.do_Reqt()
        print("opid:{} texts_size:{}".format(data['opid'], len(data['texts'])))
        sentences = []
        for line in data['texts']:
            if len(line) != 2:
                continue
            sentences.append(line[1])

        classify_result = infer(sentences)
        # pdb.set_trace()
        self.do_Resp(json.dumps({'opid': data['opid'], 'engine': data['engine'],
                                 'version': 'classfy_v1.0', 'output': classify_result})
                    )

# Http服务
class HttpServer():
    def __init__(self, port):
        self.http_server = HTTPServer(('', int(port)), HTTPHandler)
    def start(self):
        self.http_server.serve_forever() #设置一直监听并接收请求  
    def stop(self):
        self.http_server.shutdown()

# demo
# server = HttpServer(8080)
# server.start()
# #server.stop()
