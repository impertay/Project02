from server import app

@app.route('/<username>')
def user_page(username):
    return 'Hello, %s' % username
