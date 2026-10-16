import mysql.connector

class Messaging:
    def __init__(self):
        self.mydb = mysql.connector.connect(
          host="127.0.0.1",
          port=3305,
          user="root",
          password="Mysql1234"
        )

        self.cur = self.mydb.cursor()
        self.cur.execute('use Messaging;')
    def new(self,username):
        self.cur.execute('select user_id from accounts where username="{}";'.format(username))
        return self.cur.fetchall()
    
msg = Messaging()
a = msg.new("kanti")
for i in a:
  for z in i:
    print(z)