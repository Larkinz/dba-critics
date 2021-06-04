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


@app.route("/")
@app.route("/welcome")
def welcome():
    return render_template("welcome.html")


@app.route("/homepage")
def homepage():
    return render_template("homepage.html")


@app.route("/albums")
def albums():
    comments = list(mongo.db.comments.find())

    album001_vote_count = 0
    for x in mongo.db.ratings.find({"album_id": "001"}):
        album001_vote_count = album001_vote_count + 1

    album002_vote_count = 0
    for x in mongo.db.ratings.find({"album_id": "002"}):
        album002_vote_count = album002_vote_count + 1

    album003_vote_count = 0
    for x in mongo.db.ratings.find({"album_id": "003"}):
        album003_vote_count = album003_vote_count + 1

    album004_vote_count = 0
    for x in mongo.db.ratings.find({"album_id": "004"}):
        album004_vote_count = album004_vote_count + 1

    return render_template("albums.html",
                           comments=comments,
                           album001_vote_count=album001_vote_count,
                           album002_vote_count=album002_vote_count,
                           album003_vote_count=album003_vote_count,
                           album004_vote_count=album004_vote_count)


@app.route("/<album_id>", methods=["POST"])
def post_comment(album_id):
    if request.method == "POST":
        comment = {
            "comment": request.form.get(f"album_{album_id}_comment"),
            "album_id": f"{album_id}",
            "username": session["user"]
        }
        mongo.db.comments.insert_one(comment)
        return redirect(url_for('albums'))


@app.route("/edit_comment/<comment_id>/<album_id>", methods=["POST"])
def edit_comment(comment_id, album_id):
    if request.method == "POST":
        comment_edit = {
            "comment": request.form.get(f"album_{album_id}_comment_edit"),
            "album_id": f"{album_id}",
            "username": session["user"]
        }
        mongo.db.comments.update({"_id": ObjectId(comment_id)}, comment_edit)
        return redirect(url_for('albums'))


@app.route("/delete_comment/<comment_id>")
def delete_comment(comment_id):
    mongo.db.comments.remove({"_id": ObjectId(comment_id)})
    return redirect(url_for('albums'))


@app.route("/post_rating/<album_id>", methods=["POST"])
def post_rating(album_id):
    if request.method == "POST":
        # check if user album rating already exists in database
        existing_rating = mongo.db.ratings.find_one(
            {"$and": [{"username": session["user"]}, {"album_id": album_id}]})

        if existing_rating:
            rating_edit = {
                "rating": request.form.get(f"slider-album-{album_id}"),
                "album_id": f"{album_id}",
                "username": session["user"]
            }
            mongo.db.ratings.update(
                {"_id": existing_rating.get('_id')}, rating_edit)
            flash("You updated your rating!")
            return redirect(url_for('login'))

        rating = {
            "rating": request.form.get(f"slider-album-{album_id}"),
            "album_id": f"{album_id}",
            "username": session["user"]
        }
        mongo.db.ratings.insert_one(rating)
        flash("rating posted")
        return redirect(url_for('login'))


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


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username"),
            "password": generate_password_hash(request.form.get("password"), method='pbkdf2:sha512')
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username")
        flash("Registration complete!")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
