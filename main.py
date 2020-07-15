from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/admin"
mongo = PyMongo(app)

#leos_collection = mongo.db.leos

#leos_collection.insert_one({'url' : 'https://media.discordapp.net/attachments/683191369237528609/709185080219664394/image0.png?width=740&height=851'})
#leos_collection.insert_one({'url' : 'https://images-ext-1.discordapp.net/external/jw78C8Xm_adTGtjf_KtrnDxNV3drQduEHjVVNw8A30Y/https/i.imgur.com/MLHYVFt.png'})
#leos_collection.insert_one({'url' : 'https://media.discordapp.net/attachments/683191369237528609/708047448240816188/image0.png?width=738&height=851'})
#leos_collection.insert_one({'url' : 'https://media.discordapp.net/attachments/683191369237528609/706782734646902836/unknown.png?width=312&height=851'})
#leos_collection.insert_one({'url' : 'https://images-ext-2.discordapp.net/external/skj1nr9de1nrDsXrpSWOzadS7ql9k5dVdr5gQvhYELU/https/i.imgur.com/JogqW1u.png'})


@app.route("/")
@app.route("/home")
def home():
    url_collection = mongo.db.leos.find()
    return render_template("home.html", items=url_collection.distinct('url'))


if __name__ == "__main__":
    app.run(debug=True)