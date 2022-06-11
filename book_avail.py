import json
import bs4
import requests
import sys

# Defining a loop function
def loop():

    # Creating the correct url
    book_name = str(input("Enter book name: "))
    book_name = book_name.split(' ')
    print(f"Searching for {book_name} in repository...")
    book_name = '+'.join(book_name)
    url = f"https://catalogue.nlb.gov.sg/cgi-bin/spydus.exe/ENQ/WPAC/BIBENQ?optionsDrop=Books&ENTRY={book_name}&ENTRY_NAME=BS&ENTRY_TYPE=K&SORTS=SQL_REL_BIB&GQ={book_name}&ISGLB=0&NRECS=20&QRY=BFRMT%3ABK+-+LON%3AOVERDRIVE*&QRYTEXT=Books"

    # Requesting the url for initial page
    print("Requesting url...")
    page = requests.get(url)
    page.raise_for_status()

    # Extracting a elements
    avail_links = list()

    soup = bs4.BeautifulSoup(page.text, 'html.parser') # Parsing the html
    for a in soup.find_all('a', href = True):
        if a.text == "View availability":
            avail_links.append(a['href'])

    # Requesting avail webpage
    l = "https://catalogue.nlb.gov.sg/"
    l += avail_links[0]
    r = requests.get(l)
    r.raise_for_status()
    s = bs4.BeautifulSoup(r.text, 'html.parser')
    table = s.find('table')
    # print(f"Table is: {table}")
    rows = table.find_all('tr')
    # print(f"Rows found: {rows}")
    info = list()
    for row in rows:
        info.append(row.get_text())

    info = info[1:]
    # print(info)
    print("Available in:\n")
    for i in info:
        info = i.split(' ')
        for counter in info:
            # print(counter)
            if counter[-9:] == "Available":
                print(i)

condition = 'y'
while condition=="y":
    loop()
    condition = str(input("\nEnter condition: "))
