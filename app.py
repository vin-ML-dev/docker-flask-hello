from flask import Flask,render_template
import os
import pickle


app = Flask(__name__)

@app.route("/")
def hello():
   return render_template('home.html')


if __name__ == "__main__":
   #port = int(os.environ.get("PORT", 5000))
   app.run(host='0.0.0.0', port="5000")
