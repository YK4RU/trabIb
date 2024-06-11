nome = input('digite seu nome: ')
idade = int(input('digite sua idade: '))
if (idade >= 16):
	print(f'{nome} pode emitir seu titulo de eleitor')
else:
	print(f'{nome} não pode emitir seu titulo de eleitor ainda')