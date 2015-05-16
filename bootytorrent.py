from bs4 import BeautifulSoup
import requests
import subprocess


def getUrl():
	query = input('What would you like to torrent?')
	return query

def search():
	baseURL = 'https://thepiratebay.se/search/'
	query = getUrl()
	url = baseURL + query + '/0/99/100'
	r = requests.get(url)
	cont = BeautifulSoup(r.content)
	table = cont.find(id='SearchResults')
	body = table.find(id='searchResult')
	magnet = body.find("a", { "title" : "Download this torrent using magnet" })
	link = magnet['href']
	process = subprocess.Popen(['transmission-gtk', link])
	search()
	
search()

