from flask import Flask,request
import mysql.connector
import json

app = Flask(__name__)

mydb = mysql.connector.connect(
  host="10.64.11.1",
  user="root",
  password="yazlab123",
  database="users"
)

mycursor = mydb.cursor()

@app.route("/users",methods=['GET','POST','PUT','DELETE'])
def add_or_get_users():
    if(request.method=='GET'):
       
       mycursor.execute("SELECT * FROM users")
       myresult = mycursor.fetchall()
       return json.dumps(myresult)
    
    if(request.method=='POST'):
      input_json = request.get_json(force=True) 
      
      firstname=input_json['firstname']
      lastname=input_json['lastname']
      password=input_json['password']
      
      sql_query="INSERT INTO users (name, surname, password) VALUES (%s,%s,%s)"
      val=(firstname,lastname,password)
      mycursor.execute(sql_query,val)
      mydb.commit()
      
      return str(mycursor.rowcount)+" record inserted to db"

    if(request.method=='PUT'):
      try:
        input_json = request.get_json(force=True) 
        id=input_json['id']
        firstname=input_json['firstname']
        lastname=input_json['lastname']
        password=input_json['password']

        sql = "UPDATE users SET name = %s, surname = %s, password = %s WHERE id = %s"
        values=(firstname,lastname,password,id)
        mycursor.execute(sql,values)
        mydb.commit()
        return str(mycursor.rowcount)+" record affected."
      except:
        return "User is not found!"

      
    if(request.method=='DELETE'):
        try:
          input_json = request.get_json(force=True) 
          id=input_json['id']
          sql = "DELETE FROM users WHERE id = %s"
          mycursor.execute(sql,(id,))
          mydb.commit()
          return str(mycursor.rowcount)+" record deleted."
        except:
          return 'User is not found!' 
@app.route("/")
def hello_world():
    return "<p> Hello </p>"
  
@app.route("/healthcheck",methods=['GET'])
def healthcheck():
    try: 
      mycursor.execute("SELECT * FROM users")
      myresult = mycursor.fetchall()
      return "Healthy"
    except:
      return "Unhealthy"
  
  @app.route("/apinfo")
def get_api_info():
    return "<p> Hello! This api doing user crud process. </p>"
  
  
if __name__ == '__main__':
  app.run("0.0.0.0",debug=True,port=5001)