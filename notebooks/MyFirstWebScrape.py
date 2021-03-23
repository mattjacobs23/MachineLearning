# do shift command p to set syntax to python
from urllib.request import urlopen as uReq #grabs page itself
from bs4 import BeautifulSoup as soup #parses html text

my_url = 'https://www.newegg.com/p/pl?d=graphics+cards'

#opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read() #offload the content into a variable
uClient.close()
#right now html is a big jumble of text. Need to call soup function
page_soup = soup(page_html, "html.parser") #does the parsing

# grabs each product
containers = page_soup.findAll("div", {"class":"item-container"})

filename = "products.csv"
f = open(filename, "w")

headers = "brand, product_name, shipping\n"

f.write(headers)

for container in containers:
    brand = container.div.div.a.img["title"]

    title_container = container.findAll("a", {"class":"item-title"}) #still have to extract title out of this thing
    product_name = title_container[0].text

    shipping_container = container.findAll("li", {"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    print("brand: " + brand)
    print("product name: " + product_name)
    print("shipping: " + shipping)

    f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")
