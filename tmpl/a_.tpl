<html><head>
[% INCLUDE 'style.inc.tpl' %]
[% fsi %]
<!--[% ver %]-->
<title>全BBS最新更新記事 [All BBS New Subject]</title>
<meta http-equiv="Content-type" content="text/html; charset=Shift_JIS"></head>
<body text=[% text %] link=[% link %] vlink=[% vlink %] bgcolor=[% bg %]
[% IF back %] background=[% back %][% END %]
>
<table summary="update" width="100%"><tr>
<th>全BBS最終更新記事</th></tr></table><br>
<ul>
<li>Child Tree に設定されているBBSの最終更新記事を表示します。</li>
<li>BBSタイトルをクリックするとその掲示板へ、親記事タイトルをクリックするとその記事群へ飛びます。</li>
</ul>
<table summary="list" width="95%" border="1"><tr><th>BBSタイトル</th>
<th>最新更新された親記事タイトル</th><th>記事数</th><th>更新者</th><th>更新時間</th></tr>

[% FOREACH res = resources %]
<tr>
  <th><a href="[% res.cgi_f %]?[% res.no %]">[% res.title %]</a></th>
  <td align="center">
    <span class="ArtId">[[% res.namber %]]
    <a href="[% res.cgi_f %]?[% res.MD %]&amp;[% res.no %]">
    <strong>[% res.d_may %]</strong></a></span></td>
  <th>[% res.N %]</th>
  <th>[% res.Name %]</th>
  <td align="center">[% res.date %]</td>
</tr>
[% END %]

</table>


