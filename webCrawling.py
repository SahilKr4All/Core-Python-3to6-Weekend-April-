import urllib.request as url
import bs4

home_path = "https://www.imdb.com"
movieName = input("Enter Movie Name : ")
path = "https://www.imdb.com/find?q="+movieName
print(path)
response = url.urlopen(path)

data = bs4.BeautifulSoup(response)
td = data.find("td",class_="result_text")
href = td.find("a")['href']

path = home_path + href
print(path)