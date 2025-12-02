import json
from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'yunyi'

# ---------------------- DB 사용자 로드 ----------------------
def load_users():
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Mm2478510!!',
        database='한빛무역',
    )
    cursor = conn.cursor()

    select_query = "SELECT * FROM 한빛무역.users"
    cursor.execute(select_query)
    res = cursor.fetchall()

    return res


# ---------------------- JSON 저장 ----------------------
def save_users(users_data):
    try:
        with open('users.json', 'w', encoding='utf-8') as f:
            json.dump(users_data, f, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Error saving users.json: {e}")


# ---------------------- 회원가입 ----------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'username' in session:
        flash('이미 계정이 존재합니다.', 'error')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('비밀번호가 일치하지 않습니다.', 'error')
            return render_template('register.html')

        users = load_users()

        if username in users:
            flash('이미 존재하는 사용자 이름입니다.', 'error')
            return render_template('register.html')

        users[username] = {'password': password}
        save_users(users)

        flash('성공적으로 가입되었습니다! 로그인해주세요.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')


# ---------------------- 메인(index) ----------------------
@app.route('/')
def index():
    data = load_users()
    print(data)
    return redirect('login')


# ---------------------- 로그인 ----------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    data = load_users()

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        for user in data:
            if user[0] == username and user[1] == password:
                print("login succesful")
                session['username'] = username
                return render_template('welcome.html', username=username)

        print('사용자 이름 또는 비번 틀림')
        flash('사용자 이름 또는 비번 틀림', 'error')
        return render_template('login.html')

    return render_template('login.html')


# ---------------------- 회원정보 수정 ----------------------
@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    if 'username' not in session:
        flash('로그인이 필요합니다.', 'error')
        return redirect(url_for('login'))

    username = session['username']

    if request.method == 'POST':
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        if new_password != confirm_password:
            flash('새 비밀번호가 일치하지 않습니다.', 'error')
            return render_template('edit_profile.html', username=username)

        users = load_users()

        if username in users:
            users[username]['password'] = new_password
            save_users(users)
            flash('비밀번호가 성공적으로 변경되었습니다.', 'success')
            return redirect(url_for('welcome'))
        else:
            flash('사용자 정보를 찾을 수 없습니다.', 'error')
            session.pop('username', None)
            return redirect(url_for('login'))

    return render_template('edit_profile.html', username=username)


# ---------------------- 환영 페이지 ----------------------
@app.route('/welcome')
def welcome():
    username = session.get('username')
    return render_template('welcome.html', username=username)


# ---------------------- 로그아웃 ----------------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


# ---------------------- 앱 실행 ----------------------
if __name__ == '__main__':
    app.run(debug=True)
