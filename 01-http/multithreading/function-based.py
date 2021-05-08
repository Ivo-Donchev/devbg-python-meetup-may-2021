import requests
import threading
from common import Timer


def http_get(url):
    response = requests.get(url)
    print(f'HTTP GET {url} - response {response.status_code}')
    return response


def singlethreaded():
    for i in range(20):
        http_get('https://abv.bg')


def multithreaded():
    threads = []

    # Start 10 separate threads
    for i in range(20):
        thread = threading.Thread(
            target=http_get,
            args=('https://abv.bg',)
        )

        thread.start()
        threads.append(thread)

    # Wait for all the threads to finish
    for thread in threads:
        thread.join()


def main():
    print('Running....')

    with Timer('Single threaded'):
        singlethreaded()

    with Timer('Multiple threads'):
        multithreaded()


if __name__ == '__main__':
    main()
