#!/usr/bin/env python3
import json
from flask import Flask
from flask import render_template
app = Flask(__name__)

app.config.update(
    DEBUG=True,
    FREEZER_DEFAULT_MIMETYPE='text/html',
    FREEZER_RELATIVE_URLS=True,
)

data = dict()
data['news'] = json.load(open('../data/output-json/news.json'))

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/news/')
def news_index():
	return render_template('news_index.html', data=data)
	
@app.route('/news/<int:id>.html')
def news_item(id):
	item = [x for x in data['news'] if x['id'] == id][0]
	return render_template('news_item.html', data=data, id=id, item=item)

if __name__ == '__main__':
    app.run()