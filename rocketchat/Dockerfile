FROM node:14.21.3-bullseye

ARG PUID=2000
ARG PGID=2000

# set user/group id for rocketchat
RUN groupadd -g ${PGID} rocketchat  \
  && useradd -u ${PUID} -g rocketchat rocketchat \
  && mkdir -p /app/uploads \
  && chown rocketchat:rocketchat /app/uploads

VOLUME /app/uploads

ENV RC_VERSION 6.7.2

WORKDIR /app
RUN set -eux \
  && apt-get update \
  && apt-get install -y --no-install-recommends fontconfig \
  && aptMark="$(apt-mark showmanual)" \
  && apt-get install -y --no-install-recommends g++ make python ca-certificates curl gnupg \
  && rm -rf /var/lib/apt/lists/* \
  # gpg: key 4FD08104: public key "Rocket.Chat Buildmaster <buildmaster@rocket.chat>" imported
  && gpg --batch --keyserver keyserver.ubuntu.com --recv-keys 0E163286C20D07B9787EBE9FD7F9D0414FD08104 \
  && curl -fSL "https://releases.rocket.chat/${RC_VERSION}/download" -o rocket.chat.tgz \
  && curl -fSL "https://releases.rocket.chat/${RC_VERSION}/asc" -o rocket.chat.tgz.asc \
  && gpg --batch --verify rocket.chat.tgz.asc rocket.chat.tgz \
  && tar zxf rocket.chat.tgz \
  && rm rocket.chat.tgz rocket.chat.tgz.asc \
  && cd bundle/programs/server \
  && set METEOR_SKIP_NPM_REBUILD=1 \
  && npm install @rocket.chat/forked-matrix-sdk-crypto-nodejs@0.1.0-beta.13 --no-save \
  && rm -rf npm/node_modules/@rocket.chat/forked-matrix-sdk-crypto-nodejs \
  && mv -fu node_modules/@rocket.chat/forked-matrix-sdk-crypto-nodejs npm/node_modules/@rocket.chat/ \
  && unset METEOR_SKIP_NPM_REBUILD \
  && npm install --production --unsafe-perm \
  && apt-mark auto '.*' > /dev/null \
  && apt-mark manual $aptMark > /dev/null \
  && find /usr/local -type f -executable -exec ldd '{}' ';' \
  | awk '/=>/ { print $(NF-1) }' \
  | sort -u \
  | xargs -r dpkg-query --search \
  | cut -d: -f1 \
  | sort -u \
  | xargs -r apt-mark manual \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && npm cache clear --force \
  && chown -R rocketchat:rocketchat /app

USER rocketchat

WORKDIR /app/bundle

# needs a mongoinstance - defaults to container linking with alias 'db'
ENV DEPLOY_METHOD=docker-official \
  MONGO_URL=mongodb://db:27017/meteor \
  HOME=/tmp \
  PORT=3000 \
  ROOT_URL=http://localhost:3000 \
  Accounts_AvatarStorePath=/app/uploads

EXPOSE 3000

CMD ["node", "main.js"]