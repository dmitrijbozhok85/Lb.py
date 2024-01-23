import hashlib
import itertools

def crack(digest):
    combinations = itertools.product(range(10), repeat=5)
    for combination in combinations:
        pin_attempt = ''.join(map(str, combination))
        attempt_hash = hashlib.md5(pin_attempt.encode()).hexdigest()
        if attempt_hash == digest:
            return pin_attempt
    return None
