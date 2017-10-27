Heilongjiang = ['harbin','qiqihaer','jiamusi','mudanjiang']
Heilongjiang.append('jixi')
print(Heilongjiang)

del Heilongjiang[-1]
print (Heilongjiang)

Heilongjiang[3] = 'shuangyasha'
print (Heilongjiang)

Heilongjiang.insert(0,'jixi')
Heilongjiang.insert(-1,'qitaihe')
Heilongjiang.insert(1,'mudanjing')
print (Heilongjiang)

Heilongjiang.pop()
Heilongjiang.pop(-1)
print (Heilongjiang)

Heilongjiang.remove('jixi')
print (Heilongjiang)
print (len(Heilongjiang))

Heilongjiang.sort()
print (Heilongjiang)
Heilongjiang.sort(reverse = True)
print (Heilongjiang)
print (sorted(Heilongjiang))
print (Heilongjiang)
Heilongjiang.reverse()
print (Heilongjiang)
print (len(Heilongjiang))
