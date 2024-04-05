# LoLDuoMatching
---

팀장: 지효상, 
조원: 이정우, 김범중, 이태훈

### 사이트 개요
---

목적: 같이 롤 할 듀오를 구인하는 게시판
기능: 게시글 CRUD, 댓글 CRUD, Riot API 이용 실시간 최상위권 유저 조회, 회원가입(회원가입 만)

### 개발환경
---
기술스택: Django, HTML, CSS

### 개발기간
---
2024/04/01 ~ 2024/04/04

### 기능설명
---
1. Create 
    * <post_register.html>
    * 글/댓글 작성 한 것을 게시판에 추가해 주는 기능


2. Read
    * <post_detail.html>
    * 글 작성 한 것을 게시판에서 상세페이지로 이동해 보여주는 기능
    * 글 상세 페이지에 댓글 보여주는 기능

    
3. Update
    * <post_edit.html>
    * 글/댓글을 수정하는 기능


4. Delete  
    * <index.html>
    * 글/댓글을 삭제하는 기능

5. Signup
    * <signup.html>
    * 회원가입하는 기능

6. API
    * <api.py>
    * Riot API를 가져와서 실시간 상위권 유저 리스트 출력