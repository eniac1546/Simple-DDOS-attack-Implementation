# multithreading_programming_example.py

import threading
from http_flood_attack import send_http_request

# Run multiple threads
def run_threads():
    threads = list()
    
    # Start and run multiple threads
    for index in range(1, 6):
        t = threading.Thread(target=send_http_request)
        threads.append(t)
        t.start()
    
    # Wait until all threads terminate
    for index, thread in enumerate(threads):
        thread.join()

if __name__ == "__main__":
    run_threads()
