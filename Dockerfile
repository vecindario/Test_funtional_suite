FROM python:2.7.17-alpine

ARG TEST_NAME_ARG
ARG USERNAME_ARG
ARG ACCES_KEY_ARG
ARG REPO=test-funcional-suite
ENV TEST_TO_EXECUTE=Test/${TEST_NAME_ARG}.py
ENV APP_DIR=/var/app/${REPO}
ENV PYTHON_ENV=production
ENV USERNAME=${USERNAME_ARG}
ENV ACCES_KEY=${ACCES_KEY_ARG}

RUN addgroup web_app && adduser -S web_app -G web_app

WORKDIR ${APP_DIR}

COPY --chown=web_app:web_app requirements.txt ./

RUN pip install -r requirements.txt

COPY --chown=web_app:web_app ./ .

USER web_app

RUN chmod +x ./run-test.sh 

CMD [ "./run-test.sh" ]