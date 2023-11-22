## Dockerfile for linux arm64 rocketchat
rocketchat version: 6.4.8

## Setup steps
1. Build rocketchat docker image
```sh
mkdir -p ~/build/rocketchat
cd ~/build/rocketchat
wget https://github.com/hibobmaster/useful-notes/raw/main/rocketchat/Dockerfile
docker build . -t rocketchat-arm:6.4.8
```

2. Prepare and spin up container
```sh
mkdir /opt/rocketchat
cd /opt/rocketchat
mkdir chat
mkdir uploads
chown 2000:2000 -R . 
wget https://github.com/hibobmaster/useful-notes/raw/main/rocketchat/compose.yaml
```
Change `chat.example.com` to your server's name.

Launch mongodb first
```sh
docker compose up mongodb -d
docker exec -it rocketchat-mongodb bash
mongosh
rs.initiate()
exit
exit
```
Spin up container
```sh
docker compose up -d
```
Wait a bit and visit your site.