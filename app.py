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
    """
    Check the database for votes that match a certain album id,
    then return the total number of votes for that specific album id.
    """
    album_vote_count = 0
    try:
        for x in mongo.db.ratings.find({"album_id": album_id}):
            album_vote_count = album_vote_count + 1
    except:
        album_vote_count = 0
    return album_vote_count


def find_album_ratings(album_id):
    """
    Check the database for votes that match a certain album id,
    then return these as a list of dictionaries.
    """
    album_ratings = []
    try:
        album_ratings = list(mongo.db.ratings.find({"album_id": album_id}))
    except:
        album_ratings = []
    return album_ratings


def sum_album_ratings(album_ratings):
    """
    Sum up all the rating key values from a list of dictionaries,
    then return the result.
    """
    album_rating_sum = 0
    ### credits #7 (see README.md credits section) ###
    try:
        album_rating_sum = sum(int(d["rating"]) for d in album_ratings)
    except:
        album_rating_sum = 0
    return album_rating_sum


def calc_album_avg_rating(album_rating_sum, album_vote_count):
    """
    Calculate the average album rating,
    then return the result.
    """
    album_avg_rating = 0
    try:
        album_avg_rating = round(album_rating_sum / album_vote_count)
    except:
        album_avg_rating = 0
    return album_avg_rating


@app.route("/")
def starting_url():
    """
    Redirects to the welcome page,
    no logic is executed.
    """
    return redirect("/welcome")


@app.route("/welcome")
def welcome():
    """
    Returns the welcome page template,
    no logic is executed.
    """
    return render_template("welcome.html")


@app.route("/homepage")
def homepage():
    """
    Returns the homepage template,
    no logic is executed.
    """
    return render_template("homepage.html")


@app.route("/albums")
def albums():
    """
    Grabs every comment from the database,
    counts the total amount of votes per album_id,
    finds all the album ratings per album_id,
    sums up all the album ratings per album_id,
    calculates the average album rating per album_id,
    checks on what albums the user has voted,
    then returns the albums page template.
    """
    # grab all comments from the database
    try:
        comments = list(mongo.db.comments.find())
    except:
        comments = []

    # count the total amount of votes on album 001
    album001_vote_count = vote_count("001")
    # count the total amount of votes on album 002
    album002_vote_count = vote_count("002")
    # count the total amount of votes on album 003
    album003_vote_count = vote_count("003")
    # count the total amount of votes on album 004
    album004_vote_count = vote_count("004")

    # find all album 001 ratings
    album001_ratings = find_album_ratings("001")
    # find all album 002 ratings
    album002_ratings = find_album_ratings("002")
    # find all album 003 ratings
    album003_ratings = find_album_ratings("003")
    # find all album 004 ratings
    album004_ratings = find_album_ratings("004")

    # sum up all the album 001 ratings
    album001_rating_sum = sum_album_ratings(album001_ratings)
    # sum up all the album 002 ratings
    album002_rating_sum = sum_album_ratings(album002_ratings)
    # sum up all the album 003 ratings
    album003_rating_sum = sum_album_ratings(album003_ratings)
    # sum up all the album 004 ratings
    album004_rating_sum = sum_album_ratings(album004_ratings)

    # calculate average album 001 rating
    album001_avg_rating = calc_album_avg_rating(
        album001_rating_sum, album001_vote_count)
    # calculate average album 002 rating
    album002_avg_rating = calc_album_avg_rating(
        album002_rating_sum, album002_vote_count)
    # calculate average album 003 rating
    album003_avg_rating = calc_album_avg_rating(
        album003_rating_sum, album003_vote_count)
    # calculate average album 004 rating
    album004_avg_rating = calc_album_avg_rating(
        album004_rating_sum, album004_vote_count)

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
    """
    Receives user input from HTML form,
    inserts the input into the database,
    then redirects to the albums page.
    """
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
    """
    Receives user input from HTML form,
    updates the database item,
    then redirects to the albums page.
    """
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
    """
    Deletes the database item,
    then redirects to the albums page.
    """
    try:
        mongo.db.comments.delete_one({"_id": ObjectId(comment_id)})
        return redirect(url_for('albums'))
    except:
        return render_template("500_error.html")


# posting and updating album rating functionality
### credits #8 (see README.md credits section) ###
@app.route("/post_rating/<album_id>", methods=["POST"])
def post_rating(album_id):
    """
    Receives user input from HTML form,
    checks the database if the user already voted,
    if the user already voted it updates their vote,
    else if they haven't voted it inserts their vote,
    then redirects to the albums page.
    """
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
    """
    If the method is POST,
    user input is received from HTML form,
    it checks the database if the user exists,
    if the user exists it checks if the password matches,
    if the password matches it puts the user into session,
    then redirects to the albums page.
    If the password doesn't match,
    then it redirects back to the login page.

    Else if the user doesn't exist,
    it redirects back to the login page.

    If the method is GET,
    it returns the login page template.
    """
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
    """
    If the method is POST,
    user input is received from HTML form,
    it checks the database if the user exists,
    if the user exists,
    it redirects back to the register page.

    Else if the user doesn't exist,
    it inserts their username and password into the database,
    then it redirects to the login page.

    If the method is GET,
    it returns the register page template.
    """
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
    """
    Removes the user from session,
    then redirects to the login page.
    """
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# 404 'page not found' error handler
### credits #9 (see README.md credits section) ###
@app.errorhandler(404)
def page_not_found(e):
    """
    Catches and handles a 404 error,
    by returning the 404 error page template.
    """
    return render_template("404_error.html"), 404


# 405 'method not allowed' error handler
### credits #9 (see README.md credits section) ###
@app.errorhandler(405)
def page_not_found(e):
    """
    Catches and handles a 405 error,
    by returning the 405 error page template.
    """
    return render_template("405_error.html"), 405


# 500 'internal server error' error handler
### credits #9 (see README.md credits section) ###
@app.errorhandler(500)
def page_not_found(e):
    """
    Catches and handles a 500 error,
    by returning the 500 error page template.
    """
    return render_template("500_error.html"), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get("DEBUG"))
