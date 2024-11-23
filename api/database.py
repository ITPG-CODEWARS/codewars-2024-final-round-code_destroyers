
import sqlite3

import utils

# Connect to database
db_config = utils.getFromConfig("database")
db_name = db_config.get('db_name', 'database')
hostname = db_config.get('hostname', 'localhost')
port = db_config.get('port', 27017)

conn = sqlite3.connect(f"{db_name}.db", check_same_thread=False)
cursor = conn.cursor()

# Create database table
database_base = '''
    CREATE TABLE IF NOT EXISTS urls (
        trainId TEXT PRIMARY KEY,
        routeStart TEXT NOT NULL,
        routeEnd TEXT NOT NULL,
        routeEstimate TEXT,
        bordingTime TEXT,
        departureTime TEXT NOT NULL,
        arrivalTime TEXT NOT NULL
    )
'''
cursor.execute(database_base)
conn.commit()

######################
# Database functions #
######################

def insert_train_data(data: utils.TrainObj) -> None:
    cursor.execute('INSERT INTO urls (trainId, routeStart, routeEnd, routeEstimate, bordingTime, departureTime, arrivalTime) VALUES (?, ?, ?, ?, ?, ?, ?)',
                   (data.routeId, data.routeStart, data.routeEnd, data.routeEstimate, data.bordingTime, data.departureTime, data.arrivalTime))
    conn.commit()

# def shortcode_exists(shortcode: str) -> bool:
#     cursor.execute('SELECT 1 FROM urls WHERE shortcode = ?', (shortcode,))
#     return cursor.fetchone() is not None


# def insert_url(url: str, shortcode: str = None):
#     if shortcode is None:
#         shortcode = generate_unique_shortcode()
    
#     cursor.execute('INSERT INTO urls (shortcode, url) VALUES (?, ?)', (shortcode, url))
#     conn.commit()
    
# # Generate a unique shortcode using hex representation of a UUID
# def generate_unique_shortcode() -> str:
#     while True:
#         shortcode = uuid.uuid4().hex[:utils.getFromConfig("short_url_length")]
#         if not shortcode_exists(shortcode):
#             return shortcode
    
# # Get URL from shortcode
# def get_url(shortcode) -> str:
#     cursor.execute('SELECT url FROM urls WHERE shortcode = ?', (shortcode,))
#     result = cursor.fetchone()
#     return result[0] if result else None

# # Get all URLs in a list of URLShortcode objects
# def get_all_urls() -> list[utils.URLShortcode]:
#     cursor.execute('SELECT * FROM urls')
#     return [utils.URLShortcode(url, shortcode, metadata) for shortcode, url, metadata in cursor.fetchall()]


# def update_url(shortcode, new_url) -> None:
#     cursor.execute('UPDATE urls SET url = ? WHERE shortcode = ?', (new_url, shortcode))
#     conn.commit()
    
    
# def delete_url(shortcode) -> None:
#     cursor.execute('DELETE FROM urls WHERE shortcode = ?', (shortcode,))
#     conn.commit()
    

# def purgeAllData() -> None:
#     cursor.execute('DROP TABLE urls')
#     conn.commit()
#     cursor.execute(database_base)
#     conn.commit()
    
# # Append metadata
# def appendMetadata(shortcode: str, key: str, value: str) -> None:
#     cursor.execute('SELECT metadata FROM urls WHERE shortcode = ?', (shortcode,))
#     metadata = cursor.fetchone()[0]
#     if metadata is None or metadata == 'None':
#         metadata = {}
#     else:
#         metadata = eval(metadata)
#     metadata[key] = value
#     cursor.execute('UPDATE urls SET metadata = ? WHERE shortcode = ?', (str(metadata), shortcode))
#     conn.commit()
    
# # Get metadata
# def getMetadata(shortcode: str) -> dict:
#     cursor.execute('SELECT metadata FROM urls WHERE shortcode = ?', (shortcode,))
#     metadata = cursor.fetchone()[0]
#     return eval(metadata) if metadata is not None else {}

# # Remove metadata
# def removeMetadata(shortcode: str, key: str) -> None:
#     cursor.execute('SELECT metadata FROM urls WHERE shortcode = ?', (shortcode,))
#     metadata = cursor.fetchone()[0]
#     if metadata is None or metadata == 'None':
#         return
#     metadata = eval(metadata)
#     if key in metadata:
#         metadata.pop(key)
#         cursor.execute('UPDATE urls SET metadata = ? WHERE shortcode = ?', (str(metadata), shortcode))
#         conn.commit()
        
# # Update metadata
# def updateMetadata(shortcode: str, key: str, value: str) -> None:
#     cursor.execute('SELECT metadata FROM urls WHERE shortcode = ?', (shortcode,))
#     metadata = cursor.fetchone()[0]
#     if metadata is None or metadata == 'None':
#         return
#     metadata = eval(metadata)
#     if key in metadata:
#         metadata[key] = value
#         cursor.execute('UPDATE urls SET metadata = ? WHERE shortcode = ?', (str(metadata), shortcode))
#         conn.commit()
        

# def hideUrl(shortcode: str) -> None:
#     appendMetadata(shortcode, 'hidden', True)


# Test the database functions    
if __name__ == '__main__':
    from main import main
    main()