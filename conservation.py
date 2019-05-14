from time import sleep
import requests
import json


def get_message(message):
    test = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": message
            },
            "selfInfo": {
                "location": {
                    "city": "北京",
                    "province": "北京",
                    "street": "信息路"
                }
            }
        },
        "userInfo": {
            "apiKey": "a56db8d95cd54524922d9f86d046ef13",
            "userId": "234"
        }
    }
    return json.dumps(test)


def tuling_reply(msg):
    reply = get_message()


questions = input("请输入话题：")
flag = 1
TULING = '海增'
MOLI = '梦梦'
# print(TULING+':'+question)          #导火索  哈哈
while True:
    #图灵
    """
    tuling_data = {
        "key": "5da047a95db8450ea6e710dd065d4be4",
        "info": question,
        "userid": "272872"
    }
    tuling_api_url = 'http://www.tuling123.com/openapi/api'
    t = requests.post(tuling_api_url, data=tuling_data) #post请求

    print(TULING+':'+eval(t.text)["text"]) #用eval函数处理一下图灵返回的消息
    question = eval(t.text)["text"]     #重置question —>让茉莉回答
    """
    #梦
    """ 
    moli_api_url = 'http://www.tuling123.com/openapi/api'       #api地址
    moli_data = {
        "key": "a56db8d95cd54524922d9f86d046ef13",
        "info": question,
        "userid": "2723423"
    }
    m = requests.post(moli_api_url, data = moli_data).json()
    print(MOLI + "："+m.get("text"))
    """

    """
    sleep(1)        # 设置循环延迟
    conservation = get_message(questions)
    x = requests.post(url="http://openapi.tuling123.com/openapi/api/v2", data=conservation).json()
    # print(x)
    questions = x['results'][0]['values']['text']
    # print(questions)
    if flag == 1:
        print("小明: " + x['results'][0]['values']['text'])
        flag = 0
    else:
        print("小红: " + x['results'][0]['values']['text'])
        flag = 1
    questions = x['results'][0]['values']['text']
    """