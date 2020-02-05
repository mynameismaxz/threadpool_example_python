import requests
from concurrent.futures import ThreadPoolExecutor
import time

def request_url(url):
    return requests.get(url)

def main():
    # do something in main thread
    test_url = ["https://jsonplaceholder.typicode.com/posts", "https://jsonplaceholder.typicode.com/users"]
    with ThreadPoolExecutor(max_workers=50) as pool:
        result1, result2 = pool.map(request_url, test_url)
        print(result1.text + "\n\n")
        print(result2.text + "\n\n")
        time.sleep(1)

if __name__ == "__main__":
    main()