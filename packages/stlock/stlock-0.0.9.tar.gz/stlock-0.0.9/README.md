Библиотека для сервиса авторизации **STLock** *(powered by **SmartTechnoLab**)*

**Статус:** *В разработке*

# Библиотека Python STLock


# Быстрый старт
Пример с библиотекой FastAPI


```
pip install stlock
pip install fastapi
pip install uvicorn
```

main.py:
```
from fastapi import FastAPI, HTTPException, Body, Query
from stlock import AuthClient

# создание экземпляра класса
AC = AuthClient(
    endpoint="https://d5du1ra5pgq6gr2ba1jc.apigw.yandexcloud.net/",
    user_pool_id="USER_POOL_ID",
    owner_id="OWNER_ID",
    api_key="API_KEY"
)
app = FastAPI()


# Регистрация пользователя
@app.post("/register", status_code=201)
def register_user(username=Body(...), email=Body(...), phone=Body(...), password=Body(...)):
   data, status_code = AC.register(username, email, phone, password)
   if status_code >= 400:
       raise HTTPException(status_code, data)
   return data


# Авторизация пользователя
@app.post('/login')
def login(username: str = Body(...), password: str = Body(...)):
   data, status_code = AC.authorize_user(username, password)
   if status_code >= 400:
       raise HTTPException(status_code, data)
   return data


# Обмен refresh токена но новые refresh и access токены
@app.post("/refresh")
def do_refresh_token(refresh_token=Body(...)):
    data, status_code = AC.do_refresh(refresh_token['refresh_token'])
    if status_code >= 400:
        raise HTTPException(status_code, data)
    return data


# Отозвать refresh token для выхода из аккаунта
@app.post("/logout")
def do_refresh_token(refresh_token=Body(...)):
    data, status_code = AC.unauthorized(refresh_token['refresh_token'])
    if status_code >= 400:
        raise HTTPException(status_code, data)
    return data


# Получение информации из токена
@app.get("/user")
def get_user_info(token: str = Query(...)):
    user_data = AC.decode(token)
    return user_data

```

Для запуска сервера:
```
uvicorn main:app
```

# Описание методов:

    AC.register(username, email, phone, password)

Создаёт нового пользователя в базе данных

    AC.authorize_user(username, password)

Авторизирует запрос на логин пользователя, выдаёт access & refresh токены

    AC.decode(access_token)

Декодирует токен, возвращает словарь с данными о пользователе

    AC.do_refresh(refresh_token)

Обменивает refresh token на новый access и refresh токены

    AC.unauthorized(refresh_token)

Отзывает refresh_token

# примеры запросов :
создание пользователя:

Input:
```
POST http://localhost:8000/register
Body {
    "username": "test",
    "email": "test@gmail.com",
    "phone": "79111111111",
    "password": "test"
}
```

Output:
```
{
    "policy_ids": [],
    "user_pool_id": "0e2173b5-b55f-4ea4-bec5-450e2c12a458",
    "owner_id": "b3893a06-5931-4160-9e62-938ab173b6c8",
    "username": "test6",
    "email": "test6@gmail.com",
    "phone": "79520546024",
    "id": "a351d4db-4e7f-48ef-b667-e7af3a480086",
    "status": "ACTIVE",
    "creation_timestamp": 1693303651
}
```
авторизация пользователя:

Input:
```
POST http://localhost:8000/login
Body {
    "username": "test",
    "password": "test"
}
```

Output:
```
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI3YWZkYjM5Yi0zZDZmLTQyZTMtODU1NS02NjE2OGRjYTczNDAiLCJleHAiOjE2OTMzMDQzMDEsImlhdCI6MTY5MzMwMzcwMSwidHlwZSI6IkFDQ0VTUyIsImF1ZCI6IlVTRVIiLCJzdWIiOiI1ZjMzMTE1MS00OWQxLTRkMTItYTk3Ny1hOTRhMjIzYTk0OGEiLCJvd25lcl9zdWIiOiJiMzg5M2EwNi01OTMxLTQxNjAtOWU2Mi05MzhhYjE3M2I2YzgiLCJ1c2VyX3Bvb2xfc3ViIjoiMGUyMTczYjUtYjU1Zi00ZWE0LWJlYzUtNDUwZTJjMTJhNDU4In0.gsVRcQ0R_tlL_s1aHz71YilLEuEH7Gyn3BgY6a4acgc",
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJhZTBjZWYwYS02MzU0LTRlYjYtODQwNi04NDY2NjE4ZGM1MDMiLCJleHAiOjE2OTMzMDczMDEsImlhdCI6MTY5MzMwMzcwMSwidHlwZSI6IlJFRlJFU0giLCJhdWQiOiJVU0VSIiwic3ViIjoiNWYzMzExNTEtNDlkMS00ZDEyLWE5NzctYTk0YTIyM2E5NDhhIiwib3duZXJfc3ViIjoiYjM4OTNhMDYtNTkzMS00MTYwLTllNjItOTM4YWIxNzNiNmM4IiwidXNlcl9wb29sX3N1YiI6IjBlMjE3M2I1LWI1NWYtNGVhNC1iZWM1LTQ1MGUyYzEyYTQ1OCJ9.MufGATyo2Co9evSRXd0yPTEhsLgYdb5r4qOUrsMwWmw"
}
```

