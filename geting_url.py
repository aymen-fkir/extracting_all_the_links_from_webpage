# we need this library to make requets
import requests

# this library allow you to read html files and xml files
from bs4 import BeautifulSoup


# specify the url that you want to extract from it
url = "example.com"
# make a get request 
reqs = requests.get(url)

# this part is to create the to save in you can just created by your self
try:
    f = open("urls.txt", "x")
except FileExistsError:
    print("The file already exists.")
# open a file with the argument w so you can write in it
f = open("urls.txt","w")
# reading the html file
soup = BeautifulSoup(reqs.text,'html.parser')

urls =[]
# a loop so you can save all the extracted texts
for link in soup.find_all('a'):
    urls.append(link.get('href'))
# save only the links in a file 
for i in urls:
    if i != None:
        if i[0:5]=="https":
            i+='\n'
            f.write(i)
# clear this list 
urls.clear
