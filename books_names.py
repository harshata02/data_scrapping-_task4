import requests as rq

from bs4 import BeautifulSoup 

from bs4.element import NavigableString

import pandas as pd

bookUrl='https://books.toscrape.com/'

bookHeader = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
bookResp = rq.get(url=bookUrl,headers=bookHeader)

booksoup = BeautifulSoup(bookResp.content,'html.parser')

book_findings=booksoup.find_all('h3')

for book_names in book_findings:


    print('book_names',book_names.text)


books_names =[book_names.text for book_names in book_findings]

booksDf = pd.DataFrame(books_names)

booksDf.to_csv('books.csv')









