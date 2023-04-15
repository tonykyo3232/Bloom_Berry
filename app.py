from flask import Flask, render_template, redirect, url_for
from pymongo import MongoClient

# Create Flask App
app = Flask(__name__)

@app.route("/")
def Home():

	client = MongoClient("mongodb+srv://tonywang1023:osurqnrftjDvJKxP@cluster0.qldlbek.mongodb.net/?retryWrites=true&w=majority")
	
	db = client.get_database("Homepage")

	records = db.image

	image_list = list(records.find())

	return render_template("index.html", img_list = image_list)

@app.route("/about")
def About():

	# Image DB
	client = MongoClient("mongodb+srv://tonywang1023:osurqnrftjDvJKxP@cluster0.qldlbek.mongodb.net/?retryWrites=true&w=majority")
	
	db = client.get_database("Homepage")

	records = db.image

	image_list = list(records.find())


	# Profile DB
	db = client.get_database("Profile")

	profiles = db.profile

	profile_list = list(profiles.find())


	return render_template("about.html", img_list = image_list, prof_list = profile_list)


@app.route("/post")
def Post():

	# Image DB
	client = MongoClient("mongodb+srv://tonywang1023:osurqnrftjDvJKxP@cluster0.qldlbek.mongodb.net/?retryWrites=true&w=majority")
	
	db = client.get_database("Homepage")

	records_image = db.image

	image_list = list(records_image.find())

	# Profile DB
	db = client.get_database("Profile")

	records_profile = db.profile

	profile_list = list(records_profile.find())

	list_profile = list()

	for p in profile_list:
		list_profile.append(p.get('content'))

	# Posts DB
	client = MongoClient("mongodb+srv://tonywang1023:osurqnrftjDvJKxP@cluster0.qldlbek.mongodb.net/?retryWrites=true&w=majority")
	
	db = client.get_database("Posts")

	records_post = db.post

	post_list = list(records_post.find())

	#
	list_post_title = list()
	list_content = list()
	list_author = list()
	list_author_position_title = list()
	list_paragraph = list()
	list_upload_time = list()
	list_image_content = list()

	#
	for post in post_list:
		post_title = post.get('post_title')
		content = post.get('content')
		author = post.get('author')
		author_position_title = post.get('author_position_title')
		paragraph = post.get('paragraph')
		upload_time = post.get('upload_time')
		image_content = post.get('image_content')

		#
		list_post_title.append(post_title)
		list_content.append(content)
		list_author.append(author)
		list_author_position_title.append(author_position_title)
		list_paragraph.append(paragraph)
		list_upload_time.append(upload_time)
		list_image_content.append(image_content)

	return render_template("post.html", img_list = image_list, list_profile = list_profile, list_post_title = list_post_title, 
		list_content = list_content, list_author = list_author, list_author_position_title = list_author_position_title, 
		list_paragraph = list_paragraph, list_upload_time = list_upload_time, list_image_content = list_image_content)

@app.route("/gallery")
def Gallery():

	# Image DB
	client = MongoClient("mongodb+srv://tonywang1023:osurqnrftjDvJKxP@cluster0.qldlbek.mongodb.net/?retryWrites=true&w=majority")
	
	db = client.get_database("Homepage")

	records = db.image

	image_list = list(records.find())


	# Profile DB
	db = client.get_database("Profile")

	profiles = db.profile

	profile_list = list(profiles.find())


	return render_template("gallery.html", img_list = image_list, prof_list = profile_list)


if __name__ == "__main__":
    app.run(debug=True)