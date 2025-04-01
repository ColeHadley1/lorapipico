from machine import UART, Pin
import time

# Initialize UART0 (TX=GPIO0, RX=GPIO1) with 115200 baud rate
uart = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1))

wait_time = 1  # Adjust this if needed for specific commands

def send_command():
    """Send an AT command and handle the response."""
    command = input("Enter AT command: ").strip()  # Strip unnecessary whitespace
    if not command:  # Skip empty commands
        print("Command cannot be empty!")
        return

    uart.write(command + "\r\n")  # Send the AT command, \r\n is required by AT commands
    print(f"Sent: {command}")
    time.sleep(wait_time)  # Wait for the response
    
    if uart.any():  # Check if data is available
        response = uart.readline()  # Read the entire line
        if response:  # Make sure response is not None
            print(f"Response: {response.decode('utf-8').strip()}")
        else:
            print("No response received.")
    else:
        print("No data available from UART.")

# Main loop
print("Enter AT commands (type 'exit' to quit):")
while True:
    try:
        send_command()
    except KeyboardInterrupt:
        print("\nExiting...")
        break
    except Exception as e:
        print(f"Error: {e}")
