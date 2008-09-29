<div class="menubar">

<div class="Menu">
  [% IF topok == 1 %]
    <a class="Menu[% IF mode_id == 'newpost' %]Act[% END %]" href="[% cgi_f %]?mode=new&amp;[% no %][% pp %]">新規投稿</a>
  [% END %]
  <a class="Menu[% IF mode_id == 'incoming' %]Act[% END %]" href="[% cgi_f %]?mode=n_w&amp;[% no %][% pp %]">新着記事</a>
  [% IF TrON == 1 %]
    <a class="Menu[% IF mode_id == 'disp_tree' %]Act[% END %]" href="[% cgi_f %]?H=T&amp;[% no %][% pp %][% Wf %]">ツリー表示</a>
  [% END %]
  [% IF ThON == 1 %]
    <a class="Menu[% IF mode_id == 'disp_thread' %]Act[% END %]" href="[% cgi_f %]?mode=alk&amp;[% no %][% pp %][% Wf %]">スレッド表示</a>
  [% END %]
  [% IF TpON == 1 %]
    <a class="Menu[% IF mode_id == 'disp_topic' %]Act[% END %]" href="[% cgi_f %]?H=F&amp;[% no %][% pp %][% Wf %]">トピック表示</a>
  [% END %]
  [% IF M_Rank == 1 %]
    <a class="Menu[% IF mode_id == 'postrank' %]Act[% END %]" href="[% cgi_f %]?mode=ran&amp;[% no %][% pp %]">発言ランク</a>
  [% END %]
  [% IF i_mode == 1 %]
    <a class="Menu[% IF mode_id == 1 %]Act[% END %]" href="[% cgi_f %]?mode=f_a&amp;[% no %][% pp %]">アップファイル一覧</a>
  [% END %]
  <a class="Menu[% IF mode_id == 'search' %]Act[% END %]" href="[% srch %]?[% no %][% pp %]">検索</a>
  [% IF klog_s == 1 %]
    <a class="Menu[% IF mode_id == 'oldlog' %]Act[% END %]" href="[% srch %]?mode=log&amp;[% no %][% pp %]">過去ログ</a>
  [% END %]
  [% IF in_group('admin') == 1 %]
    <a class="Menu[% IF mode_id == 'admin' %]Act[% END %]" href="./adminmenu.cgi">管理</a>
  [% END %]
  [% IF user.uid != 0 %]
    <a class="Menu" href="login.cgi?logout=1">ログアウト ([% user.name %])</a>
  [% ELSE %]
    <a class="Menu[% IF mode_id == 'login' %]Act[% END %]" href="login.cgi">ログイン</a>
  [% END %]
  <a class="Menu[% IF mode_id == 'manual' %]Act[% END %]" href="[% cgi_f %]?mode=man&amp;[% no %][% pp %]">ヘルプ</a>
</div>

[% IF in_group('admin') == 1 %]
  <div class="Menu">
    <a class="Menu[% IF mode_adm == 'ip' %]Act[% END %]" href="editdenyip.cgi">IP</a>
    <a class="Menu[% IF mode_adm == 'word' %]Act[% END %]" href="editdenyword.cgi">Word</a>
    <a class="Menu[% IF mode_adm == 'count' %]Act[% END %]" href="editcounter.cgi">counter</a>
    <a class="Menu[% IF mode_adm == 'admin' %]Act[% END %]" href="managearticle.cgi">admin</a>
  </div>
[% END %]

</div>
