from tkinter import * 
import os
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rd


def salvararq():                    #Esse função abre o arquivo texto e salva os dados digitados pelo usuário na interface gráfica
    arquivo = open('Dados.txt','w') #Abre arquivo texto no modo Write
    entry1xt = entry1x.get()        #Pega os dados do usuário
    entry1yt = entry1y.get()
    arquivo.write(str(entry1xt + " " + entry1yt + "\n")) #Escreve os dados no arquivo
    entry2xt = entry2x.get()
    entry2yt = entry2y.get()
    arquivo.write(str(entry2xt + " " + entry2yt + "\n"))
    entry3xt = entry3x.get()
    entry3yt = entry3y.get()
    arquivo.write(str(entry3xt + " " + entry3yt + "\n"))
    entry4xt = entry4x.get()
    entry4yt = entry4y.get()
    arquivo.write(str(entry4xt + " " + entry4yt + "\n"))
    entry5xt = entry5x.get()
    entry5yt = entry5y.get()
    arquivo.write(str(entry5xt + " " + entry5yt + "\n"))
    entry6xt = entry6x.get()
    entry6yt = entry6y.get()
    arquivo.write(str(entry6xt + " " + entry6yt + "\n"))
    entry7xt = entry7x.get()
    entry7yt = entry7y.get()
    arquivo.write(str(entry7xt + " " + entry7yt + "\n"))
    entry8xt = entry8x.get()
    entry8yt = entry8y.get()
    arquivo.write(str(entry8xt + " " + entry8yt + "\n"))
    entry9xt = entry9x.get()
    entry9yt = entry9y.get()
    arquivo.write(str(entry9xt + " " + entry9yt + "\n"))
    entry10xt = entry10x.get()
    entry10yt = entry10y.get()
    arquivo.write(str(entry10xt + " " + entry10yt + "\n"))
    arquivo.close() #Fecha e salva o arquivo texto

def ajuslin():
    '''
    utiliza o método dos mínimos quadrados para calcular a melhor reta de ajuste dos pontos fornecidos. Ademais, também
    calcula o coeficiente de correlação que mede a qualidade do ajuste e as incertezas dos coeficientes linear e angular
    calculados.

    Entrada:

    x = array com os dados que serão linearizados
    y = array com os dados que serão linearizados

    Saída:
    b = coeficiente linear da reta
    m = coeficiente angular da reta
    plt.show() = gráfico da reta ajustada 


    '''
    x, y = np.genfromtxt('Dados.txt', unpack=True)

    n = x.size
    sx = x.sum()
    sy = y.sum()

    sxx = sx**2
    sx2 = (x**2).sum()
    sxy = (x*y).sum()

    m = (n * sxy - sx * sy) / (n * sx2 - sxx)

    xm = x.mean()
    ym = y.mean()

    b = ym - m * xm

    # Cálculo do coeficiente de correlação

    ycalc = m * x + b
    eq = ((ycalc - y)**2).sum()
    ym = y.mean()
    eqm = ((y - ym)**2).sum()
    r2 = 1 - eq/eqm


    # Cálculo das incertezas

    p1 = m*x
    p2 = b - y
    p3 = np.sqrt(((x - xm)**2).sum())

    dispy = np.sqrt((((p1 + p2)**2).sum())/n) # Dispersão média do ajuste

    deltay = y[n-1] - y[0]

    deltam = (deltay/p3) # Incerteza do coeficiente angular

    p4 = np.sqrt((x**2).sum())

    p5 = n*(((x - xm)**2).sum())

    deltab = (deltay)*(p4/p5) # Incerteza do coeficiente linear

    # criando a reta de ajuste
    xajuste = np.linspace(x.min(), x.max(), 2)  # é uma reta, não precisa de muitos pontos!
    yajuste = m * xajuste + b

    # criação do gráfico
    plt.figure()

    plt.xlabel('$x$')
    plt.ylabel('$y$')

    plt.plot(x, y, 'o', label='experimental')
    plt.plot(xajuste, yajuste, '-', label='ajuste linear')


    eq = f'$y(x) = {m:.5f} x {b:+.5f}$'  # formatando números com 5 casas decimais
    ax = plt.subplot(111)
    ax.plot(.6, b-1, label=f'$R^2={r2:.5f}$') # Colacando o coeficiente de correlação no gráfico
    ax.plot(.6, b-1.4,label= eq)  # colocando a equação no gráfico!
    ax.plot(.6, b-1.8,label=f'$ΔY={dispy:.5f}$') # Colcando a dispersão médio do ajuste no gráfico
    ax.plot(.6, b-2.2,label=f'$Δm={deltam:.5f}$') # Colcando a incerteza do coeficiente angular no gráfico
    ax.plot(.6, b-2.6,label= f'$Δb={deltab:.5f}$') # Colcando a incerteza do coeficiente linear no gráfico
    chartBox = ax.get_position()
    ax.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.6, chartBox.height])
    ax.legend(loc='upper center', bbox_to_anchor=(1.45, 0.8), shadow=True, ncol=1)
    plt.show()

    plt.legend()

    # Salvando a figura como arquivo
    plt.savefig('ajuste.png', bbox_inches='tight')

    plt.show()


