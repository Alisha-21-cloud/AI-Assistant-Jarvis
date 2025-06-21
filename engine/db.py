import csv
import re
import sqlite3

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'one note', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.exe')"
# cursor.execute(query)
# con.commit()

# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)

# cursor.execute("INSERT INTO web_command VALUES (null, 'hackerrank', 'https://www.hackerrank.com/')")
# con.commit()

# testing module
# app_name = "word"
# cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
# results = cursor.fetchall()
# print(results[0][0])



# 1. Create contacts Table 

# Create a table with the desired columns
# cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')


# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
# desired_columns_indices = [0, 1, 2, 20]

# # Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         first, middle, last, phone = [row[i] for i in desired_columns_indices]
#         full_name = " ".join(part for part in [first, middle, last] if part.strip())
#         cursor.execute(
#             '''INSERT INTO contacts (id, name, mobile_no) VALUES (null, ?, ?)''',
#             (full_name, phone)
#         )

# Commit changes and close connection
# con.commit()
# con.close()

# Get all contacts
# cursor.execute("SELECT id, mobile_no FROM contacts")
# rows = cursor.fetchall()

# for contact_id, phone in rows:
#     if phone:
#         # This finds the first group of digits, optionally starting with +
#         match = re.search(r"(\+?\d+)", phone)
#         if match:
#             cleaned = match.group(1)  # First valid number
#             cursor.execute(
#                 "UPDATE contacts SET mobile_no = ? WHERE id = ?",
#                 (cleaned, contact_id)
#             )

# con.commit()
# con.close()

# print("✅ All mobile numbers cleaned using regex.")

# cursor.execute("DELETE FROM contacts")  # Deletes all rows but keeps table structure
# con.commit()
# con.close()

# print("✅ All contacts deleted from database.")

# desired_columns_indices = [0, 1, 2, 20]  # First Name, Middle, Last, Phone

# ✅ Step: Read and insert cleaned data
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     next(csvreader)  # Skip header row

#     for row in csvreader:
#         try:
#             first, middle, last, raw_phone = [row[i] for i in desired_columns_indices]
#             full_name = " ".join(part for part in [first, middle, last] if part.strip())

#             # ✅ Clean phone number
#             raw_phone = raw_phone.split(":::")[0].strip()

#             # Handle scientific notation like 9.1906E+11
#             try:
#                 if 'e' in raw_phone.lower():
#                     raw_phone = str(int(float(raw_phone)))
#             except:
#                 pass

#             # Remove all non-digit characters (except + at beginning)
#             cleaned_phone = re.sub(r"[^\d+]", "", raw_phone)

#             # ✅ Insert into DB
#             cursor.execute(
#                 "INSERT INTO contacts (id, name, mobile_no) VALUES (null, ?, ?)",
#                 (full_name, cleaned_phone)
#             )
#         except Exception as e:
#             print(f"⚠️ Skipped row due to error: {e}")

# # ✅ Final commit and close
# con.commit()
# con.close()

# print("✅ Contacts re-imported and cleaned successfully.")

# def remove_emojis(text):
#     emoji_pattern = re.compile(
#         "["
#         u"\U0001F1E6-\U0001F1FF"  # flags
#         u"\U0001F300-\U0001F5FF"  # symbols & pictographs
#         u"\U0001F600-\U0001F64F"  # emoticons
#         u"\U0001F680-\U0001F6FF"  # transport & map symbols
#         u"\U0001F700-\U0001F77F"  # alchemical symbols
#         u"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
#         u"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
#         u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
#         u"\U0001FA00-\U0001FA6F"  # Chess symbols, tools
#         u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
#         u"\U00002702-\U000027B0"  # Dingbats
#         u"\U000024C2-\U0001F251"
#         u"\U0001f926-\U0001f937"
#         u"\u200d"                 # Zero Width Joiner
#         u"\u2640-\u2642"
#         u"\u2600-\u2B55"
#         u"\u23cf"
#         u"\u23e9"
#         u"\u231a"
#         u"\ufe0f"                 # Dingbats variation selector
#         u"\u3030"
#         "]+",
#         flags=re.UNICODE
#     )
#     return emoji_pattern.sub(r'', text).strip()

# # Fetch all contact names
# cursor.execute("SELECT id, name FROM contacts")
# rows = cursor.fetchall()

# # Clean each name and update the table
# for contact_id, name in rows:
#     cleaned_name = remove_emojis(name)
#     cursor.execute(
#         "UPDATE contacts SET name = ? WHERE id = ?",
#         (cleaned_name, contact_id)
#     )

# # Save changes
# con.commit()
# con.close()

# print("✅ All contact names cleaned of emojis.")

# # 1. Remove exact duplicates (same name + mobile_no)
# cursor.execute("""
#     DELETE FROM contacts
#     WHERE id NOT IN (
#         SELECT MIN(id) FROM contacts
#         GROUP BY name, mobile_no
#     )
# """)

# # 2. Remove name duplicates with empty or NULL mobile numbers (if number already exists once)
# cursor.execute("""
#     DELETE FROM contacts
#     WHERE mobile_no IS NULL OR TRIM(mobile_no) = ''
#     AND name IN (
#         SELECT name FROM contacts
#         GROUP BY name
#         HAVING COUNT(*) > 1
#     )
# """)


# con.commit()
# con.close()

# print("✅ Duplicate contacts cleaned successfully.")

# Delete contacts with NULL or empty mobile_no
# cursor.execute("""
#     DELETE FROM contacts
#     WHERE mobile_no IS NULL
#        OR TRIM(mobile_no) = ''
# """)

# con.commit()
# con.close()

# print("✅ All contacts without a mobile number have been removed.")

# cursor.execute("""
#     UPDATE contacts
#     SET name = 'Dad'
#     WHERE name = 'Abba'
# """)

# con.commit()
# con.close()

#### 5. Search Contacts from database

# query = 'Rahul'
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(results[0][0])



