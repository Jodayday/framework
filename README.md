# django & docker 통한 홈페이지 배포

개발 연습을 위해 pinterest와 유사하게 제작되었습니다.

## 아키텍처

![구성](https://user-images.githubusercontent.com/86402585/177923336-068efd3c-197e-426a-97a0-68ec00fb322f.jpg)

## 실행방법

로컬

>

    pip install -r requirements.txt
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ❗ SECRET_KEY 값 .env에 저장 필요

## 실행

![작업1](https://user-images.githubusercontent.com/86402585/177924793-76f5fb8f-be39-403d-85fd-22fc1694976e.png)
![작업2](https://user-images.githubusercontent.com/86402585/177924800-9075e109-a056-44d9-bece-c5f3ce563704.png)

