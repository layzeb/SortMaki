from tkinter import *

class Sorteador:
    def __init__(self, janela):   #colocar todos os widgets dentro da classe

        # criando as fontes que serão usadas no programa
        # Fonte é definida como uma tupla contendo nome/tam/estilo
        self.tfont = ('Verdana','20','bold')    #fonte do título
        self.cfont = ('Verdana', '12', 'bold')      #fonte do corpo
        self.bfont = ('Verdana', '14', 'bold')


        # criando imagens
        logo = PhotoImage(file = 'makilandialogo.gif')
        sorteio = PhotoImage(file = 'sorteio3.gif')


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



        # cria o texto na tela (Label)
        # O metodo Label deve chamar o pai (o conteiner/instancia em que está contido, no caso, a janela e o texto
        # pack() irá mostrar o conteúdo criado na tela. A ordem de empacotamento define a ordem de aparecimento dos widgets no programa
        #self.titulo = Label(self.frame1, text = 'Sorteio Makilandia', fg = 'green', font = self.tfont)
        #self.titulo.pack()

        self.lb_numeros = Label(self.frame2, text='Quantos números deseja sortear? ', font = self.cfont)
        self.ent_numeros = Entry(self.frame2, width = 8)		# cria uma entrada de texto
        self.lb_range = Label(self.frame3, text='Sortear do número 1 ao: ', font = self.cfont)
        self.ent_range = Entry(self.frame3, width = 8)

        self.lb_numeros.pack(side = LEFT)
        self.ent_numeros.pack(side = RIGHT)
        self.lb_range.pack(side = LEFT)
        self.ent_range.pack(side = RIGHT)

        # cria o check button
        self.lb_ord = Label(self.frame5, text = 'Ordenar resultado? ', font = self.cfont)
        self.ordenar = Checkbutton(self.frame5, text = 'Sim', font = self.cfont)
        self.lb_ord.pack(side = LEFT)
        self.ordenar.pack(side = RIGHT)


        # cria um botao
        # command lida com o evento, acionando o método criado
        self.botao = Button(self.frame4, text = 'Sortear', bg = '#25b05d', command = self.gerador, width = 10, font = self.bfont)
        self.botao.pack()

        # exibe os numeros sorteados
        self.lb_resultado = Label(self.frame4, font = self.cfont, pady = 8)
        self.lb_resultado.pack()

    def gerador(self):
        """Método para criar o texto quando o botão for acionado"""
        self.lb_resultado['text'] = 'Números sorteados: '
        self.lb_resultado['fg'] = 'blue'




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