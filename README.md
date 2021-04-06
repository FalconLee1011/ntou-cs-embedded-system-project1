# 嵌入式系統 專案1

## Requirements
- Arduino IDE or vscode with arduino/platformIDE or any other arduino-supported IDE
- docker >= 19.03.5
- docker-compose >= 1.25.4
- pipenv
- node >= 14.12.0
- npm >= 7.6.0

## Usage

### code-7697
- This is the code for the 7697, upload it to the board.

### db-conpose
- This an image for our database.
  - `docker-compose run -d` under `db-conpose`.
  - Check if `mongodb://admin:<pass>@127.0.0.1:5717`

### code-backend
- Before any thing, run `pipenv install` under `code-backend`
- This is the code for all the backend stuff, including
  - MQTT subscriber
    - To start it, run `pipenv run mqtt-service` under `code-backend`
  - A flask-based HTTP server
    - To start it, run `pipenv run http-server` under `code-backend`

### code-frontend
- This is the frontend, which contains all the visual stuff.
  - run `npm install` under `code-frontend` to install dependencies.
  - To start it run `npm run serve` under `code-frontend` for a temporary server.