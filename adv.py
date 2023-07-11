from flask import Flask,request,render_template
import pickle
import re
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression
read = pickle.load(open("model.pkl","rb"))
app = Flask(__name__,template_folder="template")
@app.route("/")
def home():
    return render_template("sal.html")
@app.route("/pre" ,methods=["POST","GET"])
def prediction():
    TV = float(request.form["TV"])
    Radio = float(request.form["Radio"])
    Newspaper=float(request.form["Newspaper"])
    result = read.predict([[TV, Radio, Newspaper]])[0] * 100000
    return render_template("sal.html",**locals())
if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)