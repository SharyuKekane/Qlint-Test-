package com.qlintdemo;

import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import java.security.KeyPairGenerator;
import java.security.MessageDigest;
import java.security.Signature;

public class Legacy {

    public KeyPairGenerator generateRSAKey() throws Exception {
        KeyPairGenerator kpg = KeyPairGenerator.getInstance("RSA");
        kpg.initialize(2048);
        return kpg;
    }

    public KeyPairGenerator generateECKey() throws Exception {
        KeyPairGenerator kpg = KeyPairGenerator.getInstance("EC");
        return kpg;
    }

    public Signature signWithECDSA() throws Exception {
        return Signature.getInstance("SHA256withECDSA");
    }

    public MessageDigest hashMD5() throws Exception {
        return MessageDigest.getInstance("MD5");
    }

    public MessageDigest hashSHA1() throws Exception {
        return MessageDigest.getInstance("SHA-1");
    }

    public Cipher encryptDES() throws Exception {
        return Cipher.getInstance("DES/ECB/PKCS5Padding");
    }

    public KeyGenerator generateAES128Key() throws Exception {
        KeyGenerator kg = KeyGenerator.getInstance("AES");
        kg.init(128);
        return kg;
    }
}
