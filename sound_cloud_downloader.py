import re
import requests

def get_link(url):
	html = requests.get(url)
	regEx = re.compile(r'soundcloud://sounds:(.+?)"')
	mo = re.search(regEx, html.text)
	final_page = requests.get("https://api.soundcloud.com/i1/tracks/{0}/streams?client_id=eeBnt1uSZxQBwR3x2gyLtF5nekoouMvM".format(mo.group(1)))

	return final_page.json()['http_mp3_128_url']
