# 🧮 프론트엔드 ↔ 백엔드 통신 흐름 이해 프로젝트

프론트엔드와 백엔드의 통신 흐름을 이해하기 위해, **덧셈 계산기**를 프론트엔드와 백엔드로 나누어 구현해보는 프로젝트입니다.

---

## 📁 폴더 구조

```bash
$ tree -L 2
.
├── backend
│   └── app.py
│   └── calculator.py
├── frontend
│   ├── index.html
│   └── script.js
├── README.md
├── requirements.txt
├── .gitignore
└── venv(생략)

추가계획 : 프론트엔드 페이지 폰트 다듬기, 숫자배열 늘리기, 웹페이지 올라가도록
장기계획 : 도커 등등 실행 자동화(백엔드 프론트엔드 모두)