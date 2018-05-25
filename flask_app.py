from flask import Flask, request, redirect, render_template
from sound_cloud_downloader import get_link

app = Flask(__name__)

@app.route('/')
def hello():
	return render_template('index.html')
	#return "Hello World! So simple!"
	
@app.route("/download_mp3", methods=['GET'])	
def download_mp3():
	#media_url = request.args.get('url', '')
	media_url = request.args['url'] #request.form[...] didnt work so alternatively .args[...]
	return redirect(get_link(media_url), code=302)
	