#Задача «Часть от целого».

name='«Сейчас на Земле появился новый вид роботов. Раньше их называли „железной оравой “, но это не очень точное определение»'
print(name[1:44])

#Задача «Палиндром».

name='радар'
print(name[::-1])
name='норма'
print(name[::-1])

#Задача «Равные части».

name='кенгуру'
a=(name[0:4])
b=(name[4:8])
print(b+a)

#Задача «Четные и нечетные».

name='нейропрограммирование' #print(len(name))=21
a=(name[0:21:2])
b=(name[1:20:2])
print(a+' '+b)

#Задача «Обратный порядок».

name='нейропластичность' #print(len(name))=17
a=name[1:16]
print(a[::-1])