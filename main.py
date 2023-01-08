from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox


def mensagem(msg,texto_janela):
    msg1 = QMessageBox()
    msg1.setIcon(QMessageBox.Information)
    msg1.setWindowTitle(texto_janela)
    msg1.setText(msg)
    x = msg1.exec()


def codificar(texto):
    
    dados = texto.replace("a", "ꔽ").replace("á", "𑢡").replace("à", "𑢢").replace("â", "𑢥").replace("ã", "𑢧")\
        .replace("A", "𑢾").replace("Á", "𑢨").replace("Á", "𑢨").replace("À", "𑢫").replace("Â", "𑢬").replace("Ã", "𑢭")\
        .replace("b", "ꔑ").replace("B", "𑢯").replace("c", "ꔾ").replace("C", "𑢱").replace("d", "ꔉ").replace("D", "𑢳")\
        .replace("e", "ꔿ").replace("é", "ꔃ").replace("ê", "𑢴").replace("E", "𑢶").replace("É", "𑢷").replace("Ê", "𑢹")\
        .replace("f", "𑣤").replace("F", "𑢺").replace("g", "ꕀ").replace("G", "𑢽").replace("h", "ꔊ").replace("H", "𑢾")\
        .replace("i", "ꔀ").replace("I", "𑣊").replace("j", "ꔄ").replace("J", "𑣋").replace("l", "ꔌ").replace("L", "𑣌")\
        .replace("m", "ꕁ").replace("M", "𑣍").replace("o", "ꔅ").replace("ó", "𑣎").replace("ô", "𑣑").replace("O", "𑣏")\
        .replace("Ó", "𑣐").replace("Ô", "𑣒").replace("p", "ꔆ").replace("P", "𑣓").replace("q", "ꔍ").replace("Q", "𑣔")\
        .replace("r", "ꔁ").replace("R", "𑣕").replace("s", "ꔇ").replace("S", "𑣖").replace("t", "ꔎ").replace("T", "𑣗")\
        .replace("u", "𑣢").replace("U", "𑣘").replace("v", "ꔈ").replace("V", "𑣙").replace("w", "𑣝").replace("W", "𑣞")\
        .replace("x", "ꔂ").replace("X", "𑣚").replace("y", "𑣟").replace("Y", "𑣡").replace("z", "ꔏ").replace("Z", "𑣜")\
        .replace("!", "ꔐ").replace("@", "ꔒ").replace("#", "ꔓ").replace("%", "ꔕ").replace("&", "ꔖ").replace("*", "ꔗ")\
        .replace("(", "ꔘ").replace(")", "ꔙ").replace("-", "ꔚ").replace("_", "ꔛ").replace("=", "ꔜ").replace("{", "ꔝ")\
        .replace("}", "ꔞ").replace("[", "ꔟ").replace("]", "ꔠ").replace(";", "ꔡ").replace(":", "ꔢ").replace("'", "ꔣ")\
        .replace(",", "ꔤ").replace("<", "ꔥ").replace(">", "ꔦ").replace(".", "ꔧ").replace("/", "ꔨ").replace("?", "ꔩ")\
        .replace("|", "ꔪ").replace("1", "ꔫ").replace("2", "ꔬ").replace("3", "ꔮ").replace("4", "ꔯ")\
        .replace("5", "ꔰ").replace("6", "ꔱ").replace("7", "ꔲ").replace("8", "ꔳ").replace("9", "ꔴ").replace("0", "ꔵ")
    return dados


def decodificar(texto):
    dados = texto.replace("ꔽ", "a").replace("𑢡", "á").replace("𑢢", "à").replace("𑢥", "â").replace("𑢧", "ã")\
        .replace("𑢾", "A").replace("𑢨", "Á").replace("𑢫", "À").replace("𑢬", "Â").replace("𑢭", "Ã")\
        .replace("ꔑ", "b").replace("𑢯", "B").replace("ꔾ", "c").replace("𑢱", "C").replace("ꔉ", "d").replace("𑢳", "D")\
        .replace("ꔿ", "e").replace("ꔃ", "é").replace("𑢴", "ê").replace("𑢶", "E").replace("𑢷", "É").replace("𑢹", "Ê")\
        .replace("𑣤", "f").replace("𑢺", "F").replace("ꕀ", "g").replace("𑢽", "G").replace("ꔊ", "h").replace("𑢾", "H")\
        .replace("ꔀ", "i").replace("𑣊", "I").replace("ꔄ", "j").replace("𑣋", "J").replace("ꔌ", "l").replace("𑣌", "L")\
        .replace("ꕁ", "m").replace("𑣍", "M").replace("ꔅ", "o").replace("𑣎", "ó").replace("𑣑", "ô").replace("𑣏", "O")\
        .replace("𑣐", "Ó").replace("𑣒", "Ô").replace("ꔆ", "p").replace("𑣓", "P").replace("ꔍ", "q").replace("𑣔", "Q")\
        .replace("ꔁ", "r").replace("𑣕", "R").replace("ꔇ", "s").replace("𑣖", "S").replace("ꔎ", "t").replace("𑣗", "T")\
        .replace("𑣢", "u").replace("𑣘", "U").replace("ꔈ", "v").replace("𑣙", "V").replace("𑣝", "w").replace("𑣞", "W")\
        .replace("ꔂ", "x").replace("𑣚", "X").replace("𑣟", "y").replace("𑣡", "Y").replace("ꔏ", "z").replace("𑣜", "Z")\
        .replace("ꔐ", "!").replace("ꔒ", "@").replace("ꔓ", "#").replace("ꔕ", "%").replace("ꔖ", "&").replace("ꔗ", "*")\
        .replace("ꔘ", "(").replace("ꔙ", ")").replace("ꔚ", "-").replace("ꔛ", "_").replace("ꔜ", "=").replace("ꔝ", "{")\
        .replace("ꔞ", "}").replace("ꔟ", "[").replace("ꔠ", "]").replace("ꔡ", ";").replace("ꔢ", ":").replace("ꔣ", "'")\
        .replace("ꔤ", ",").replace("ꔥ", "<").replace("ꔦ", ">").replace("ꔧ", ".").replace("ꔨ", "/").replace("ꔩ", "?")\
        .replace("ꔪ", "|").replace("ꔫ", "1").replace("ꔬ", "2").replace("ꔮ", "3").replace("ꔯ", "4")\
        .replace("ꔰ", "5").replace("ꔱ", "6").replace("ꔲ", "7").replace("ꔳ", "8").replace("ꔴ", "9").replace("ꔵ", "0")
    return dados


def executa_codificador():
    if tela.txt_texto.toPlainText() != "":
        tela.txt_texto.setText(codificar(tela.txt_texto.toPlainText()))        

    else:
        mensagem("Favor digitar um texto!", "Atenção")


def executa_decodificador():
    if tela.txt_texto.toPlainText() != "":
        tela.txt_texto.setText(decodificar(tela.txt_texto.toPlainText()))       

    else:
        mensagem("Favor digitar um texto!", "Atenção")


def limpar_texto(mensagem):
    tela.txt_texto.setText("")



app = QtWidgets.QApplication([])
tela = uic.loadUi("conversor.ui")
tela.setFixedSize(400, 554)
tela.bt_encriptar.clicked.connect(executa_codificador)
tela.bt_desencriptar.clicked.connect(executa_decodificador)
tela.bt_limpar.clicked.connect(limpar_texto)

tela.show()
app.exec()