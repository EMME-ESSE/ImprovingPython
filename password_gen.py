#pip install werkzeug
import random
from werkzeug.security import generate_password_hash

minus = "abcdefghijklmñopqrstuvwxyz"
mayus = minus.upper()
numeros = "0123456789"
simbolos = "*¨[!#/$%=]:=)(&|°_-{};,."
all = minus+mayus+numeros+simbolos
long = 12

for i in range(10):
    muestra = random.sample(all, long)
    password="".join(muestra)
    if password.count(password) >= 3:
            pass_encr = generate_password_hash(password)
    pass_encr=generate_password_hash(password)
    print("{} -> {}".format(password, pass_encr))
