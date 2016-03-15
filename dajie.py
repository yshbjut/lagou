import sys
import urllib.request
import urllib.parse
import time
import csv
import random
import datetime
import time
GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'

global_agent = dict()

keyword = 'PHP%E5%B7%A5%E7%A8%8B%E5%B8%88'
referer = 'http://so.dajie.com/job/search?jobsearch=4&'
referer += 'keyword=PHP%E5%B7%A5%E7%A8%8B%E5%B8%88&city=&ct=144498644'


SO_COOKIE = 'SO_COOKIE=9477fBzjlm0IKpUDbb1CDUvftmNAzGD/ybue19357eitPW1W1gowoikHTbFWlAn+WLagU2MvCFJRke9xeUtsf2g3x35CuTBoxYiY'



def read_file(filename):
    file = open(filename)
    reader = csv.reader(file)
    index = 1
    for line in reader:
        global_agent[index] = line[0]
        index += 1
    file.close()
def run(index):
    print('start....',index)
    global SO_COOKIE
    agent = global_agent[random.randint(1,29)]
    #print(index)
    url = 'http://so.dajie.com/job/ajax/search/filter?jobsearch=4&pagereferer=http%3A%2F%2Fjob.dajie.com%2F%3Ff%3Dnav&ajax=1&'
    url += 'keyword='+keyword+'&page='
    ##print(url)
    url += str(index)+'&order=0&from=user&salary=&recruitType=&city=&positionIndustry=&positionFunction=&degree=&quality=&experience=&_CSRFToken=ZQIUinaw3_DhG0cgzNDUR48b78ueLpTP2CKMMxM*'
    req = urllib.request.Request(url)
    req.add_header('Accept', 'application/json, text/javascript, */*; q=0.01')
    
    req.add_header('User-Agent',agent);
    req.add_header('X-Requested-With','XMLHttpRequest')
    
    ##req.add_header('Cookie','SO_COOKIE=689cHuCNpyAyHL+g/XQn1fV4SJf/xTayUoe2ud3QSmDW6W23UZw6+5OZQWrbViIqAqGFMfmImXzcWegy1bewA2qeLveLRlwJ+1+g; DJ_UVID=MTQzNzU0Njc4MTAxNjMzNTc5; login_email=1208706282%40qq.com; DJ_RF=http%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DBD2R5CZPOv84jsoBa34tG27NF3X6p7xERjJCMKV7OJu%26wd%3D%26eqid%3Dd2f9301d0001b60d00000003561f48a3; DJ_EU=http%3A%2F%2Fwww.dajie.com%2F; __login_tips=1; dj_cap=c57d9b61393eedb9d06de1a21ba56f88; dj_auth_v3=MRBMERESdrCfnT2-ssEWwAkd6NdxOLap_ee88tAnJnHSl0QEW8fX-pqpCZNJu-8*; uchome_loginuser=33860966; USER_ACTION="request^ACampus^AAUTO^Ajobdetail:^A-"')
    cookie = SO_COOKIE+';'
    cookie += ' DJ_UVID=MTQzNzU0Njc4MTAxNjMzNTc5;'
    cookie += ' login_email=1208706282%40qq.com; __login_tips=1; dj_auth_v3=MRBMERESdrCfnT2-ssEWwAkd6NdxOLap_ee88tAnJnHSl0QEW8fX-pqpCZNJu-8*; uchome_loginuser=33860966;'
    cookie += ' DJ_EU="http://www.dajie.com/zhiwei/seo/job_1100_0_310000_0_0_110000_0_0_0_0_1"; DJ_RF=empty; USER_ACTION=request^ACampus^AAUTO^A-^A-'
    req.add_header('Cookie',cookie)

    req.add_header('Referer',referer)
    
    response = urllib.request.urlopen(req)
    html = response.read()
    html = html.decode("UTF-8")
    if html.find('404_')==-1:
        file = open("json/PHP工程师/"+str(index)+".txt",mode="w+",encoding="UTF-8")
        file.write(html)
        file.close()
        print("end....")
    else:
        '''req = urllib.request.Request(referer)
        req.add_header("Cookie",cookie)
        req.add_header("Host",'so.dajie.com')
        req.add_header('User-Agent',agent);
        req.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
        response = urllib.request.urlopen(req)
        date = response.getheader('Date')
        set_cookie = response.getheader('Set-Cookie')
        if date:
            date = datetime.datetime.strptime(date, GMT_FORMAT)
            print(date)
        if set_cookie:
            list_cookie = set_cookie.split(';')
            SO_COOKIE = list_cookie[0]
            print(list_cookie[0])
        else:
            print("stop")
        
            sys.exit(0)'''
        get_so_cookie(cookie,agent)
        print("start....index: %d agent: %s"%(index,agent))
    ##print(html)
    
    time.sleep(3)
def get_so_cookie(cookie,agent):
    req = urllib.request.Request(referer)
    req.add_header("Cookie",cookie)
    req.add_header("Host",'so.dajie.com')
    req.add_header('User-Agent',agent);
    req.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    response = urllib.request.urlopen(req)
    date = response.getheader('Date')
    set_cookie = response.getheader('Set-Cookie')
    '''if date:
        type(date)
        date = datetime.datetime.strptime(date, GMT_FORMAT)
        type(date)
        print(int(time.time()))'''
    if set_cookie:
        list_cookie = set_cookie.split(';')
        global SO_COOKIE
        SO_COOKIE = list_cookie[0]
        print(list_cookie[0])
    else:
        print("stop")
        sys.exit(0)
if __name__ == "__main__":
    read_file('agent.csv')
    for i in range(27,301):
        run(i)
    
    
    
        
