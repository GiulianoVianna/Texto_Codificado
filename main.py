import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMessageBox

# Dicionário de codificação contendo o mapeamento de caracteres
# para seus respectivos símbolos codificados 
CODIFICA = {'a':'ꔽ', 'á':'𑢡', 'à':'𑢢', 'â':'𑢥', 'ã':'𑢧', 'A':'𑢾', 'Á':'𑢨', 
    'À':'𑢫', 'Â':'𑢬', 'Ã':'𑢭', 'b':'ꔑ', 'B':'𑢯', 'c':'ꔾ', 'C':'𑢱', 'd':'ꔉ', 
    'D':'𑢳', 'e':'ꔿ', 'é':'ꔃ', 'ê':'𑢴', 'E':'𑢶', 'É':'𑢷', 'Ê':'𑢹', 'f':'𑣤', 
    'F':'𑢺', 'g':'ꕀ', 'G':'𑢽', 'h':'ꔊ', 'H':'𑢾', 'i':'ꔀ', 'I':'𑣊', 'j':'ꔄ', 
    'J':'𑣋', 'l':'ꔌ', 'L':'𑣌', 'm':'ꕁ', 'M':'𑣍', 'o':'ꔅ', 'ó':'𑣎', 'ô':'𑣑', 
    'O':'𑣏', 'Ó':'𑣐', 'Ô':'𑣒', 'p':'ꔆ', 'P':'𑣓', 'q':'ꔍ', 'Q':'𑣔', 'r':'ꔁ', 
    'R':'𑣕', 's':'ꔇ', 'S':'𑣖', 't':'ꔎ', 'T':'𑣗', 'u':'𑣢', 'U':'𑣘', 'v':'ꔈ', 
    'V':'𑣙', 'w':'𑣝', 'W':'𑣞', 'x':'ꔂ', 'X':'𑣚', 'y':'𑣟', 'Y':'𑣡', 'z':'ꔏ', 
    'Z':'𑣜', '!':'ꔐ', '@':'ꔒ', '#':'ꔓ', '%':'ꔕ', '&':'ꔖ', '*':'ꔗ', '(':'ꔘ', ')':'ꔙ', 
    '-':'ꔚ', '_':'ꔛ', '=':'ꔜ', '{': 'ꔝ', '}': 'ꔞ', '[': 'ꔟ', ']': 'ꔠ', ';': 'ꔡ', 
    ':':'ꔢ', "'":'ꔣ', ',':'ꔤ', '<':'ꔥ', '>':'ꔦ', '.':'ꔧ', '/':'ꔨ', '?':'ꔩ', 
    '|':'ꔪ', '1':'ꔫ', '2':'ꔬ','3':'ꔮ', '4':'ꔯ', '5':'ꔰ', '6':'ꔱ', '7':'ꔲ', '8':'ꔳ', 
    '9':'ꔴ', '0':'ꔵ'}

# Dicionário de decodificação mapeando símbolos para caracteres originais
DECODIFICA = {v: k for k, v in CODIFICA.items()}

# Codifica o texto usando o dicionário CODIFICA
def codificar(texto):
  return ''.join([CODIFICA.get(c, c) for c in texto])

# Decodifica o texto usando o dicionário DECODIFICA  
def decodificar(texto):
  return ''.join([DECODIFICA.get(c, c) for c in texto])

# Exibe caixa de mensagem com título e texto fornecidos
def mostrar_mensagem(mensagem, titulo):
  msg = QMessageBox()
  msg.setIcon(QMessageBox.Information)
  msg.setWindowTitle(titulo)
  msg.setText(mensagem) # Passando a string da mensagem
  msg.exec_()
  
# Limpa o conteúdo da caixa de texto  
def limpar_texto():
  tela.txt_texto.clear()

# Pega o texto, codifica e mostra mensagem se vazio
def executar_codificacao():
  texto = tela.txt_texto.toPlainText()
  if texto:
    tela.txt_texto.setPlainText(codificar(texto))
  else:
    mostrar_mensagem('Favor digitar um texto!', 'Atenção')
    
# Pega o texto, decodifica e mostra mensagem se vazio  
def executar_decodificacao():
  texto = tela.txt_texto.toPlainText()
  if texto:
    tela.txt_texto.setPlainText(decodificar(texto))
  else:
    mostrar_mensagem('Favor digitar um texto!', 'Atenção')

# Cria a aplicação Qt    
app = QApplication(sys.argv)

# Carrega interface criada no Qt Designer
tela = uic.loadUi("conversor.ui")  

# Define tamanho fixo para a janela
tela.setFixedSize(400, 554)

# Vincula métodos aos eventos de clique dos botões
tela.bt_encriptar.clicked.connect(executar_codificacao)
tela.bt_desencriptar.clicked.connect(executar_decodificacao)
tela.bt_limpar.clicked.connect(limpar_texto)  

# Exibe a janela
tela.show() 

# Executa o loop de eventos da aplicação
app.exec()
