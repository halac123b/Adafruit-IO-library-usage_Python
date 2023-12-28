# Publishes an incrementing value to a feed

import time

# Import Adafruit IO REST client.
from Adafruit_IO import Client, Feed

# holds the count for the feed
run_count = 0

# Set to your Adafruit IO key and username
ADAFRUIT_IO_KEY = "aio_vZjz18MOcEb9ehFPCe25V9HOe9H1"
ADAFRUIT_IO_USERNAME = "halac123b"

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Create a new feed named 'counter'
# New feed must have unique name, not exist in your account already
feed = Feed(name="counter")
response = aio.create_feed(feed)

while True:
    print("sending count: ", run_count)
    run_count += 1
    # Publish data to feed
    aio.send_data("counter", run_count)
    # Adafruit IO is rate-limited for publishing
    # so we'll need a delay for calls to aio.send_data()
    time.sleep(3)
