#!/bin/sh

echo RUN TEST $TEST_TO_EXECUTE
echo USERNAME $USERNAME
echo ACCES_KEY $ACCES_KEY

pytest -rP $TEST_TO_EXECUTE