from flask import Flask, render_template, request
from dzmi import db, Regform

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('Name')
        surname =  request.form.get('Surname')
        email = request.form.get('Email')
        password = request.form.get('Password')
        newbie = Regform(name=f'{name}', surname=f'{surname}', email=f'{email}', password=f'{password}')
        db.session.add(newbie)
        db.session.commit()
    return render_template("base.html")

@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('Датабаза готова к работе.')

@app.cli.command('drop-db')
def drop_db():
    db.drop_all()
    print('Датабаза очищена.')


if __name__=="__main__":
    app.run(debug=True)