"""AES-128 and DES — Grover-weakened or classically broken."""

from Crypto.Cipher import AES, DES


def encrypt_aes128(key: bytes, data: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_CBC)
    return cipher.encrypt(data)


def encrypt_des(key: bytes, data: bytes) -> bytes:
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)
