#coding: utf-8

def ComissaoSalario():
    nome = input("entre com o nome do vendedor: ")
    SalarioFixo = float(input("informe o salário: "))
    vendas = float(input("informe o total de vendas: "))
    comissao = 0.15*vendas
    PagamentoEsperado=SalarioFixo+comissao
    return nome, comissao, PagamentoEsperado
    
if __name__=="__main__":  
    nome, comissao, PagamentoEsperado=ComissaoSalario()
    strg = "{0} obteve R$ {1:.2f} de  comissão e vai receber {2:.2f}".format(nome, comissao, PagamentoEsperado)
    print(strg)