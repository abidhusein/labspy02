
a = int(input('Masukan Nilai a : '))
b = int(input('Masukan Nilai b : '))
c = int(input('Masukan Nilai c : '))

if a > b and a > c:
    print ('Nilai yang tertinggi', a)
elif b > a and b > c:
    print ('Nilai yang tertinggi', b)
else:
    print ('Nilai yang tertinggi', c)