from selenium import webdriver
import time 


#abrir navegador
navegador = webdriver.Chrome()

#acessando site
navegador.get("https://admin.thexpos.net/users")

#navegador tela cheia 
navegador.maximize_window()

#selecionar elemento e clicar nele se pega a classe por meio do inspecionar
botao_verde = navegador.find_element("calss name", "botao-verde")
#após tornar o botao uma variavel damos o comando a ele
botao_verde.click()


#trabalhando com vários botões 
lista_botoes = navegador.find_elements("class name", "header_botoes")

for botao in lista_botoes:
    if "Assinatura" in botao.text:
        botao.click()
        break



#mexendo com abas
#isso gera uma lista com onde os indices são as abas abertas
abas = navegador.window_handles
#e aqui alteramos o processo de aba ou seja todo código a baixo sera
#executado na aba 2 do nav
navegador.switch_to.window(abas[1])





time.sleep(20)