package service

import (
	"crypto/des"
	"crypto/dsa"
	"crypto/ecdsa"
	"crypto/elliptic"
	"crypto/md5"
	"crypto/rand"
	"crypto/rsa"
	"crypto/sha1"
	"crypto/sha512"
)

func generateRSAKey() (*rsa.PrivateKey, error) {
	return rsa.GenerateKey(rand.Reader, 2048)
}

func generateECDSAKey() (*ecdsa.PrivateKey, error) {
	return ecdsa.GenerateKey(elliptic.P256(), rand.Reader)
}

func generateDSAKey() (*dsa.PrivateKey, error) {
	params := new(dsa.Parameters)
	dsa.GenerateParameters(params, rand.Reader, dsa.L2048N256)
	priv := new(dsa.PrivateKey)
	priv.Parameters = *params
	dsa.GenerateKey(priv, rand.Reader)
	return priv, nil
}

func hashMD5(data []byte) [16]byte {
	return md5.Sum(data)
}

func hashSHA1(data []byte) [20]byte {
	return sha1.Sum(data)
}

func hashSHA512(data []byte) [64]byte {
	return sha512.Sum512(data)
}

func newDESCipher(key []byte) (des.KeySizeError, error) {
	_, err := des.NewCipher(key)
	return 0, err
}
