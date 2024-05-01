FROM python:3.11-alpine as base

# Installl poetry and its dependencies
RUN pip install pipx --no-cache &&\
    pipx install poetry &&\
    apk add gcc python3-dev musl-dev linux-headers

# add the pipx apps directory to PATH so poetry can be called
ENV PATH /root/.local/bin:$PATH
WORKDIR /src/

COPY ./pyproject.toml ./poetry.lock ./

FROM base as app

RUN poetry install --only main --no-cache

COPY ./todo_app ./todo_app/
EXPOSE 5000

ENTRYPOINT [ "poetry", "run", "flask", "run" ]
CMD [ "--host=0.0.0.0" ]

FROM base as test

COPY ./ .

RUN poetry install

ENTRYPOINT [ "poetry", "run", "pytest" ]
