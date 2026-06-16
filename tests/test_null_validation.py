import json

#------Mock api response-------
with open(
    "mock_data/null_db.json"
) as file:
    api_users = json.load(file)
#------------Source users-------------
def test_source_null_validation(db_connection):
    cursor = db_connection.cursor()
    query = """
    SELECT *
    FROM source_users
    WHERE user_name IS NULL
       OR email IS NULL
    """
    cursor.execute(query)
    null_records = cursor.fetchall()
    print(f"\nTotal Null Records : {len(null_records)}")
    for record in null_records:
        print(record)
    assert len(null_records) == 0, \
        f"Null Records Found In Source Table: {null_records}"
#----------API Validation------------------
def test_api_null_validation():
    null_records = []
    for row in api_users:
        if row.get("user_name") is None:
            null_records.append(
                f"User ID {row['user_id']} has NULL user_name"
            )
        if row.get("email") is None:
            null_records.append(
                f"User ID {row['user_id']} has NULL email"
            )
    print(f"\nTotal Null Records : {len(null_records)}")
    for record in null_records:
        print(record)
    assert len(null_records) == 0,f"Null Records Found In API: {null_records}"