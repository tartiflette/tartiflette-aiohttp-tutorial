FROM python:3.7.2

RUN apt-get update && apt-get install -y cmake bison flex

RUN pip install --user pipenv

ENV PYTHONPATH=/usr/src/app/
ENV PATH="$PATH:/root/.local/bin"

WORKDIR /usr/src/app

COPY Pipfile /usr/src/app/
COPY Pipfile.lock /usr/src/app/

ARG parameters=install
RUN pipenv "${parameters}"

COPY . /usr/src/app/

EXPOSE 8080

CMD ["pipenv", "run", "python", "-m", "recipes_manager"]