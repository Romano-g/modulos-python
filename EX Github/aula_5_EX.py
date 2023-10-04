"""
Maria pegou um empréstimo de 1.000.000 para realizar o pagamento em 5 anos.
A data em que pegou o empréstimo foi  20/12/2020 e o vencimento de cada parcela
se dá no dia 20 de cada mês.
 - Crie a data do empréstimo
 - Crie a data final do empréstimo
 - Mostre todas as datas de vencimento e o valor de cada parcela
"""
from datetime import datetime
from dateutil.relativedelta import relativedelta


valor = 1000000

inicio = datetime(2020, 12, 20)
dif = relativedelta(years=5)
fim = inicio + dif

data_parcelas = []
data_parcela = inicio

while data_parcela < fim:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)


numero_parcelas = len(data_parcelas)
valor_parcelas = valor/numero_parcelas


for data in data_parcelas:
    print(data.strftime('%d/%m/%Y'), f'R$ {valor_parcelas:,.2f}')
