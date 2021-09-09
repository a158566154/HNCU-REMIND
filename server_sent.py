import requests
from get_cmd import get_data

def server_sent(img):
    

    url = 'https://sctapi.ftqq.com/【server酱密钥】.send?title=电费不足提醒,当前电费剩余{}'.format(img)
    
    return requests.get(url).status_code

