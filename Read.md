ETL - Extract Transform Load
Flow - Source_DB -> Extract -> Transform -> Target_DB
Example - Suppose bank app stores customer data -           Transformation rule - co. wants salary in yearly_format
        Source_Table =>     id      name    salary                      Target_Table =>     id      name    salary
                            1       Raj     50000                                           1       Raj     600000
                            2       Rahul   60000                                           2       Rahul   720000
Above movement - Source -> Transformation -> Target, is called ETL. Data can be corrupted during migration. If source has Rohit and
                if that is missing then ETL testing catches that issue.
ETL Tester does - validate source data , validate transformation logic , validate target data

ETL Testing - It's the process of validating data during Extract, Transform, and Load operations. We ensure that data 
              is extracted correctly from the source, transformed according to business rules, and loaded accurately 
              into the target system without data loss, duplication, or corruption.
Real-time ETL Flow - Orders_Db -> ETL Jobs -> Data Warehouse -> Power BI Dashboard
                    If it fails - Dashboard show wrong sales , Management takes wrong decision
Pyodbc in ETL Testing - Used pyodbc to connect Python automation scripts with MySQL. Data was extracted from APIs 
                using requests, loaded into target tables, and validated using SQL queries. Performed record count validation, null checks, duplicate checks, source-to-target comparison, and business rule validation. The validations were automated using pytest and pyodbc cursor operations
Aggregate Validation - It verifies summarized data between source and target systems using functions like COUNT, SUM, AVG, 
                   MIN and MAX. It helps ensure that data has been loaded correctly without comparing every individual row.
---------------------------------SQL connection Setup------------------
import pyodbc
def get_connection():
    conn = pyodbc.connect(
        "DRIVER=MySQL ODBC 9.7 Unicode Driver;"
        "SERVER=localhost;"
        "DATABASE=etl_testing;"
        "UID=root;"
        "PWD=root123;"
    )
    return conn
----------FETCHING ALL DATABASES----------
conn = get_connection()
cursor = conn.cursor()
cursor.execute("SHOW DATABASES")
databases = cursor.fetchall()
db_names = [db[0] for db in databases]  
print(db_names)
---------CHECKING IF etl_testing EXISTS--------
if "etl_testing" in db_names:
    print("etl_testing database found")
else:
    print("etl_testing database NOT found")
    return
----------FETCHING ALL TABLES----------
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()
for table in tables:
    print(table[0])
----------FETCHING DATA FROM source_users---------
cursor.execute("SELECT * FROM source_users")
source_records = cursor.fetchall()
if source_records:
   for row in source_records:
        print(row)
else:
    print("No records found in source_users")
conn.close()