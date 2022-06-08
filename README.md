

1. ビルド
```sh
docker-compose build
```

2. pyproject.tomlの作成
```sh
docker-compose run --entrypoint "poetry init --name connect --dependency fastapi --dependency uvicorn[standard]" connect
```

3. FastAPIのインストール
```sh
docker-compose run --entrypoint "poetry install" connect
```

- 新しいPythonパッケージを追加した場合などは以下のようにイメージを再ビルドするだけで、 pyproject.toml に含まれている全てのパッケージをインストールすることができます。
```sh
docker-compose build --no-cache
```

4. Pythonアプリケーションの起動
```sh
docker-compose up
```

- テーブルの作成（リセット）
```sh
docker-compose exec connect poetry run python -m api.migrate_db
```

5. サーバー起動確認  
http://localhost:8000/docs

- PostgreSQLに接続
```sh
docker-compose exec db /bin/bash
su - postgres
psql
```

- Pythonライブラリの追加
```sh
docker-compose exec connect poetry add sqlalchemy asyncpg psycopg2
```
