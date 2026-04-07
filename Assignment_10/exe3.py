from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/prime_number/<int:number>')
def check_prime(number):
    is_prime = True
    if number <= 1:
        is_prime = False
    else:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
                
    result = {
        "Number": number,
        "isPrime": is_prime
    }
    return jsonify(result)

app.run(port=5000)