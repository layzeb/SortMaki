from tkinter import *

class Sorteador:
    def __init__(self, janela):   #colocar todos os widgets dentro da classe

        # criando Frames (organizador de widgets dentro do conteiner)
        # Frame do título do programa (no futuro, a logo do Maki
        self.frame1 = Frame(janela)

        # Frame que contém texto + caixa de texto da quantidade de números a sortear
        self.frame2 = Frame(janela)

        # Frame que contém texto + caixa de texto do intervalo de sorteio
        self.frame3 = Frame(janela)

        # Frame que contém botão + resultado do sorteio
        self.frame4 = Frame(janela)

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()



        # cria o texto na tela (Label)
        # O metodo Label deve chamar o pai (o conteiner/instancia em que está contido, no caso, a janela e o texto
        # pack() irá mostrar o conteúdo criado na tela. A ordem de empacotamento define a ordem de aparecimento dos widgets no programa
        self.titulo = Label(self.frame1, text = 'Sorteio Makilandia!!!', fg = 'green')
        self.titulo.pack()

        self.lb_numeros = Label(self.frame2, text='Quantos numeros deseja sortear? ')
        self.ent_numeros = Entry(self.frame2)		# cria uma entrada de texto
        self.lb_range = Label(self.frame3, text='Sortear do numero 1 ao: ')
        self.ent_range = Entry(self.frame3)

        self.lb_numeros.pack()
        self.ent_numeros.pack(side = RIGHT)
        self.lb_range.pack()
        self.ent_range.pack(side = RIGHT)


        # cria um botao
        # command lida com o evento, acionando o método criado
        self.botao = Button(self.frame4, text = 'Sortear', bg = 'green', command = self.gerador)
        self.botao.pack()

        # exibe os numeros sorteados
        self.lb_resultado = Label(self.frame4)
        self.lb_resultado.pack()

    def gerador(self):
        """Método para criar o texto quando o botão for acionado"""
        self.lb_resultado['text'] = 'Números sorteados: '
        self.lb_resultado['fg'] = 'blue'




# cria a tela
janela = Tk()

Sorteador(janela)

# configura o tamanho da janela
janela.geometry('600x400')

# título da janela
janela.title('Sorteio Maki')

# cria o ícone da janela, que deve ser armazenado na mesma pasta do programa
# janela.wm_iconbitmap('icone.ico')


# cria a janela
janela.mainloop()