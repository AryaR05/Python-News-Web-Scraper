import sqlite3 as sq


class NewsDatabase:

# Get database name
    def __init__(self, db_name="news_database.db"):
        self.db_name = db_name

# Creating the initial database object
    def __enter__(self):
        self.conn = sq.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.setup_db()
        return self
    
# Save the information and close the connection to the database, and if there's an error, roll back all changes to their state before the error and close the connection
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.conn.rollback()
        else:
            self.conn.commit()
        self.conn.close()

# Creating the database structure, tables, and columns...
    def setup_db(self):

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS news(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            web_name TEXT,
            category TEXT,
            title TEXT NOT NULL,
              description TEXT,
                url TEXT UNIQUE NOT NULL,
                  image_url TEXT,
                  published_date TEXT,
                  sent_status INTEGER DEFAULT 0
                  )
                  """)

# Saving information in the database
    def save_news(self,web_name,category, title, description, url,image_url, published_date):

        self.cursor.execute(
            """ 
            INSERT OR IGNORE INTO news(web_name,category,title, description, url, image_url, published_date )
              VALUES (?,?,?,?,?,?,?) 
              """, (web_name, category, title, description, url, image_url, published_date))
    
# Checking if the news is not a duplicate through the news link
    def check_exists_news(self,url):
        self.cursor.execute("SELECT id FROM news WHERE url = ?",(url,))
        return self.cursor.fetchone() is not None

# The two functions below were designed to send news to other platforms in the future

# Marking Sent News
#    def mark_as_sent(self,url):
#        self.cursor.execute("UPDATE news SET sent_status = 1 WHERE url = ?",(url,))

# Receiving Unsent News
#    def get_unsent_news(self):
#        self.cursor.execute("SELECT id, title, description, url, FROM news WHERE sent_status= 0")
#        return self.cursor.fetchall()
        
