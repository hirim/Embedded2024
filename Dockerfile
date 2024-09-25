FROM golang

WORKDIR /app

RUN go mod init opensource

COPY . /app

CMD ["go", "run", "wow_opensource.go"]