def  abrirdados():  #Essa função abre o arquivo texto para que o usuário possa manipular livremente os dados
    os.system('Dados.txt')


   
root = Tk(className="Aproximador Linear BR") #Aqui começa a criação da interface gráfica

labelx = Label(root, text='X')# Cria um texto na inteface gráfica
labely = Label(root, text="Y")

entry1x = Entry(root)# Cria uma entrada de dados na inteface gráfica
entry2x = Entry(root)
entry3x = Entry(root)
entry4x = Entry(root)
entry5x = Entry(root)
entry6x = Entry(root)
entry7x = Entry(root)
entry8x = Entry(root)
entry9x = Entry(root)
entry10x = Entry(root)

entry1y = Entry(root)
entry2y = Entry(root)
entry3y = Entry(root)
entry4y = Entry(root)
entry5y = Entry(root)
entry6y = Entry(root)
entry7y = Entry(root)
entry8y = Entry(root)
entry9y = Entry(root)
entry10y = Entry(root)

labelx.grid(row=0) #Posiciona as entradas de dados nos lugares desejados
labely.grid(row=0, column=1)
entry1x.grid(row=1, column=0)
entry2x.grid(row=2, column=0)
entry3x.grid(row=3, column=0)
entry4x.grid(row=4, column=0)
entry5x.grid(row=5, column=0)
entry6x.grid(row=6, column=0)
entry7x.grid(row=7, column=0)
entry8x.grid(row=8, column=0)
entry9x.grid(row=9, column=0)
entry10x.grid(row=10, column=0)
entry1y.grid(row=1, column=1)
entry2y.grid(row=2, column=1)
entry3y.grid(row=3, column=1)
entry4y.grid(row=4, column=1)
entry5y.grid(row=5, column=1)
entry6y.grid(row=6, column=1)
entry7y.grid(row=7, column=1)
entry8y.grid(row=8, column=1)
entry9y.grid(row=9, column=1)
entry10y.grid(row=10, column=1)

dados = Button(root, text="+ Dados", command = abrirdados, height = 1, width = 10)# Cria um botão e da sua propriedades
dados.grid(columnspan=2)# Posiciona o botão no lugar desejado
salvar = Button(root, text="Salvar", command =salvararq , height = 1, width = 10)
salvar.grid(columnspan=2)
gerar = Button(root, text="Gerar gráfico", command= ajuslin, height = 1, width =10)
gerar.grid(columnspan=2)





root.mainloop()#Cria um loop para que a interface gráfica não se feche sem que o usuário solicite