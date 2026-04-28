import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS regtb (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Age TEXT NOT NULL,
            Mobile TEXT NOT NULL,
            Email TEXT NOT NULL,
            Address TEXT NOT NULL,
            UserName TEXT NOT NULL,
            Password TEXT NOT NULL
        )
    ''')

    # Check if data already exists
    cursor.execute("SELECT COUNT(*) FROM regtb")
    if cursor.fetchone()[0] == 0:
        # Insert sample data
        sample_data = [
            ('sangeeth Kumar', '20', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'san', 'san'),
            ('sangeeth Kumar', '20', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'muzammin', 'muzammin'),
            ('sangeeth Kumar', '20', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'san12', 'san12'),
            ('varsha', '40', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'varsha', 'varsha')
        ]
        cursor.executemany('''
            INSERT INTO regtb (Name, Age, Mobile, Email, Address, UserName, Password)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', sample_data)

    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == "__main__":
    init_db()
