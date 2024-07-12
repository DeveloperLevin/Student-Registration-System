import mysql.connector as mysql
from tkinter import messagebox

def get_db_connection():
    return mysql.connect(
            host="localhost",
            user="root",
            passwd="123456",
            database="student",
            auth_plugin="mysql_native_password"
        )

def intializeDB():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        # SQL statement to create a table if it does not exist
        create_table_query = """
        CREATE TABLE IF NOT EXISTS student (
            roll_no INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            class VARCHAR(20) NOT NULL,
            section VARCHAR(20) NOT NULL,
            contact VARCHAR(20) UNIQUE NOT NULL,
            father VARCHAR(50),
            address VARCHAR(255) NOT NULL,
            gender VARCHAR(10),
            dob DATETIME
        )
        """
        cursor.execute(create_table_query)
        conn.commit()

    except mysql.Error as err:
        messagebox.showwarning("Error", str(e))

    finally:
        cursor.close()
        conn.close()

# Function to submit all entries to the database
def submitDB():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        #SQL query to insert into database

    