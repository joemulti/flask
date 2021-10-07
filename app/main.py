# pylint: disable=c0103
"""
TestApp
"""
import socket
from flask import Flask
from flask import request
from flask import Response
from flask import abort

local_server_ip = socket.gethostbyname(socket.gethostname())

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hallo():
    """
    Hallo
    """
    data = "Hallo"
    return Response(data, status=200)
@app.route('/status')
def home():
    """
    Status-Rückgabe
    """
    data = (
        f'Aktueller Status des Servers:<br>'
        f'IP address of the server is {local_server_ip}.<br>'
    )
    return Response(data, status=200)
@app.route('/add', methods=['GET'])
def add_op():
    """
    Addition
    """
    if 'zahleins' in request.args:
        zahleins = request.args.get('zahleins', type=int)
    else:
        abort(400)
    if 'zahlzwei' in request.args:
        zahlzwei = request.args.get('zahlzwei', type=int)
    else:
        abort(400)
    ergebnis = (zahleins + zahlzwei)
    data = '{"ergebnis": ' + str(ergebnis) + "}"
    return Response(data, status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
