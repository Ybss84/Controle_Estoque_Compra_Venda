inf = 0
while (inf < 4):
    from datetime import datetime
    now = datetime.now()

    a = now.year #ano
    m = now.month #mês
    d = now.day #dia
    h = now.hour #hora
    mi = now.minute #minuto
    s = now.second #segundo
    
    print("Olá, seja bem vindo!")
    print("Informações abaixo: ")
    print("\n(1) Comprar")
    print("\n(2) Vender")
    print("\n(3) Ver estoque")
    print("\n(4) Sair")
    inf      = int(input("\nQual opção deseja:"))
    inf = inf + 1
    est = 0
    if inf == 1:
        buy = float(input("\nQuantos Kg deseja comprar de Arroz: "))
        est = est + buy
        arquivo = open('buy.txt','a')
        arquivo.write("\nFoi comprado: {}Kg".format(buy))
        arquivo.write("\nHorário da compra: {}:{}:{}".format(h,mi,s))
        arquivo.write("\nData da compra: {}/{}/{}".format(d,m,a))
        arquivo.write("\nEstoque atual: {}Kg".format(est))
        arquivo.close()
    if inf == 2:
        sell = float(input("\nDeseja vender quantos Kg de Arroz: "))
        est = est - sell
        arquivo = open('sell.txt','a')
        arquivo.write("\nFoi vendido: {}Kg".format(sell))
        arquivo.write("\nHorário da venda: {}:{}:{}".format(h,mi,s))
        arquivo.write("\nData da compra: {}/{}/{}".format(d,m,a))
        arquivo.write("\nEstoque atual: {}Kg".format(est))
        arquivo.close()
    if inf == 3:
        print("\nO estoque atual: {}Kg".format(est))
                    
else:
    print("\nPrograma encerrado com sucesso!")