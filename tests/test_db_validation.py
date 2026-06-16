from database.db_connection import get_connection
def test_database_and_table_validation():

    conn = get_connection()
    cursor = conn.cursor()

    print("\n----------FETCHING ALL DATABASES----------")
    cursor.execute("SHOW DATABASES")
    databases = cursor.fetchall()

    db_names = [db[0] for db in databases]  
    print(db_names)

    print("---------CHECKING IF etl_testing EXISTS--------")

    db_names = [db[0] for db in databases]

    if "etl_testing" in db_names:
        print("etl_testing database found")
    else:
        print("etl_testing database NOT found")
        return

    print("----------FETCHING ALL TABLES----------")
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()

    for table in tables:
        print(table[0])

    print("----------FETCHING DATA FROM source_users---------")

    cursor.execute("SELECT * FROM source_users")

    source_records = cursor.fetchall()

    if source_records:
        for row in source_records:
            print(row)
    else:
        print("No records found in source_users")

    print("-------FETCHING DATA FROM target_users--------")

    cursor.execute("SELECT * FROM target_users")

    target_records = cursor.fetchall()

    if target_records:
        for row in target_records:
            print(row)
    else:
        print("No records found in target_users")

    conn.close()