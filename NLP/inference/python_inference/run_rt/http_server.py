# -*- coding: utf-8 -*-
import json
import re
import sys
if sys.version_info<(3, 0):
    from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler  #导入HTTP处理相关的模块
else :
    from http.server import HTTPServer, BaseHTTPRequestHandler 
    from socketserver import ThreadingMixIn
#import os
#os.environ["CUDA_VISIBLE_DEVICES"] = '1'
from infer import prepare, inference
# import pdb

# 参数设置，与打包的模型结构有关，模型不变不用改
engine_model_path = "/workspace/results/bert_static_16.trt"
premodel_path = "/workspace/pre_model/chinese-xlnet-base"
batch_size = 1
max_length = 1024
# 输出结果中数字和分类结果对应
digit2str = {
    0 : '诈骗',
    1 : '涉政',
    2 : '走私偷渡',
    3 : '宗教',
    4 : '其它'
}
remap = {
	ord('佢') : '他',
	ord('乜') : '什么',
ord('嘅') : '的',
ord('嬲') : '操',
ord('系') : '是',
ord('咁') : '这样',
ord('哋') : '们',
ord('唔') : '不是',
ord('睇') : '看',
ord('啲') : '的',
ord('冧') : '陶醉',
    ord('冇') : '没有',
ord('惗') : '想',
    ord('嘎') : '',
ord('咩') : '什么',
ord('嗻') : '',
ord('嗟') : '',
ord('嚟') : '来',
ord('叻') : '棒',
ord('喱') : '那',
ord('咪') : '不要',
ord('梗') : '当然',
ord('喺') : '在',
	ord('抦') : '打',
	ord('啵') : '',
ord('俾') : '给',
ord('嘈') : '吵',
ord('噏') : '唠叨',
ord('噏') : '扔',
ord('嘞') : '',
ord('靓') : '漂亮',
ord('囖') : '',
ord('揾') : '找',
ord('嗮') : '浪费',
    ord('攞') : '拿',
ord('嘥') : '浪费',
    ord('摞') : '拿',
ord('咗') : '了',
ord('喔') : '',
ord('疴') : '拉',
ord('拗') : '矛盾',
ord('乸') : '雌性',
ord('啖') : '口',
ord('憇') : '哄',
ord('呃') : '骗',
ord('掂') : '完',
ord('唓') : '',
ord('嘢') : '东西',
ord('噉') : '吃',
ord('瞓') : '睡',
ord('係') : '是',
ord('㖞') : '',
ord('嗰') : '那',
ord('畀') : '给'
}
zstd_keys=['番薯','外伶仃','淇澳','上岸','蛇头','车夫','蛇仔','猪仔','蛇仔','骑师','孖机','大飞','拜神','派片','冰库',
           '厕所位','常州','抄码','车过嚟','车过去','去吃奶','打灯','电筒','鼎船','屙尿','屙屎','瘟神','机场尾','鸡翼角','进货',
           '靓唔靓','喇妈','烂角咀','老細','龙门架','中记','孖机','走货','海警','货未到']
zstd_keys2=['纯净水','饭堂','棍','珠海','仓库']
zstd_keys3=['香港','澳门','珠海','半夜','猪肉','吃饱','定位','加水','开饭','纯净水']
zp_keys=['退费','加一下我','加群','刷单','卡单','直播课','返利','无抵押','免征信','快速放贷','保证金','代办','理赔退款','重新激活',
         '安全账户','逮捕证','冻结','个人征信','对接账户','贷款app','贷款APP','海外代购','0元购物','论文代写','私家侦探','跟踪定位',
         '交易税','关税','手续费','定金','总经理','解冻','注册费','会员费']
zj_key=['佛','菩萨','业障','法轮','三退','退党','基督','教主','先知','真主','我主']
pattern_zstd = re.compile('|'.join(zstd_keys))
pattern_zstd2 = re.compile('|'.join(zstd_keys2))
pattern_zstd3 = re.compile('|'.join(zstd_keys3))
pattern_zp = re.compile('|'.join(zp_keys))
pattern_zj = re.compile('|'.join(zj_key))

