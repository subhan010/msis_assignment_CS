

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
print("QUesiton 1 seive of ert")



def is_prime(n):
    
    if n <= 1:
        return False
 
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


ar=[0]*101
   
for i in range(2,101):
    if(ar[i]==-1):
        continue
    if  is_prime(i):
        temp=i
        ar[i]=1
        count=2
        while(temp<101 and temp*count<101):
            temp=temp*count
            
            ar[temp]=-1
            count=count+1

     
for i in range(len(ar)):
    if(ar[i]==1):
        print(i)





# 1. Generate RSA private and public keys
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

public_key = private_key.public_key()

# 2. Export keys to PEM format (optional)
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# 3. Encrypt a message using the public key
message = b'This is a secret message.'
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),  # Specify the mask generation function (MGF1)
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Encrypted:", ciphertext)

# 4. Decrypt the message using the private key
decrypted_message = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),  # Specify the mask generation function (MGF1)
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Decrypted:", decrypted_message.decode())