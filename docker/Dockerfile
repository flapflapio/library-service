# STAGE 1: build the app
# ==============================================================================
FROM python:3.9 AS build
WORKDIR /build
COPY ./ /build/
RUN pip install poetry \
    && poetry export -f requirements.txt --output requirements.txt

# STAGE 2: Running the app :D
# ==============================================================================
FROM python:3.9

EXPOSE 8080
ENV PORT=8080 \
    WORKERS=1 \
    APP_PACKAGE=library_service.main:app \
    FORWARDED_ALLOW_IPS=*

HEALTHCHECK \
    --interval=30s \
    --timeout=30s \
    --start-period=5s \
    --retries=3 \
    CMD [ "/app", "-health" ]

WORKDIR /app
COPY --from=build /build/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt \
    && adduser \
    --disabled-password \
    --gecos "" \
    --home "/homeless" \
    --shell "/noshell" \
    --no-create-home \
    --uid 666 \
    library-service \
    && chown -R library-service:library-service ./
COPY --from=build /build/library_service ./library_service

USER library-service:library-service
ENTRYPOINT [ "/bin/sh", "-c" ]
CMD [ \
    "python3 -m gunicorn ${APP_PACKAGE} \
    --workers ${WORKERS} \
    --worker-class uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:${PORT} \
    --forwarded-allow-ips=\"${FORWARDED_ALLOW_IPS}\" \
    --access-logfile '-' \
    " ]
