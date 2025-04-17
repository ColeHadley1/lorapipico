from machine import UART, Pin
import time

# Initialize UART0 (TX=GPIO0, RX=GPIO1) with 115200 baud rate
uart = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1))

def check_for_incoming_data():
    """Continuously check for incoming data and process it."""
    if uart.any():  # Check if there's data in the UART buffer
        incoming_data = uart.readline()  # Read the data from the buffer
        if incoming_data:  # Ensure data is not None
            print(f"Received: {incoming_data.decode('utf-8').strip()}")  # Decode and print
        else:
            print("No data received.")

# Main loop to receive data
print("Listening for incoming data...")
while True:
    check_for_incoming_data()  # Continuously check for incoming data
    time.sleep(0.1)  # Small delay 

