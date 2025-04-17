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

def send_command(command: str):
    """Send an AT command and handle the response."""
    uart.write(command + "\r\n")  # Send the AT command, \r\n is required by AT commands
    print(f"Sent: {command}")
    time.sleep(0.2)
    

# Main thread for user input
print("****LoRa Tx and Rx****")
while True:
    try:
        user_input = input("Enter AT Command: ").strip()
        
        if not user_input:
            print("Command cannot be empty.")
            continue
        
        send_command(user_input)
    except KeyboardInterrupt:
        print("\nExiting...")
        break
    except Exception as e:
        print(f"Error: {e}")
