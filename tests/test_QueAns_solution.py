# Write a python program to create a table called Student with the below columns: - 
# SID - INT, PRIMARY KEY               SNAME - VARCHAR(20)         COURSE - VARCHAR(20)             MARKS - INT

def test_create_table_student(db_connection):
    cursor = db_connection.cursor()
    query = """
    CREATE TABLE Student(
    SID  INT PRIMARY KEY,
    SNAME  VARCHAR(20),       
    COURSE  VARCHAR(20),           
    MARKS  INT
    )
    """
    cursor.execute(query)
    db_connection.commit()
    print('Create table successfully')

# Write a python program to insert data in student table -
#   1,Rohit,Python,82    2,Rahul,Java,81     3,Ram,JavaScript,90        4,Raj,Python,90
def test_enter_table_student(db_connection):
    cursor = db_connection.cursor()
    query = """
    INSERT INTO Student (SID,SNAME,COURSE,MARKS)
    VALUES (?,?,?,?)
    """
    data = [
        (1,"Rohit","Python",82),    
        (2,"Rahul","Java",81),     
        (3,"Ram","JavaScript",90),        
        (4,"Raj","Python",90)
    ]
    cursor.executemany(query,data)
    db_connection.commit()
    print('Enter data into student table successfully')

# Update student id 3 and change the marks to 92
def test_update_table_student(db_connection):
    cursor = db_connection.cursor()
    query = """
    UPDATE Student 
    SET MARKS = ?
    WHERE SID = ?
    """
    cursor.execute(query,92,3)
    db_connection.commit()
    print('Updated data successfully')

# Delete student id 4
def test_delete_table_student(db_connection):
    cursor = db_connection.cursor()
    query = """
    DELETE FROM Student 
    WHERE SID = ?
    """
    cursor.execute(query,4)
    db_connection.commit()
    print('Delete data successfully')