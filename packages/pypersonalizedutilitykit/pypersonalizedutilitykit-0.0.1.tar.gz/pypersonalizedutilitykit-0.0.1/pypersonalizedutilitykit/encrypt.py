# -*- coding:utf-8 -*-
"""
# File       : encrypt.py
# Time       ：2023/1/21 
# Author     ：lyz
# version    ：python 3
# Description：
"""

from cryptography.fernet import Fernet
# class Encrypt:
#     """
#     随机加密、解密
#     """
#     key = Fernet.generate_key()
#     def encrypt_text(self, text):
#         cipher_suite = Fernet(Encrypt().key)
#         print(Encrypt().key)
#         encrypted_text = cipher_suite.encrypt(text.encode())
#         return encrypted_text.decode()
#     def decrypt_text(self, encrypted_text):
#         cipher_suite = Fernet(Encrypt().key)
#         print(Encrypt().key)
#         decrypted_text = cipher_suite.decrypt(encrypted_text.encode())
#         return decrypted_text.decode()

class Crypt:
    """
    固定key加密
    Returns:
    """
    # 创建Fernet实例
    f = Fernet('Nb-vOHiMwpAug9q4NAG53bEFbaf40F1H-gx1WtthMFs=')
    def enc(self):
        # 加密数据
        text = input("请输入需要加密的数据：")
        encrypted_text = Crypt().f.encrypt(text.encode())
        return print('加密后的数据：', encrypted_text.decode())
    def dec(self, encrypted_text):
        # 解密数据
        try:
            decrypted_text = Crypt().f.decrypt(encrypted_text.encode())
            return decrypted_text.decode()
        except Exception:
            pass


if __name__ == '__main__':
    while True:
        a = Crypt().enc()
        Crypt().dec('gAAAAABlpMJWRhIbAIQG0BXMfGHh6bkx6AYaOU4O7s7tkV_CJ7d2lRQqaCXc13FZMYFz680u34_pZ-wdjDFBt08zTuMfUqYVFQ==')


