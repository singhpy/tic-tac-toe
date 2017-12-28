"""
    Download beautifulsoup4
    https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/
    https://docs.python.org/3.6/library/stdtypes.html
"""

from bs4 import BeautifulSoup
import urllib.request

address = "https://docs.python.org/3.6/library/stdtypes.html"
with urllib.request.urlopen(address) as url:
    html = url.read()

soup = BeautifulSoup(html, "html.parser")

# print(soup.title.string)
# print(soup.title.text)
# print(soup.h1)
# print(soup.p)

methods = soup.findAll("dl", {"class": "method"})   # lists
# print(len(methods))

try:
    for method in methods:
        if(method.dt["id"])
except:
    KeyError("Key Error")
