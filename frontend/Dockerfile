# Usar a imagem base do Node.js
FROM node:16

WORKDIR /app

COPY . /app
RUN mv .env-exemple .env


RUN npm install
RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
