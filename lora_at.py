from machine import UART, Pin
import time

# Initialize UART0 (TX=GPIO0, RX=GPIO1) with 115200 baud rate
uart = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1))

wait_time = 0.5  

def send_command(command: str) -> str:
    """Send an AT command and handle the response."""
    uart.write(command + "\r\n")  # Send the AT command, \r\n is required by AT commands
    print(f"Sent: {command}")
    
    time.sleep(wait_time)  # Wait for the response
    
    if uart.any():  # Check if there's data in the UART buffer
        response = uart.readline()  # Read the data from the buffer
    else:
        print("No data available from UART.")
    
    return response

# Main loop
print("LoRa AT Command Interface")
while True:
    try:
        user_input = input("Enter AT Command: ").strip()
        
        if not user_input:
            print("Command cannot be empty.")
            continue
        
        result = send_command(user_input)
        if result:  # Make sure response is not None
            print(f"Response: {result.decode('utf-8').strip()}") # decode and strip take away junk around the message
        else:
            print("No response received.")
    except KeyboardInterrupt:
        print("\nExiting...")
        break
    except Exception as e:
        print(f"Error: {e}")

