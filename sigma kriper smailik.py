pole=[[' ','📎','📎','📎','📎','📎','📎','📎','📎','📎'],
      [' ','📎','📎','📎','📎','📎','📎','📎','📎','📎'],
      [' ','📎','📎','📎','📎','📎','📎','📎','📎','📎'],
      [' ',' ','📎','📎','📎','📎','📎','📎','📎','📎'],
      ['📎',' ','📎',' ',' ',' ',' ',' ','📎','📎'],
      ['📎',' ','📎',' ','📎','📎','📎',' ',' ','📎'],
      [' ',' ',' ',' ','📎','📎','📎','📎',' ','📎'],
      ['📎','📎','📎','📎','📎','📎','📎','📎',' ',' '],
      ['📎','📎','📎','📎','📎','📎','📎','📎','📎','📎'],
      ['📎','📎','📎','📎','📎','📎','📎','📎','📎','📎']]
pole[0][0]='🤡'
for i in pole:
    print(i)
a=int(input("Введите координаты "))
b=int(input("Введите координаты "))
comand=input("В какую сторону ")
while 1:
    if comand=="r":
        pole[a][b]=" "
        b=b+1
    elif comand=='l':
        pole[a][b]=" "
        b=b-1
    elif comand=="d":
        pole[a][b]=" "
        a=a+1
    elif comand=="u":
        pole[a][b]=" "
        a=a-1
    if pole[a][b]=="📎":
        a=0
        b=0
    pole[a][b]="🤡"
    for i in pole:
        print(i)
    comand=input("l,d,r,u ")
