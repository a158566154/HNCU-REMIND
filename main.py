import time
from get_cmd import get_data
from server_sent import server_sent


if __name__ == '__main__':
    money = get_data()
    img ='经过查询，当前剩余电费{}元，剩余水费{}元'.format(money[0],money[1])
    print(img)
    

    if money[0] < 10 :
        server_sent(img+'电费不足10元，请及时点击下面链接缴纳电费')
        time.sleep(3600)

    elif money[1] < 10:


        server_sent(img)

        time.sleep(3600)