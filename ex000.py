#importando função de outros arquivos (from=da) (fuc=nomeDoArquivo) (nq=nomeDaFunção)
from fuc import nq, p,  et, v, f,v1 ,f1
#nq=numero da questão
nq()
p('Ola, mundo!!!')
nq()
p('Respondendo o usuário')
nome=input('Digite seu nome: ')
p('É um prazer te conhecer {}!!'.format(nome))
nq()
p('Somando dois numeros')
n1=int(input('Digite um valor: '))
n2=int(input('Digite outro valor: '))
s = n1 + n2 
p('A soma entre {} e {} é {}'.format(n1,n2,s))
nq()
a = input('Digite algo: ')
print('O tipo primitivo desse valor é ',type(a))
if a.isspace()==True:
    v()
else:
    f()
print('Só tem espaços?'),et()
if a.isnumeric()==True:
    v()
else:
    f()
print('É um numero?'),et()
if a.isalpha()==True:
    v()
else:
    f()
print('É um alfa?'),et()
if a.isalnum()==True:
    v()
else:
    f()
print('É um alfanumérico? '),et()
if a.isupper()==True:
    i=v1()
else:
    i=f1()
print('Está em maiúsculas? ',i)

