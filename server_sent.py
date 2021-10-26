import requests,json,urllib3
from get_cmd import get_data
urllib3.disable_warnings()


# Corpid是企业ID
Corpid = ""

# Secret是管理组凭证密钥
Secret = ""

# 应用ID
Agentid = ""

# token_config文件放置路径
Token_config = r'./config.json'




###下面的代码都不需要动###
def server_sent(meg):
    

    url = 'https://sctapi.ftqq.com/【server酱密钥】.send?title=电费不足提醒,当前电费剩余{}'.format(meg) #server酱推送url
    
    return requests.get(url).status_code


def GetTokenFromServer(Corpid, Secret):
    """获取access_token"""
    Url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    Data = {
        "corpid": Corpid,
        "corpsecret": Secret
    }
    r = requests.get(url=Url, params=Data, verify=False)
    print(r.json())
    if r.json()['errcode'] != 0:
        return False
    else:
        Token = r.json()['access_token']
        file = open(Token_config, 'w')
        file.write(r.text)
        file.close()
        return Token


def SendMessage(Partyid=1, Subject=None, Content=None):
    """发送消息"""
    # 获取token信息
    try:
        file = open(Token_config, 'r')
        Token = json.load(file)['access_token']
        file.close()
    except:
        Token = GetTokenFromServer(Corpid, Secret)

    # 发送消息
    Url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % Token
    Data = {
        "toparty": Partyid,
        "msgtype": "text",
        "agentid": Agentid,
        "text": {"content": Subject + '\n' + Content},
        "safe": "0"
    }
    data=json.dumps(Data,ensure_ascii=False)
    
    r = requests.post(url = Url,data = data.encode(), verify=False)


    # 如果发送失败，将重试三次
    n = 1
    while r.json()['errcode'] != 0 and n < 4:
        n = n + 1
        Token = GetTokenFromServer(Corpid, Secret)
        if Token:
            Url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % Token
            
            r = requests.post(url=Url, data=json.dumps(Data,ensure_ascii=False), verify=False)
            print(r.json())

    return r.json()
