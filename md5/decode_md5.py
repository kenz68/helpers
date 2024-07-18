import hashlib
import itertools
import string

def md5_brute_force(target_hash, max_length=5):
    chars = string.ascii_lowercase + string.digits
    for length in range(1, max_length + 1):
        for guess in itertools.product(chars, repeat=length):
            guess_str = ''.join(guess)
            guess_hash = hashlib.md5(guess_str.encode()).hexdigest()
            if guess_hash == target_hash:
                return guess_str
    return None

target_hash = 'ACC4CFC0773695795955F187D86342C3'  # Example hash for 'hello'
result = md5_brute_force(target_hash)
print(f'The original input is: {result}')