Обновление токена:

Input:
```
POST http://localhost:8000/refresh
Body {
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI0MjRhYjhlMy0zMzA3LTQ0MjgtODY0Ny1iNjQzMTYwZjQxMjciLCJleHAiOjE2OTMzMDc0NDYsImlhdCI6MTY5MzMwMzg0NiwidHlwZSI6IlJFRlJFU0giLCJhdWQiOiJVU0VSIiwic3ViIjoiY2Y3ZmRmYzYtYTU0ZC00MDFlLWIxYTUtMGFiYmFkMWNjNjQzIiwib3duZXJfc3ViIjoiYjM4OTNhMDYtNTkzMS00MTYwLTllNjItOTM4YWIxNzNiNmM4IiwidXNlcl9wb29sX3N1YiI6IjBlMjE3M2I1LWI1NWYtNGVhNC1iZWM1LTQ1MGUyYzEyYTQ1OCJ9.KMHpDmVTJWsaY4L1Z6DwtiSapSNOKvRqr-4omb_96Fk"
}
```

Output:
```
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiYjZjNmEzMC05Y2Y2LTQwNTEtODc5Yi1kMjU1YTQ2MjkxZDIiLCJleHAiOjE2OTMzMDQ0NTksImlhdCI6MTY5MzMwMzg1OSwidHlwZSI6IkFDQ0VTUyIsImF1ZCI6IlVTRVIiLCJzdWIiOiJjZjdmZGZjNi1hNTRkLTQwMWUtYjFhNS0wYWJiYWQxY2M2NDMiLCJvd25lcl9zdWIiOiJiMzg5M2EwNi01OTMxLTQxNjAtOWU2Mi05MzhhYjE3M2I2YzgiLCJ1c2VyX3Bvb2xfc3ViIjoiMGUyMTczYjUtYjU1Zi00ZWE0LWJlYzUtNDUwZTJjMTJhNDU4In0.GI_hkak_GhjdeSPH25K66fggB_QhNohyLQJ1PXoz3ag",
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzNWJiOTVkNS0yOTFiLTQyNTQtOTU4Zi02NmE4YmQyY2NjZTEiLCJleHAiOjE2OTMzMDc0NTksImlhdCI6MTY5MzMwMzg1OSwidHlwZSI6IlJFRlJFU0giLCJhdWQiOiJVU0VSIiwic3ViIjoiY2Y3ZmRmYzYtYTU0ZC00MDFlLWIxYTUtMGFiYmFkMWNjNjQzIiwib3duZXJfc3ViIjoiYjM4OTNhMDYtNTkzMS00MTYwLTllNjItOTM4YWIxNzNiNmM4IiwidXNlcl9wb29sX3N1YiI6IjBlMjE3M2I1LWI1NWYtNGVhNC1iZWM1LTQ1MGUyYzEyYTQ1OCJ9.FfXom1owSaTjaFCBpj8nSZXK-d4MEetFpJCMvYQ44mQ"
}
```

Отзыв refresh токена:

Input:
```
POST http://localhost:8000/logout
Body {
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzNWJiOTVkNS0yOTFiLTQyNTQtOTU4Zi02NmE4YmQyY2NjZTEiLCJleHAiOjE2OTMzMDc0NTksImlhdCI6MTY5MzMwMzg1OSwidHlwZSI6IlJFRlJFU0giLCJhdWQiOiJVU0VSIiwic3ViIjoiY2Y3ZmRmYzYtYTU0ZC00MDFlLWIxYTUtMGFiYmFkMWNjNjQzIiwib3duZXJfc3ViIjoiYjM4OTNhMDYtNTkzMS00MTYwLTllNjItOTM4YWIxNzNiNmM4IiwidXNlcl9wb29sX3N1YiI6IjBlMjE3M2I1LWI1NWYtNGVhNC1iZWM1LTQ1MGUyYzEyYTQ1OCJ9.FfXom1owSaTjaFCBpj8nSZXK-d4MEetFpJCMvYQ44mQ"
}
```

Output:
```
STATUS_CODE: 200
```

