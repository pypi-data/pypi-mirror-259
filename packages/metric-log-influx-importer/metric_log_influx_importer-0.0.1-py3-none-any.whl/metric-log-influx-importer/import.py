import csv
from influxdb_client import InfluxDBClient, Point, WriteOptions
from datetime import datetime
import configparser

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')

INFLUXDB_URL = config.get('InfluxDB', 'URL')
INFLUXDB_TOKEN = config.get('InfluxDB', 'Token')
INFLUXDB_ORG = config.get('InfluxDB', 'Org')
INFLUXDB_BUCKET = config.get('InfluxDB', 'Bucket')
DATA_SOURCE = config.get('Data', 'Source')
DATA_FORMAT = config.get('Data', 'Format')

def import_csv_to_influxdb(file_path):
    """Imports CSV data to InfluxDB."""
    with InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=INFLUXDB_ORG) as client:
        write_api = client.write_api(write_options=WriteOptions(batch_size=1000, flush_interval=10_000))
        with open(file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                point = Point("metrics")\
                    .tag("host", row["host"])\
                    .field("usage", float(row["usage"]))\
                    .time(datetime.utcnow())
                write_api.write(bucket=INFLUXDB_BUCKET, org=INFLUXDB_ORG, record=point)

if __name__ == "__main__":
    if DATA_FORMAT.lower() == 'csv':
        import_csv_to_influxdb(DATA_SOURCE)
    else:
        print("Unsupported data format. Currently, only CSV is supported.")
