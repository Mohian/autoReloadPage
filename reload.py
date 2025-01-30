import requests
import time

def load_page(url, timeout=2):
    while True:
        try:
            response = requests.get(url, timeout=timeout)
            if response.status_code == 200:
                print("Page loaded successfully!")
                break
            else:
                print(f"Received status code {response.status_code}. Retrying...")
        except requests.exceptions.RequestException:
            print("Request timed out or failed. Retrying...")
        time.sleep(5)  # Wait before retrying

if __name__ == "__main__":
    url = "https://google.com/"
    load_page(url)