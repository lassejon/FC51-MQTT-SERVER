import paho.mqtt.client as mqtt
import sqlite3
from datetime import datetime
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DB_FILE = "detections.db"

class DetectionSubscriber:
    def __init__(self):
        self.setup_database()
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_message = self.on_message
        
    def setup_database(self):
        try:
            with sqlite3.connect(DB_FILE) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS detections (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp TEXT,
                        detection_number INTEGER,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
            logger.info("Database setup complete")
        except Exception as e:
            logger.error(f"Database setup failed: {e}")
            raise

    def on_connect(self, client, userdata, flags, rc):
        logger.info(f"Connected with result code {rc}")
        client.subscribe("sensor/detections")

    def on_message(self, client, userdata, msg):
        try:
            data = msg.payload.decode()
            timestamp, detection_number = data.split(',')
            
            with sqlite3.connect(DB_FILE) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO detections (timestamp, detection_number)
                    VALUES (?, ?)
                """, (timestamp, detection_number))
                conn.commit()
            
            logger.info(f"Stored detection: {data}")
            
        except Exception as e:
            logger.error(f"Error processing message: {e}")

    def run(self):
        self.mqtt_client.connect("localhost", 1883, 60)
        logger.info("Starting MQTT loop...")
        self.mqtt_client.loop_forever()

if __name__ == "__main__":
    subscriber = DetectionSubscriber()
    subscriber.run()