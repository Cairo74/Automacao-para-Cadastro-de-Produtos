import pyautogui
import time


pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write("(sua lista)")
pyautogui.press("enter")

time.sleep(2.5)

pyautogui.click(x=777, y=408)
pyautogui.write("emailaleatorio@gmail.com")

pyautogui.press("tab")
pyautogui.write("senhaaleatoria")

pyautogui.click(x=956, y=565)

time.sleep(2)

import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:

    pyautogui.click(x=744, y=293)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab") 

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
      pyautogui.write(str(obs))

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)