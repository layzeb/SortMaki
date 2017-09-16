from tkinter import *
from random import randrange, seed


class Sorteador:

    def __init__(self, janela):   #colocar todos os widgets dentro da classe

        # criando as fontes que serão usadas no programa
        # Fonte é definida como uma tupla contendo nome/tam/estilo
        self.cfont = ('Verdana', '12', 'bold')      #fonte do corpo
        self.bfont = ('Verdana', '14', 'bold')      #fonte do botao


        #----------------------------------------------------------------------------------------------------


        # criando Frames (organizador de widgets dentro do conteiner)
        # Frame das imagens título do programa
        # pady = distância dos frames no eixo y, aplicado a mesma distância pra cima e pra baixo
        self.frame1 = Frame(janela, pady = 50)

        # Frame que contém texto + caixa de texto da quantidade de números a sortear
        self.frame2 = Frame(janela)

        # Frame que contém texto + caixa de texto do intervalo de sorteio
        self.frame3 = Frame(janela, pady = 15)

        # Frame que contém botão + resultado do sorteio
        self.frame4 = Frame(janela, pady = 10)

        # Frame que contém texto + check button de ordenação do resultado
        self.frame5 = Frame(janela)

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame5.pack()
        self.frame4.pack()

        #-------------------------------------------------------------------------------------------------------


        # criando imagens
        logo = PhotoImage(file = 'makilandialogo.gif')
        sorteio = PhotoImage(file = 'sorteio3.gif')

        # imagem do sorteio
        self.sorteio = Label(self.frame1)
        self.sorteio['image'] = sorteio
        self.sorteio.image = sorteio
        self.sorteio.pack()

        # cria a logo do aplicativo
        self.logo = Label(self.frame1)
        self.logo['image'] = logo
        self.logo.image = logo
        self.logo.pack()

        #------------------------------------------------------------------------------------------------------

        # cria o texto na tela (Label)
        # O metodo Label deve chamar o pai (o conteiner/instancia em que está contido, no caso, a janela e o texto
        # pack() irá mostrar o conteúdo criado na tela. A ordem de empacotamento define a ordem de aparecimento dos widgets no programa
        #self.titulo = Label(self.frame1, text = 'Sorteio Makilandia', fg = 'green', font = self.tfont)
        #self.titulo.pack()

        self.lb_numeros = Label(self.frame2, text='Quantos números deseja sortear? ', font = self.cfont)

        self.ent_numeros = Entry(self.frame2, width = 8)		# cria uma entrada de texto
        self.ent_numeros.focus_force()      #faz o programa iniciar com a primeira entrada focada com cursor

        self.lb_range = Label(self.frame3, text='Sortear do número 1 ao: ', font = self.cfont)
        self.ent_range = Entry(self.frame3, width = 8)
        self.ent_range.bind('<Return>', self.go_enter)

        self.lb_numeros.pack(side = LEFT)
        self.ent_numeros.pack(side = LEFT)
        self.lb_range.pack(side = LEFT)
        self.ent_range.pack(side = LEFT)

        # cria o check button
        self.lb_ord = Label(self.frame5, text = 'Ordenar resultado? ', font = self.cfont)
        self.ordenar = Checkbutton(self.frame5, text = 'Sim', font = self.cfont)
        self.lb_ord.pack(side = LEFT)
        self.ordenar.pack(side = LEFT)


        # cria um botao
        # command lida com o evento, acionando o método criado
        self.botao = Button(self.frame4, text = 'Sortear', bg = '#25b05d', command = self.checker, width = 10, font = self.bfont)
        self.botao.pack()

        # exibe os numeros sorteados
        self.lb_resultado = Label(self.frame4, font = self.cfont, pady = 8)
        self.lb_resultado.pack()


    def checker(self):
        '''Testa as entradas antes de calcular o resultado'''
        ent1 = self.ent_numeros.get()
        ent2 = self.ent_range.get()
        if ent1 == '' or ent2 == '':
            self.missing_entry()
        elif not ent1.isnumeric() or not ent2.isnumeric():
            self.erro_alfa()
        else:
            self.aleatorio()



    def go_enter(self, event):
        """Determina a ativacao do botao sortear caso a segunda entrada esteja focada"""
        self.checker()

    def erro_alfa(self):
        self.lb_resultado['text'] = 'Digite somente números inteiros'
        self.lb_resultado['fg'] = 'red'
        self.ent_numeros.focus_force()


    def erro_valor(self):
        self.lb_resultado['text'] = 'Valor inválido'
        self.lb_resultado['fg'] = 'red'
        self.ent_numeros.focus_force()


    def missing_entry(self):
        self.lb_resultado['text'] = 'Campos obrigatórios'
        self.lb_resultado['fg'] = 'red'
        self.ent_numeros.focus_force()


    # -------------------------------------------------------------------------------------------------------
    # LOGICA

    def aleatorio(self):

        seed()

        qt_num = int(self.ent_numeros.get())
        stop = int(self.ent_range.get())

        if qt_num < stop:

            if qt_num == 1:
                sorteado = randrange(1, stop)
                self.lb_resultado['text'] = ('Número sorteado: {}'.format(sorteado))
                self.lb_resultado['fg'] = 'blue'
            elif qt_num > 1:
                aux = []
                ganhadores = []
                while len(ganhadores) < qt_num:
                    aux.append(randrange(1, stop))
                    for numero in aux:
                        if numero not in ganhadores:
                            ganhadores.append(numero)
                sorteado = ganhadores

                self.lb_resultado['fg'] = 'blue'
                self.lb_resultado['text'] = ('Números sorteados: {}'.format(sorteado))
            else:
                self.erro_valor()
        else:
            self.erro_valor()




# cria a tela
janela = Tk()

Sorteador(janela)

# configura o tamanho da janela
janela.geometry('800x600')

# título da janela
janela.title('Sorteio Makilandia')

# cria o ícone da janela, que deve ser armazenado na mesma pasta do programa
janela.wm_iconbitmap('Icone_Makilandia.ico')


# cria a janela
janela.mainloop()