import json
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'yunyi'

import mysql.connector

def load_users():
    conn = mysql.connector.connect(
        host='127.0.0.1',   #해당 DB가 있는 곳을 지정
        user='root',
        password='Mm2478510!!',
        database='한빛무역',
    )
    cursor = conn.cursor() 

    select_query = "SELECT * FROM 한빛무역.users"
    cursor.execute(select_query)
    res = cursor.fetchall()

    return res

def save_users(users_data):
    try:
        with open('users.json', 'w', encoding='utf-8') as f:
            json.dump(users_data, f, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Error saving users.json: {e}")

# 회원가입 페이지 보여주기 (GET) 및 가입 처리 (POST)
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
            return render_template('register.html') # 오류 시 다시 가입 페이지 표시

        users = load_users()

        # 이미 존재하는 사용자 이름인지 검사
        if username in users:
            flash('이미 존재하는 사용자 이름입니다.', 'error')
            return render_template('register.html') # 오류 시 다시 가입 페이지 표시

        # 새 사용자 정보 추가 (실제로는 비밀번호 해싱 필요!)
        users['username'] = {'password': password}

        # 변경된 사용자 정보 저장
        save_users(users)

        flash('성공적으로 가입되었습니다! 로그인해주세요.', 'success')
        return redirect(url_for('login')) # 가입 성공 시 로그인 페이지로 이동

    # GET 요청 시 회원가입 페이지 표시
    return render_template('register.html')

@app.route('/')     #listener
def index():

    data = load_users()
    print(data)

    return redirect('login')

@app.route('/login', methods=['GET', 'POST'])  #GET 보여줘 / POST 보내줘
def login():
    data = load_users()  #file을 여는 작업이 무거움. 따라서 파일을 연 결과 값을 변수에 저장
    if request.method == 'POST':
        username = request.form['username']     #함수 아님. form data에서 꺼내는 것
        password = request.form['password']

        for user in data:
            if user[0] == username and user[1] == password:
                print("login succesful")
                session['username'] = username
                return render_template('welcome.html',username = username)

        print('사용자 이름 또는 비번 틀림')
        flash('사용자 이름 또는 비번 틀림', 'error')
        flash('사용자 이름 또는 비번 틀림','success')
        return render_template('login.html')
    return render_template('login.html')

# 회원 정보 수정 페이지 보여주기 (GET) 및 처리 (POST)
@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    # 로그인이 되어 있지 않으면 로그인 페이지로 보냄
    if 'username' not in session:
        flash('로그인이 필요합니다.', 'error')
        return redirect(url_for('login'))

    username = session['username'] # 현재 로그인된 사용자 이름

    if request.method == 'POST':
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        # 새 비밀번호와 확인 비밀번호가 일치하는지 검사
        if new_password != confirm_password:
            flash('새 비밀번호가 일치하지 않습니다.', 'error')
            # 오류 발생 시 GET 요청처럼 다시 렌더링 (username 전달 필요)
            return render_template('edit_profile.html', username=username)

        users = load_users()

        # 사용자가 존재하는지 다시 한번 확인 (필수는 아님)
        if username in users:
            # 새 비밀번호로 업데이트 (실제로는 해싱 필요!)
            users[username]['password'] = new_password
            save_users(users) # 변경된 정보 저장
            flash('비밀번호가 성공적으로 변경되었습니다.', 'success')
            return redirect(url_for('welcome')) # 성공 시 환영 페이지로 이동
        else:
            # 혹시 모를 오류 (세션은 있는데 사용자가 삭제된 경우 등)
            flash('사용자 정보를 찾을 수 없습니다.', 'error')
            session.pop('username', None) # 안전을 위해 로그아웃 처리
            return redirect(url_for('login'))

    # GET 요청 시: 현재 사용자 이름과 함께 수정 페이지 표시
    return render_template('edit_profile.html', username=username)

@app.route('/welcome')
def welcome():
    username = session.get('username')  #세션에서 꺼내기
    return render_template('welcome.html', username=username)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':      #__name__ -> ?�스?�에???�정?�는 변??
    app.run(debug=True)
