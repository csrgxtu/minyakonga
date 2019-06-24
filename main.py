from Cocoa import Cocoa

app = Cocoa()

@app.route('/')
def welcome():
    return 'Minya Konga'

# app.run(host='0.0.0.0', port=8000)
