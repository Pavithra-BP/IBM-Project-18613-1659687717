import ibm_db
dictionary={}
def printTableData(conn):
    sql = "SELECT * FROM userdetails" out = ibm_db.exec_immediate(conn, sql)document =ibm_db.fetch_assoc(out) 
while:
    document != False:
        dictionary.update({document['EmailID']:document['password']})
        document = ibm_db.fetch_assoc(out)
def insertTableData(Firstname,Lastname,EmailID,password):
    sql="INSERT INTO userdetails(Firstname,Lastname,EmailID,password) VALUES ('{}','{}','{}','{}')".format(Firstname,Lastname,EmailID,password) out = ibm_db.exec_immediate(conn,sql) 
print('Number of affected rows : ',ibm_db.num_rows(out),"\n")
def updateTableData(Firstname,Lastname,EmailID,password):
    sql = "UPDATE userdetails SET ( Firstname,Lastname,email,password)=('{}','{}','{}') WHERE rollno={}".format(Firstname,Lastname,EmailID,password) out = ibm_db.exec_immediate(conn,sql) 
print('Number of affected rows : ', ibm_db.num_rows(out), "\n")
try:
    conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=2d46b6b4-cbf6-40eb-bbce-6251e6ba0300.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=32328;SECURITY=SSL;SSLServerCertificate=DigiCertGlo balRootCA.crt;PROTOCOL=TCPIP;UID=bjn03696;PWD=ef96tLJX2VjzaCPX;", "", "")
print("Db connected")
except:
    print("Error")