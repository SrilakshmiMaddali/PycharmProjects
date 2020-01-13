'''weight=float(input('Weight:'))
lb_or_kg=input('(L)bs or (K)gs:')


if lb_or_kg in ('L','l'):
    qty=weight*0.45
    print(f'You are {qty} kgs')
elif lb_or_kg in ('K','k'):
    qty=weight*2.2
    print(f'You are {qty} pounds')
else:
    print('Enter a proper value ')'''

#triangle
'''
i=6
while i>=1:
    print('*'*i)
    i-=1


# guess game
i=1
while i <= 3:
    num = int(input('Guess:'))
    if num == 8:
        print('You Win!')
        break

    i+=1
if i>3 and num!=8 :
    print('You failed')
'''