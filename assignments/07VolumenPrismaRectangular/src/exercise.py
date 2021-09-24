def area(base, altura):
    areaBase = base * altura
    return areaBase

def volumen(base, altura, profundidad):
    areaBase = area(base,altura)
    volumen = areaBase * profundidad
    return volumen

base = float(input("Dame la base: "))
altura = float(input("Dane la altura: "))
profundidad = float(input("Dame la profundidad: "))
areaBase = 0
volumenPrisma = volumen(base, altura, profundidad)
print("El volumen del prisma es:",volumenPrisma)

if __name__=='__main__':
    main()
