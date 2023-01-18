from flask import Flask, render_template, request, jsonify
import pymysql  
pymysql.install_as_MySQLdb()
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] ="localhost"
app.config['MYSQL_USER'] ="root"
app.config['MYSQL_PASSWORD'] ="root1234"
app.config['MYSQL_DB'] ="flaskapp"

mysql = MySQL(app)

# @app.route('/users', methods=['POST'])
# def users():
#     # if(request.method =='POST'):
#     res = request.get_json()
#     name = res["name"]
#     email = res["email"]
#     cur = mysql.connection.cursor()
#     cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)",[name, email])
#     mysql.connection.commit()
#     cur.close()
#     return f"done"

    #user registration details into databse
@app.route('/usersRegistration', methods=['POST'])
def users():
    # if(request.method =='POST'):
    res = request.get_json()
    username = res["username"]
    email = res["email"]
    firstname = res["firstname"]
    lastname = res["lastname"]
    password = res["password"]
    type=res["type"]
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO registration (username,email,first_name,last_name,password,type) VALUES (%s, %s, %s, %s, %s, %s)",[username, email,firstname,lastname,password,type])
    mysql.connection.commit()
    cur.close()
    return f"done"


       #admins details into databse
@app.route("/adminsDetails", methods=['POST'])
def admins():
    # if(request.method =='POST'):
    res = request.get_json()
    title = res["title"]
    description = res["description"]
    assignto = res["assignto"]
    startdate = res["startdate"]
    enddate = res["enddate"]
    deadline=res["deadline"]
    status=res["status"]
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO task (title,description,assignto,start_date,end_date,deadline,task_status) VALUES (%s, %s, %s, %s, %s, %s, %s)",[title,description,assignto,startdate,enddate,deadline,status])
    mysql.connection.commit()
    cur.close()
    return f"done"

@app.route('/login', methods=['GET'])    
def login():
    # if request.args.get('username'):
        username = request.args.get('username')
        cur =mysql.connection.cursor()
        cur.execute(''' SELECT password,type,username FROM registration where username like (%s) ''', [username])
        value= cur.fetchall()
        cur.close()
        return jsonify(value) 

#to get id and name of then user 


@app.route('/getAdminDetails', methods=['GET'])    
def admindetails():
    # if request.args.get('username'):
        assignto = request.args.get('assignto')
        cur =mysql.connection.cursor()
        cur.execute(''' SELECT id, assignto FROM task where assignto like (%s) ''', [assignto])
        value= cur.fetchall()
        cur.close()
        return jsonify(value) 

@app.route('/getAdminUsers', methods=['GET'])    
def adminUserdetails():
    # if request.args.get('username'):
        
        cur =mysql.connection.cursor()
        cur.execute(''' SELECT username FROM registration where type="users" ''')
        value= cur.fetchall()
        cur.close()
        return jsonify(value)      

@app.route('/getassigntousers123', methods=['GET'])    
def assigntouserdetails():
    # if request.args.get('username'):
        
        cur =mysql.connection.cursor()
        cur.execute(''' SELECT assignto FROM task ''')
        value= cur.fetchall()
        cur.close()
        return jsonify(value)            
# usersdetails for task particular user!!

@app.route('/givingtasktouser', methods=['GET'])    
def taskassignment():
    # if request.args.get('username'):
        username = request.args.get('username')
        cur =mysql.connection.cursor()
        cur.execute(''' SELECT id,title,description,assignto,start_date,end_date,deadline,task_status FROM task where assignto like (%s) ''', [username])
        value= cur.fetchall()
        cur.close()
        return jsonify(value) 

#method to update the task of and particular user
@app.route("/updatestatusofuser", methods=['POST'])
def updatestatus():
    res = request.get_json()
    newstatus = res["newstatus"]
    id = res["id"]
    cursor = mysql.connection.cursor()
    cursor.execute(
        ''' update tasks set taskstatus = (%s) where id = (%s)''',[newstatus, id]
    )
    mysql.connection.commit()
    cursor.close()
    return f"Done!!"        
    
if(__name__=="__main__"):
     app.run(debug=True)
