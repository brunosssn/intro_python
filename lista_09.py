#Questão 1
def soma(a, b):
    print(a + b)
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
soma(n1, n2)

#Questão 2
def épar(x):
 return(x%2==0)
def par_ou_ímpar(x):
 if épar(x):
     return "par"
 else:
     return "ímpar"