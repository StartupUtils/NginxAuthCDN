FROM nginx:1.19.0-alpine

RUN apk --no-cache add git
RUN git clone -b AuthV2 https://github.com/anomalizer/ngx_aws_auth.git && \
    ./configure --with-http_ssl_module --add-module=ngx_aws_auth && 

RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/conf.d