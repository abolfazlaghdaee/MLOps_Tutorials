from flask import Flask, render_template, url_for, flash, redirect, request
from form import registration 



app = Flask(__name__)
app.secret_key = 'alkg;hadhals;flasl;df'


@app.route('/')
def hello_world():
    return '<a href="form">form</a>'



@app.route('/form', methods=['GET', 'POST'])
def Register():


    form = registration()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            confirm_password = request.form['confirm_password']


            
            return redirect(url_for('accept'))

 
            




    return render_template('form.html', form=form)



@app.route('/error')
def ErrorPass():
    return 'Passwords do not match'



@app.route('/accept')
def accept():
    return 'YOU HAVE SUCCESSFULLY REGISTERED'



if __name__ == '__main__':
    app.run(debug=True)