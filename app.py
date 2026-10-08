from flask import Flask, request, render_template


general_posts = []
game_posts = []
tv_posts = []
book_posts = []

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/general/', methods = ["GET", "POST"])
def general():

  if request.method == "POST":
    name = request.form["name"]
    subject = request.form["subject"]
    post = request.form["post"]

    post_obj = {"name": name, "subject": subject, "post": post}
    general_posts.append(post_obj)
 
  return render_template("general.html", posts = general_posts)


@app.route('/games/', methods = ["GET", "POST"])
def games():
  return render_template('games.html')

@app.route('/tv/')
def tv():
  return render_template('tv.html')

@app.route('/books/')
def books():
  return render_template('books.html')

@app.route('/about/')
def about():
  return render_template('about.html')

if __name__ == "__main__":
  app.run()