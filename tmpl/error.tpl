[% IF BG == "" %]
    [% PROCESS htmlhead.tpl
        htmltitle = "エラー"
    %]
[% END %]

<div class="ErrMsg">
[% adminerror = 0 %]
[% IF errmsg == 'noname' %]
  名前が未入力です。ブラウザの［戻る］ボタンを使ってもう一度入力してください
[% ELSIF errmsg == 'nodmay' %]
  タイトルが未入力です。ブラウザの［戻る］ボタンを使ってもう一度入力してください
[% ELSIF errmsg == 'nocomment' %]
  内容が未入力です。ブラウザの［戻る］ボタンを使ってもう一度入力してください
[% ELSIF errmsg == 'invalidemail' %]
  E-メールの入力内容が正しくありません。よく確認してください。
  ブラウザの［戻る］ボタンを使ってもう一度入力してください
[% ELSIF errmsg == 'invaliddeleky' %]
  パスワードは8文字以内です。長すぎるとエラーがでます。
  ブラウザの［戻る］ボタンを使ってもう一度入力してください
[% ELSIF errmsg == 'namelength' %]
  名前は半角[% NMAX %]字以内でお願いします。
  ブラウザの［戻る］ボタンを使ってもう一度入力してください
[% ELSIF errmsg == 'dmaylength' %]
  タイトルは半角[% TMAX %]字以内でお願いします。
  ブラウザの［戻る］ボタンを使ってもう一度入力してください
[% ELSIF errmsg == 'commentlength' %]
  コメントは半角[% CMAX %]字以内でお願いします。
  ブラウザの［戻る］ボタンを使ってもう一度入力してください
[% ELSIF errmsg == 'notxtt' %]
  [% TXT_T %]が未入力です。
  ブラウザの［戻る］ボタンを使ってもう一度入力してください
[% ELSIF errmsg == 'nodelkey' %]
  トピック追加にはパスワードが必須です。
  ブラウザの［戻る］ボタンを使ってもう一度入力してください
[% ELSIF errmsg == 'iprefused' %]
  あなたのアクセス元IPアドレスは、過去に掲示板運営に重大な支障を及ぼす行為を行った
  などの理由で拒否されています。 [% COMipaddr %]
[% ELSIF errmsg == 'adminicon' %]
  管理者用アイコンは使用できません。
[% ELSIF errmsg == 'nopass' %]
  指定された記事にはパスワードが設定されていません。
[% ELSIF errmsg == 'invpass' %]
  パスワードが未入力か、入力されたパスワードが一致しません。
[% ELSIF errmsg == 'longmail' %]
  投稿されたメールアドレスが長すぎます。
[% ELSIF errmsg == 'longurl' %]
  投稿された URL が長すぎます。
[% ELSIF errmsg == 'invid' %]
  削除しようとしている投稿の登録 No が未入力もしくは無効です。
[% ELSIF errmsg == 'editinvid' %]
  編集しようとしている投稿の No が未入力もしくは無効です。
[% ELSIF errmsg == 'cookieoff' %]
  ブラウザの cookie が無効化されています。
  この状態ではこの掲示板への投稿はできません。
  cookie 対応のブラウザを利用するか、cookie を有効にしてください。
[% ELSIF errmsg == 'twicepost' %]
  同一内容で2度書き込もうとしています。多重投稿は無効です。再確認してください。
[% ELSIF errmsg == 'notcreator' %]
  このトピックへはトピックの作成者のみが返信できます。
[% ELSIF errmsg == 'uplimit' %]
  アップロードが許可されているサイズを超えるサイズのファイルをアップロードしようとしています。
  アップロード操作は無効化されました。
[% ELSIF errmsg == 'oldlogs' %]
  過去ログには書き込みできません。
[% ELSIF errmsg == 'viaproxy' %]
  ProxyServer経由では書き込みできません!
[% ELSIF errmsg == 'noflag' %]
  アップできないファイル形式です!
[% ELSIF errmsg == 'upoverflow' %]
  ファイルサイズが大きすぎます!
[% ELSIF errmsg == 'newpasserr' %]
  パスワードが違います!
[% ELSIF errmsg == 'novalidsetcgi' %]
  設定ファイルがCGIに設定されてません!
[% ELSIF errmsg == 'invalidfile' %]
  そのファイルは閲覧できません!
[% ELSIF errmsg == 'invalidpass' %]
  パスワードが違います!
[% ELSIF errmsg == 'locked' %]
  LOCK is BUSY (ロック中)
[% ELSIF errmsg == 'renerr' %]
  Rename Error
[% ELSIF errmsg == 'nobackup' %]
  バックアップがないので修復不可能です!
[% ELSIF errmsg == 'alreadyct' %]
  すでに ChildTree 用になっています!
[% ELSIF errmsg == 'captcha0' %]
  captchaの設定エラーです。
  [% adminerror = 1 %]
[% ELSIF errmsg == 'captcha-1' %]
  captchaの有効期限が切れました。再度取得してください。
[% ELSIF errmsg == 'captcha-2' %]
  captchaのコードが見つかりません。同じcaptchaは一度しか利用できません。
[% ELSIF errmsg == 'captcha-3' %]
  captchaのコードが一致しません。
  入力フォームをリロードしてcaptchaを取得しなおしてやり直してください。
  captchaには、2-9の数字とa-yまでの英小文字のみが利用されています。
[% ELSIF errmsg == 'cannot_write' %]
  このエントリには書き込みできません。
[% ELSIF errmsg == 'cannot_write_oldlogs' %]
  この過去ログには書き込みできません。
[% ELSIF errmsg == 'captchaoth' %]
  未知のcaptchaに関するエラーです。
  [% adminerror = 1 %]
[% ELSIF errmsg == 'edit_not_allowed' %]
  このフォーラムでは投稿記事の編集・削除は許可されていません。
[% ELSIF errmsg == 'range_undefined' %]
  範囲が指定されていません。
[% ELSIF errmsg == 'disabled' %]
  この機能は設定で無効にされています。
  必要と思われる場合は、管理者まで問い合わせてください。
[% ELSE %]
  ERROR - [% errmsg %]
[% END %]
</div>

[% IF adminerror == 1 %]
<div>
このエラーが出たときにどのような操作をしていたかとエラーコード [% errmsg %] を、
<a href="http://bugzilla.mozilla.gr.jp">bugzilla-jp</a> にバグとして登録してください。
</div>
[% END %]

[% PROCESS htmlfoot.tpl %]

