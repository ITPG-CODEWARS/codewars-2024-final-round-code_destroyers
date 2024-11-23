
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
        routeID TEXT PRIMARY KEY NOT NULL,
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
                   (data.routeID, data.routeStart, data.routeEnd, data.routeEstimate, data.bordingTime, data.departureTime, data.arrivalTime))
    conn.commit()

    
def get_train_data(routeID: str) -> utils.TrainObj:
    cursor.execute('SELECT * FROM urls WHERE trainId = ?', (routeID,))
    result = cursor.fetchone()
    return utils.TrainObj(result[0], result[1], result[2], result[3], result[4], result[5], result[6]) if result else None


def get_train_data(routeStart: str, routeEnd: str) -> utils.TrainObj:
    cursor.execute('SELECT * FROM urls WHERE routeStart = ? AND routeEnd = ?', (routeStart, routeEnd))
    result = cursor.fetchone()
    return utils.TrainObj(result[0], result[1], result[2], result[3], result[4], result[5], result[6]) if result else None


def get_all_train_data() -> list[utils.TrainObj]:
    cursor.execute('SELECT * FROM urls')
    return [utils.TrainObj(routeID, routeStart, routeEnd, routeEstimate, bordingTime, departureTime, arrivalTime) for routeID, routeStart, routeEnd, routeEstimate, bordingTime, departureTime, arrivalTime in cursor.fetchall()]


def delete_train_data(routeID: str) -> None:
    cursor.execute('DELETE FROM urls WHERE trainId = ?', (routeID,))
    conn.commit()


# Test the database functions    
if __name__ == '__main__':
    from main import main
    main()