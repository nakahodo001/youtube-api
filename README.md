# youtubeの特定の動画からシーンコメントを抽出するAPI

## 内容
特定のyoutube動画のコメントから時間指定のあるコメントを抽出するAPI

## 目的
* <b>「好きな」 or 「注目されている」シーンを振り返る</b>システムを作りたかった．https://github.com/nakahodo001/chrome-youtube-time-comment

## 使用方法
video_idの対の部分にyoutubeの動画IDを指定．

「v=xxx」 の 「xxx」 部：https://www.youtube.com/watch?v=<b>LM33oX5oJhM</b>

`curl -X POST -H "Content-Type: application/json" -d "{\"video_id\":\"LM33oX5oJhM\"}" https://youtube-comment-emotions-api.herokuapp.com/youtube_time_comment`

## やっていること
* youtubeAPI を使って特定動画のコメントを取得
* 取得したコメントからシーンと共にコメントしているものだけを抽出

## やりたいこと
* そのシーンの感情推定までを行いたい．
(localでは出来ているが，まだmecubをherokuに導入できていない)