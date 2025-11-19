# Eagle-X-Gen-AIアプリの活用-Dify-ChatBot構築

## 概要
Gen AIアプリの活用についてのメモ。Pain points、Solution、Difyとは、Difyでやりたいこと、Schedule、システム構成について記録されています。

## 内容

### Pain points
- **Eagle Xは全世界の営業やPricerからの問い合わせを昼夜受けており、イージーな質問はユーザが自己解決できる手段を提供したい**

### Solution
- **Gen AIのChatBotにEagle XのプロセスやFAQなどの個別資料やEagle X Portal上のコンテンツを読み込ませて、そのBotをEagle X Portal（Google Site）上に表示することで、ユーザ側での自己解決を促進したい**

### Difyとは
- **特化型のGen AIアプリを簡易に作れるプラットフォーム**
- **LLM（GPT4oやGemini 1.5ProやClaude3.5などのプロバイダー）はAPIを設定して選択する形式**
- **Openソース、クラウド型の2種類で提供されている**
- **NotebookLMやGPTsにはない強みは①RAGと②Workflowを細かく設定できること**

### Difyでやりたいこと
#### PJ特化形RAG（Knowledge）の作成
- **Pricer向けのノウハウText・FAQ**
- **Sales向けのノウハウText・FAQ**
- **Pricer/Sales共通ノウハウText・FAQ**
- **FirecrawlでEagle X Portalコンテンツの読み込み**

#### Workflow
- **はじめにPricer/SalesなどのRoleを選択させて、それに応じたRAGを参照させ回答させる**
- **質問内容がない場合はEagle Xチームにメールすることを促す、もしくはユーザ情報を取得する**
- **（Advanced）Eagle XのStatus List（Gシート）を読み込ませてアカウントごとの状況を回答させる**

#### Eagle X portalへのChatBotの組み込み
- **ユーザが慣れている箇所で完結させたい（できれば別ページに飛ばしたくない）**
- **Eagle Xチームがユーザの回答内容を常にモニターして、うまく返せていない質問へのフォローアップやFAQへの追加を行う中でPDCAを回して精度を向上させたい（管理画面が必要）**

### Schedule
- **可能であれば9月1日までにEagle X Portalに組み込みたい（FY25の開始になるため）遅くとも10月1日**
- **可能であればその前のトレーニングのときなどに紹介したい**

### システム構成
- **DifyのクラウドSaaS版（59ドル/Month）はセキュリティ上NGの場合はGCP上のVMにOpenソースのDifyを立ち上げる**
  - Google Cloud上に仮想マシンの立ち上げ（Compute Engine）
  - Dockerのインストール
  - Difyのデプロイ（ソースをGitから落としてDocker上で立ち上げ）
  - Dify管理者ユーザの作成
  - Dify上でのLLMへのAPI（Gemini 1.5Pro?）の設定
  - 各種ネットワークの設定
- **上記くらいであれば数日で実行可能と想定**
- **Dify上にRAGの登録とワークフローの構築（こちらも元データはビジネスサイドで準備できるので数日程度と想定）**

### 参考
- [今流行りの複合llm　oss「dify」をとりあえずgcpにデプロイしてみた](https://zenn.dev/furnqse/articles/df77992b76542e)
- [【Difyアプリ】RAGデータを生成し社内問合せ用チャットボットアプリを作成しました｜Ryutaro Imai](https://note.com/ryutaro_imai/n/n7349f8efd951)
- [全社的な生成AI活用プラットフォームとしての Difyの導入事例紹介](https://speakerdeck.com/tokita_kakaku/quan-she-de-nasheng-cheng-aihuo-yong-puratutohuomutositeno-difynodao-ru-shi-li-shao-jie)

## 次アクション
- [ ] 関連ノートにリンク（[[Eagle X]]、[[Gen AI]]、[[Dify]]など）
- [ ] 必要に応じてMemory Noteに変換

#gen-ai #dify #chatbot`n#memory #work/one #work/one/eagle-x #work/one/dx