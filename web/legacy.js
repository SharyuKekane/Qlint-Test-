// Legacy cryptographic operations for demonstration.
const crypto = require('crypto');

function signWithRSA(privateKey, data) {
  const sign = crypto.createSign('RSA-SHA256');
  sign.update(data);
  return sign.sign(privateKey);
}

function signWithECDSA(privateKey, data) {
  const sign = crypto.createSign('SHA256');
  sign.update(data);
  return sign.sign(privateKey);
}

function hashMD5(data) {
  return crypto.createHash('md5').update(data).digest();
}

function hashSHA1(data) {
  return crypto.createHash('sha1').update(data).digest();
}

function encryptDES(key, data) {
  const cipher = crypto.createCipheriv('des-ecb', key, null);
  return cipher.update(data);
}

function hashSHA512(data) {
  return crypto.createHash('sha512').update(data).digest();
}

module.exports = { signWithRSA, signWithECDSA, hashMD5, hashSHA1, encryptDES, hashSHA512 };
