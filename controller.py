from flask import Flask,render_template,redirect,request,Blueprint,jsonify
import random
 
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/changeText', methods=['POST'])
def changeText():
    text = request.form['text']
    result = text_to_int(text)
    hex_result = hex(result)
    str_hex_result = str(hex_result)
    print("********** before *******")
    print(str_hex_result)
    while(len(str_hex_result) < 8):
        rand = hex(random.randint(0,0xF))
        print(rand)
        str_hex_result = str_hex_result + str(rand)[2:]
        print("********** after *******")
        print(str_hex_result)
    code = str_hex_result[2:8]
    return code

def text_to_int(text):
    sum = 0
    for word in text:
        hex = int(word.encode('utf-8','replace').hex(),16)
        sum = sum + hex
    return sum

if __name__ == "__main__":
    app.run(debug=True)