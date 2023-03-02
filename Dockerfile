FROM python:2.7.17-alpine

ARG USERNAME_ARG
ARG ACCES_KEY_ARG
ARG REPO=test-funcional-suite
ENV APP_DIR=/var/app/${REPO}
ENV PYTHON_ENV=production

RUN addgroup web_app && adduser -S web_app -G web_app

WORKDIR ${APP_DIR}

COPY --chown=web_app:web_app requirements.txt ./

RUN pip install -r requirements.txt

COPY --chown=web_app:web_app ./ .

USER web_app

RUN chmod +x ./run-test.sh

ENV TEST_NAME=test_scheduler
ENV USERNAME=${USERNAME_ARG}
ENV ACCES_KEY=${ACCES_KEY_ARG}

CMD [ "./run-test.sh" ]

# docker build --build-arg USERNAME_ARG=$USERNAME --build-arg ACCES_KEY_ARG=$ACCES_KEY -t suite/funcional-test:1.0.0 .
# docker run --rm --name funcional-test -e TEST_NAME=$TEST_NAME suite/funcional-test:1.0.0