# ⚡ JavaScript 벼락치기 [심화편]

기초(변수, 제어문) 외에 **시험 변별력을 위해 자주 출제되는 내장 객체와 메서드**입니다.

---

## 1. 문자열(String) 다루기 (시험 출제 1순위)

문자열을 자르고 찾고 바꾸는 기능은 무조건 나옵니다.

* **길이 확인**: `str.length`
* **문자 찾기**: `str.indexOf("찾을거")`
    * 있으면 인덱스(0부터 시작) 반환, 없으면 `-1` 반환 (중요!)
* **문자 자르기**:
    * `str.substring(시작, 끝)`: 시작부터 끝 **직전**까지 자름.
    * `str.split(",")`: 콤마를 기준으로 잘라서 **배열**로 만듦.
* **공백 제거**: `str.trim()` (양쪽 공백 제거)

```javascript
let text = "Hello, World";
console.log(text.indexOf("World")); // 7
console.log(text.split(","));       // ["Hello", " World"]
2. 수학(Math) 객체
숫자 계산 문제나 랜덤 뽑기 문제에 나옵니다.

Math.random(): 0.0 이상 1.0 미만의 랜덤 실수 생성 (가장 중요)

응용: 1부터 10까지 랜덤 정수 뽑기

Math.floor(Math.random() * 10) + 1

Math.floor(): 내림 (소수점 버림)

Math.ceil(): 올림

Math.round(): 반올림

Math.max(1, 5, 3): 최댓값 찾기 (5)

3. 날짜(Date) 객체
현재 시간을 구하거나 날짜를 조작할 때 씁니다.

JavaScript

let now = new Date(); // 현재 시간 객체 생성

let year = now.getFullYear(); // 연도
let month = now.getMonth();   // 월 (★주의: 0부터 시작함. 0이 1월임!)
let date = now.getDate();     // 일
let day = now.getDay();       // 요일 (0: 일요일 ~ 6: 토요일)
4. 배열(Array) 심화 메서드
for문 대신 쓰는 고급 배열 기능입니다. (최신 시험 트렌드)

forEach: 배열 돌면서 반복 실행

JavaScript

arr.forEach(function(item) { console.log(item); });
map: 배열을 변형해서 새로운 배열 리턴 (중요)

JavaScript

let arr = [1, 2, 3];
let newArr = arr.map(x => x * 2); // [2, 4, 6]
filter: 조건에 맞는 것만 골라서 새로운 배열 리턴

JavaScript

let evens = arr.filter(x => x % 2 === 0); // 짝수만 필터링
5. 타이머 함수 (비동기)
일정 시간 뒤에 실행하거나 반복할 때 씁니다.

setTimeout(함수, 시간): 시간(ms) 뒤에 함수 한 번 실행.

setInterval(함수, 시간): 시간(ms) 마다 함수 반복 실행.

clearInterval(변수): 반복하던 타이머 멈춤.

JavaScript

// 3초 뒤에 경고창 뜸 (1000ms = 1초)
setTimeout(() => alert("시간 끝!"), 3000);
6. DOM 제어 심화
HTML 태그를 다루는 조금 더 고급 기술입니다.

클래스 조작 (classList):

el.classList.add("active"): 클래스 추가

el.classList.remove("active"): 클래스 삭제

el.classList.toggle("active"): 있으면 끄고, 없으면 켬 (토글)

요소 생성 및 추가 (동적 생성):

let newDiv = document.createElement("div"); (생성)

newDiv.innerText = "새 요소"; (내용 채우기)

document.body.appendChild(newDiv); (화면에 붙이기)

⚠️ 진짜 마지막 주의사항
월(Month) 계산: getMonth()는 0월부터 11월까지입니다. 출력할 땐 무조건 +1 해줘야 합니다.

parseInt(): 문자열 숫자를 계산할 땐 parseInt("100")으로 숫자로 바꿔서 계산하세요. 안 그러면 문자로 이어 붙여집니다 ("10" + 10 = "1010").
