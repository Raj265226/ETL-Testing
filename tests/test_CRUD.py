#-------Create User-----------
def create_user(db_connection, user_id, user_name, email):
    cursor = db_connection.cursor()
    query = """
    INSERT INTO source_users
    (user_id, user_name, email)
    VALUES (?, ?, ?)
    """
    cursor.execute(
        query,
        user_id,
        user_name,
        email
    )
    db_connection.commit()
    print("User Created Successfully")
# create_user(db_connection,4,"Amit","amit@gmail.com")

#------------------Get user by Id---------------
def get_user_by_id(db_connection, user_id):
    cursor = db_connection.cursor()
    cursor.execute("""
        SELECT *
        FROM source_users
        WHERE user_id = ?
    """, user_id)
    return cursor.fetchone()
print(get_user_by_id(db_connection, 1))

#---------Update User----------------
def update_user(db_connection,user_id,user_name,email):
    cursor = db_connection.cursor()
    query = """
    UPDATE source_users
    SET user_name = ?,
        email = ?
    WHERE user_id = ?
    """
    cursor.execute(query,user_name,email,user_id)
    db_connection.commit()
    print("User Updated Successfully")
# update_user(db_connection,1,"Rohit K","rohitk@ABC.com")

#----------------Delete User-------------
def delete_user(
db_connection,user_id):
    cursor = db_connection.cursor()
    cursor.execute("""
        DELETE
        FROM source_users
        WHERE user_id = ?
    """, user_id)
    db_connection.commit()
    print("User Deleted Successfully")
# delete_user(db_connection,4)