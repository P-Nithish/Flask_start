students = {
         
         '18PT01':{'name':'name1','class':'18pt'},
         '18PT02':{'name':'name2','class':'18pt'},
         '18PD01':{'name':'name11','class':'18pd'}
         }



from flask import Flask

app = Flask(__name__)

# To get all student data:
@app.route("/students")
def get_students():
    return students

# To get particular student data:
@app.route("/students/<id>")
def get_student(id):
    return students[id]

'''
x='18PT03'
y={'name':'name3','class':'18pt'}

@app.route("/students")
def post_students(x,y):
    students[x]=y
    return students
'''  


if __name__ == "__main__":
    app.run()







'''
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/users")
def hello():
    return "<p>1234</p>"

if __name__ == "__main__":
    app.run()
'''