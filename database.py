import pyodbc

# Define the connection string
server = 'VOKO\SQLEXPRESS'
database = 'Pet Adoption System'
driver = '{ODBC Driver 17 for SQL Server}'  # This is the ODBC driver for SQL Server

# Construct the connection string
conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes'

# Establish a connection
connection = pyodbc.connect(conn_str)

# Function to execute SQL queries
def execute_query(query):
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows

# Function to execute SQL queries that modify data (INSERT, UPDATE, DELETE)
def execute_update(query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()

# Function to insert user into the database
def insert_user(username, email, password, address):
    query = f"INSERT INTO USERS (USER_USERNAME, USER_PASSOWRD, USER_EMAIL, USER_ADDRESS) VALUES ('{username}', '{password}', '{email}', '{address}')"
    execute_update(query)
