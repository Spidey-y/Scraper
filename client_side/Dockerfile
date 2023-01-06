FROM node:16.19.0

WORKDIR /usr/src/app

COPY package*.json ./

# RUN npm i
RUN npm ci --only=production
RUN npm install postcss-loader


COPY . .

EXPOSE 3000
CMD [ "npm", "run", "start" ]