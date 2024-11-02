# 1.	Quyidagi ifodaning ma'lumot turi qanday?
type(10 / 2)
# a) int    b) float      c) str    d) bool

# 2.Quyidagilardan qaysi biri Python’da lug‘at (dictionary) yaratishning to‘g‘ri usuli
# a) {1: 'a', 2: 'b'}  b) [1, 2, 3]   c) ('a', 'b', 'c')   d) Hech biri emas

# 3.Python’da 3 + 2 * 2 ifodasining natijasi qanday bo‘ladi?
# a) 10   b) 7   c) 12   d) Hech biri emas

# 4.Quyidagilardan qaysi biri Python’da darajaga ko‘tarish operatoridir?
# a) **  b) ^  c) //  d) *

# 5.Quyidagi kodning natijasi nima bo‘ladi?
x = 10
y = 5 
x //= y 
print(x)
# a) 2.0  b) 2 c) 5 d) 10

# 6.Quyidagilardan qaysi biri if-else operatorining to‘g‘ri sintaksisi hisoblanadi?
# a) if x > 0 then   b) if (x > 0):   c) if x > 0:   d) else if x > 0:

# 7.Quyidagi kodning natijasi nima bo‘ladi?
for i in range(0, 5):
    print(i)
    if i == 3:
        break
    
# a) 0 1 2 3   b) 0 1 2   c) 0 1 2 3 4   d) Hech biri emas

# 8.Quyidagi sikl necha marta ishlaydi?
count = 0
while count < 4:
    count += 1
# a) 3  b) 4  c) 5 d) Cheksiz

# 9.Siklning hozirgi iteratsiyasini o'tkazib yuborish uchun qaysi kalit so‘z ishlatiladi?
# a) pass  b) skip  c) continue  d) break

# 10.Quyidagi kodning natijasi nima bo‘ladi?
for letter in "Python":
    if letter == "h":
        continue
    print(letter)
# a) Python  b) Pythn  c) Pyon  d) Pyonth

# 11.Python’da funksiyani aniqlashning to‘g‘ri usuli qaysi?
# a) func my_function():   b) def my_function():   c) my_function() def:   d) function my_function():


# 12.Quyidagi funksiyaning natijasi nima bo‘ladi?
def add(a, b=10):
    return a + b

print(add(5))
# a) 5 b) 10 c) 15 d) Hech biri emas

#13. Python funksiyasidagi return operatorining vazifasi nima?
# a) U natijani chop etadi
# b) U funksiyadan chiqadi va qiymat qaytaradi
# c) U o‘zgaruvchi e'lon qiladi
# d) U funksiyani qayta ishga tushiradi

# 14.Quyidagilardan qaysi biri bir nechta argumentlarni funksiyaga uzatishning to‘g‘ri usuli hisoblanadi?
# a) def func(*args):
# b) def func(args*):
# c) def func(*arg):
# d) Hech biri emas

# 15.Quyidagi kodning natijasi qanday bo‘ladi?
def multiply(a, b):
    return a * b
print(multiply(2, 3))
# a) 5 b) 6 c) 23 d) Hech biri emas

# 16.Agar try blokida xato yuz bermasa, qaysi blok bajariladi?
# a) except b) finally c) else d) Hech biri emas

# 17.Python’da bo‘lishda nolga bo‘lishda qaysi istisno yuzaga keladi?
# a) ValueError
# b) ZeroDivisionError
# c) ArithmeticError
# d) NameError

# 18.Python’da try bloki nima qiladi?
# a) Dasturdagi xatolarni qayta ishlaydi
# b) Kodni xatolar uchun sinaydi
# c) Dastur ishini to‘xtatadi
# d) U xatoni o‘chiradi

# 19.Quyidagi kod nima qiladi?
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Nolga bo‘lib bo‘lmaydi")
# a) Xato ko‘tariladi
# b) 10 / 0 chop etiladi
# c) Nolga bo‘lib bo‘lmaydi chop etiladi
# d) Hech narsa qilinmaydi

# 20.Quyidagilardan qaysi biri Python’da o‘zgaruvchan ma'lumot turi hisoblanadi?
# a) Tuple b) List c) String d) Dictionary

# 21.Python’da ro‘yxatning birinchi elementiga qanday murojaat qilinadi?
# a) my_list(0)
# b) my_list[1]
# c) my_list[0]
# d) my_list.first()

# 22.Lug‘atga element qo‘shish uchun qaysi metod ishlatiladi?
# a) append()
# b) add()
# c) update()
# d) insert()

# 23.Quyidagi kodning natijasi qanday bo‘ladi?
my_tuple = (1, 2, 3)
print(my_tuple[1])
# a) 1 b) 2 c) 3 d) Xato

# 24.Quyidagi ma'lumot turlaridan qaysi biri takrorlanadigan qiymatlarni qabul qilmaydi?
# a) List b) Tuple c) Set d) Dictionary

# 25.Python’da sanalar bilan ishlash uchun qaysi modul ishlatiladi?
# a) calendar b) time c) datetime d) date

# 26.Sanani Yil-Oy-Kun formatida chop etish uchun strftime() ning to‘g‘ri formati qaysi?
# a) "%Y/%m/%d"
# b) "%d/%m/%Y"
# c) "%m/%d/%Y"
# d) "%Y-%m-%d"


# 27. Quyidagi kod nima chop etadi?
x = [1, 2, 3]
y = x
y.append(4)
print(x)

# 28.Quyidagi kodning natijasi qanday bo‘ladi?
my_list = [10, 20, 30]
my_list.insert(1, 15)
print(my_list)

# 29.Quyidagi kodda qanday xato yuzaga keladi?
my_dict = {'a': 1, 'b': 2}
print(my_dict['c'])

# 30.Quyidagi kod nima qaytaradi?
def power(x, y):
    return x ** y

print(power(2, 3))

# 31.Quyidagi kod nima qaytaradi?
my_tuple = (5, 10, 15)
print(my_tuple[0])


# 32.Python’da bir vaqtning o‘zida else va except operatorlari birga ishlatiladimi?
# 33.Python’dagi finally bloki qachon ishlaydi?
# 34.set va frozenset, birbirdan va boshqa ma’lumot turlaridan farqlari?,	ular qanday hosil qilinadi?
# 35.Pythonda kamida 6 ta error ni sanang va nima sababdan kelib	chiqishini tushuntiring
