import nltk
import requests # download files and webpages
import bs4 # parse html
from collections import Counter
import re
from nltk.corpus import stopwords

def main():
    url = 'http://www.analytictech.com/mb021/mlk.htm'
    page = requests.get(url)
    page.raise_for_status()
    soup = bs4.BeautifulSoup(page.text, 'html.parser') # Parsing the html
    p_elems = [element.text for element in soup.find_all('p')] # taking all the text in the p tag

    speech = ''.join(p_elems)
    """
    Can also be written as:
    p_elems = soup.select('p') # more succint however is more limited than find_all method
    """
    # Not finished
    
