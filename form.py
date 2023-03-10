from flask import Flask, redirect, render_template, request, url_for

app= Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_data", methods=["POST", "GET"])
def get_data():
    data=request.form
    marathi=float(data["html_marathi"])
    hindi=  float(data["html_hindi"])
    science=float(data["html_science"])
    maths=  float(data["html_maths"])
    history=float(data["html_history"])
    total_score=((marathi+hindi+science+maths+history)/500)*100

    return render_template("index.html", total=total_score) 


if __name__=="__main__":
    app.run()
  