# 获取推理所需的推理框架,只需要执行一次
threadNums = 5
workThreadNum = [0]
tokenizers = []
contexts = []
inputs = []
outputs = []
bindings = []
streams = []
for i in range(threadNums):
    tokenizer, context, input, output, binding, stream = prepare(engine_model_path, premodel_path,
                                                batch_size, max_length)
    tokenizers.append(tokenizer)
    contexts.append(context)
    inputs.append(input)
    outputs.append(output)
    bindings.append(binding)
    streams.append(stream)

# 送入推理框架和输入到inference_function中，只要推理框架没有变动，可以反复执行，送入不同的输入，输出为list[int,int...,int]，长度和输入等长（64）
# pred = inference(sentence1, tokenizer, context, input, output, bindings, stream)
def infer(sentences,tokenizer,context,input,output,binding,stream):
    # sentences_size = len(sentences)
    # print("input engine sentences_size[{}]".format(sentences_size))
    results = []
    # do inference
    zstd_score=len(pattern_zstd.findall(sentences))+0.5*len(pattern_zstd2.findall(sentences))+0.25*len(pattern_zstd3.findall(sentences))
    zp_score = len(pattern_zp.findall(sentences))
    zj_score = len(pattern_zj.findall(sentences))
    if zj_score >= 1:
        str_results='宗教'
    elif zp_score >= 1:
        str_results = '诈骗'
    elif zstd_score>= 1:
        str_results = '走私偷渡'
    else:
        results = inference(sentences.translate(remap), tokenizer, context, input, output, binding, stream)
        # print("engine output results_size[{}]".format(len(results)))
        # str_results = []
        # 不足一个batch_size时，只取前sentances_size个推理结果返回
        str_results=digit2str[results[0]]
        # print("output str_results_size[{}]".format(len(str_results)))
    return str_results

#自定义处理程序，用于处理HTTP请求  
class HTTPHandler(BaseHTTPRequestHandler):

    # # 获取推理所需的推理框架,只需要执行一次
    # threadNums = 5
    # workThreadNum = [0]
    # tokenizers = []
    # contexts = []
    # inputs = []
    # outputs = []
    # bindings = []
    # streams = []
    # for i in range(threadNums):
    #     tokenizer, context, input, output, binding, stream = prepare(engine_model_path, premodel_path,
    #                                                 batch_size, max_length)
    #     tokenizers.append(tokenizer)
    #     contexts.append(context)
    #     inputs.append(input)
    #     outputs.append(output)
    #     bindings.append(binding)
    #     streams.append(stream)

        
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
        
        # sentences = ''
        sentences = []
        for line in data['texts']:
            if len(line) != 2:
                continue
            # sentences.append(line[1])
            if len(sentences) > 0:
                sentences[0] += line[1]
            else:
                sentences.append(line[1])
            # sentences += line[1]
        
        # lock ??
        ids = workThreadNum[0] = (workThreadNum[0] + 1) % threadNums
        # unlock
        
        classify_result = infer(sentences,
                            tokenizers[ids],
                            contexts[ids],
                            inputs[ids],
                            outputs[ids],
                            bindings[ids],
                            streams[ids])
        # pdb.set_trace()
        self.do_Resp(json.dumps({'opid': data['opid'], 'engine': data['engine'],
                                 'version': 'classfy_v1.0', 'output': classify_result})
                    )

class ThreadingSimpleServer(ThreadingMixIn,HTTPServer):
    pass

# Http服务
class HttpServer():
    def __init__(self, port):
        self.http_server = ThreadingSimpleServer(('', int(port)), HTTPHandler)
    def start(self):
        self.http_server.serve_forever() #设置一直监听并接收请求  
    def stop(self):
        self.http_server.shutdown()

# demo
# server = HttpServer(8080)
# server.start()
# #server.stop()
