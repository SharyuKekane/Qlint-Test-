package com.qlintdemo;

import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import java.security.KeyPairGenerator;
import java.security.MessageDigest;
import java.security.Security;
import java.security.Signature;
import org.bouncycastle.pqc.jcajce.provider.BouncyCastlePQCProvider;

public class Legacy {

    public KeyPairGenerator generateRSAKey() throws Exception {
        Security.addProvider(new BouncyCastlePQCProvider());
        KeyPairGenerator kpg = KeyPairGenerator.getInstance("ML-KEM-768", "BCPQC");
        kpg.generateKeyPair();
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
        return MessageDigest.getInstance("SHA3-512");
    }

    public MessageDigest hashSHA1() throws Exception {
        return MessageDigest.getInstance("SHA-1");
    }

    public Cipher encryptDES() throws Exception {
        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(256);
        Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
        return cipher;
    }

    public KeyGenerator generateAES128Key() throws Exception {
        KeyGenerator kg = KeyGenerator.getInstance("AES");
        kg.init(256);
        return kg;
    }
}
