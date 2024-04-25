# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@Project  : will-be-famous
@Time     : 2024/4/19
@Author   : Zhang ZiXu
@Software : PyCharm
@Desc     :  
@Last Modify          @Version        @Author
---------------       --------        -----------
2024/4/19               1.0             Zhang ZiXu
"""
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

from Crypto.Util.Padding import pad


def generate_key(key_size=16):
    """
    生成指定长度的密钥。
    默认长度为16字节（对应AES-128）。
    """
    return get_random_bytes(key_size)


def generate_iv(iv_size=16):
    """
    生成指定长度的初始化向量（IV）。
    默认长度为16字节。
    """
    return get_random_bytes(iv_size)


def pad_plaintext(block_size=16):
    """
    使用PKCS7填充法对明文进行填充，确保其长度是块大小的整数倍。
    """
    padding = block_size - len(plaintext) % block_size
    return plaintext + bytes([padding]) * padding


def unpad(padded_text):
    """
    移除PKCS7填充。
    """
    padding = padded_text[-1]
    if padding > 16:
        raise ValueError("Invalid padding")
    return padded_text[:-padding]


def encrypt(plaintext, key, iv):
    """
    使用AES-CBC模式加密明文。
    """
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_plaintext = pad(plaintext)
    ciphertext = cipher.encrypt(padded_plaintext)
    return (ciphertext, cipher.iv)


def decrypt(ciphertext, key, iv):
    """
    使用AES-CBC模式解密密文。
    """
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = cipher.decrypt(ciphertext)
    return unpad(decrypted_text)


# 示例使用：
plaintext = b"This is a secret message."

# 生成密钥和IV
key = generate_key()
iv = generate_iv()

# 加密过程
ciphertext, actual_iv = encrypt(plaintext, key, iv)
print("Encrypted message:")
print(base64.b64encode(ciphertext).decode('utf-8'))
print("IV:", base64.b64encode(actual_iv).decode('utf-8'))

# 解密过程
decrypted_text = decrypt(ciphertext, key, actual_iv)
print("\nDecrypted message:")
print(decrypted_text.decode('utf-8'))
