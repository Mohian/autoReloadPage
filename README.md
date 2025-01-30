# Reload Web Page

This script is written for users who feel bore to interact with slow servers. It continuously attempts to load a very slow web page, in this case it is `https://google.com/` until the server responds successfully within 5 seconds. If the response fails or times out, the script retries every 2 seconds.

## Features
- Automatically retries if the request times out or fails.
- Stops reloading once the page loads successfully.
- Uses a timeout of 5 seconds for each request.

## Prerequisites
Ensure you have Python installed on your system. You can check by running:

```sh
python --version
```

## Setup
### 1. Clone the Repository
```sh
git clone <repository-url>
cd <repository-folder>
```

### 2. Create and Activate Virtual Environment (Optional)
if you don't want to make any change into your real python library.
```sh
python -m venv venv
```
- **For Windows:**
  ```sh
  venv\Scripts\activate
  ```
- **For macOS/Linux:**
  ```sh
  source venv/bin/activate
  ```
### 3. Run 
```sh
pip install -r requirements.txt
```

## Running the Script
```sh
python reload.py
```

## Dependencies

```sh
pip install requests
```

## License
This project is licensed under the GNU General Public License v3.0.

---

Feel free to contribute or raise issues!

