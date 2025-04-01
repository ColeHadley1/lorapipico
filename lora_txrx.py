from machine import UART, Pin
import _thread
import time

# Initialize UART0 (TX=GPIO0, RX=GPIO1) with 115200 baud rate
uart = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1))

# Thread to continuously receive data
def receive_thread():
    while True:
        if uart.any():  # Check if data is available in the UART buffer
            incoming_data = uart.readline()  # Read the data
            if incoming_data:
                print(f"\nReceived: {incoming_data.decode('utf-8').strip()}")  # Decode and display
        time.sleep(0.1)  # Small delay to prevent excessive CPU usage

# Start the receive thread
_thread.start_new_thread(receive_thread, ())

# Main thread for user input
print("Listening for incoming data. Type messages to send them:")
while True:
    try:
        # Get user input for sending data
        message = input("Enter a message to send: ").strip()
        if message:  # If a message is entered
            uart.write(message + "\r\n")  # Send the message
            print(f"Sent: {message}")
    except KeyboardInterrupt:
        print("\nExiting...")
        break
    except Exception as e:
        print(f"Error: {e}")
