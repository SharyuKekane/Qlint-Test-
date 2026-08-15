"""Quantum-safe and Grover-resistant cryptographic operations."""

from Crypto.Cipher import AES
from Crypto.Hash import SHA384, SHA512, SHA3_256


def encrypt_aes256(key: bytes, data: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_GCM)
    return cipher.encrypt(data)


def hash_sha384(data: bytes) -> bytes:
    h = SHA384.new()
    h.update(data)
    return h.digest()


def hash_sha512(data: bytes) -> bytes:
    h = SHA512.new()
    h.update(data)
    return h.digest()


def hash_sha3(data: bytes) -> bytes:
    h = SHA3_256.new()
    h.update(data)
    return h.digest()
crypto/weak_symmetric.py
"""AES-128 and DES — Grover-weakened or classically broken."""

from Crypto.Cipher import AES, DES


def encrypt_aes128(key: bytes, data: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_CBC)
    return cipher.encrypt(data)


def encrypt_des(key: bytes, data: bytes) -> bytes:
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)
