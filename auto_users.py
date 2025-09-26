import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

login_page = "https://admin.thexpos.net/users"

usuario = 'henro.isquierdo'
senha = '@Fr33d0m02'

new_user = "teste kendrick orichi"

aniv = "05/10/2004"

cpf = "03494064300"

celular = "5191733189"

email = "teste.silva@gmail.com"

senha_padrao = "Master@2025"

def login_maker(nome_usuario):    
    nome = new_user.split(" ")
    primeiro = nome[0]
    ultimo = nome[-1]
    log = f"{primeiro}.{ultimo}"
    return log





navegador = webdriver.Chrome()

navegador.get(login_page)

navegador.maximize_window()



wait = WebDriverWait(navegador, 10)

login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.po-input[placeholder='Insira seu usuário']")))
login.send_keys(usuario)

password = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.po-input[placeholder='Insira sua senha']")))
password.send_keys(senha)


botao_login = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'po-button')))
botao_login.click()

produto = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.po-menu-item[aria-label='Usuários']")))
produto.click()

novo_usuario = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[@class='po-button' and @p-kind='primary']//span[normalize-space(text())='Novo Usuário']"))
)
novo_usuario.click()

nome_u = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.po-input[name='name']")))
nome_u.click()
nome_u.send_keys(new_user)


logs = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.po-input[name='hidden']")))
logs.click()
login = login_maker(new_user)
logs.send_keys(login)

birth_date = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.po-input[name='datepicker']")))
birth_date.click()
birth_date.send_keys(aniv)

apelido = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.po-input[name='nickName']")))
apelido.click()
apelido.send_keys(new_user)

dropdown = navegador.find_element(By.CSS_SELECTOR, "select.po-select[name='select']")

select = Select(dropdown)

select.select_by_visible_text("Cpf")

i_cpf = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.po-input[name='documentNumber']")))
i_cpf.click()
i_cpf.send_keys(cpf)

i_celular = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.po-input[name='phone']")))
i_celular.click()
i_celular.send_keys(celular)

i_email = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.po-input[name='email']")))
navegador.execute_script("""
arguments[0].value = arguments[1];
arguments[0].dispatchEvent(new Event('input'));
arguments[0].dispatchEvent(new Event('change'));
""", i_email, email)


senha = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.po-input[name='password']")))
senha.click()
senha.send_keys(senha_padrao)

confirme_senha = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.po-input[name='confirmNewPassword']")))
confirme_senha.click()
confirme_senha.send_keys(senha_padrao)



elemento = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.po-input-icon-right[aria-label='Perfil']")))

navegador.execute_script("arguments[0].scrollIntoView(true);", elemento)
elemento.click()


caixa = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.po-item-list[aria-label='Caixa']")))
caixa.click()


salvar = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'po-button')]//span[normalize-space(text())='Salvar']")))
salvar.click()














time.sleep(20)