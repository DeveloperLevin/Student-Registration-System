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
        messagebox.showerror("Error", str(e))
        conn.rollback()

    finally:
        cursor.close()
        conn.close()

# Function to submit all entries to the database
def submitDB(data):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        #SQL query to insert into database
        insert_query = """
        INSERT INTO student(roll_no, name, class, section, contact, father, address, gender, dob)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(insert_query, data)
        conn.commit()
    
    except mysql.Error as err:
        messagebox.showerror("Error", str(err))
        conn.rollback()

    else:
        messagebox.showinfo("Success", "Data Inserted Successfully")
    
    finally:
        cursor.close()
        conn.close()
    
def deleteDB(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        #SQL query to insert into database
        delete_query = """
        DELETE FROM student WHERE roll_no = %s
        """

        cursor.execute(delete_query, (id,))
        conn.commit()
    
    except mysql.Error as err:
        messagebox.showerror("Error", str(err))
        conn.rollback()

    else:
        messagebox.showinfo("Success", "Data Deleted Successfully")

    finally:
        cursor.close()
        conn.close()

def updateDB():
    return