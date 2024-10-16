from flask import Flask, render_template, request, session, redirect, url_for
import os

USER = 'DW'
PASS = 'n00b'

SUCCESS = 1
BAD_PASS = -1
BAD_USER = -2

form_site = Flask(__name__)
form_site.secret_key = os.urandom(64)

def authenticate(user, passw):
    if user == USER:
        if passw == PASS:
            return  SUCCESS
        else:
            return BAD_PASS
    else:
        return BAD_USER

@form_site.route('/')
def root():
    if 'user' not in session:
        return render_template('form.html', title="Login")
    else:
        return redirect( url_for('welcome') )

@form_site.route('/auth', methods=['POST'])
def auth():
    user = request.form['user']
    passw = request.form['pw']
    
    result = authenticate(user, passw)

    flash('WOOHOO!')

    if result == SUCCESS:
        session['user'] = user
        return redirect( url_for('welcome') )
    if result == BAD_PASS:
        pass
    elif result == BAD_USER:
        pass
    return redirect(url_for('root'))

@form_site.route('/welcome')
def welcome():
    if 'user' not in session:
        return redirect( url_for('root') )
    else:
        return render_template('welcome.html', user=session['user'], title='Welcome')

@form_site.route('/logout', methods=['POST'])
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect( url_for('root') )
                               

if __name__ == '__main__':
    form_site.debug = True
    form_site.run()