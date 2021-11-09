import requests
import json
import os

# 配置开始
user = os.environ["USER"]
account = user.split( )[0] # 账号
password = user.split( )[1] # 密码
school_id = user.split( )[2] # 学校ID
sign_gps = os.environ["SIGN_GPS"]  # 签到坐标（注意小数点取后6位）
longitude = sign_gps.split(",")[0] # 经度
latitude = sign_gps.split(",")[1] # 纬度
data = {
  "account":account,
  "password":password,
  "school_id":school_id,
  "longitude":longitude,
  "latitude":latitude,
  "address_name":os.environ["ADDRESS_NAME"] 
}
headers = {'Content-Type': 'application/json'}

response = requests.post(url='http://xxy.kuileii.cn/release/xixunyun', headers=headers, data=json.dumps(data))
print(response.json())

SCKEY=os.environ["SCKEY"]
if len(SCKEY) >= 1:
  url = 'https://sc.ftqq.com/'+SCKEY+'.send'
  requests.post(url, data={"text": "习讯云签到提醒", "desp": response.json()})

#新增
headers={
    "User-Agent":"Mozilla/5.0 (Linux; Android 9; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.93 Mobile Safari/537.36",
    'Content-Type': 'application/json'
}
url='http://pushplus.hxtrip.com/send'
data={'token':'ff9c3611d6624c478956accbff26f67b','title':'习讯云签到','content':'xxxx','template':'html'}
res=requests.post(headers=headers,url=url,data=json.dumps(data),timeout=10)
print(res.status_code)
print(res.text)
