from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "layan"
password = "555"
facebook_friends=["dunia","roaa","maya", "joleen", "layan", "hala"]


@app.route('/' , methods =["GET", "POST"])  # '/' for the default page
def login():
	if request.method == "GET":
		return render_template('login.html')

	else : 
		name = request.form['username']
		password1 = request.form ['password']
		if username == name and password1 == password :
			return render_template('home.html' , facebookfriends = facebook_friends , username = name , password = password  )
		return render_template ('login.html')

@app.route ('/home')
def home():
	return render_template ('home.html' , facebookfriends= facebook_friends , )

@app.route('/friends_exists/<string:name>',methods = ["GET" ,"POST"])
def friends (name) :
	if name in facebook_friends :
		check = "True";
	else :
		check = "False" ; 

	return render_template ('friend_exists.html' , check = check )

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)