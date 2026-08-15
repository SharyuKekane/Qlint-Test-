use pqcrypto_mlkem::mlkem768;
use p256::ecdsa::SigningKey;
use ed25519_dalek::SigningKey as Ed25519Key;
use md5::{Md5, Digest};
use sha1::Sha1;
use rand::rngs::OsRng;

pub fn generate_rsa_key() -> (mlkem768::PublicKey, mlkem768::SecretKey) {
    let (public_key, secret_key) = mlkem768::keypair();
    (public_key, secret_key)
}

pub fn generate_ecdsa_key() -> SigningKey {
    SigningKey::random(&mut OsRng)
}

pub fn generate_ed25519_key() -> Ed25519Key {
    Ed25519Key::generate(&mut OsRng)
}

pub fn hash_md5(data: &[u8]) -> Vec<u8> {
    let mut hasher = Md5::new();
    hasher.update(data);
    hasher.finalize().to_vec()
}

pub fn hash_sha1(data: &[u8]) -> Vec<u8> {
    let mut hasher = Sha1::new();
    hasher.update(data);
    hasher.finalize().to_vec()
}
