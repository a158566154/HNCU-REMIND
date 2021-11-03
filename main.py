
import time
from get_data import get_data
#from server_sent import server_sent
from server_sent import SendMessage


def select_money():
    power_url = 'http://smart.hncu.net/microhome/classic/html/index.html#?publicUserId=admin&weixin_openid=oKAGAwzqqC9AGIMd-rTYDJHaJuEY&tab=5'
    woter_url = 'http://smart.hncu.net/microhomes/classic/html/index.html#?publicUserId=admin&weixin_openid=oKAGAwzqqC9AGIMd-rTYDJHaJuEY&tab=5'

    money = get_data()
    img ='经过查询，当前剩余电费{}元，剩余水费{}元'.format(money[0],money[1])
    print(img)
    while True:
        if money[0] < 10 :

            power_money = img+'电费不足10元，请及时点击下面链接缴纳电费'+power_url
            #server_sent(power_money)
            SendMessage(Subject='# 电费不足10元提醒',Content='### 点击<a href=\"{}">这里</a>进行电费缴纳,{}}'.format(power_url,img))
            print(power_money)
            time.sleep(3600)

        elif money[1] < 10:

            woter_money = img+'水费不足10元，请及时点击下面链接缴纳电费'+woter_url
            print(woter_money)
            SendMessage(Subject='# 水费不足10元提醒',Content='### 点击<a href=\"{}">这里</a>进行水费缴纳,{}'.format(woter_url,img))

            time.sleep(3600)
        else:
            SendMessage(Subject='电费不足10元提醒',Content='点击<a href=\"{}">这里</a>进行电费缴纳,{}'.format(power_url,img))
            
            time.sleep(3600)


if __name__ == '__main__':
    
    select_money()
                    
 
