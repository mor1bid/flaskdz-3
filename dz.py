from flask import Flask
from dzmi import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)

@app.route('/')
def index():
    return 42

@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('Датабаза готова к работе.')

if __name__=="__main__":
    app.run(debug=True)