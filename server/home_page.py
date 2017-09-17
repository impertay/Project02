from server import app

@app.route('/')
def index():
    return 'Home page'
