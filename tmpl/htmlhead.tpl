<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
[% 
  styledir = "style/default/"
%]
<html lang="ja">
<head>
  <meta http-equiv="Content-type" content="text/html; charset=Shift_JIS">

  <!-- meta names -->
  <meta name="keywords" content="mozilla,Gecko,bugzilla,newzilla,mozillazine,bbs">
  <meta name="classification" content="コンピュータ,インターネット,ブラウザ">
  <meta name="description" content="mozilla.orgで開発されているmozilla Webブラウザに関連する日本の情報を集約したサイトのBBSです">
  <meta name="date" content="2002-02-22">
  <meta name="author" content="Mozilla-gumi">

  <meta http-equiv="Content-Script-Type" content="text/javascript">
  <script language="JavaScript" type="text/javascript" src="common.js"></script>
  <script language="JavaScript" type="text/javascript" src="bbcode.js"></script>

  <!-- relations -->
  <link rel="top" href="http://www.mozilla.gr.jp" title="もじら組トップ">
  <link rel="up" href="cbbs.cgi" title="BBSトップ">
  <link rel="search" href="srch.cgi?no=0" title="BBS内検索">
  <link rel="help" href="cbbs.cgi?mode=man&amp;no=0" title="BBSヘルプ">
  <link rel="author" href="http://www.mozilla.gr.jp/info.html" title="連絡先について">

  <!-- bookmarks -->
  <link rel="bookmark" href="http://bugzilla.mozilla.gr.jp/" title="Bugzilla-jp">
  <link rel="bookmark" href="http://http://www.mozilla.gr.jp/newzilla/" title="NewZilla Japan">
  <link rel="bookmark" href="http://www.mozilla.gr.jp/mozilland/recruit.html" title="プロジェクト求人情報">
  <link rel="bookmark" href="http://www.mozilla.gr.jp/docs/" title="もじら組 ドキュメント">
  <link rel="bookmark" href="http://mozillazine.jp/" title="MozillaZine 日本語版">

  <link rel="alternate" type="application/xml" title="もじら組forum RSS" href="http://www.mozilla.gr.jp/forums/news.rdf">
  <link rel="stylesheet" type="text/css" href="[% styledir %]/cbbs.css" title="現代版">
  <link rel="alternate stylesheet" type="text/css" href="[% styledir %]/mozillagumi.css" title="幕末版（もじら組標準）">
  <link rel="alternate stylesheet" type="text/css" href="[% styledir %]/monochrome.css" title="白黒版">
  <link rel="alternate stylesheet" type="text/css" href="[% styledir %]/jlp.css" title="未来版（JLP標準）">
  <link rel="alternate stylesheet" type="text/css" href="[% styledir %]/cjc.css" title="紅鮭版（CJ-C風）">

  <title>もじら組フォーラム [[% htmltitle %]]</title>
</head>
<body text="#003366" link="blue" vlink="purple" bgcolor="#C7D0D9">

<div class="banner">
  <h1>
    <a href="http://www.mozilla.gr.jp/"><img src="common/logo.png" border="0" alt="もじら組纏"></a>
    <a href="./">もじら組フォーラム</a>
  </h1>
</div>

[% INCLUDE toolbar.inc.tpl %]

[% IF kiji_exist == 2 %]
  <h2>指定された記事は削除されたか過去ログへ流れたため、<br>現行ログ内には存在しませんでした。</h2>
[% END %]
[% IF KLOG %]
  <h2>過去ログ表示</h2><br><div class="Caption03l">過去ログ [% KLOG %] を表示</div>
[% END %]

