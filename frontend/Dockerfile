# use current LTS for node
FROM node:18.14.2-buster as build

WORKDIR  /code

COPY package.json package.json
COPY package-lock.json package-lock.json

# RUN npm install
RUN npm ci --production

# copy all files into the image 
COPY . . 

# CMD ["npm", "run","start"]

# Build the image dev-mode
# docker build -t ounass-frontend:1.0.0-dev . 

# docker run --rm -it --name frontent -p 3001:3001 -v $(pwd):/code ounass-frontend:1.0.0-dev

RUN npm run build


# second stage
FROM nginx:1.22-alpine as prod

# copy artifact into the default nginx serve location
COPY --from=build /code/build /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

# docker build -t ounass-frontend:1.0.0-prod .



# docker run --rm -it --name frontend -p 3001:3001  ounass-frontend:1.0.0-prod
