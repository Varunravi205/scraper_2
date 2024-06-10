import requests
import re

company = input("Enter Company Name: ")
response = requests.get(
    f'https://autocomplete.clearbit.com/v1/companies/suggest?query={company}')
data = response.json()
if len(data) > 0:
    domain = data[0]['domain']
    url = f"https://www.{domain}"
    print(f"The Company Website:{url}")
else:
    url="none"

if url == "none":
    print("the company website not found,please check the company name again")
else:
    p = requests.get(url)
    phone_regex = "\\+?[1-9][0-9]{7,14}"
    phones = []
    for re_match in re.findall(phone_regex, p.text):
        if re_match not in phones:
            phones.append(re_match)

    email_regex = r"[\w\.-]+@[\w\.-]+"
    mails = []
    for re_match in re.findall(email_regex, p.text):
        if re_match not in mails:
            mails.append(re_match)
    print(" ")
    print("The Phone Numbers:")
    for i in phones:
        print(i)
    print(" ")
    print("The Email Address:")
    for i in mails:
        print(i)
    facebook_regex = r'https?://(www\.)?facebook\.com/([a-zA-Z0-9.\-_/]+)/?'
    instagram_regex = r'https?://(www\.)?instagram\.com/([a-zA-Z0-9._]+)/?'
    x_regex = r'https?://(www\.)?twitter\.com/([a-zA-Z0-9.\-_/]+)/?'
    youtube_regex = r'https?://(www\.)?youtube\.com/(user|channel)/([a-zA-Z0-9.\-_/]+)/?'
    fb=[]
    ig=[]
    x=[]
    yt=[]
    for re_match in re.findall(facebook_regex, p.text):
        if re_match not in fb:
            fb.append(re_match)
    for re_match in re.findall(instagram_regex, p.text):
        if re_match not in ig:
            ig.append(re_match)
    for re_match in re.findall(x_regex, p.text):
        if re_match not in x:
            x.append(re_match)
    for re_match in re.findall(youtube_regex, p.text):
        if re_match not in yt:
            yt.append(re_match)
    print(" ")

    print("X:")
    for i in x:
        print(i)
    print("facebook:")
    for i in fb:
        print(i)
    print("instagram:")
    for i in ig:

        print(i)
    print("youtube:")
    for i in yt:
        print(i)


