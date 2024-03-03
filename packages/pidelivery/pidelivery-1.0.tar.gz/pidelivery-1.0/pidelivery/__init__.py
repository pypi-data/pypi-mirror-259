import threading
import queue

import requests as rq


LIMIT = 100_000_000_000_000


class PiError(Exception):
    """
    This will be raised if site returns error
    """


def fetch_pi(length: int = 1000, offset: int = 0):
    """
    Get part of Pi of specified length from specified offset
    :param length: Length of returned part (max 1000)
    :param offset: Offset of returned part (max 100 trillion)
    :return: Part of Pi
    """
    if offset < 0:
        raise ValueError('Offset can\'t be negative!')
    if offset > LIMIT:
        raise ValueError(f'Offset can\'t be higher than {LIMIT}!')
    if length < 1:
        raise ValueError('Length can\'t be less than 1!')
    if length > 1000:
        raise ValueError('Length can\'t be higher than 1000!')
    r = rq.get(f'https://api.pi.delivery/v1/pi?start={offset}&numberOfDigits={length}')
    if r.status_code == 200:
        return r.json()['content']
    else:
        raise PiError(r.text)


def iter_pi(length: int = 10000, offset: int = 0, preload: bool = False):
    """
    Iterate digits from Pi
    :param length: Length of returned part (max 100 trillion)
    :param offset: Offset of returned part (max 100 trillion)
    :param preload: Whether you want to load numbers in background (useful if you are doing something in real time)
    :return Yields numbers one-by-one until limit is reached
    """
    if (length + offset) > LIMIT:
        raise ValueError(f'Sum of length and offset can\'t be higher than {LIMIT}')
    if preload:
        q = queue.Queue()

        def worker(_offset):
            nonlocal offset
            i = 0
            while True:
                for x in fetch_pi(1000, _offset):
                    i += 1
                    if i >= length:
                        return
                    q.put(x)
                _offset += 1000

        thread = threading.Thread(target=worker, args=[offset])
        thread.start()
        while (not q.empty()) or thread.is_alive():
            yield q.get()
    else:
        current = 0
        should_stop = False
        while True:
            for digit in fetch_pi(1000, offset):
                current += 1
                if current >= length:
                    should_stop = True
                    break
                yield digit
            if should_stop:
                break
            offset += 1000


def get_pi(length: int = 10000, offset: int = 0):
    """
    Get digits from Pi
    :param length: Length of returned part (max 100 trillion)
    :param offset: Offset of returned part (max 100 trillion)
    :return Flattened list from iter_pi (use ''.join to turn it into string)
    """
    return list(iter_pi(length, offset, False))
