#SortMaki v1.0 - BETA

from random import randrange, seed


#str.center(width)
print('\t\tSorteio Makilandia!\n')


qt_num = int(input('Quantos números deseja sortear? '))
start = 1
stop = int(input('Sortear do número {} ao: '.format(start)))

seed()

if qt_num == 1:
    print('Número sorteado: {}'.format(randrange(start,stop)))
else:
    aux = []
    sorteados = []
    while len(sorteados) < qt_num:
        aux.append(randrange(start,stop))
        for num in aux:
            if num not in sorteados:
                sorteados.append(num)

    ordenar = input('Deseja ordenar o resultado? [S/N] ').lower().strip()
    if ordenar == 's':
        sorteados.sort()
        print(sorteados)
    else:
        print('Números sorteados: {}'.format(sorteados))