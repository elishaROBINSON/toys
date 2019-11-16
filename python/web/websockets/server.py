from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="null")

@socketio.on('my event')
def test_message(message):
    print("we are connected")


if __name__ == '__main__':
    socketio.run(app, host = "0.0.0.0")

