import os
os.environ["CUDA_VISIBLE_DEVICES"] = '1'
from infer import prepare, inference

# 输入len(sentence)=64，可以输入空字符[str1,str2,...,'']
# [a,b]*2=[a,b,a,b]为简化写法
sentence1 = [
                "中国一年要生产揍叫世界暴光引起民众的恐慌一份怒又打过问题疫苗的受害儿童家长纰漏孩子出现偏瘫编前等症状极品政府隐瞒真相要求头公道。也有大陆家政录制中共统治下道德沦丧已失去信心纷纷转往香港打印哟。七月十五日吉林省长春长生生物公司因为狂犬病疫苗记录造价遭受时要争取通报谁料三天后在公司在披露七百白破疫苗被验出不合格。事件暴光后立即轰动全国一时间疫苗成为引爆名分的最敏感话题而且黑幕越学越多。当心做人难做中国人更难除了区蛮有毒奶粉有毒食品环境污染之外现在还出现有毒一牛直接毒害我们的下一代。当这个社会连小孩子都保护不了这个社会还有和希望还有什么正义和明天。更别说社会上黄赌毒无官不贪黑社会大兴起到。这一切的背后都离不开道德危机诚信为基和信仰危机。听众朋友如果您有问题需要解答性随时按下八号键北京时间早上九点去晚上十点将有专人回拨电话给您通话过程免费。中华古国五千年文明任何一个朝代灭亡时也没有混乱到如今这种地步。中国的今天究竟是谁造成的今天的中国与历史上的各个朝代有什么不同。事实上就是共产党执政之后不停的搞政治运动政风三反五反正反反右文化大革命六四天安门。",
                '河南的朋友好济源市政府为征地建桥出动三百多特警到村庄抢地。与近百村民发生冲突有十多名村民被打伤。最少三人被捕在中国何止是村民有苦不能言。共产党贪污腐败官官相护无视百姓的权益和生命。共产党总是说一套做一套说要让农民有土地。但是强行圈地让百姓没饭吃承诺给工人工厂结果是更多的人下岗。说要社会公平实际却是贪污腐败豺狼横行。说人民要用生命保卫党中央原来是要拉百姓下水当它罪恶下的陪葬品。这样的共产党还能相信他吗目前超过一亿四千多万的人退出共产党共青团少先队。不再相信共产党的谎言远离他的罪恶不做他的陪葬品。天灭中共是天意中国人都知道大义灭亲都知道顺天意不可逆天而行。请把握机缘希望善良的你也能远离共产党的罪恶选择幸福平安祝福您。',
                '其实作业号码通知用户包裹快变成语言月六号位为了解您因请按三用户包括快件到九月后退回了解您殷勤按三。其实专业号码通知用户包括快件将于九月二号退回了解零一请按三用户包括快件将于九月二号退回了姐您殷勤按三。',
                '喂跟我们冲过来比七的如此的冰美国人吃的好吗一切都是比较而一个我比较想自己去考进去看。就看过感受过就不打面色他说都和外全是鼻祖多自然接触的。这是在生日脸蛋。嗯。而且。什么丢人玩意儿。油膜大师欢度赵家人。甲。笨蛋。这下解放了。一。小。嗯大包大人的亲自指挥下泉州光束到除了交通很顺畅。加速西方红太阳升。嗯强国精神病院日常住。中。嗯。稍有常识的人都能看出一九八九。问题。你家。我。性感维尼塞县基金。讲。你爱的是哪个国维尼果吧。他。家属。够罕见透由勒令维尼熊下台。哎。搜索结果居然是这个男人而不是那个男人六百度屁股歪了加速。嗯这下文化斯进了家事。嗯这定九九六奋斗者。加速。嗯。你家冰箱故障的原因找到了。王景别以为我不知道你说的是谁。一张图看懂b站毛左小粉红家属。需求新的水平文物导致诞生。当小粉红的家里真的有一头牛。猪。要回来了。我。加死。当年的轮有毕竟还是图样。加速。好。很难不支持复习就是卖国贼暖金子进口辉瑞疫苗优先安排给赵家宠物够大呀死。把你城市都给你了骆家死了。三。嗯。严不严立马太艳丽了这个家务没有我那时候卡二百斤卖的。十里山路我不换间呢看来习大大还是太谦虚了家属思路。哎。嗯。懂了这就去发朋友圈称赞警察是较真全这样做。这家粪土不让的这样子的。兴盛的标语希望大哥陋习早日脏脏加速。家。然后。星期一。嗯。人人配合外推夹层。这次的幸运儿会训。家属。哎。嗯。嗯。喂。后浪义和团缅怀前浪义和团。考验诚实的衣服抽象画。你这是充满恶意的问题吧。简单健康也有从他一场栋家属。惧你用着美丽风景线。家属。心情台服密码失效了吗。用你家属。不知道。你刷个碗也卷起来了。假如人口数据延迟发布逼战评论区。家属看一下。快进键。点赞点赞点赞。与非网络。与非网络。哎我是先把文保区法院人家请带好你的口罩海竿将您的红色不够注意稍微起来凑合穿单。大爱的漏工地他爬起。'
            ] * 16
sentence2 = [
                "这我跟你说哈共产党没安好心眼只要跟着共产党就会走向火葬场",
                "老公我已经偷渡到深圳了，正在吃宵夜",
                "打倒中国帝国主义打倒东亚病夫",
                ''
            ] * 16
# sentence2 = [
#                 "在全中国还有全世界都非常关心三峡大坝到底安不安全如果你之前去吃鱼三峡大坝安全与否的问题他中国戒严类的否认真的不会有问题但现在他们也承认了。现在这个水他已经超过王红线两公示生活氛围艳两公尺你赶赶快放水呀带不起因为我现在松下有收在业说我现在三亚大包的水如果再上去的话那我底下不是回音的更可怕哇那如果说我把你赌咒我就慢慢消化不行吗不行。。",
#                 '请问是王兰王女士吗。王女士你好我这边是通信管理局我姓陈。这边想请问呃是这边想请问我们通信管理局先前有像你发送两次通知你是没有收到吗。我发个短信。主要是要告知你名下的手机号不要再发送广告短信。那王女士你怎么都没有改善呢。不知道。',
#                 '啊啊嗯嗯嗯。在中国呀可能大多数人都对天法国是吧。在您加入共产党共青团和少先队的时候都曾经举着拳头宣誓说要把自己的一生献给党最等很逗终生。三尺头上有神灵从那个时候起呀您就被打伤了印记这可。',
#                 ''
#             ] * 16
# 参数设置，与打包的模型结构有关，模型不变不用改
engine_model_path = "/workspace/results/bert_static_64.trt"
premodel_path = "/workspace/pre_model/chinese-xlnet-base"
batch_size = 64
max_length = 1024
# 获取推理所需的推理框架,只需要执行一次
tokenizer, context, inputs, outputs, bindings, stream = prepare(engine_model_path, premodel_path, batch_size,
                                                                max_length)
# 送入推理框架和输入到inference_function中，只要推理框架没有变动，可以反复执行，送入不同的输入，输出为list[int,int...,int]，长度和输入等长（64）
pred = inference(sentence1, tokenizer, context, inputs, outputs, bindings, stream)
print(pred)
pred = inference(sentence2, tokenizer, context, inputs, outputs, bindings, stream)
print(pred)
# 输出结果中数字和分类结果对应
# 0：诈骗
# 1：涉政
# 2：走私偷渡
# 3：宗教
# 4：其它
