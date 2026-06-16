import json

#------Mock api response-------
with open(
    "mock_data/mock_api_response.json"
) as file:
    api_users = json.load(file)

#--------Record Count Validation--------
def test_source_target_count(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM source_users")
    source_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM target_users")
    target_count = cursor.fetchone()[0]
    print(f"Source Count : {source_count}")
    print(f"Target Count : {target_count}")
    assert source_count == target_count,f"Record Count Mismatch. Source = {source_count}, Target = {target_count}"

#-------Name validation--------
def test_source_target_name_match(db_connection):
    cursor = db_connection.cursor()
    query = """
    SELECT
        s.user_id,
        s.user_name AS source_name,
        t.user_name AS target_name
    FROM source_users s
    INNER JOIN target_users t
        ON s.user_id = t.user_id
    WHERE s.user_name <> t.user_name
    """
    cursor.execute(query)
    mismatches = cursor.fetchall()
    print(f"\nTotal Name Mismatches : {len(mismatches)}")
    for row in mismatches:
        print(
            f"User ID: {row[0]}, "
            f"Source Name: {row[1]}, "
            f"Target Name: {row[2]}"
        )
    assert len(mismatches) == 0,f"Name Mismatch Found. Total Mismatches = {len(mismatches)}"
# #--------API and Source data---------------
def test_source_api_data_match(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("""
        SELECT
            user_id,
            user_name,
            email
        FROM source_users
    """)
    source_users = cursor.fetchall()
    api_dict = {
        row["user_id"]: row
        for row in api_users
    }
    mismatches = []
    for source in source_users:
        source_id = source[0]
        source_name = source[1]
        source_email = source[2]
        api_record = api_dict.get(source_id)
        if not api_record:
            mismatches.append(
                f"User ID {source_id} Missing In API"
            )
            continue
        if source_name != api_record["user_name"]:
            mismatches.append(
                f"User ID {source_id} Name Mismatch "
                f"(DB={source_name}, API={api_record['user_name']})"
            )
        if source_email != api_record["email"]:
            mismatches.append(
                f"User ID {source_id} Email Mismatch "
                f"(DB={source_email}, API={api_record['email']})"
            )
    print("\nTotal Mismatches:", len(mismatches))
    for mismatch in mismatches:
        print(mismatch)
    assert len(mismatches) == 0,f"Source vs API Validation Failed. Mismatches Found = {len(mismatches)}"