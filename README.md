# cLoudER help service

Service that helps me to collect new music releases from beatport and create playlists.

## .env
SECRET_KEY - str, you can use `openssl rand -hex 32`
ALGORITHM - str, default is `HS256`
ACCESS_TOKEN_EXPIRE_MINUTES - int, JWT lifetime in minutes

## Run
```shell
docker-compose up --build
```