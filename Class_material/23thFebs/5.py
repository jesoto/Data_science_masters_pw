from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/user/<username>')
def user_profile(username):
    return f'Profile page of {username}'

with app.test_request_context():
    print(url_for('index'))
    # Output: '/'

    print(url_for('user_profile', username='John Doe'))
    # Output: '/user/John%20Doe'

if __name__=="__main__":
    app.run(host="0.0.0.0")
