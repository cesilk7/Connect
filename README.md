
### 1. ビルド
```sh
docker-compose build
```

### 2. pyproject.tomlの作成
```sh
docker-compose run --entrypoint "poetry init --name connect --dependency fastapi --dependency uvicorn[standard]" connect
```

### 3. ライブラリのインストール
```sh
docker-compose run --entrypoint "poetry install" connect
```

### 新しいPythonパッケージを追加した場合などは以下のようにイメージを再ビルドするだけで、 pyproject.toml に含まれている全てのパッケージをインストールすることができます。
```sh
docker-compose build --no-cache
```

### 4. Pythonアプリケーションの起動
```sh
docker-compose up
```

### テーブルの作成（リセット）
```sh
docker-compose exec backend poetry run python -m api.migrate_db
```

### 5. サーバー起動確認
```sh
poetry run uvicorn api.main:app --host '0.0.0.0' --reload
docker-compose run --entrypoint "poetry run uvicorn api.main:app --host '0.0.0.0' --reload" backend
```
http://localhost:8000/docs

### MySQLに接続
```sh
docker-compose exec db /bin/bash
mysql -u root -p
```

### Python環境に接続
```sh
docker-compose exec backend /bin/bash
```

### Pythonライブラリの追加
```sh
# 本番
docker-compose exec backend poetry add sqlalchemy asyncpg psycopg2

# 開発
docker-compose exec backend poetry add -D pytest-asyncio aiosqlite httpx
```

### テストの実行
```sh
docker-compose run --entrypoint "poetry run pytest" backend
```
