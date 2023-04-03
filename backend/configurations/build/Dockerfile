FROM golang:1.20-alpine

WORKDIR /backend

COPY . .

RUN go build -o ./server
RUN ls
EXPOSE 8000
ENTRYPOINT ["./server"]