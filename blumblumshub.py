# Blum Blum Shub pseudorandom sequence generator

print("Blum Blum Shub:")
print("X[n+1] = ((X[n])^2)mod(p*q)")

def input_nums():
    try:
        p = int(input("Give p: "))
        if p <= 1:
            print("Too small!")
            raise ValueError
        if p % 4 != 3:
            print("Not 3 mod 4!")
            raise ValueError
        for i in range(2,p):
            if p % i == 0:
                print("Not prime!")
                raise ValueError
        q = int(input("Give q: "))
        if q <= 1:
            print("Too small!")
            raise ValueError
        if q % 4 != 3:
            print("Not 3 mod 4!")
            raise ValueError
        for i in range(2,q):
            if q % i == 0:
                print("Not prime!")
                raise ValueError
        global M
        M = p * q
        global seed
        seed = int(input("Give seed: "))
        if seed <= 1 or seed % p == 0 or seed % q == 0:
            print("Incorrect seed!")
            raise ValueError
        global length
        length = int(input("How many numbers: "))
        if length <= 0:
            print("Too short!")
            raise ValueError
    except ValueError:
        input_nums()
    return M, seed

def bbs(M, x, list, c):
    list.append(x)
    x1 = (x**2)%M
    c += 1
    if c == length:
        return list
    bbs(M, x1, list, c)

def lsb(numbers, list_lsb):
    for i in range(0,len(numbers)):
        one = bool(numbers[i] & (1 << 0))
        if one:
            list_lsb.append(1)
        else:
            list_lsb.append(0)
    return list_lsb

def execute():
    numbers = []
    list_lsb = []
    input_nums()
    global counter
    counter = 0
    bbs(M, seed, numbers, counter)
    print("Generated number sequence:")
    print(*numbers)
    lsb(numbers, list_lsb)
    print("LSB sequence:")
    print(*list_lsb)

if __name__ == '__main__':
    while True:
        execute()