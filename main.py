#!/usr/bin/env python
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as openLink

from SQLlib import SQLThing

'''Scanning GPU Program:
1. Load main page
2. Scann products add price, product name.
3. click on product url and copy the link to the database
'''

class GPUScanner:

    #NUMBER OF URLs TO SCANN
    numOfPages = 10
    URLArray = []
    List = True

    # DECLARE ARRAYS TO STORE DATA
    productArray = []
    priceArray = []
    URLDBArray = []

    #SETS ALL URLs TO EXTRACT INFORMATION FROM
    def __init__(self):

        #INSERT FIRST PAGE SEARCH RESULT URL
        self.URLArray.append("https://listado.mercadolibre.com.co/tarjeta-de-video#D[A:tarjeta%20de%20video]")
        #self.driver = webdriver.Edge(executable_path='C:\\Users\\jamar\\Downloads\\edgedriver_win64\\msedgedriver.exe')

        #INCREMENT FOR URL PAGE
        num = 51
        m = 0
        middle = "_Desde_"
        #SET AND SAVE ALL WEBPAGES INTO THE URLARRAYg
        for i in range(self.numOfPages):
            finalURL = "https://computacion.mercadolibre.com.co/componentes-pc-tarjetas-video/tarjeta-de-video%s%s" % (
            middle, num + m)
            self.URLArray.append(finalURL)
            m = m + 50

    #SCANN INFORMATION FROM MANY URLs
    def scannWebsite(self):

        for i in range(self.numOfPages):

            self.scannWebPage(self.URLArray[i])


    def scanProduct(self):
        pass

    #EXTRACT INFORMATION FROM A SIGNLE URL
    def scannWebPage(self,URL):

        #SET VARIABLES FOR EXTRACTION
        getpage = openLink(URL)
        page_html = getpage.read()
        getpage.close()
        pagedata = soup(page_html, "html.parser")  # library allows us to parse html and xml files

        #CHOOSE ELEMENT WITH PRICE AND PRODUCT
        containers=pagedata.findAll("li",{"class":"ui-search-layout__item"},)



        #FILL ARRAYS WITH DATA
        for i in range(50):


            try:

                self.productArray.append(containers[i].h2.string)
                print(containers[i].h2.string)

            except AttributeError:
                self.productArray.append("No product")
                print("No product")



            try:
                price=""
                for character in containers[i].span.span.string:
                    if character.isalnum() & character.isdigit():
                       price += character
                self.priceArray.append(float(price))
                print(price)
            except AttributeError:
                self.priceArray.append(0)

            try:

                self.URLDBArray.append(containers[i].a['href'])
                print(containers[i].a['href'])

            except AttributeError:
                self.priceArray.append(0)







def main():

    Scanobject = GPUScanner()
    #print(Scanobject.scannWebsite())
    Scanobject.scannWebsite()
    #print(Scanobject.URLArray[0])
    print(Scanobject.priceArray[0])
    #print(Scanobject.productArray[50])

    SQLObject = SQLThing()

    for i in range(len(Scanobject.URLArray)):

        SQLObject.commitURLS(str(Scanobject.URLDBArray[i]), str(Scanobject.productArray[i]), float(Scanobject.priceArray[i]))
        print(Scanobject.productArray[i]+", product inserted in URL table.")

    '''
    Scanobject = GPUScanner()
    getpage = openLink("https://listado.mercadolibre.com.co/tarjeta-de-video#D[A:tarjeta%20de%20video]")
    page_html = getpage.read()
    getpage.close()
    pagedata = soup(page_html, "html.parser")  # library allows us to parse html and xml files

    # CHOOSE ELEMENT WITH PRICE AND PRODUCT
    containers = pagedata.findAll("li", {"class": "ui-search-layout__item"}, )


    #Scanobject.productArray.append(containers.h2.string)
    print(soup.prettify(containers[1]))
    print(containers[1].h2.string)
    print(containers[1].span.span.string)
    print(containers[1].a['href'])
    '''


if __name__== "__main__":
    main()


