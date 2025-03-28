import sqlite3
from flask import Flask, render_template, redirect, url_for, request, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Initialize the SQLite3 database
def init_db():
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL UNIQUE,
                        password TEXT NOT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS blogs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER NOT NULL,
                        title TEXT NOT NULL,
                        content TEXT NOT NULL,
                        FOREIGN KEY (user_id) REFERENCES users (id))''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute('SELECT title, content FROM blogs ORDER BY RANDOM() LIMIT 9')
    blogs = cursor.fetchall()
    conn.close()
    return render_template('index.html', blogs=blogs)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            session['username'] = username
            session['user_id'] = user[0]
            return redirect(url_for('home'))
        else:
            conn = sqlite3.connect('app.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
            user_exists = cursor.fetchone()
            conn.close()
            if user_exists:
                flash('Invalid password')
            else:
                flash('User does not exist. Please register first.')
                return redirect(url_for('register'))
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
            user_id = cursor.lastrowid
            session['username'] = username
            session['user_id'] = user_id
            flash('Registration successful!')
            return redirect(url_for('home'))
        except sqlite3.IntegrityError:
            flash('Username already exists')
        finally:
            conn.close()
    
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('user_id', None)
    return redirect(url_for('home'))

@app.route('/create_blog', methods=['GET', 'POST'])
def create_blog():
    if 'username' not in session:
        flash('You need to log in first')
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        user_id = session['user_id']

        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO blogs (user_id, title, content) VALUES (?, ?, ?)', (user_id, title, content))
        conn.commit()
        conn.close()

        flash('Blog created successfully!')
        return redirect(url_for('home'))

    return render_template('create_blog.html')

@app.route('/blog/<int:blog_id>', methods=['GET', 'POST'])
def view_blog(blog_id):
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute('SELECT user_id, title, content FROM blogs WHERE id = ?', (blog_id,))
    blog = cursor.fetchone()
    conn.close()

    if request.method == 'POST':
        if 'username' in session and session['user_id'] == blog[0]:
            title = request.form['title']
            content = request.form['content']
            conn = sqlite3.connect('app.db')
            cursor = conn.cursor()
            cursor.execute('UPDATE blogs SET title = ?, content = ? WHERE id = ?', (title, content, blog_id))
            conn.commit()
            conn.close()
            flash('Blog updated successfully!')
            return redirect(url_for('view_blog', blog_id=blog_id))

    can_edit = 'username' in session and session['user_id'] == blog[0]
    return render_template('view_blog.html', blog=blog, can_edit=can_edit)

if __name__ == '__main__':
    app.run(debug=True)