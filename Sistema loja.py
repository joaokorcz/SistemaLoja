'''
Aluno: João Otavio Martini Korczovei
RA: 1817833
Trabalho de vetores
'''

def opcoes():
    print('==== CONTROLE DE ESTOQUE ====')
    print('====  <ESTABELECIMENTO>  ====')
    print('--=-        MENU         -=--')
    print('1 - Cadastro de produtos')
    print('2 - Alterar preço de produtos')
    print('3 - Remover produtos')
    print('4 - Alimentar estoque')
    print('5 - Vender')
    print('6 - Lista de produtos (A-Z)')
    print('7 - Sair')
    print('=============================')

def posicao(prod,x):
    if x in prod:
        for i in range(len(prod)):
            if x==prod[i]:
                return i
    else:
        return -1
    
def cadastrar(prod,quant,preco):
    n=input('Nome do produto: ')
    while n in prod:
        n=input('Este produto já está registrado, informe o nome do produto que quer adicionar: ')
    qt=int(input('Quantidade do produto: '))
    while qt<0:
        qt=int(input('Você não pode adicionar uma quantidade negativa, quantidade que deseja adicionar do produto: '))
    p=float(input('Preço do produto(unidade): '))
    while p<0:
        p=int(input('O preço do produto não pode ser negativo, informe o preço do produto: '))
    prod.append(n)
    quant.append(qt)
    preco.append(p)
    return prod,quant,preco

def alterar(prod,preco):
    p=input('Produto que deseja alterar o preço: ')
    while p not in prod or p!='':
        p=input('Este produto não está registrado, informe qual produto deseja alterar o preço, ou pressione enter para sair: ')
    pos=posicao(prod,p)
    np=float(input('Digite o novo preço do produto: '))
    preco[pos]=np
    return preco

def remover(prod,quant,preco):
    p=input('Produto que deseja remover: ')
    while p not in prod:
        p=input('Este produto não está registrado, informe qual produto deseja remover: ')
    pos=posicao(prod,p)
    del prod[pos]
    del quant[pos]
    del preco[pos]

def alimentar(prod,quant):
    p=input('Produto que deseja abastecer o estoque: ')
    while p not in prod:
        p=input('Este produto não está registrado, informe qual produto deseja abastecer o estoque: ')
    pos=posicao(prod,p)
    qt=int(input('Quantidade que deseja adicionar do produto: '))
    while qt<0:
        qt=int(input('Você não pode adicionar uma quantidade negativa, quantidade que deseja adicionar do produto: '))
    quant[pos]+=qt
    return prod,quant

def vender(prod,quant,preco,saldo):
    p=input('Produto que deseja vender: ')
    while p not in prod:
        p=input('Este produto não está registrado, informe qual produto deseja vender: ')
    pos=posicao(prod,p)
    qt=int(input('Quantidade que deseja vender: '))
    while qt<0:
        qt=int(input('Você não pode vender uma quantidade negativa, informe a quantidade que deseja vender: '))
    while qt>quant[pos]:
        qt=int(input('Essa quantidade excede o limite, quantidade que deseja vender: '))
    quant[pos]-=qt
    saldo+=qt*preco[pos]
    return prod,quant,preco,saldo

def listagem(prod):
    l=prod
    for i in range(len(prod)-1):
        for j in range(len(prod)-1):
            if l[j]>l[i+1]:
                a=l[j]
                l[j]=l[j+1]
                l[j+1]=a
    for i in range(len(l)):
        print(l[i])
    
def menu():
    prod=['po']
    quant=[]
    preco=[]
    saldo=0
    opcoes()
    opcao=int(input('Escolha uma opção: '))
    while opcao!=7:
        if opcao==1:
            prod,quant,preco=cadastrar(prod,quant,preco)
            print('PRODUTO CADASTRADO!')
            print('=============================')
        elif opcao==2:
            preco=alterar(prod,preco)
            print('PREÇO DO PRODUTO ALTERADO!')
            print('=============================')
        elif opcao==3:
            prod,preco,produto=remover(prod,quant,preco)
            print('PRODUTO REMOVIDO!')
            print('=============================')
        elif opcao==4:
            prod,quant=alimentar(prod,quant)
            print('ESTOQUE ALIMENTADO!')
            print('=============================')
        elif opcao==5:
            prod,quant,preco,saldo=vender(prod,quant,preco,saldo)
            print('PRODUTO VENDIDO!')
            print('=============================')
        elif opcao==6:
            print('LISTA DOS PRODUTOS EM ORDEM ALFABÉTICA')
            listagem(prod)
            print('\n''=============================')
        opcoes()
        opcao=int(input('\n''Escolha uma opção: '))
    print('Saldo adquirido durante vendas:',saldo)
    print('Obrigado por utilizar nosso sistema!')
menu()
