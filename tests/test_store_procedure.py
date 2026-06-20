#-----------Get data from Source users--------- 
#-----Mysql code---------
# CREATE PROCEDURE sp_get_all_users()
# BEGIN
#     SELECT *
#     FROM source_users;
# END
def test_sp_get_source_users(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("CALL sp_get_all_users();")
    source_count = cursor.fetchall()
    print(source_count)


#-----------Create Source users data--------- 
#-----Mysql code---------
# CREATE PROCEDURE sp_insert_user(
#     IN p_user_id INT,
#     IN p_user_name VARCHAR(100),
#     IN p_email VARCHAR(100)
# )
# BEGIN

#     INSERT INTO source_users
#     (
#         user_id,
#         user_name,
#         email
#     )
#     VALUES
#     (
#         p_user_id,
#         p_user_name,
#         p_email
#     );

# END
def test_sp_create_source_users(db_connection):
    cursor = db_connection.cursor()
#    cursor.execute("CALL sp_insert_user(4,'Amit','amit@gmail.com');")
    db_connection.commit()
    print("User Inserted Successfully")


#-----------Update for Source users--------- 
#-----Mysql code---------
# CREATE PROCEDURE sp_update_user(
#     IN p_user_id INT,
#     IN p_user_name VARCHAR(100),
#     IN p_email VARCHAR(100)
# )
# BEGIN

#     UPDATE source_users
#     SET
#         user_name = p_user_name,
#         email = p_email
#     WHERE user_id = p_user_id;

# END
def test_sp_update_source_users(db_connection):
    cursor = db_connection.cursor()
#    cursor.execute("CALL sp_update_user(4,'Amit K','amit@xyz.com');")
    db_connection.commit()
    print("User Updated Successfully")


#-----------Update for Source users--------- 
#-----Mysql code---------
# CREATE PROCEDURE sp_delete_user(
#     IN p_user_id INT
# )
# BEGIN

#     DELETE
#     FROM source_users
#     WHERE user_id = p_user_id;

# END
def test_sp_delete_source_users(db_connection):
    cursor = db_connection.cursor()
#    cursor.execute("CALL sp_delete_user(4);")
    db_connection.commit()
    print("User Deleted Successfully")