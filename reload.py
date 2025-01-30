import requests
import time
import threading
import winsound

def ring_bell(frequency, interval):
    while not stop_ringing:
        winsound.Beep(frequency, 500)  # 500ms er jonno beep dibe
        time.sleep(interval)  # beep er majhe interval

def load_page(url, timeout=2, reload_interval=8):
    global stop_ringing
    while True:
        try:
            response = requests.get(url, timeout=timeout)
            if response.status_code == 200:
                print("Page loaded successfully!")
                stop_ringing = False
                bell_thread = threading.Thread(target=ring_bell, args=(bell_frequency, beep_interval))
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
        time.sleep(reload_interval)  # Wait before retrying

if __name__ == "__main__":
    stop_ringing = True  # Bell ringing er switch
    
    print("Insert your URL:")
    url = input().strip()  # Prompt user for URL input
    print(f"Press enter to confirm {url} ")
    
    print("Insert Bell Frequency (in Hz):")
    bell_frequency = int(input().strip())  # Prompt user for frequency input
    
    beep_interval = 0.5  #beep er interval
    
    print("Insert Time Interval between Page Reloads (in seconds):")
    reload_interval = float(input().strip())  # Prompt user for reload interval input

    input("Press Enter to start...")
    load_page(url, reload_interval=reload_interval) #page load nibe
