<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html lang="ja">
<head>
  <meta http-equiv="Content-type" content="text/html; charset=Shift_JIS">

  <!-- meta names -->
  <meta name="keywords" content="mozilla,Gecko,bugzilla,newzilla,mozillazine,bbs">
  <meta name="classification" content="�R���s���[�^,�C���^�[�l�b�g,�u���E�U">
  <meta name="description" content="mozilla.org�ŊJ������Ă���mozilla Web�u���E�U�Ɋ֘A������{�̏����W�񂵂��T�C�g��BBS�ł�">
  <meta name="date" content="2002-02-22">
  <meta name="author" content="Mozilla-gumi">

  <meta http-equiv="Content-Script-Type" content="text/javascript">
  <script language="JavaScript" type="text/javascript" src="common.js"></script>
  <script language="JavaScript" type="text/javascript" src="bbcode.js"></script>

  <!-- relations -->
  <link rel="top" href="http://www.mozilla.gr.jp" title="������g�g�b�v">
  <link rel="up" href="cbbs.cgi" title="BBS�g�b�v">
  <link rel="search" href="srch.cgi?no=0" title="BBS������">
  <link rel="help" href="cbbs.cgi?mode=man&amp;no=0" title="BBS�w���v">
  <link rel="author" href="http://www.mozilla.gr.jp/info.html" title="�A����ɂ���">

  <!-- bookmarks -->
  <link rel="bookmark" href="http://bugzilla.mozilla.gr.jp/" title="Bugzilla-jp">
  <link rel="bookmark" href="http://http://www.mozilla.gr.jp/newzilla/" title="NewZilla Japan">
  <link rel="bookmark" href="http://www.mozilla.gr.jp/mozilland/recruit.html" title="�v���W�F�N�g���l���">
  <link rel="bookmark" href="http://www.mozilla.gr.jp/docs/" title="������g �h�L�������g">
  <link rel="bookmark" href="http://mozillazine.jp/" title="MozillaZine ���{���">

  <!-- icon -->
  <link rel="icon" type="image/png" href="http://www.mozilla.gr.jp/images/marumo16.png" title="������g�A�C�R��">

  <link rel="alternate" type="application/xml" title="������gforum RSS" href="http://www.mozilla.gr.jp/forums/news.rdf">
  <link rel="stylesheet" type="text/css" href="cbbs.css" title="�����">
  <link rel="alternate stylesheet" type="text/css" href="mozillagumi.css" title="�����Łi������g�W���j">
  <link rel="alternate stylesheet" type="text/css" href="monochrome.css" title="������">
  <link rel="alternate stylesheet" type="text/css" href="jlp.css" title="�����ŁiJLP�W���j">
  <link rel="alternate stylesheet" type="text/css" href="cjc.css" title="�g���ŁiCJ-C���j">

  [% fsi %]
  <title>Mozilla-gumi Forum [[% htmltitle %]]</title>
</head>
<body text="[% text %]" link="[% link %]" vlink="[% vlink %]" bgcolor="[% bg %]"
  [% IF back != '' %] background="[% back %]"[% END %]>

<div class="banner">
  <h1>
    <a href="[% backurl %]"><img src="[% t_img %]" width="[% twid %]"
      height="[% thei %]" border="0" alt="[% talt %]"></a>
    <a href="./">Mozilla-gumi Forum</a>
  </h1>
</div>


[% INCLUDE toolbar.inc.tpl %]

[% IF kiji_exist == 2 %]
  <h2>�w�肳�ꂽ�L���͍폜���ꂽ���ߋ����O�֗��ꂽ���߁A<br>���s���O���ɂ͑��݂��܂���ł����B</h2>
[% END %]
[% IF is_set(KLOG) %]
  <h2>�ߋ����O�\\��</h2><br><div class="Caption03l">�ߋ����O1 ��\\��</div>
[% END %]

