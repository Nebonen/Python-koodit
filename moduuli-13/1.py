from flask import Flask, request

app = Flask(__name__)
@app.route('/alkuluku')
def alkuluku():
    args = request.args
    luku = int(args.get('luku'))
    is_prime = True
    for i in range(2, luku):
        if luku % i == 0:
            is_prime = False
            break
    
    vastaus = {
        'number' : luku,
        'isPrime' : is_prime
    }
    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port='3000', debug=True)