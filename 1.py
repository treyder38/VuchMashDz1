alph = '0123456789ABCDEFGHIJKLMNOQRSTUVWXYZabcdefghijklmnopqrstuvwxyz#$&'

def to_10(n, k):
    ans = 0
    for i in range(len(n)):
        ans += alph.find(n[i]) * (k ** (len(n) - i - 1))
    return ans

def from_10(n, k):
    ans = ''
    cur = int(n)
    while cur >= k:
        ans += alph[cur % k]
        cur //= k
    ans += alph[cur]
    return ans[::-1]

def to_10_point(n, k):
    ans = 0
    size = n.find('.')
    n = n.replace('.', '')
    for i in range(len(n)):
        ans += alph.find(n[i]) * (k ** (size - i - 1))
    return ans

def after_point(n, k, x):
    ans = ''
    cur = float("0.{x}".format(x = n))
    for i in range(x):
        cur *= k
        ans += alph[int(cur)]
        cur -= int(cur)
    ans += alph[int(cur)]
    ans[::-1]
    return ans

def check(n, k):
    points = 0
    for el in n:
        if el == '.' or el == ',':
            points += 1
            if points == 2:
                return False
            else:
                continue
        if el not in alph or alph.find(el) >= k:
            return False
    return True

#sign = input('Знак исходного числа: ')
n = input('Исходное число: ')
k1 = int(input('Cистема счисления исходного числа: '))
k2 = int(input('В какую систему счисления переводить: '))

#if sign !=  '-' or sign != '+':
#    print('Неправильно введен знак исходного числа')
if check(n, k1) == 0:
    print('Неправильно введено исходное число')
elif str(k1).isalnum() == 0:
    print('Неправильно введена система счисления исходного числа')
elif str(k2).isalnum() == 0:
    print('Неправильно введена система счисления, в которую нужно сделать перевод')
else:
    point = 0
    n = n.replace(',', '.')
    for i in range(len(n)):
        if n[i] == '.':
            point = 1
            break

    if point == 0:
        a = to_10(n, k1)
        b = from_10(a, k2)
        print(b)
    
    else:
        x = int(input('Число знаков после запятой: '))
        n = str(to_10_point(n, k1))

        point_ind = n.find('.')
        
        s1 = n[:(point_ind)]
        s2 = n[(point_ind + 1):]
        print(from_10(s1, k2) + '.' + after_point(s2, k2, x))