# ER_Hub
コラボレーション可能なER図作成・管理プラットフォーム

## 概要
**ER_Hub**は、エンジニア動詞がER図を共同で作成、編集・レビューできるwebアプリケーションです。
GitHubのように、ER図に対してバージョン管理を可能にし、プロジェクトの設計過程を可視化・共有します。

## 主な機能
### MVP
- プロジェクトの作成
- ER図の新規作成/編集/保存
- JSONベースでのER図構造管理

## ディレクトリ構成
- /web   ... PHP/Laravel + Vue.js + TypeScript
- /api   ... Python/FastAPI
- /infra
    - /local      = Docker / Docker COmpose
    - /production = Terraform

## 今後の展開予定
- コミット単位でのER図バージョン保存
- ER図のリアルタイム編集
- プルリク・コメント・レビュー機能
- ER図のバージョン比較・差分表示
- DDL・マイグレーションファイル・モデルクラスのエクスポート
