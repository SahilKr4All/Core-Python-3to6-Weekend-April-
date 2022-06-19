import urllib.request as url
import bs4

home_path = "https://www.imdb.com/"
moviename = input("Enter a moviename : ")
path = "https://www.imdb.com/find?q="+moviename
response = url.urlopen(path)
data = bs4.BeautifulSoup(response,'lxml')

td = data.find("td", class_="result_text")
href = td.find("a")['href']

path = home_path + href
print(path)
response = url.urlopen(path)
data = bs4.BeautifulSoup(response,'lxml')

h1 = data.find("h1",class_="sc-b73cd867-0 eKrKux")
print("Movie Name : ",h1.text)


ul = data.find("ul",class_="ipc-inline-list ipc-inline-list--show-dividers sc-8c396aa2-0 kqWovI baseAlt")
li = ul.findAll("li")[-1]
print("TimeDuration : ",li.text)


sec = data.find("div",class_="sc-388740f9-0 hJjREK")
print("storyline : ",sec)