from flask import Flask, render_template, request, url_for, redirect
import base64
app = Flask(__name__)

def base64_decode(cipher):
   decoded_bytes = base64.b64decode(cipher)
   decoded_string = decoded_bytes.decode('utf-8')
   return decoded_string

def base64_encode(text):
    encoded_bytes = base64.b64encode(text.encode('utf-8'))
    encoded_string = encoded_bytes.decode('utf-8')
    return encoded_string

@app.route('/')
def HomePage():
    return render_template("index.html")

@app.route('/base64_',methods=['GET','POST'])
def base64_():
    if request.method == "POST":
        text = request.form["text"]
        if 'encrypt' in request.form:
            output = base64_encode(text)
        elif 'decrypt' in request.form:
            output = base64_decode(text)
        else:
            output = "Invalid request"

        return render_template("base64_.html", output=output)
    else:
        return render_template("base64_.html")
    
@app.route('/rsa',methods=['GET','POST'])
def rsa():
    return render_template('rsa.html')

@app.route('/Ceaser',methods=['GET','POST'])
def Ceaser():
    return render_template('Ceaser.html')

@app.route('/Hill',methods=['GET','POST'])
def Hill():
    return render_template('Hill.html')

@app.route('/Shift',methods=['GET','POST'])
def Shift():
    return render_template('Shift.html')

if __name__ == '__main__':
    app.run(debug=True,port=8080)