# ==========================
# CRUD QUERIES
# ==========================

GET_ALL_SOURCE_USERS = """
SELECT *
FROM source_users
"""

GET_SOURCE_USER_BY_ID = """
SELECT *
FROM source_users
WHERE user_id = ?
"""

INSERT_SOURCE_USER = """
INSERT INTO source_users
(user_id,user_name,email)
VALUES (?,?,?)
"""

UPDATE_SOURCE_USER = """
UPDATE source_users
SET user_name = ?,
    email = ?
WHERE user_id = ?
"""

DELETE_SOURCE_USER = """
DELETE
FROM source_users
WHERE user_id = ?
"""

# ==========================
# ETL VALIDATIONS
# ==========================

SOURCE_RECORD_COUNT = """
SELECT COUNT(*)
FROM source_users
"""

SOURCE_NULL_CHECK = """
SELECT *
FROM source_users
WHERE user_name IS NULL
OR email IS NULL
"""

SOURCE_DUPLICATE_CHECK = """
SELECT user_id,
       COUNT(*)
FROM source_users
GROUP BY user_id
HAVING COUNT(*) > 1
"""

INVALID_EMAIL_CHECK = """
SELECT *
FROM source_users
WHERE email NOT LIKE '%@%'
"""

SOURCE_MAX_ID = """
SELECT MAX(user_id)
FROM source_users
"""

SOURCE_MIN_ID = """
SELECT MIN(user_id)
FROM source_users
"""

SOURCE_TOTAL_USERS = """
SELECT COUNT(*)
FROM source_users
"""