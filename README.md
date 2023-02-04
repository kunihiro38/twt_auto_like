# twitter-apiを利用して、自動で「いいね」をする
## 概要
### 1. image の構築とコンテナ起動
```
docker-compose up -d --build
```
### 2. コンテナへ接続
```
% docker exec -it python3 /bin/bash
# ls
python3_for_twt.py
```
### 3. プログラムの実行
```
# python twt_auto_like.py
```
### 4. コンテナの削除
```
% docker-compose down
```
