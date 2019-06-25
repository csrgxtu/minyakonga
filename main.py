from Cocoa import Cocoa

app = Cocoa()

@app.route('/')
def welcome():
    return 'Minya Konga'

@app.route('/static/<file_name>')
def static(file_name):
    with open('./static/{}'.format(file_name), 'r') as file_handler:
        return file_handler.read()

# app.run(host='0.0.0.0', port=8000)
