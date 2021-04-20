def step(array, k):
    if array.count(5)==k:
        s='Повышенная стипендия'
    if (array.count(3)==0) and (array.count(5)!=k):
        s='Обычная стипендия'
    if array.count(3)!=0:
        s='Стипендии нет'
    return s

a=[]
b=[]
n=int(input('Количество студентов: ')) #ввод количества учеников
k=int(input('Количество предметов: ')) #ввод количества предметов
student=[]

for i in range(n):
    student.append(input('ФИО: '))#ввод фио учеников
    
for i in range(len(student)):
    b=[]
    for j in range(k):
        b.append(int(input()))#ввод оценок
    a.append(b)

for i in range(len(student)):
    sr=0
    s=0
    for j in range(len(a[i])):
        s+=a[i][j]
        sr=s/k 
    print(student[i], ':', a[i], 'Средняя оценка: ', sr, 'Стипендия: ', step(a[i], k))
    print()








