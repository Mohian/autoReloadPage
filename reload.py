import requests
import time
import sys
import threading
import winsound

def ring_bell():
    while not stop_ringing:
        winsound.Beep(1000, 500)  # Frequency: 1000 Hz, Duration: 500 ms
        time.sleep(1)

def load_page(url, timeout=2):
    global stop_ringing
    while True:
        try:
            response = requests.get(url, timeout=timeout)
            if response.status_code == 200:
                print("Page loaded successfully!")
                stop_ringing = False
                bell_thread = threading.Thread(target=ring_bell)
                bell_thread.start()
                print("Press Enter to stop the ringing...")
                input()  # Wait for user input
                stop_ringing = True
                bell_thread.join()
                break
            else:
                print(f"Received status code {response.status_code}. Retrying...")
        except requests.exceptions.RequestException:
            print("Request timed out or failed. Retrying...")
        time.sleep(2)  # Wait before retrying

if __name__ == "__main__":
    stop_ringing = True  # Control flag for bell ringing thread
    
    print("Insert your URL:")
    url = input().strip()  # Prompt user for URL input
    
    print(f"Are you Sure: {url} is your URL?")
    input("Press Enter to start...")
    load_page(url)
