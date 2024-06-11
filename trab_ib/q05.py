hora = int(input("digite a hora: "))
if hora >= 0 and hora < 12:
    print('já está de manhã.')
elif hora >=12 and hora < 18:
    print('já está de tarde')
else :
    print('já está de noite')
