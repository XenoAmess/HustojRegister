import requests
import random


def randomStr(num):
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sa = []
    for _  in range(num):
        sa.append(random.choice(seed))
    res = ''.join(sa)
    return res;


def randomNum(num):
    seed = "1234567890"
    sa = []
    for _ in range(num):
        sa.append(random.choice(seed))
    res = ''.join(sa)
    return res;


SITE = 'http://acm.sustc.edu.cn/onlinejudge/register.php';

postData = {
    'user_id':randomNum(8),
    'nick':randomStr(8),
    'password':'password',
    'rptpassword':'password',
    'school':randomStr(20),
    'email':randomStr(8) + "@" + randomStr(8),
    'submit':'Submit',
    'csrf':'fe1C8qyOG2GSoSD90MIaVmccFlTsQvcm',
}

for au in postData:
    print(au + " : " + postData[au]);
print();

cookiestr = "PHPSESSID=fkm3sevsu6nmpdhslgfj3iaf01";
cookies = {};
 
for line in cookiestr.split(';'):
    name, value = line.strip().split('=', 1)  
    cookies[name] = value
 
response = requests.post(SITE, data=postData, cookies=cookies)
print(response.text)
