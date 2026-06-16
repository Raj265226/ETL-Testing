# ==========================
# FETCH DATA
# ==========================

GET_ALL_TARGET_USERS = """
SELECT *
FROM target_users
"""

GET_TARGET_USER_BY_ID = """
SELECT *
FROM target_users
WHERE user_id = ?
"""

# ==========================
# ETL VALIDATIONS
# ==========================

TARGET_RECORD_COUNT = """
SELECT COUNT(*)
FROM target_users
"""

TARGET_NULL_CHECK = """
SELECT *
FROM target_users
WHERE user_name IS NULL
"""

TARGET_DUPLICATE_CHECK = """
SELECT user_id,
       COUNT(*)
FROM target_users
GROUP BY user_id
HAVING COUNT(*) > 1
"""

TARGET_MAX_ID = """
SELECT MAX(user_id)
FROM target_users
"""

TARGET_MIN_ID = """
SELECT MIN(user_id)
FROM target_users
"""

TARGET_TOTAL_USERS = """
SELECT COUNT(*)
FROM target_users
"""

# ==========================
# SOURCE VS TARGET
# ==========================

MISSING_RECORDS = """
SELECT s.user_id
FROM source_users s
LEFT JOIN target_users t
ON s.user_id = t.user_id
WHERE t.user_id IS NULL
"""

DATA_MISMATCH = """
SELECT
       s.user_id,
       s.user_name AS source_name,
       t.user_name AS target_name
FROM source_users s
JOIN target_users t
ON s.user_id = t.user_id
WHERE s.user_name <> t.user_name
"""