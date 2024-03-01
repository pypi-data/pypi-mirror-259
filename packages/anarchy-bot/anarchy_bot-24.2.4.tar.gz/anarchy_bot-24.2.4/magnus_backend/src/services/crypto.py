from typing import cast
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
import pickle
import base64
import os
from fastapi import HTTPException
from setup import data_path


class CryptoServer:
    def __init__(self, key_size=2048):
        self.key_size = key_size
        self.keys_dir = f'{data_path}/keys/'
        self._check_dir()
        self.load_private_key()
        self.load_public_key()

    def _check_dir(self):
        if not os.path.exists(self.keys_dir):
            os.makedirs(self.keys_dir)

    def load_private_key(self, filename: str = 'private.pem'):
        try:
            with open(self.keys_dir + filename, 'rb') as f:
                private = serialization.load_pem_private_key(
                    f.read(),
                    password=None,
                    backend=default_backend()
                )
                self.private_key = cast(rsa.RSAPrivateKey, private)
        except FileNotFoundError:
            self.generate_key_pair()
            self.save_private_key(filename)

    def load_public_key(self, filename: str = 'pub.pem'):
        try:
            with open(self.keys_dir + filename, 'rb') as f:
                public = serialization.load_pem_public_key(
                    f.read(),
                    backend=default_backend()
                )
                self.public_key = cast(rsa.RSAPublicKey, public)
        except FileNotFoundError:
            if self.private_key is None:
                self.generate_key_pair()
            self.public_key: rsa.RSAPublicKey = self.private_key.public_key()
            self.save_public_key(filename)

    def generate_key_pair(self):
        self.private_key: rsa.RSAPrivateKey = rsa.generate_private_key(
            public_exponent=65537,
            key_size=self.key_size,
            backend=default_backend()
        )
        self.public_key: rsa.RSAPublicKey = self.private_key.public_key()

    def save_public_key(self, filename: str = 'pub.pem'):
        with open(self.keys_dir + filename, 'wb') as f:
            f.write(self.public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))

    def save_private_key(self, filename: str = 'private.pem'):
        with open(self.keys_dir + filename, 'wb') as f:
            f.write(self.private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            ))

    def encrypt_data(self, data):
        if isinstance(self.public_key, rsa.RSAPublicKey):
            serialized_data = pickle.dumps(data)
            encrypted_data = self.public_key.encrypt(
                serialized_data,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            enc_data_base64 = base64.b64encode(encrypted_data).decode('utf-8')
            return enc_data_base64
        else:
            raise ValueError("public key not generated yet.")


class CryptoUser:
    def __init__(self):
        self.keys_dir = f'{data_path}/keys/'
        self.private_key = None
        self.load_private_key()

    def load_private_key(self, filename: str = 'private.pem'):
        with open(self.keys_dir + filename, 'rb') as f:
            self.private_key = serialization.load_pem_private_key(
                f.read(),
                password=None,
                backend=default_backend()
            )

    def decrypt_data(self, encrypted_data):
        if isinstance(self.private_key, rsa.RSAPrivateKey):
            try:
                ciphertext = base64.b64decode(encrypted_data.encode('utf-8'))
                decrypted_data = self.private_key.decrypt(
                    ciphertext,
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None
                    )
                )
                return pickle.loads(decrypted_data)
            except ValueError:
                raise HTTPException(401, 'token is not valid (not decrypt)')
        else:
            raise ValueError("private key not loaded yet.")
