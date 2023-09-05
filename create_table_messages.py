import mysql.connector

db_config = {
    "user": "user",
    "password": "password",
    "host": "localhost",
    "database": "mqtt_data",
    "port": 3306
}

def create_table():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Create the table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mqtt_messages (
            id INT AUTO_INCREMENT PRIMARY KEY,
            topic VARCHAR(255) NOT NULL,
            payload TEXT,
            received_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    cursor.close()
    connection.close()

if __name__ == "__main__":
    create_table()
