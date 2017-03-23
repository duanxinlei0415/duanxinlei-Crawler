# -*- coding: utf-8 -*-
import math

print u'''静夜思

床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。'''
'''
# -*- coding: utf-8 -*-

print '静夜思\n床前明月光，\n疑是地上霜。\n举头望明月，\n低头思故乡。'

a = 'python'
print 'hello,', a or 'world'

b = ''
print 'hello,', b or 'world'

L = [95.5,85,59]
print L[0]
print L[1]
print L[2]
print L[-2]

L = ['Adam', 'Lisa', 'Bart']
a = L[2]
L[2] = L[0]
L[0] = a
print L

t = ('Adam')
print t

t = ('Adam',)
print t

sum = 0
x = 1
n = 1
while True:
    sum += x
    x *= 2
    n += 1
    if n == 20:
        break
print sum

sum = 0
x = 0
while True:
    x = x + 1
    if x % 2 == 0:
        continue

    if x > 99:
        break
    sum += x
print sum

print (10 >= 1)

print('1'+'0')

for x in [ 1,2,3,4,5,6,7,8,9 ]:
    for y in [ 0,1,2,3,4,5,6,7,8,9 ]:
        if x < y:
            print 10*x + y
'''
d = {

    'Adam': 95,
    'Lisa': 85,
    'Bart': 59,
}


print d['Bart']

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}

s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
    print x[0]+':'+str(x[1])

s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for li in L:
    if li in s:
        s.remove(li)
    else:
        s.add(li)
print s

L = [x*x for x in range(1,101)]
print sum(L)


k=range(1,101)
z = []
for i in k:
    i = i * i
    z.append(i)
print sum(z)

def square_of_sum(L):
    return sum(x*x for x in L)

print square_of_sum([1, 2, 3, 4, 5])
print square_of_sum([-5, 0, 5, 15, 25])

print(pow(3,2))
print(math.sqrt(4))

import math

def quadratic_equation(a, b, c):
    x = (-b+math.sqrt(pow(b,2)-4*a*c))/(2*a)
    y = (-b-math.sqrt(pow(b,2)-4*a*c))/(2*a)
    return x,y
print quadratic_equation(2, 3, 0)
print quadratic_equation(1, -6, 5)

#汉诺塔
def move(n, a, b, c):

    if(n==1):

        print a+'-->'+c

    else:

        move(n-1,a,c,b)

        print a+'-->'+c

        move(n-1,b,a,c)

move(4, 'A', 'B', 'C')


def fn(*args):
    print args
fn(2)

p=(1,2,3)
print(len(p),sum(p))

def average(*args):
    if len(args) == 0:
        return 0
    else:
        return float(sum(args))/len(args)
print average()
print average(1, 2)
print average(1, 2, 2, 3, 4)

print(range(1,3))
print(range(3))

L = range(1, 101)
print L[0:10]
print L[2::3]
print L[4:50:5]

L = range(1, 101)
print L[-10:]
print L[-46::5]

L = range(1, 101)
print L[-10:]
print L[4::5][-10:]  #先获取5的倍数，再取后10个

def firstCharUpper(s):
    return s[:1].upper()+s[1:]
print firstCharUpper('hello')
print firstCharUpper('sunday')
print firstCharUpper('september')

for i in range(1,101):
    if i % 7 == 0:
        print i

L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(L):
    print index+1, '-', name
#或者
l = ['Adam', 'Lisa', 'Bart', 'Paul']
k=range(1,5)
for index, name in zip(k,l):
    print index, '-', name

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
print d.itervalues()
for v in d.itervalues():
    print v

print [x*(x+1) for x in range(1,100)[::2]]

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    if score < 60:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    else:
        return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)
tds = [generate_tr(name, score) for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'

print(isinstance('a', str) )
if False:
    print(1)
else:
    print(2)

def toUppers(L):
    S = []
    for x in L:
        if isinstance(x,str):
            S.append(x.upper())
    return S
print toUppers(['Hello', 'world', 101])

print [m*100+n*10+o for m in range(1,10) for n in range(0,10) for o in range(1,10) if m == o]