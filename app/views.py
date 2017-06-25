from app import app
from flask import render_template, request
from slugify import slugify

import urllib2
import json


@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route('/<slug>', methods=['GET', 'POST'])
def show(slug):
	url = 'https://dl.dropboxusercontent.com/s/vftubbdad6fis6g/data.json'
	json_obj = urllib2.urlopen(url)
	data = json.load(json_obj)

	location = ''
	imageURL = ''
	description = ''
	for i in data['data']:
		if slug == i['location']:
			location = i['location']
			imageURL = i['url']
			description = i['description']

	return render_template("vrview.html", location = location, imageURL = imageURL, description = description , post=slug )

