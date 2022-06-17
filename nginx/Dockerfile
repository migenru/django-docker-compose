# Stage 1 - build frontend app
FROM node:16.14.0 as build-deps

WORKDIR /app

ENV NODE_ENV=production
COPY ./frontend/package.json /app/
RUN npm install

COPY ./frontend /app/
RUN npm run build

# Stage 2 - nginx & frontend dist
FROM nginx:alpine

COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY --from=build-deps /app/build/ /build/

CMD ["nginx", "-g", "daemon off;"]