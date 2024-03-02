import hashlib
import random
import re
import string
from urllib.parse import urlparse


def _generate_random_ascii_string(length: int = 30) -> str:
    return "".join(random.choice(string.ascii_lowercase) for i in range(length))


def _split_interval_string(s: str) -> tuple[int, str]:
    for i, char in enumerate(s):
        if not char.isdigit():
            return int(s[:i]), s[i:]
    return int(s), ""


def _extract_uri_scheme(path: str) -> str:
    result = urlparse(path)
    return result.scheme


def _make_python_identifier(str_: str) -> str:
    return re.sub(r"\W|^(?=\d)", "_", str_)


def _create_reproducible_hash(input_string: str) -> str:
    # Encode the input string
    encoded_string = input_string.encode()

    # Create a SHA-32 hash object
    sha256_hash = hashlib.md5()

    # Update the hash object with the bytes-like object (encoded string)
    sha256_hash.update(encoded_string)

    # Generate the hexadecimal representation of the digest
    hex_digest = sha256_hash.hexdigest()

    return hex_digest
