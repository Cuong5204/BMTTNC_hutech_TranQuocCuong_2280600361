from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher  
from cipher.railfence import RailFenceCipher
from cipher.transposition import TranspositionCipher
from cipher.playfair import PlayFairCipher
app = Flask(__name__)

# Khởi tạo đối tượng mã hóa
vigenere = VigenereCipher()

# === Home ===
@app.route("/")
def home():
    return render_template('index.html')

# === Caesar ===
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# === Vigenère ===
@app.route("/vigenere")
def vigenere_page():
    return render_template("vigenere.html")

@app.route("/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    text = request.form["inputPlainText"]
    key = request.form["inputKeyPlain"]
    result = vigenere.vigenere_encrypt(text, key)
    return render_template("vigenere.html", result=result)

@app.route("/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    text = request.form["inputCipherText"]
    key = request.form["inputKeyCipher"]
    result = vigenere.vigenere_decrypt(text, key)
    return render_template("vigenere.html", result=result)
#===
@app.route("/railfence")
def railfence_page():
    return render_template("railfence.html")

@app.route("/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    text = request.form["inputPlainText"]
    key = int(request.form["inputKeyPlain"])
    result = railfence.rail_fence_encrypt(text, key)
    return render_template("railfence.html", result=result)

@app.route("/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    text = request.form["inputCipherText"]
    key = int(request.form["inputKeyCipher"])
    result = railfence.rail_fence_decrypt(text, key)
    return render_template("railfence.html", result=result)

#==
@app.route("/transposition")
def transposition_page():
    return render_template("transposition.html")

@app.route("/transposition/encrypt", methods=["POST"])
def transposition_encrypt():
    text = request.form["inputPlainText"]
    key = int(request.form["inputKeyPlain"])
    result = transposition.encrypt(text, key)
    return render_template("transposition.html", result=result)

@app.route("/transposition/decrypt", methods=["POST"])
def transposition_decrypt():
    text = request.form["inputCipherText"]
    key = int(request.form["inputKeyCipher"])
    result = transposition.decrypt(text, key)
    return render_template("transposition.html", result=result)
#===
@app.route("/playfair")
def playfair_page():
    return render_template("playfair.html")

@app.route("/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    text = request.form["inputPlainText"]
    key = request.form["inputKeyPlain"]
    matrix = playfair.create_playfair_matrix(key)
    result = playfair.playfair_encrypt(text, matrix)
    return render_template("playfair.html", result=result)

@app.route("/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    text = request.form["inputCipherText"]
    key = request.form["inputKeyCipher"]
    matrix = playfair.create_playfair_matrix(key)
    result = playfair.playfair_decrypt(text, matrix)
    return render_template("playfair.html", result=result)



# === Run server ===
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
