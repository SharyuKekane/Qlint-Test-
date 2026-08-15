"""Legacy cryptographic operations — intentionally quantum-vulnerable
and classically-broken algorithms for demonstration purposes."""

from Crypto.PublicKey import RSA, ElGamal, DSA
from Crypto.Hash import MD5, SHA1
from Crypto.Cipher import DES3, ARC4
from cryptography.hazmat.primitives.asymmetric import ec, ed25519, x25519, dh
from cryptography.hazmat.primitives import hashes


def generate_rsa_keypair():
    key = RSA.generate(2048)
    return key


def generate_elgamal_keypair():
    key = ElGamal.generate(2048, None)
    return key


def generate_dsa_keypair():
    key = DSA.generate(2048)
    return key


def generate_ecc_keypair():
    key = ec.generate_private_key(ec.SECP256R1())
    return key


def generate_ed25519_keypair():
    key = ed25519.Ed25519PrivateKey.generate()
    return key


def generate_x25519_keypair():
    key = x25519.X25519PrivateKey.generate()
    return key


def generate_dh_parameters():
    parameters = dh.generate_parameters(generator=2, key_size=2048)
    return parameters


def hash_md5(data: bytes) -> bytes:
    h = MD5.new()
    h.update(data)
    return h.digest()


def hash_sha1(data: bytes) -> bytes:
    h = SHA1.new()
    h.update(data)
    return h.digest()


def encrypt_3des(key: bytes, data: bytes) -> bytes:
    cipher = DES3.new(key, DES3.MODE_ECB)
    return cipher.encrypt(data)


def encrypt_rc4(key: bytes, data: bytes) -> bytes:
    cipher = ARC4.new(key)
    return cipher.encrypt(data)
