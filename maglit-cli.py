import requests
import string
import secrets
import os.path
from rich import print as rprint
from rich.panel import Panel
import qrcode_terminal
def generate_random(strength):
    global output

    # if the word file from https://www.mit.edu/~ecprice/wordlist.10000 hasn't been downloaded yet, download it and save in a file called words
    if not os.path.isfile("word-list.txt"):
        response = requests.get("https://www.mit.edu/~ecprice/wordlist.10000")
        with open("word-list.txt", 'wb') as f:
            f.write(response.content)

    def get_random_word():
        with open("word-list.txt", 'r') as f:
            words = f.readlines()
        word = secrets.choice(words).strip()
        return word
    def three_random_chars():
        chars = ''.join(secrets.choice(string.ascii_lowercase + string.digits) for i in range(2))
        return chars

    # random passwords use 2 words + 2 chars, random links use 1 word + 2 chars
    if strength == "high":
        output = (get_random_word())+"-"+(get_random_word())+"-"+(three_random_chars())
    elif strength == "low":
        output = (get_random_word())+"-"+(three_random_chars())
def get_input():
    rprint(Panel("[green]Enter a link to shorten:"))
    link_to_shorten = input(str("--->  "))
    rprint(Panel("[red]Press enter = no password protection, [green]random = random password, [yellow]otherwise type a password and it will be used:"))
    password = input(str("--->  "))
    rprint(Panel("[green]Press enter = random shortened link, [yellow]otherwise type some text to go after maglit.me/ for your custom link."))
    custom_shortened_link = input(str("--->  "))

    if password == "random":
        # getting a random pass, if the word "random" was typed
        generate_random(strength="high")
        password = output

    if custom_shortened_link == "":
        # getting a random shortened_link or "slug", if none was provided
        generate_random(strength="low")
        custom_shortened_link = output

    final_shortened_link = ("https://maglit.me/"+custom_shortened_link)
    if len(password) >1:
        rprint(Panel(f"""
[blue]The shortened link is available at: [green]{final_shortened_link}
        
[blue]The password is [green]{password}

[blue] A QR code for the link is also displayed below: 
"""))
    else:
        rprint(Panel(f"""
[blue]The shortened link is available at: [green]{final_shortened_link}
        
[blue] A QR code for the link is also displayed below: 
"""))

    # display QR code
    qrcode_terminal.draw(final_shortened_link)

    # shorten link and pass the custom parameters
    shorten(link_to_shorten, password, custom_shortened_link)

def shorten(link_to_shorten, password, custom_shortened_link):
    try:
        url = 'https://maglit.me/api/create'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:112.0) Gecko/20100101 Firefox/112.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://maglit.me/',
            'Content-Type': 'application/json',
            'Origin': 'https://maglit.me',
            'DNT': '1',
            'Alt-Used': 'maglit.me',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'TE': 'trailers'
        }
        data = {
            'slug': custom_shortened_link,
            'password': password,
            'link': link_to_shorten
        }
        response = requests.post(url, headers=headers, json=data)
        print(response.json())
    except:
        pass

    # try being used since this outputs errors despite working, supressing errors

get_input()