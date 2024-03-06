from flask import Flask,request,render_template,flash
import re
app = Flask(__name__)

################################################################
@app.route("/",methods=["GET", "POST"])
def index():
    str_name =  request.form.get("str_name")
    reg_exp = request.form.get("regular_exp")

    matches = []
    if reg_exp is None:
        return render_template("index.html")
    
    elif reg_exp is not None:
        match = re.findall(reg_exp,str_name)
        print(match)
        return render_template('index.html',message=match)
    else:
        return render_template('index.html',message="Match Not Found")



@app.route("/email_validation",methods=["GET", "POST"])    
def email_validation():
    mail_id = request.form.get("mail_id")
    if mail_id is None:
        return render_template("email_validation.html")
    elif bool(re.match(r"[^@]+@[^@]+\.[^@]+",mail_id)):
        return render_template("email_validation.html",message="Valid Email")
    else:
        return render_template("email_validation.html",message="Not a Valid Email id")

    
    
    

################################################################
if __name__ == "__main__":
    app.run(debug=True)
