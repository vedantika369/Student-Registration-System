from flask import Flask,request,render_template
app=Flask(__name__)

students=[]

@app.route("/",methods=["GET","POST"])
def home():

    message=""
    if request.method=="POST":
        student={
            "name":request.form["name"],
            "roll":request.form["roll"],
            "branch":request.form["branch"],
            "mobile":request.form["mobile"]
        }
        students.append(student)

        message = "Student Registered Successfully!"

    return render_template(
        "index.html",
        students=students,
        message=message
    )
    
if __name__=="__main__":
    app.run(debug=True)