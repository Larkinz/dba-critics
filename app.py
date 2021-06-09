import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get(
    "MONGO_DBNAME")  # grab the database name
app.config["MONGO_URI"] = os.environ.get(
    "MONGO_URI")  # grab the connection string
app.secret_key = os.environ.get("SECRET_KEY")  # grab the secret key

# setup an instance of PyMongo
mongo = PyMongo(app)


def vote_count(album_id):
    """Check the database for votes that match a certain album id,
    then return the total number of votes for that specific album id."""
    album_vote_count = 0
    try:
        for x in mongo.db.ratings.find({"album_id": album_id}):
            album_vote_count = album_vote_count + 1
    except:
        album_vote_count = 0
    return album_vote_count


@app.route("/")
def starting_url():
    return redirect("/welcome")


@app.route("/welcome")
def welcome():
    return render_template("welcome.html")


@app.route("/homepage")
def homepage():
    return render_template("homepage.html")


@app.route("/albums")
def albums():
    # grab all comments from the database
    try:
        comments = list(mongo.db.comments.find())
    except:
        comments = []

    # count the total amount of votes on album 001
    album001_vote_count = vote_count("001")
    print(album001_vote_count)

    # count the total amount of votes on album 002
    album002_vote_count = vote_count("002")
    print(album002_vote_count)

    # count the total amount of votes on album 003
    album003_vote_count = vote_count("003")
    print(album003_vote_count)

    # count the total amount of votes on album 004
    album004_vote_count = vote_count("004")
    print(album004_vote_count)

    # find all album 001 ratings
    try:
        album001_ratings = list(mongo.db.ratings.find({"album_id": "001"}))
    except:
        album001_ratings = []

    # sum up all the album 001 ratings
    ### credits #7 (see README.md credits section) ###
    try:
        album001_rating_sum = sum(int(d["rating"]) for d in album001_ratings)
    except:
        album001_rating_sum = 0

    # calculate average album 001 rating
    try:
        album001_avg_rating = round(album001_rating_sum / album001_vote_count)
    except:
        album001_avg_rating = 0

    # find all album 002 ratings
    try:
        album002_ratings = list(mongo.db.ratings.find({"album_id": "002"}))
    except:
        album002_ratings = []

    # sum up all the album 002 ratings
    ### credits #7 (see README.md credits section) ###
    try:
        album002_rating_sum = sum(int(d["rating"]) for d in album002_ratings)
    except:
        album002_rating_sum = 0

    # calculate average album 002 rating
    try:
        album002_avg_rating = round(album002_rating_sum / album002_vote_count)
    except:
        album002_avg_rating = 0

    # find all album 003 ratings
    try:
        album003_ratings = list(mongo.db.ratings.find({"album_id": "003"}))
    except:
        album003_ratings = []

    # sum up all the album 003 ratings
    ### credits #7 (see README.md credits section) ###
    try:
        album003_rating_sum = sum(int(d["rating"]) for d in album003_ratings)
    except:
        album003_rating_sum = 0

    # calculate average album 003 rating
    try:
        album003_avg_rating = round(album003_rating_sum / album003_vote_count)
    except:
        album003_avg_rating = 0

    # find all album 004 ratings
    try:
        album004_ratings = list(mongo.db.ratings.find({"album_id": "004"}))
    except:
        album004_ratings = []

    # sum up all the album 004 ratings
    ### credits #7 (see README.md credits section) ###
    try:
        album004_rating_sum = sum(int(d["rating"]) for d in album004_ratings)
    except:
        album004_rating_sum = 0

    # calculate average album 004 rating
    try:
        album004_avg_rating = round(album004_rating_sum / album004_vote_count)
    except:
        album004_avg_rating = 0

    # check if user has voted on album 001
    has_voted_album001 = "false"
    try:
        if mongo.db.ratings.find_one({"$and": [{"username": session["user"]}, {"album_id": "001"}]}):
            has_voted_album001 = "true"
    except:
        has_voted_album001 = "false"

    # check if user has voted on album 002
    has_voted_album002 = "false"
    try:
        if mongo.db.ratings.find_one({"$and": [{"username": session["user"]}, {"album_id": "002"}]}):
            has_voted_album002 = "true"
    except:
        has_voted_album002 = "false"

    # check if user has voted on album 003
    has_voted_album003 = "false"
    try:
        if mongo.db.ratings.find_one({"$and": [{"username": session["user"]}, {"album_id": "003"}]}):
            has_voted_album003 = "true"
    except:
        has_voted_album003 = "false"

    # check if user has voted on album 004
    has_voted_album004 = "false"
    try:
        if mongo.db.ratings.find_one({"$and": [{"username": session["user"]}, {"album_id": "004"}]}):
            has_voted_album004 = "true"
    except:
        has_voted_album004 = "false"

    return render_template("albums.html",
                           comments=comments,
                           album001_vote_count=album001_vote_count,
                           album002_vote_count=album002_vote_count,
                           album003_vote_count=album003_vote_count,
                           album004_vote_count=album004_vote_count,
                           album001_avg_rating=album001_avg_rating,
                           album002_avg_rating=album002_avg_rating,
                           album003_avg_rating=album003_avg_rating,
                           album004_avg_rating=album004_avg_rating,
                           has_voted_album001=has_voted_album001,
                           has_voted_album002=has_voted_album002,
                           has_voted_album003=has_voted_album003,
                           has_voted_album004=has_voted_album004,
                           album001_ratings=album001_ratings,
                           album002_ratings=album002_ratings,
                           album003_ratings=album003_ratings,
                           album004_ratings=album004_ratings)


