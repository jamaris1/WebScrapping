import mysql.connector
from mysql.connector import Error
from mysql.connector.errors import IntegrityError



class SQLThing:

    mydb = None

    def __init__(self):

        try:
            self.mydb = mysql.connector.connect(host="localhost", user="root", password="Audessous", database="gpu_scann", auth_plugin='mysql_native_password')
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")




    def commitURLS(self, URL, uPName, uPrice):
        mycursor = self.mydb.cursor()
        uBuyNow = 'andes-button__content'
        uAddCart = 'andes-button__content'
        prodID = 10000
        uAvailability = 1

        sql = "INSERT INTO URLS VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (URL, prodID, uPName, uBuyNow, uAddCart, uAvailability, uPrice)

        try:
            mycursor.execute(sql, val)
            self.mydb.commit()
            print("1 record inserted, ID:", mycursor.lastrowid)

        except IntegrityError as e:
            print(f"The error '{e}' occurred")

    def commitProduct(self, URL, uPName, uPrice):
        mycursor = self.mydb.cursor()
        uBuyNow = 'andes-button__content'
        uAddCart = 'andes-button__content'
        prodID = 10000
        uAvailability = 1

        sql = "INSERT INTO URLS VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (URL, prodID, uPName, uBuyNow, uAddCart, uAvailability, uPrice)

        try:
            mycursor.execute(sql, val)
            self.mydb.commit()
            print("1 record inserted, ID:", mycursor.lastrowid)

        except IntegrityError as e:
            print(f"The error '{e}' occurred")





    def commitOrderEvent(self, query):
        mycursor = self.mydb.cursor()
        sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        val = ("Michelle", "Blue Village")
        mycursor.execute(sql, val)

        self.mydb.commit()

        print("1 record inserted, ID:", mycursor.lastrowid)



    def __del__(self):
        self.mydb.close
