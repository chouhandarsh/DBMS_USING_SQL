import mysql.connector
import sys
class DBhelper:
    def __init__(self):
        try:
            self.conn=mysql.connector.connect(host="localhost", user="root",password="",database="dbms_demo")
            self.mycursor=self.conn.cursor()
        except Exception as e:
            print("Some error occurred, can't connect to the database:", e)
            sys.exit(0)
        else:
            print("Connected to database")
    def register(self, name, email, password):
        """Insert a new user record.

        Returns True on success or False on failure. The caller can then
        decide how to respond. The SQL column names must match the actual
        schema; adjust `password` below if your table uses a different name
        (e.g. `passwd`, `pwd`). If the table name or column names conflict
        with MySQL keywords, quote them with backticks or rename the table.
        """
        try:
            # make sure the column names exist in your `user` table;
            # change `password` if necessary.
            self.mycursor.execute(
                "INSERT INTO `user` (name, email, password) VALUES (%s, %s, %s)",
                (name, email, password),
            )
            self.conn.commit()
            return True
        except Exception as e:
            print("Error inserting data:", e)
            return False
    
    def login(self, email, password):
        """Check credentials and return True/False."""
        try:
            self.mycursor.execute(
                "SELECT * FROM `user` WHERE email=%s AND password=%s",
                (email, password),
            )
            result = self.mycursor.fetchone()
            return bool(result)
        except Exception as e:
            print("Error during login:", e)
            return False

    
