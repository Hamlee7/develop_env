import numpy as np
from transformers import AutoTokenizer
import tensorrt as trt
import common

"""
a、获取 engine，建立上下文
"""
TRT_LOGGER = trt.Logger(trt.Logger.WARNING)


def get_engine(engine_file_path):
    print("Reading engine from file {}".format(engine_file_path))
    with open(engine_file_path, "rb") as f, trt.Runtime(TRT_LOGGER) as runtime:
        engine = runtime.deserialize_cuda_engine(f.read())
        return engine


engine_model_path = "/workspace/results/bert_static_64.trt"
premodel_path = "/workspace/pre_model/chinese-xlnet-base"
# Build a TensorRT engine.
engine = get_engine(engine_model_path)
# Contexts are used to perform inference.
context = engine.create_execution_context()

"""
b、从engine中获取inputs, outputs, bindings, stream 的格式以及分配缓存
"""


def to_numpy(tensor):
    return tensor.detach().cpu().numpy() if tensor.requires_grad else tensor.cpu().numpy()


#sentence = ["荣耀强", '法轮功']*8
sentence = ["中国一年要生产揍叫世界暴光引起民众的恐慌一份怒又打过问题疫苗的受害儿童家长纰漏孩子出现偏瘫编前等症状极品政府隐瞒真相要求头公道。也有大陆家政录制中共统治下道德沦丧已失去信心纷纷转往香港打印哟。七月十五日吉林省长春长生生物公司因为狂犬病疫苗记录造价遭受时要争取通报谁料三天后在公司在披露七百白破疫苗被验出不合格。事件暴光后立即轰动全国一时间疫苗成为引爆名分的最敏感话题而且黑幕越学越多。当心做人难做中国人更难除了区蛮有毒奶粉有毒食品环境污染之外现在还出现有毒一牛直接毒害我们的下一代。当这个社会连小孩子都保护不了这个社会还有和希望还有什么正义和明天。更别说社会上黄赌毒无官不贪黑社会大兴起到。这一切的背后都离不开道德危机诚信为基和信仰危机。听众朋友如果您有问题需要解答性随时按下八号键北京时间早上九点去晚上十点将有专人回拨电话给您通话过程免费。中华古国五千年文明任何一个朝代灭亡时也没有混乱到如今这种地步。中国的今天究竟是谁造成的今天的中国与历史上的各个朝代有什么不同。事实上就是共产党执政之后不停的搞政治运动政风三反五反正反反右文化大革命六四天安门。",
            '河南的朋友好济源市政府为征地建桥出动三百多特警到村庄抢地。与近百村民发生冲突有十多名村民被打伤。最少三人被捕在中国何止是村民有苦不能言。共产党贪污腐败官官相护无视百姓的权益和生命。共产党总是说一套做一套说要让农民有土地。但是强行圈地让百姓没饭吃承诺给工人工厂结果是更多的人下岗。说要社会公平实际却是贪污腐败豺狼横行。说人民要用生命保卫党中央原来是要拉百姓下水当它罪恶下的陪葬品。这样的共产党还能相信他吗目前超过一亿四千多万的人退出共产党共青团少先队。不再相信共产党的谎言远离他的罪恶不做他的陪葬品。天灭中共是天意中国人都知道大义灭亲都知道顺天意不可逆天而行。请把握机缘希望善良的你也能远离共产党的罪恶选择幸福平安祝福您。',
            '其实作业号码通知用户包裹快变成语言月六号位为了解您因请按三用户包括快件到九月后退回了解您殷勤按三。其实专业号码通知用户包括快件将于九月二号退回了解零一请按三用户包括快件将于九月二号退回了姐您殷勤按三。',
            '喂跟我们冲过来比七的如此的冰美国人吃的好吗一切都是比较而一个我比较想自己去考进去看。就看过感受过就不打面色他说都和外全是鼻祖多自然接触的。这是在生日脸蛋。嗯。而且。什么丢人玩意儿。油膜大师欢度赵家人。甲。笨蛋。这下解放了。一。小。嗯大包大人的亲自指挥下泉州光束到除了交通很顺畅。加速西方红太阳升。嗯强国精神病院日常住。中。嗯。稍有常识的人都能看出一九八九。问题。你家。我。性感维尼塞县基金。讲。你爱的是哪个国维尼果吧。他。家属。够罕见透由勒令维尼熊下台。哎。搜索结果居然是这个男人而不是那个男人六百度屁股歪了加速。嗯这下文化斯进了家事。嗯这定九九六奋斗者。加速。嗯。你家冰箱故障的原因找到了。王景别以为我不知道你说的是谁。一张图看懂b站毛左小粉红家属。需求新的水平文物导致诞生。当小粉红的家里真的有一头牛。猪。要回来了。我。加死。当年的轮有毕竟还是图样。加速。好。很难不支持复习就是卖国贼暖金子进口辉瑞疫苗优先安排给赵家宠物够大呀死。把你城市都给你了骆家死了。三。嗯。严不严立马太艳丽了这个家务没有我那时候卡二百斤卖的。十里山路我不换间呢看来习大大还是太谦虚了家属思路。哎。嗯。懂了这就去发朋友圈称赞警察是较真全这样做。这家粪土不让的这样子的。兴盛的标语希望大哥陋习早日脏脏加速。家。然后。星期一。嗯。人人配合外推夹层。这次的幸运儿会训。家属。哎。嗯。嗯。喂。后浪义和团缅怀前浪义和团。考验诚实的衣服抽象画。你这是充满恶意的问题吧。简单健康也有从他一场栋家属。惧你用着美丽风景线。家属。心情台服密码失效了吗。用你家属。不知道。你刷个碗也卷起来了。假如人口数据延迟发布逼战评论区。家属看一下。快进键。点赞点赞点赞。与非网络。与非网络。哎我是先把文保区法院人家请带好你的口罩海竿将您的红色不够注意稍微起来凑合穿单。大爱的漏工地他爬起。'
            ]*16
tokenizer = AutoTokenizer.from_pretrained(premodel_path)
tokenizer.padding_side = 'right'
inputs = tokenizer.batch_encode_plus(sentence, return_tensors='pt', add_special_tokens=True,max_length=1024 ,padding='max_length', truncation=True)

tokens_id = to_numpy(inputs['input_ids'].int())
attention_mask = to_numpy(inputs['attention_mask'].int())
token_type_ids = to_numpy(inputs['token_type_ids'].int())

context.active_optimization_profile = 0
origin_inputshape = context.get_binding_shape(0)  # (1,-1)
origin_inputshape[0], origin_inputshape[1] = tokens_id.shape  # (batch_size, max_sequence_length)
context.set_binding_shape(0, (origin_inputshape))
context.set_binding_shape(1, (origin_inputshape))

"""
c、输入数据填充
"""
inputs, outputs, bindings, stream = common.allocate_buffers_v2(engine, context)
inputs[0].host = tokens_id
inputs[1].host = token_type_ids
inputs[2].host = attention_mask

"""
d、tensorrt推理
"""
import time
while 1:
    time1 = time.time()
    trt_outputs = common.do_inference_v2(context, bindings=bindings, inputs=inputs, outputs=outputs, stream=stream)
    preds = np.argmax(np.array(trt_outputs).reshape(-1,4), axis=1)
    time2 = time.time()
    #print("====sentence=:", sentence)
    print("====preds====:", preds)
    print("====use time:=", time2 - time1)
