FROM python:2.7.17-alpine

ARG REPO=test-funcional-suite
ARG TEST_NAME=test_preaproved
ENV TEST_TO_EXECUTE=Test/${TEST_NAME}.py
ENV APP_DIR=/var/app/${REPO}
ENV USERNAME=qa.testing
ENV ACCES_KEY=pTKXtmbr4JmEdVICsRIS5ZXVQxkyN6f3oy2DIs8Qx8CWcChHS9
ENV PYTHON_ENV = production

RUN addgroup web_app && adduser -S web_app -G web_app

WORKDIR ${APP_DIR}

COPY --chown=web_app:web_app requirements.txt ./

RUN pip install -r requirements.txt

COPY --chown=web_app:web_app ./ .

USER web_app

RUN chmod +x ./run-test.sh 

CMD [ "./run-test.sh" ]