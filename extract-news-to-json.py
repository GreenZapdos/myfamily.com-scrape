#!/usr/bin/env python3
from bs4 import BeautifulSoup as bs
import json

def _format_text(text):
	return text.replace('\u00a0', ' ').strip()


news = list()

for c in range(1, 1930):
	post = dict()
	
	#Open file
	with open('data/raw-html/news/' + str(c) + '.html') as f:
		soup = bs(f.read())
	
	post['id'] = c
		
	#locate main content
	main_post_body = soup.select('table.BodyBG')[0].tbody.contents[2].td
	post['title'] = main_post_body.find_all('td', bgcolor="ffffff", nowrap="nowrap")[0].get_text().strip()

	#get comments
	post['body'] = dict()
	_posts_html = [x for x in main_post_body.contents[3].tbody if x.name == 'tr' and x.tr is not None][:-1] #remove non-post on the end
	del _posts_html[1] # remove another non-post
	
	post['body']['author'] =  _format_text(_posts_html[0].a.get_text())
	post['body']['date'] =  _format_text(_posts_html[0].span.contents[1]).replace('-', '').split('\n')[0].strip()
	post['body']['text'] =  _format_text(''.join([str(y) for y in _posts_html[0].tbody.tbody.tr.contents[1].tbody.tr.contents[3].contents if str(type(y)) != "<class 'bs4.element.Comment'>"]))#.encode(formatter=None).strip()
	post['body']['replies'] = list()
	
	
	for x in _posts_html[1:]:
		y = dict()
		y['body'] = dict()
		y['width'] = (int(x.tbody.img['width']) / 20)
		y['body']['author'] =  _format_text(x.a.get_text())
		y['body']['date'] =  _format_text(x.contents[5].tbody.tr.contents[3].contents[3].replace('-', '').split('\n')[0])
		y['body']['text'] =  _format_text(''.join([str(y) for y in x.tbody.tbody.tr.contents[1].tbody.tr.contents[3].contents if str(type(y)) != "<class 'bs4.element.Comment'>"]))#.encode(formatter=None).strip()
		y['body']['replies'] = list()
		post['body']['replies'].append(y)
	
	news.append(post)
	
with open('data/output-json/news.json', 'w') as f:
	f.write(json.dumps(news))