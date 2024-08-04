from flask import Flask,render_template,url_for,request,redirect
import csv

app = Flask(__name__)

@app.route("/")
def my_web():
    return render_template('index.html')

@app.route("/<string:page_name>")
def about(page_name):
    return render_template(page_name)


def save_data(data):
    with open('C://Users//arhit//OneDrive//Desktop//my web//database.txt',mode='a') as db:
        email=data["email"]
        subject=data["subject"]
        chat=data["message"]
        print(f'\n{email},{subject},{chat}')
        db.write(f'\n{email},{subject},{chat}')

def save_csv(data):
    with open("C://Users//arhit//OneDrive//Desktop//my web//database.csv",'a',newline='') as file:
        email=data["email"]
        subject=data["subject"]
        chat=data["message"]
        file=csv.writer(file,delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        file.writerow([email,subject,chat])


@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
    if request.method=='POST':
        data=request.form.to_dict()
        save_data(data)
        save_csv(data)
        return redirect("/thankyou.html")
    else:
        return "Something went wrong"

