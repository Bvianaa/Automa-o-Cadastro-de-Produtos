# Passo 1 - Entrar no Sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login.
# pip install (pyautogui) - Biblioteca para controlar o mouse e tela do computador por meio de codigo.
import pyautogui
#import time - Biblioteca para controlar o tempo de execução 
import time

# pyautogui.write()- escreve um texto.
# pyautogui.click(x= , y=)- clica com o mouse.
# pyautogui.press()- apertar uma tecla (win,enter)
# pyautogui.hotkey()- apertar um atalho de teclado (tipo Ctrl+C )
# pyautogui.PAUSE()= 0.5 / 1.0 seg - Configuração padrão para ter um intervalo de execução.
# pyautogui.position() - diz qual a posição do mouse
# pyautogui.scroll() - rolar a tela pra baixo ou pra cima (Pra cima = numero positivo 5000 - Pra baixo = numero negativo -3000))

pyautogui.PAUSE = 1.0

# apertar a tecla win
pyautogui.press("win")

# abrir o navegador 
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
#pausa de 0.3 seg para carrega a pagina
time.sleep(2)

# Passo 2 - Fazer login 
pyautogui.click(x=719, y=511)
pyautogui.write("bruno07.viana@gmail.com")

# ir para o proximo campo podendo ser ultilizado o pyautogui.press("tab") ou pyautogui.click(x=832, y=624)
pyautogui.press("tab")
pyautogui.write("12345")
pyautogui.press("enter")

#pausa de 0.3 seg para carrega a pagina
time.sleep(2)

# Passo 3 - Importar base de dados
# pip install pandas - ferramenta para ultilizar com base de dados
import pandas 
# pandas.read_(aquivo) ler a base de dados e armazenar 
# variavel tabela recebendo o arquivo produtos.csv
tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4 - Cadastrar 1 produto 

# para cada linha da tabela = loop
for Linha in tabela.index:
    # selecionar o 1º campo
    pyautogui.click(x=820, y=364)
    # texto = string = str()
    
    # Codigo
    codigo = tabela.loc[Linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # Marca
    marca = tabela.loc[Linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # Tipo
    tipo = tabela.loc[Linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # Categoria
    categoria = tabela.loc[Linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # Preço Unitario
    preco = tabela.loc[Linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    # Custo
    custo = tabela.loc[Linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # Observação
    obs = tabela.loc[Linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    #clicar no botão enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)

# Passo 5 - Repetir o Processo de Cadastro até acabar os produtos
