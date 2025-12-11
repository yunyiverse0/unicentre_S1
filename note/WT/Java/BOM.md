# 🌐 BOM (Browser Object Model) 핵심 요약

**"웹 페이지 내용이 아니라, 브라우저 창(Window) 자체를 제어하는 것"**

---

## 1. 최상위 객체: `window`

* BOM의 가장 대장이자 전역 객체입니다.
* 모든 전역 변수와 함수는 사실 `window` 객체의 속성입니다.
* `window.`은 생략 가능합니다. (예: `window.alert()` → `alert()`)

---

## 2. BOM의 주요 하위 객체 (시험 필수 4대장)

### ① `location` 객체 (주소창 제어) ★★★
URL 정보를 담고 있거나 페이지를 이동시킬 때 씁니다.

* **`location.href`**: 현재 페이지의 URL을 가져오거나, 값을 넣어서 **다른 페이지로 이동**시킵니다.
    ```javascript
    // 구글로 이동 (시험에 자주 나옴)
    location.href = "[https://www.google.com](https://www.google.com)";
    
    // 현재 페이지 새로고침
    location.reload();
    ```

### ② `history` 객체 (방문 기록)
브라우저의 뒤로 가기 / 앞으로 가기 버튼 기능을 합니다.

* **`history.back()`**: 뒤로 가기 (이전 페이지)
* **`history.forward()`**: 앞으로 가기
* **`history.go(-1)`**: 한 단계 뒤로 가기 (`back()`과 동일)

### ③ `navigator` 객체 (브라우저 정보)
사용자가 무슨 브라우저(크롬, 사파리 등)를 쓰는지, 운영체제가 뭔지 알아낼 때 씁니다.

* **`navigator.userAgent`**: 브라우저와 OS 정보를 담은 긴 문자열 반환.

### ④ `screen` 객체 (화면 정보)
사용자의 모니터 해상도 정보를 가집니다.

* **`screen.width`**: 화면 너비
* **`screen.height`**: 화면 높이

---

## 3. 대화상자 (Popup) 메서드

사용자에게 메시지를 띄우는 창들도 BOM(`window`)의 기능입니다.

1. **`alert("메시지")`**: 경고창 (확인 버튼만 있음)
2. **`confirm("메시지")`**: 확인/취소창 (True/False 리턴함)
    ```javascript
    if (confirm("삭제하시겠습니까?")) {
        // 확인 눌렀을 때 실행
    }
    ```
3. **`prompt("질문", "기본값")`**: 입력창 (사용자가 입력한 값을 문자열로 리턴)

---

## ⚡ BOM vs DOM 차이점 (시험 족보)

| 구분 | BOM (Browser Object Model) | DOM (Document Object Model) |
| :--- | :--- | :--- |
| **대상** | **브라우저 창** 그 자체 (주소창, 뒤로가기 등) | 웹 페이지 내의 **HTML 문서 내용** (태그, 텍스트) |
| **최상위** | `window` 객체 | `document` 객체 (사실 window 안에 document가 있음) |
| **예시** | `location.href`, `alert()`, `history` | `document.getElementById()`, `innerHTML` |

> **한 줄 요약:**
> 브라우저 주소를 바꾸거나 경고창을 띄우려면 **BOM**,
> 태그 색깔을 바꾸거나 글자를 바꾸려면 **DOM**.
