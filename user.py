import sqlite3

# Connect to the database
conn = sqlite3.connect('users.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute SQL query to fetch data from the users table
cursor.execute("SELECT * FROM users")

# Fetch all rows from the result set
rows = cursor.fetchall()

# Print the rows (or process them as needed)
for row in rows:
    print(row)

# Close the connection
conn.close()
