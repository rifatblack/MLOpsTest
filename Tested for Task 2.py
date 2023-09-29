#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Task 2: Working with databases
    
import sqlite3

conn = sqlite3.connect('users.db')

cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER
    )
''')

def add_user(name, email, age):
    cur.execute('INSERT INTO Users (name, email, age) VALUES (?, ?, ?)', (name, email, age))
    conn.commit()

def get_all_users():
    cur.execute('SELECT * FROM Users')
    return cur.fetchall()

def update_user(id, name, email, age):
    cur.execute('UPDATE Users SET name=?, email=?, age=? WHERE id=?', (name, email, age, id))
    conn.commit()

def delete_user(id):
    cur.execute('DELETE FROM Users WHERE id=?', (id,))
    conn.commit()

add_user('John Doe', 'john.doe@example.com', 30)
add_user('Jane Smith', 'jane.smith@example.com', 25)

print("All Users:")
print(get_all_users())

update_user(1, 'John Updated', 'john.doe.updated@example.com', 31)

print("All Users after update:")
print(get_all_users())

delete_user(2)

print("All Users after deletion:")
print(get_all_users())

conn.close()


# Explanation:

# Database Connection:
# The script establishes a connection to the SQLite database (or creates it if it doesn't exist) named "users.db".

# Table Creation:
# A "Users" table is created if it doesn't already exist, with columns for ID, name, email, and age.

# CRUD Operations:
# Create (Add User): add_user function inserts a new user into the Users table.
# Read (Get All Users): get_all_users function retrieves all users from the Users table.
# Update (Update User): update_user function modifies user data based on the user's ID.
# Delete (Delete User): delete_user function removes a user from the Users table based on the user's ID.

# Example Usage:
# Two users are added, then the first user's data is updated, and the second user is deleted.
# The state of the Users table is printed after each operation to demonstrate the CRUD operations.

# This structure allows for basic user data management with the ability to add, retrieve, update, and delete user records. SQLite is used here due to its simplicity and suitability for small-scale applications. For larger-scale applications or when there's a need for complex queries, other databases like PostgreSQL or MySQL might be more appropriate.


# In[ ]:




