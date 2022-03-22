import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
from Crypto.Cipher import PKCS1_OAEP
import binascii


key = RSA.generate(2048)



private_key = key.export_key().decode("utf-8") 
public_key1 = key.publickey().exportKey().decode("utf-8")







class CryptoGraphy():
    def __init__(self, model) -> None:
        ...

    def decrypt(self, exText):
        key1 = RSA.importKey(private_key)
        decryptor = PKCS1_OAEP.new(key1)
        decrypted = decryptor.decrypt(exText)
        return decrypted

    def encrypt(self, data: str=''):
        key = RSA.importKey(public_key1)

        encryptor = PKCS1_OAEP.new(key)
        encrypted = encryptor.encrypt(bytes(data, encoding='utf8'))
        return encrypted


crypto = CryptoGraphy(model=None)
l = crypto.encrypt('salim suleiman')

# print(l)
# print(binascii.hexlify(l))
# print(binascii.unhexlify(binascii.hexlify(l)))
# print(crypto.decrypt(b'539762a45c00a163b6419a09dbb8b9b7ca13165766ffd61cd6e9b2fe5e61d036558b4b61d6caab6242acb0f01e17d78422bdd424fe63bc6ac9dc2e7f5231dd36488228a1e9ff02a310220945979aef9c2dae7add5263f79c99e120d6acab63b3069ba7f0a9823f7e4a0b87f8f3f7f621ec43a9ddbf7bd0c56442993df11194a3a65d5b8ec0a5ec28de08339e7951ae6f2b013d740e1e5fb1026f45fc10ad7de5852d4e6d9be9bd9b7a513f14c01ea7092d4c3fc56834dfc8473f20817ad86d757d0286883693890f5b26a153cf336cbc8efa7d6388badcab3a28c3a1a624ae7a298dd8a4a0c6ed39a357386e6f7bbfe97b7ab5938be9d84a306f9e133e94b04a').decode("utf-8") )
