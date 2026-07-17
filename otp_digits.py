import random
import secrets
pin = random.randint(100000, 999999)

print(pin)


# 2. randrange()
pin2 = random.randrange(100000, 1000000)

# 3. choices()
pin3 = ''.join(random.choices('0123456789', k=4))

# 4. secrets — better for secure PINs

pin4 = ''.join(secrets.choice('0123456789') for _ in range(4))

print(type(pin2))
print(type(pin3),pin3)
print(type(pin4),pin4)

print(secrets.choice('0123456789') for _ in range(4))

print(random.choices('0123456789', k=4))

print(''.join(["1","2"]))