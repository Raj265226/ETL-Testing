import json

#------Mock api response-------
with open(
    "mock_data/mock_duplicate_api_response.json"
) as file:
    api_users = json.load(file)
#--------Duplicate validation source---------
def test_source_duplicate_records(db_connection):
    cursor = db_connection.cursor()
    query = """
    SELECT
        user_id,
        COUNT(*) AS record_count
    FROM source_users
    GROUP BY user_id
    HAVING COUNT(*) > 1
    """
    cursor.execute(query)
    duplicates = cursor.fetchall()
    print(f"\nTotal Duplicate Records : {len(duplicates)}")
    for row in duplicates:
        print(
            f"User ID: {row[0]}, "
            f"Count: {row[1]}"
        )
    assert len(duplicates) == 0,f"Duplicate Records Found In Source Table: {duplicates}"
#--------Duplicate validation API---------
from collections import Counter
def test_api_duplicate_records():
    api_ids = [
        row["user_id"]
        for row in api_users
    ]
    duplicate_ids = [
        user_id
        for user_id, count in Counter(api_ids).items()
        if count > 1
    ]
    print(f"\nTotal Duplicate IDs : {len(duplicate_ids)}")
    print(f"Duplicate IDs : {duplicate_ids}")
    assert not duplicate_ids, f"Duplicate User IDs Found In API Response: {duplicate_ids}"