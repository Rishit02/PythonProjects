import requests

url = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLScBqgshsW8NhVYZmdI4VXXu-yL1I1TaZDZ99GZG32ncc53Pug/formResponse'

d = {
    'entry.2005620554': 'Hmds',
    'entry.1045781291': 'jsdnf@gmail.com',
    'entry.1065046570': 'somehting',
    'entry.1166974658': '55555555',
    'entry.839337160': ''
}

htext = '''
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: en-GB,en-US;q=0.9,en;q=0.8
cache-control: no-cache
content-length: 313
content-type: application/x-www-form-urlencoded
cookie: HSID=AYkfk9hUjaaxvjpTF; SSID=AvNoGKQPwF4455gC0; APISID=iq6DKkEANiBaimHo/A6Mv3vmDNxnnE7PXl; SAPISID=_cs0rVQ_z6krLRry/Ae-Pw5FbmRUgZMC_O; __Secure-3PAPISID=_cs0rVQ_z6krLRry/Ae-Pw5FbmRUgZMC_O; SEARCH_SAMESITE=CgQI25IB; OGPC=19022552-1:; OGP=-19022552:; SID=-AcyqNgIS2L6m7Jz7ScGZlUiTnBXmi1PPmUJGxyP-3ai3Qdo9jhMsFPJ-vhEIFhzNkcUcA.; __Secure-3PSID=-AcyqNgIS2L6m7Jz7ScGZlUiTnBXmi1PPmUJGxyP-3ai3QdoZfWOjp9SyX2tn0YpnoCr5w.; 1P_JAR=2021-06-11-12; NID=216=oEOHH8mRPANF16cLdnwQ_KqM6So3gbZXMTEWvTonj0t3FBPCJM9yi8p7AUR39CGGh5iP6oDn2b9YFS1DBM9DhDZ3rcOLjSkPu69SptxTzOQw2hLWq-OzPjmIxuVrSwHXodF7DF-sWNT-Sh0GdZtFaNO5KygoI_ys_nhwoOPpli7ZnWViWCrWBEu6-igDfsVCiWDpQYLFVMm6C8-mafC0bmjga5xy8cELxYMUyhEQOzVs2iCrK_-9LcCW38TVnw; SIDCC=AJi4QfFZhaqDL7bii4s7mQI2zILQ4S9YMwPDIUvVXCJZvfRqDJ2ld4GkukeRsu9qI0xm7HcQ2w; __Secure-3PSIDCC=AJi4QfFlmvx_hm57rL52szM9_kWnGbgQW8zFGye-eqhnqGJSlQeDovRmYwkn---9bxza6t8WVE0
origin: https://docs.google.com
pragma: no-cache
referer: https://docs.google.com/forms/d/e/1FAIpQLScBqgshsW8NhVYZmdI4VXXu-yL1I1TaZDZ99GZG32ncc53Pug/viewform?vc=0&c=0&w=1&flr=0&fbzx=-4269512122676071623
sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"
sec-ch-ua-mobile: ?0
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: same-origin
sec-fetch-user: ?1
upgrade-insecure-requests: 1
'''
def parse_headers(text):
    # Init dictionary
    headers = {}

    # Loop through lines
    for line in text.split("\n"):
        # Split field name and value up so they can be assigned
        header = line.split(": ")

        if len(header) < 2:
            continue # no ": ", so it's probably just an empty line
        elif len(header) > 2:
            print("Help!") # This shouldn't happen
        else:
            headers[header[0]] = header[1]

    return headers

headers=parse_headers(htext)

print('what')
r = requests.post(url, data=d, headers=headers).text
print(r)
print('huh?')
print(r.status_code)

# 'fvv': '1',
# 'draftResponse': '[null,null,"-4269512122676071623"]',
# 'pageHistory': '0',
# 'token': 'BQRD-3kBAAA.-WwgkUDE9KAdeVUOQQaGag.AhBPvxiK0-sr9FUh6OZlSg',
# 'fbzx': '-4269512122676071623'
