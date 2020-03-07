def fn3(b, c, **a):
    print('a =', a, type(a))
    print('b =', b)
    print('c =', c)


fn3(b=1,d=2,c=3,e=10,f=20)
#a = {'d': 2, 'e': 10, 'f': 20} <class 'dict'>
#b = 1
#c = 3