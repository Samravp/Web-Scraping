from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)

@app.route("/")
def index():
    Mars_data = mongo.db.marspages.find_one()
    return render_template("index.html", Mars_data=Mars_data)

@app.route("/scrape")
def scraper():
    Mars_data = mongo.db.marspages
    Mars_data = scrape_mars.scrape()
    Mars_datas.update({}, Mars_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
