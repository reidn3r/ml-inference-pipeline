FROM node:20-alpine AS build

WORKDIR /app
COPY . .

RUN npm i
RUN npm run build

FROM node:20-alpine AS prod

WORKDIR /app
COPY --from=build /app/package*.json ./
COPY --from=build /app/dist ./dist
RUN npm install --omit=dev

EXPOSE 3030

CMD ["node", "./dist/src/server.ts"]