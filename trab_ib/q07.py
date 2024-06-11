nome = input('digite o nome do aluno: ')
matéria = input('digite a matéria: ')
n1 = int(input('digite a nota parcial: '))
n2 = int(input('digite a nota bimestral: '))
m = (n1+n2)/2
if(m >= 6 ):
	print(f'{nome} está aprovado em disciplina {matéria} ')
else:
	print(f'{nome} está reprovado em disciplina {matéria} ')