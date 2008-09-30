<table summary="topic">
  <tr><th>No[% namber %]の記事</th></tr>
</table>

<br />

[% IF range_err == 'wide' %]
  幅が大きすぎるため [% start_no %] - [% end_no %] に変更しました。
[% ELSIF range_err == 'start_undef' %]
  開始値が未指定のため [% start_no %] - [% end_no %] に変更しました。
[% ELSIF range_err == 'end_undef' %]
  終了値が未指定のため [% start_no %] - [% end_no %] に変更しました。
[% ELSIF range_err == 'large_count' %]
  No 指定が多いために 50 件以降は非表示です。
[% END %]

[% FOREACH out IN out_sort %]
  [% out %]
[% END %]
[% IF N.size > 0 %]
  <hr />
  <ul>
  [% FOREACH n_no IN N %]
    <li>No [% n_no %] の記事は現在のログ内にありません！</li>
    [% IF klog_s %]
      → <a href="[% srch %]?[% no %]&amp;word=
      [%- n_no %]&amp;andor=and&amp;logs=all&amp;PAGE=
      [%- klog_h.0 %]&amp;ALL=1">全過去ログから No [% n_no %] の記事を探す</a>
    [% END %]
  [% END %]
  </ul>
[% END %]

<hr />

[% PROCESS htmlfoot.tpl %]