# posting a comment functionality
### credits #8 (see README.md credits section) ###
@app.route("/<album_id>", methods=["POST"])
def post_comment(album_id):
    if request.method == "POST":
        try:
            comment = {
                "comment": request.form.get(f"album_{album_id}_comment"),
                "album_id": f"{album_id}",
                "username": session["user"]
            }
            mongo.db.comments.insert_one(comment)
            return redirect(url_for('albums'))
        except:
            return render_template("500_error.html")


# editing a comment functionality
### credits #8 (see README.md credits section) ###
@app.route("/edit_comment/<comment_id>/<album_id>", methods=["POST"])
def edit_comment(comment_id, album_id):
    if request.method == "POST":
        try:
            comment_edit = {
                "comment": request.form.get(f"album_{album_id}_comment_edit"),
                "album_id": f"{album_id}",
                "username": session["user"]
            }
            # update comment
            mongo.db.comments.replace_one(
                {"_id": ObjectId(comment_id)}, comment_edit)
            return redirect(url_for('albums'))
        except:
            return render_template("500_error.html")


# deleting a comment functionality
### credits #8 (see README.md credits section) ###
@app.route("/delete_comment/<comment_id>")
def delete_comment(comment_id):
    try:
        mongo.db.comments.delete_one({"_id": ObjectId(comment_id)})
        return redirect(url_for('albums'))
    except:
        return render_template("500_error.html")


# posting and updating album rating functionality
### credits #8 (see README.md credits section) ###
@app.route("/post_rating/<album_id>", methods=["POST"])
def post_rating(album_id):
    if request.method == "POST":
        try:
            # check if user album rating already exists in database
            existing_rating = mongo.db.ratings.find_one(
                {"$and": [{"username": session["user"]}, {"album_id": album_id}]})

            # update album rating
            if existing_rating:
                rating_edit = {
                    "rating": request.form.get(f"slider-album-{album_id}"),
                    "album_id": f"{album_id}",
                    "username": session["user"]
                }
                mongo.db.ratings.replace_one(
                    {"_id": existing_rating.get('_id')}, rating_edit)
                flash("You updated your rating!")
                return redirect(url_for('albums'))

            # post album rating
            rating = {
                "rating": request.form.get(f"slider-album-{album_id}"),
                "album_id": f"{album_id}",
                "username": session["user"]
            }
            mongo.db.ratings.insert_one(rating)
            flash("Rating posted!")
            return redirect(url_for('albums'))
        except:
            return render_template("500_error.html")


# log in functionality
### credits #8 (see README.md credits section) ###
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                # put the user into 'session' cookie
                session["user"] = request.form.get("username")
                return redirect(url_for("albums"))
            else:
                # invalid password match
                flash("Incorrect username and/or password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect username and/or password")
            return redirect(url_for("login"))

    return render_template("login.html")


# register functionality
### credits #8 (see README.md credits section) ###
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})

        if existing_user:
            flash("Username already taken!")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username"),
            "password": generate_password_hash(request.form.get("password"), method='pbkdf2:sha512')
        }
        mongo.db.users.insert_one(register)
        flash("Registration complete!")
        return redirect(url_for("login"))

    return render_template("register.html")


# log out functionality
### credits #8 (see README.md credits section) ###
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# 404 'page not found' error handler
### credits #9 (see README.md credits section) ###
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404_error.html"), 404


# 405 'method not allowed' error handler
### credits #9 (see README.md credits section) ###
@app.errorhandler(405)
def page_not_found(e):
    return render_template("405_error.html"), 405


# 500 'internal server error' error handler
### credits #9 (see README.md credits section) ###
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500_error.html"), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get("DEBUG"))
