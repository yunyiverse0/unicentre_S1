```markdown
# Flask + MySQL 로그인/회원가입 전체 정리

## 1. Flask 앱 생성

Flask 애플리케이션을 생성하고 secret_key를 설정한다.  
secret_key는 세션을 암호화하는 데 필요하다.

```python
app = Flask(__name__)
app.secret_key = 'yunyi'
```

---

## 2. MySQL에서 사용자 로드

MySQL 서버에 연결한 뒤 users 테이블 전체 데이터를 가져온다.  
결과는 리스트 안의 튜플 형태다.

```python
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
```

---

## 3. JSON 저장 함수

JSON 파일로 데이터를 저장하는 간단한 유틸 함수.  
현재 프로젝트는 MySQL을 사용하지만 백업용으로 존재한다.

```python
def save_users(users_data):
    with open('users.json', 'w', encoding='utf-8') as f:
        json.dump(users_data, f, indent=4, ensure_ascii=False)
```

---

## 4. 회원가입(register)

- 비밀번호와 확인 비밀번호 비교  
- username 중복 검사  
- 새 사용자 저장  
- 성공 시 login 페이지로 이동

```python
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
```

---

## 5. 메인 페이지(index)

서버 첫 접속 시 DB 연결이 정상인지 출력하고  
/login 으로 리다이렉트한다.

```python
@app.route('/')
def index():
    data = load_users()
    print(data)
    return redirect('login')
```

---

## 6. 로그인(login)

- DB에서 사용자 목록 불러오기  
- 각 row(user)에서 user[0] = username, user[1] = password  
- 일치하면 세션 생성 후 welcome 페이지 이동

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    data = load_users()

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        for user in data:
            if user[0] == username and user[1] == password:
                session['username'] = username
                return render_template('welcome.html', username=username)

        flash('사용자 이름 또는 비번 틀림', 'error')
        return render_template('login.html')

    return render_template('login.html')
```

---

## 7. 회원정보 수정(edit_profile)

- 세션에 username 없으면 로그인 필요  
- 새 비밀번호 / 비밀번호 확인 비교  
- DB 데이터 업데이트 후 저장

```python
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
```

---

## 8. 환영 페이지

세션에서 username을 가져와 welcome 페이지에 전달한다.

```python
@app.route('/welcome')
def welcome():
    username = session.get('username')
    return render_template('welcome.html', username=username)
```

---

## 9. 로그아웃

세션 삭제 후 /login 리다이렉트한다.

```python
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))
```

---

## 10. 앱 실행

```python
if __name__ == '__main__':
    app.run(debug=True)
```

---
```
