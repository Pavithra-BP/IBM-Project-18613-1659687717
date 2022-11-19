from flask import
Flask,render_template,request,url_for,session app=Flask(__name__)
@app.route("/")
@app.route("/login",methods=['POST','GET'])
def login():
    if:
        request.method=="POST"
        printTableData(conn)
        username=request.form['EmailID']
        password=request.form['password']
        try:
            if dictionary[username] == password and username in dictionary:
                return "Logged in successfully"
            except:
                return "Invalid username or password"
            return
        render_template('login.html')
        @app.route("/register",methods=['POST','GET'])
        def register():
            if request.method=="POST":
                request.form['Firstname'] Firstname =
                request.form['Lastname'] Lastname =
                request.form['EmailID'] email =
                request.form['password'] password=
                insertTableData(Firstname,Lastname,EmailID, password)
                return
            render_template('login.html') 
    return
render_template('register.html')
if:
    __name__=="__main__":
app.run(debug=True)
late,request,url_for,session
app=Flask(__name__)
@app.route("/&quo t;)
@app.route("/login",methods=['POST','GET'])
def login():
    if:
        request.method=="POST":
            printTableData(conn)
            username=request.form['username']
            password=request.form['password']
            try:
                if dictionary[EmailID] == password and EmailID in dictionary:
                    return "Logged in successfully"
                except:
                    return "Invalid username or password" 
                return
            render_template('log’)