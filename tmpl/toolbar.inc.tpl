<div class="menubar">

<div class="menu">
  [% IF topok == 1 %]
    <a [% IF mode_id == 'newpost' %]class="act"[% END %] href="[% cgi_f %]?mode=new&amp;[% no %][% pp %]">新規投稿</a>
  [% END %]
  <a [% IF mode_id == 'incoming' %]class="act"[% END %] href="[% cgi_f %]?mode=n_w&amp;[% no %][% pp %]">新着記事</a>
  [% IF TrON == 1 %]
    <a [% IF mode_id == 'disp_tree' %]class="act"[% END %] href="[% cgi_f %]?H=T&amp;[% no %][% pp %][% Wf %]">ツリー表示</a>
  [% END %]
  [% IF ThON == 1 %]
    <a [% IF mode_id == 'disp_thread' %]class="act"[% END %] href="[% cgi_f %]?mode=alk&amp;[% no %][% pp %][% Wf %]">スレッド表示</a>
  [% END %]
  [% IF TpON == 1 %]
    <a [% IF mode_id == 'disp_topic' %]class="act"[% END %] href="[% cgi_f %]?H=F&amp;[% no %][% pp %][% Wf %]">トピック表示</a>
  [% END %]
  [% IF M_Rank == 1 %]
    <a [% IF mode_id == 'postrank' %]class="act"[% END %] href="[% cgi_f %]?mode=ran&amp;[% no %][% pp %]">発言ランク</a>
  [% END %]
  <a [% IF mode_id == 'search' %]class="act"[% END %] href="[% srch %]?[% no %][% pp %]">検索</a>
  [% IF klog_s == 1 %]
    <a [% IF mode_id == 'oldlog' %]class="act"[% END %] href="[% srch %]?mode=log&amp;[% no %][% pp %]">過去ログ</a>
  [% END %]
  [% IF in_group('admin') == 1 %]
    <a [% IF mode_id == 'admin' %]class="act"[% END %] href="./adminmenu.cgi">管理</a>
  [% END %]
  [% IF user.uid != 0 %]
    <a " href="login.cgi?logout=1">ログアウト ([% user.name %])</a>
  [% ELSE %]
    <a [% IF mode_id == 'login' %]class="act"[% END %] href="login.cgi">管理者ログイン</a>
  [% END %]
  <a [% IF mode_id == 'manual' %]class="act"[% END %] href="[% cgi_f %]?mode=man&amp;[% no %][% pp %]">ヘルプ</a>
</div>

[% IF in_group('admin') == 1 %]
  <div class="menu">
    <a [% IF mode_adm == 'ip' %]class="act"[% END %] href="editdenyip.cgi">IP</a>
    <a [% IF mode_adm == 'word' %]class="act"[% END %] href="editdenyword.cgi">Word</a>
    <a [% IF mode_adm == 'count' %]class="act"[% END %] href="editcounter.cgi">counter</a>
    <a [% IF mode_adm == 'admin' %]class="act"[% END %] href="managearticle.cgi">admin</a>
  </div>
[% END %]

</div>
