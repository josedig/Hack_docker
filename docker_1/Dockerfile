FROM ubuntu:24.04

RUN apt update -y && apt install nginx -y

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
