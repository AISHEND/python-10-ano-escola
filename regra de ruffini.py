print("by @leandroafonso.m open-source software")
y = int(input("Qual é o grau do polinómio? (3-6): "))

if (y < 3 or y > 6):
    print("Tenta novamente! Algum dos dados inseridos não está correto:(")

else:
    n = int(input("nº que anula o divisor: "))
    print("Na ausência de algum coeficiente coloque ´0´!")

if (y == 6):

    a = int(input("x⁶: "))
    b = int(input("x⁵: "))
    c = int(input("x⁴: "))
    d = int(input("x³: "))
    e = int(input("x²: "))
    f = int(input("x: "))
    g = int(input("independente: "))

    m1 = n * a
    s1 = b + m1

    m2 = n * s1
    s2 = c + m2

    m3 = n * s2
    s3 = d + m3

    m4 = n * s3
    s4 = e + m4

    m5 = n * s4
    s5 = f + m5

    m6 = n * s5
    s6 = g + m6
    def numerodedigitos(m6):
        return len(str(m6))
    if numerodedigitos(m6)>6:
        print("O número de digitos ultrapassa o limte deste programa!")
    else:
        print("{:^6}{:<2}{:^6}{:^6}{:^6}{:^6}{:^6}{:^6}{:^6}".format(" ", "¦", a, b, c, d, e, f, g))
        print("{:^6}{:<8}{:^6}{:^6}{:^6}{:^6}{:^6}{:^6}".format(n, "¦", m1, m2, m3, m4, m5, m6))
        print("-----------------------------------")
        print("{:^6}{:<2}{:^6}{:^6}{:^6}{:^6}{:^6}{:^6}{:^6}".format(" ", "¦", a, s1, s2, s3, s4, s5, s6))
        print("-----------------------------------")
        print("polinómio quociente: ({})x⁵+({})x⁴+({})x³+({})x²+({})x+({})\npolinómio-resto: {}".format(a, s1, s2, s3, s4, s5, s6))

elif (y == 5):

    a = int(input("x⁵: "))
    b = int(input("x⁴: "))
    c = int(input("x³: "))
    d = int(input("x²: "))
    e = int(input("x: "))
    f = int(input("independente: "))

    m1 = n * a
    s1 = b + m1

    m2 = n * s1
    s2 = c + m2

    m3 = n * s2
    s3 = d + m3

    m4 = n * s3
    s4 = e + m4

    m5 = n * s4
    s5 = f + m5
    def numerodedigitos(m5):
        return len(str(m5))
    if numerodedigitos(m5)>6:
        print("O número de digitos ultrapassa o limte deste programa!")
    else:
        print("{:^6}{:<2}{:^6}{:^6}{:^6}{:^6}{:^6}{:^6}".format(" ", "¦", a, b, c, d, e, f))
        print("{:^6}{:<8}{:^6}{:^6}{:^6}{:^6}{:^6}".format(n, "¦", m1, m2, m3, m4, m5))
        print("-----------------------------------")
        print("{:^6}{:<2}{:^6}{:^6}{:^6}{:^6}{:^6}{:^6}".format(" ", "¦", a, s1, s2, s3, s4, s5))
        print("-----------------------------------")
        print("polinómio quociente: ({})x⁴+({})x³+({})x²+({})x+({})\npolinómio-resto: {}".format(a, s1, s2, s3, s4,s5))

elif (y == 4):

    a = int(input("x⁴: "))
    b = int(input("x³: "))
    c = int(input("x²: "))
    d = int(input("x: "))
    e = int(input("independente: "))

    m1 = n * a
    s1 = b + m1

    m2 = n * s1
    s2 = c + m2

    m3 = n * s2
    s3 = d + m3

    m4 = n * s3
    s4 = e + m4
    def numerodedigitos(m4):
        return len(str(m4))
    if numerodedigitos(m4)>6:
        print("O número de digitos ultrapassa o limte deste programa!")
        print("{:^6}{:<2}{:^6}{:^6}{:^6}{:^6}{:^6}".format(" ", "¦", a, b, c, d, e))
        print("{:<6}{:<8}{:^6}{:^6}{:^6}{:^6}".format(n, "¦", m1, m2, m3, m4))
        print("-----------------------------------")
        print("{:^6}{:<2}{:^6}{:^6}{:^6}{:^6}{:^6}".format(" ", "¦", a, s1, s2, s3, s4))
        print("-----------------------------------")
        print("polinómio quociente: ({})x³+({})x²+({})x+({})\npolinómio-resto: {}".format(a, s1, s2, s3,s4))


elif (y == 3):

    a = int(input("x³: "))
    b = int(input("x²: "))
    c = int(input("x: "))
    d = int(input("independente: "))

    m1 = n * a
    s1 = b + m1

    m2 = n * s1
    s2 = c + m2

    m3 = n * s2
    s3 = d + m3


    def numerodedigitos(m3):
        return len(str(m3))
    if numerodedigitos(m3)>6:
        print("O número de digitos ultrapassa o limte deste programa!")
    else:
        print("{:^6}{:<2}{:^6}{:^6}{:^6}{:^6}".format(" ", "¦", a, b, c, d))
        print("{:^6}{:<8}{:^6}{:^6}{:^6}".format(n, "¦", m1, m2, m3))
        print("-----------------------------------")
        print("{:^6}{:<2}{:^6}{:^6}{:^6}{:^6}".format(" ", "¦", a, s1, s2, s3))
        print("-----------------------------------")
        print("polinómio quociente: ({})x²+({})x+({})\npolinómio-resto: {}".format(a,s1,s2,s3))