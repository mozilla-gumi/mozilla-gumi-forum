<hr class="Hidden">
<div class="Menu">
  [% IF topok == 1 %]
    <a class="Menu[% IF curT == 3 %]Act[% END %]" href="[% cgi_f %]?mode=new&amp;[% no %][% pp %]">新規投稿</a>
  [% END %]
  <a class="Menu[% IF curT == 2 %]Act[% END %]" href="[% cgi_f %]?mode=n_w&amp;[% no %][% pp %]">新着記事</a>
  [% IF TrON == 1 %]
    <a class="Menu[% IF curT == 5 %]Act[% END %]" href="[% cgi_f %]?H=T&amp;[% no %][% pp %][% Wf %]">ツリー表示</a>
  [% END %]
  [% IF ThON == 1 %]
    <a class="Menu[% IF curT == 4 %]Act[% END %]" href="[% cgi_f %]?mode=alk&amp;[% no %][% pp %][% Wf %]">スレッド表示</a>
  [% END %]
  [% IF TpON == 1 %]
    <a class="Menu[% IF curT == 7 %]Act[% END %]" href="[% cgi_f %]?H=F&amp;[% no %][% pp %][% Wf %]">トピック表示</a>
  [% END %]
  [% IF M_Rank == 1 %]
    <a class="Menu[% IF curT == 6 %]Act[% END %]" href="[% cgi_f %]?mode=ran&amp;[% no %][% pp %]">発言ランク</a>
  [% END %]
  [% IF i_mode == 1 %]
    <a class="Menu[% IF curT == 1 %]Act[% END %]" href="[% cgi_f %]?mode=f_a&amp;[% no %][% pp %]">アップファイル一覧</a>
  [% END %]
  <a class="Menu" href="[% srch %]?[% no %][% pp %]">検索</a>
  [% IF klog_s == 1 %]
    <a class="Menu" href="[% srch %]?mode=log&amp;[% no %][% pp %]">過去ログ</a>
  [% END %]
  [% IF in_group('admin') == 1 %]
    <a class="Menu" href="./?mode=del">管理用</a>
  [% ELSE %]
    <a class="Menu" href="login.cgi">ログイン</a>
  [% END %]
<a class="Menu[% IF curT == 1 %]Act[% END %]" href="[% cgi_f %]?mode=man&amp;[% no %][% pp %]">ヘルプ</a>
</div>
<hr>

