FROM python:3.10.5-buster

ENV PYTHONDONTWRITEBYTECODE=1
# イナリレイヤ下での標準出力とエラー出力を抑制します。
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y default-mysql-client

WORKDIR /src

RUN python -m pip install --upgrade pip
# pipを使ってpoetryをインストール
RUN pip install poetry

# poetryの定義ファイルをコピー (存在する場合)
COPY pyproject.toml* poetry.lock* ./

RUN poetry config virtualenvs.create false
RUN if [ -f pyproject.toml ]; then poetry install; fi

# uvicornのサーバーを立ち上げる
# ENTRYPOINT ["poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--reload"]
