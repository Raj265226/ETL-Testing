#Yet to be done for API
#--------Record Count Validation--------
def test_source_target_count(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM source_users")
    source_count = cursor.fetchall()

    print(source_count)