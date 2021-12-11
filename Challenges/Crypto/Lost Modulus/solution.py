# Title: HTB Challenge -- Lost Modulus
# Author: J0s3ph97K
# HTB link: https://app.hackthebox.com/profile/769525

from Crypto.Util.number import getPrime, long_to_bytes, inverse

# encrypted_flag = pow(flag, e=3, n=p*q)
encrypted_flag = '05c61636499a82088bf4388203a93e67bf046f8c49f62857681ec9aaaa40b4772933e0abc83e938c84ff8e67e5ad85bd6eca167585b0cc03eb1333b1b1462d9d7c25f44e53bcb568f0f05219c0147f7dc3cbad45dec2f34f03bcadcbba866dd0c566035c8122d68255ada7d18954ad604965'
e = 3

while True:
    # brute-force attack
    p = getPrime(512)
    q = getPrime(512)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    d = inverse(e, phi_n)
    output = long_to_bytes(pow(int(encrypted_flag, 16), d, n))
    try:
        print(output.decode())
        break
    except:
        pass