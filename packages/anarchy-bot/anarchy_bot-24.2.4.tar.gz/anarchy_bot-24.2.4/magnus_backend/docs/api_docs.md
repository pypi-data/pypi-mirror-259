# api docs

### check if user registered

```shell
curl -X POST http://0.0.0.0:8000/auth/check \
    -H "Content-Type: application/json" \
    -d '{"email": "example@email.com"}'
```

### register new user

```shell
curl -X POST http://0.0.0.0:8000/auth/register \
    -H "Content-Type: application/json" \
    -d '{"email": "example@email.com", "password": "my_password"}'
```

### login existing user

```shell
curl -X POST http://0.0.0.0:8000/auth/login \
    -H "Content-Type: application/json" \
    -d '{"email": "example@email.com", "password": "my_password"}'
```
