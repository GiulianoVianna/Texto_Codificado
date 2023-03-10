from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox


def mensagem(msg,texto_janela):
    msg1 = QMessageBox()
    msg1.setIcon(QMessageBox.Information)
    msg1.setWindowTitle(texto_janela)
    msg1.setText(msg)
    x = msg1.exec()


def codificar(texto):
    
    dados = texto.replace("a", "๊ฝ").replace("รก", "๐ขก").replace("ร ", "๐ขข").replace("รข", "๐ขฅ").replace("รฃ", "๐ขง")\
        .replace("A", "๐ขพ").replace("ร", "๐ขจ").replace("ร", "๐ขจ").replace("ร", "๐ขซ").replace("ร", "๐ขฌ").replace("ร", "๐ขญ")\
        .replace("b", "๊").replace("B", "๐ขฏ").replace("c", "๊พ").replace("C", "๐ขฑ").replace("d", "๊").replace("D", "๐ขณ")\
        .replace("e", "๊ฟ").replace("รฉ", "๊").replace("รช", "๐ขด").replace("E", "๐ขถ").replace("ร", "๐ขท").replace("ร", "๐ขน")\
        .replace("f", "๐ฃค").replace("F", "๐ขบ").replace("g", "๊").replace("G", "๐ขฝ").replace("h", "๊").replace("H", "๐ขพ")\
        .replace("i", "๊").replace("I", "๐ฃ").replace("j", "๊").replace("J", "๐ฃ").replace("l", "๊").replace("L", "๐ฃ")\
        .replace("m", "๊").replace("M", "๐ฃ").replace("o", "๊").replace("รณ", "๐ฃ").replace("รด", "๐ฃ").replace("O", "๐ฃ")\
        .replace("ร", "๐ฃ").replace("ร", "๐ฃ").replace("p", "๊").replace("P", "๐ฃ").replace("q", "๊").replace("Q", "๐ฃ")\
        .replace("r", "๊").replace("R", "๐ฃ").replace("s", "๊").replace("S", "๐ฃ").replace("t", "๊").replace("T", "๐ฃ")\
        .replace("u", "๐ฃข").replace("U", "๐ฃ").replace("v", "๊").replace("V", "๐ฃ").replace("w", "๐ฃ").replace("W", "๐ฃ")\
        .replace("x", "๊").replace("X", "๐ฃ").replace("y", "๐ฃ").replace("Y", "๐ฃก").replace("z", "๊").replace("Z", "๐ฃ")\
        .replace("!", "๊").replace("@", "๊").replace("#", "๊").replace("%", "๊").replace("&", "๊").replace("*", "๊")\
        .replace("(", "๊").replace(")", "๊").replace("-", "๊").replace("_", "๊").replace("=", "๊").replace("{", "๊")\
        .replace("}", "๊").replace("[", "๊").replace("]", "๊ ").replace(";", "๊ก").replace(":", "๊ข").replace("'", "๊ฃ")\
        .replace(",", "๊ค").replace("<", "๊ฅ").replace(">", "๊ฆ").replace(".", "๊ง").replace("/", "๊จ").replace("?", "๊ฉ")\
        .replace("|", "๊ช").replace("1", "๊ซ").replace("2", "๊ฌ").replace("3", "๊ฎ").replace("4", "๊ฏ")\
        .replace("5", "๊ฐ").replace("6", "๊ฑ").replace("7", "๊ฒ").replace("8", "๊ณ").replace("9", "๊ด").replace("0", "๊ต")
    return dados


def decodificar(texto):
    dados = texto.replace("๊ฝ", "a").replace("๐ขก", "รก").replace("๐ขข", "ร ").replace("๐ขฅ", "รข").replace("๐ขง", "รฃ")\
        .replace("๐ขพ", "A").replace("๐ขจ", "ร").replace("๐ขซ", "ร").replace("๐ขฌ", "ร").replace("๐ขญ", "ร")\
        .replace("๊", "b").replace("๐ขฏ", "B").replace("๊พ", "c").replace("๐ขฑ", "C").replace("๊", "d").replace("๐ขณ", "D")\
        .replace("๊ฟ", "e").replace("๊", "รฉ").replace("๐ขด", "รช").replace("๐ขถ", "E").replace("๐ขท", "ร").replace("๐ขน", "ร")\
        .replace("๐ฃค", "f").replace("๐ขบ", "F").replace("๊", "g").replace("๐ขฝ", "G").replace("๊", "h").replace("๐ขพ", "H")\
        .replace("๊", "i").replace("๐ฃ", "I").replace("๊", "j").replace("๐ฃ", "J").replace("๊", "l").replace("๐ฃ", "L")\
        .replace("๊", "m").replace("๐ฃ", "M").replace("๊", "o").replace("๐ฃ", "รณ").replace("๐ฃ", "รด").replace("๐ฃ", "O")\
        .replace("๐ฃ", "ร").replace("๐ฃ", "ร").replace("๊", "p").replace("๐ฃ", "P").replace("๊", "q").replace("๐ฃ", "Q")\
        .replace("๊", "r").replace("๐ฃ", "R").replace("๊", "s").replace("๐ฃ", "S").replace("๊", "t").replace("๐ฃ", "T")\
        .replace("๐ฃข", "u").replace("๐ฃ", "U").replace("๊", "v").replace("๐ฃ", "V").replace("๐ฃ", "w").replace("๐ฃ", "W")\
        .replace("๊", "x").replace("๐ฃ", "X").replace("๐ฃ", "y").replace("๐ฃก", "Y").replace("๊", "z").replace("๐ฃ", "Z")\
        .replace("๊", "!").replace("๊", "@").replace("๊", "#").replace("๊", "%").replace("๊", "&").replace("๊", "*")\
        .replace("๊", "(").replace("๊", ")").replace("๊", "-").replace("๊", "_").replace("๊", "=").replace("๊", "{")\
        .replace("๊", "}").replace("๊", "[").replace("๊ ", "]").replace("๊ก", ";").replace("๊ข", ":").replace("๊ฃ", "'")\
        .replace("๊ค", ",").replace("๊ฅ", "<").replace("๊ฆ", ">").replace("๊ง", ".").replace("๊จ", "/").replace("๊ฉ", "?")\
        .replace("๊ช", "|").replace("๊ซ", "1").replace("๊ฌ", "2").replace("๊ฎ", "3").replace("๊ฏ", "4")\
        .replace("๊ฐ", "5").replace("๊ฑ", "6").replace("๊ฒ", "7").replace("๊ณ", "8").replace("๊ด", "9").replace("๊ต", "0")
    return dados


def executa_codificador():
    if tela.txt_texto.toPlainText() != "":
        tela.txt_texto.setText(codificar(tela.txt_texto.toPlainText()))        

    else:
        mensagem("Favor digitar um texto!", "Atenรงรฃo")


def executa_decodificador():
    if tela.txt_texto.toPlainText() != "":
        tela.txt_texto.setText(decodificar(tela.txt_texto.toPlainText()))       

    else:
        mensagem("Favor digitar um texto!", "Atenรงรฃo")


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