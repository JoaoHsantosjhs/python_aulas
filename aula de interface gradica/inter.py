import requests
from tkinter import *



def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_usdbrl = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    dolar: {cotacao_usdbrl}
    euro:{cotacao_euro}
    Bitcoin:{cotacao_btc}'''

    texto_cotacao["text"]=texto


janela = Tk()
janela.title("Cotação Atual das Moedas")
janela.geometry("250x250")
texto_orientação=Label(janela, text="Refresh Cotação")
texto_orientação.grid(column=0,row=0,padx=10,pady=10)
botao_refresh=Button(janela, text= "Refresh",command=pegar_cotacoes,padx=10,pady=10)
botao_refresh.grid(column=0,row=1,padx=10,pady=10)
texto_cotacao = Label(janela, text="",padx=10,pady=10)
texto_cotacao.grid(column=0,row=2,padx=10,pady=10)
janela.mainloop()