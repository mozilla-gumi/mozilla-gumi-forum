<table summary="icon">
  <tr>
    <th>アイコン画像一覧</th>
  </tr>
</table>

<br />

<a href="javascript:close()">|X| ウィンドウを閉じる</a>

<br />

[% IF page_cnt > 0 %]
  ページ移動 / 
  [%- FOREACH page IN [ 0 .. $page_cnt ] %]
    [%- IF page != 0 %]| [% END %]
    [%- IF page == page_cur %]
      <strong>[% page %]</strong>
    [% ELSE %]
      <a href="[% cgi_f %]?mode=img&amp;page=[% page %]&amp;[% no %][% pp %]">[% page %]</a>
    [% END %]
  [% END %]
[% END %]

<table summary="iconlist">
  <tr><td>名前</td><td>アイコン</td></tr>
[% FOREACH page IN [ $icon_start .. $icon_end ] %]
  <tr>
  [%- IF icon_1.$page == 'randam' %]
    <td>ランダム</td><td></td>
  [% ELSIF icon_1.$page == 'master' %]
    <td>管理者用</td>
    <td>
      [% FOREACH master IN icon_master %]
        <img src="[% icon_dir %]/[% master %]" />
      [% END %]
    </td>
  [% ELSIF icon_1.$page == '' %]
    <td>なし</td><td></td>
  [% ELSE %]
    <td>[% icon_2.$page %]</td><td><img src="[% icon_dir %]/[% icon_1.$page %]"></td>
  [% END %]
  </tr>
[% END %]
</table>
