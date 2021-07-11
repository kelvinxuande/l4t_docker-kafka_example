import time
from json import loads
from kafka import KafkaConsumer
import logging

check_interval = 3
successfully_connected = False

def _setup_logger():
    ### see streamReceiver for complete example on comprehensive logging

    # get logger
    streamLogger = logging.getLogger(__name__)
    # set level
    streamLogger.setLevel(logging.INFO)
    # setup logger format
    formatter = logging.Formatter('%(asctime)s|%(name)s|%(message)s')
    # setup a stream handler
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    streamLogger.addHandler(stream_handler)

    return streamLogger

streamLogger = _setup_logger()

while not successfully_connected:
    try:
        consumer = KafkaConsumer(
                    'test',
                    bootstrap_servers='kafka-broker:9092',
                    # bootstrap_servers='localhost:19092',
                    auto_offset_reset='latest',
                    enable_auto_commit=True, 
                    group_id='consumer_group_1',
                    value_deserializer=lambda x: loads(x.decode('utf-8'))
                )
        successfully_connected = True
    except:
        # print("still waiting for connection")
        streamLogger.info("waiting for successful connection")
        time.sleep(check_interval)

for message in consumer:
    # print(message)
    streamLogger.info(message)
    # print("Treat new messages as trigger and do some processing with each message here")
    streamLogger.info("Treat new messages as trigger and do some processing with each message here")
