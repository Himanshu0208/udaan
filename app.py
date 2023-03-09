from flask import Flask , render_template , request
import logging as log
import pymongo
log.basicConfig(filename="form.log" , level=log.INFO)
app = Flask(__name__)

def checkUser(user):
    id = user["_id"]
    

@app.route("/",methods=["GET" , "POST"])
def hello_world():
    return render_template("index.html")

@app.route("/insert",methods=["POST"])
def submit():
    if(request.method == "POST"):

        # Making connection to data base
        try:
            client = pymongo.MongoClient("mongodb+srv://UDAAN:21001016029@udaan.cb8bko3.mongodb.net/?retryWrites=true&w=majority")
            db = client.udaan_contribution
        except Exception as e:
            log.error(e)
            f = "Connection to data base failed"
            return render_template("index.html",sucess="",fail=f)

        # Getting the form results
        name = request.form["name"]
        rollno = request.form["rollno"]
        contact = request.form["contact"]
        email = request.form["email"]
        course = request.form["course"]
        branch = request.form["branch"]
        company = request.form["company"]
        year = request.form["year"]
        questions = request.form.getlist("question")
        print(questions)
        # creating user
        user = {
            "_id" : rollno,
            "name" : name,
            "contact" : contact,
            "email" : email,
            "course" : course,
            "branch" : courses[branch]
        }
        collection_user = db.user
        if collection_user.count_documents({"_id" : rollno}) == 0:
            collection_user.insert_one(user)

        print("user created")
        # creating comany
        collection_questions = db.questions
        count = collection_questions.count_documents({"_id" : "/^${count}/"})
        print(count)
        questions_data = []
        for i in questions:
            a = str(count).zfill(3)
            ques =  {
                "_id" : f'{rollno}{a}',
                "question" : i,
                "company" : company,
                "year" : year
            }
            count = count + 1
            questions_data.append(ques)
        print("error in creating list")
        print("list is" , questions_data)
        collection_questions.insert_many(questions_data)
        print("error in inserting questions")
        return render_template("index.html",fail="",sucess="Thanks for you contribution")
    return render_template("index.html", sucess="" , failed="Failed")

if __name__=="__main__":
    courses = {
        "Computer" : "01",
        "Computer-with-data-science" : "02",
        "IT" : "03",
        "Civil" : "07",
        "Mechincal" : "04",
        "Electrical" : "05",
        "Electronic-and-computer" : "06",
        "Electronics-IOT" : "08",
        "RAI": "09",
        "BCA" : "10",
        "MCA" : "11",
        "MBA" : "12"
    }
    app.run(host="0.0.0.0")
