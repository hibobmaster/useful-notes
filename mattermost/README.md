
## Dockerfile for linux arm64 mattermost
mattermost version: 9.2.2

## Setup steps
```sh
cd ~/build/mattermost
wget https://raw.githubusercontent.com/mattermost/mattermost/master/server/build/entrypoint.sh
wget https://raw.githubusercontent.com/hibobmaster/useful-notes/main/mattermost/Dockerfile
```

Build arm64 docker image
```
docker build . -t mattermost-arm:9.2.2
```

---

Mattermost working directory setup
```bash
cd /opt/mattermost
wget https://raw.githubusercontent.com/hibobmaster/useful-notes/main/mattermost/compose.yaml
mkdir -p mattermost/{config,data,logs,plugins,bleve-indexes}
mkdir -p mattermost/client/plugins
chown 2000:2000 -R .
```

Spin up container
```
docker compose up
```
If it looks okay, `Ctrl+C` then run the container in detach mode.
```
docker compose up -d
```

Cheers!