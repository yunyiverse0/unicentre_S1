USE db과제;

-- 1. 출처 테이블
CREATE TABLE `출처` (
    출처ID INT PRIMARY KEY,
    기관명 VARCHAR(50) NOT NULL
);

-- 2. 민간분야 해킹/랜섬웨어 총 침해사건수
CREATE TABLE `민간분야_해킹랜섬웨어_총침해사건수` (
    출처ID INT NOT NULL,
    연도 INT PRIMARY KEY,
    침해사건건수 INT NOT NULL,
    FOREIGN KEY (출처ID) REFERENCES `출처`(출처ID)
);

-- 3. 개인정보유출원인
CREATE TABLE `개인정보유출원인` (
    순서 INT PRIMARY KEY,
    출처ID INT NOT NULL,
    원인 VARCHAR(100) NOT NULL,
    비율 VARCHAR(10) NOT NULL,
    건수 INT NOT NULL,
    FOREIGN KEY (출처ID) REFERENCES `출처`(출처ID)
);

-- 4. 개인정보유출신고현황
CREATE TABLE `개인정보유출신고현황` (
    출처ID INT NOT NULL,
    연도 INT PRIMARY KEY,
    신고건수 INT NOT NULL,
    FOREIGN KEY (출처ID) REFERENCES `출처`(출처ID)
);

-- 5. 해킹세부유형
CREATE TABLE `해킹세부유형` (
    순서 INT PRIMARY KEY,
    출처ID INT NOT NULL,
    유형명 VARCHAR(200) NOT NULL,
    건수 INT NOT NULL,
    FOREIGN KEY (출처ID) REFERENCES `출처`(출처ID)
);

-- 6. 정보보호 안전 체감도
CREATE TABLE 정보보호안전체감도 (
    출처ID INT NOT NULL,
    항목 VARCHAR(100) NOT NULL,
    응답비율 VARCHAR(10) NOT NULL
);

-- 7. 정보보호 교육 방식
CREATE TABLE 정보보호교육방식 (
    출처ID INT NOT NULL,
    항목 VARCHAR(150) NOT NULL,
    응답비율 VARCHAR(10) NOT NULL
);

-- 8. 침해사고 경험 유형
CREATE TABLE 침해사고경험유형 (
    출처ID INT NOT NULL,
    항목 VARCHAR(200) NOT NULL,
    응답비율 VARCHAR(10) NOT NULL
);

-- 9. 침해사고 미신고 이유
CREATE TABLE 침해사고미신고이유 (
    출처ID INT NOT NULL,
    항목 VARCHAR(200) NOT NULL,
    응답비율 VARCHAR(10) NOT NULL
);
