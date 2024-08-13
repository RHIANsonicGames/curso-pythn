import tkinter
import tkinter as tk

def exibir_mensagem():
    label.config(text="olá pobre!")

janela = tkinter.Tk()

label = tk.Label(janela, text='bem vindo!')

botao = tk.Button(janela, text= 'clique aqui', command=exibir_mensagem)

label.pack()
botao.pack()
def exibir_mensagem():
    label.config(text= "")

label1 = tk.Label(janela, text= 'e ai')



janela.mainloop()