[% IF Bl != '' %]
  <div class="Caption01r">[[% Bl %]前の[% footopt %][% Ble %]]
[% END %]
[% IF Nl != '' %]
  [% IF Bl != '' %]| [% ELSE %]<div class="Caption01r">[% END %]
  [[% Nl %]次の[% footopt %][% Nle %]]</div>
[% ELSE %]
  [% IF Bl != '' %]</div>[% END %]
[% END %]
[% Plink %]
<hr>
<div class="Forms">
<form action="[% srch %]" method="[% met %]">
<strong>検索フォーム</strong><br>
<input type="hidden" name="andor" value="and">
<input type="hidden" name="logs" value="[% log %]">
[% nf %][% pf %]<input type="text" name="word" size="32" value="[% word %]">
<input type="submit" value="検索">
全記事数 [% NS %] （親 [% total %]、返信 [% RS %]） から検索
</form></div>

<hr>
<div class="Forms">
<form action="[% cgi_f %]" method="[% met %]">
[% nf %][% pf %]
<strong>削除 / 編集フォーム</strong><br>
記事番号 <input type="text" name="del" size="8" value="" [% ff %]>
<select name="mode">
  <option value="nam">編集</option>
  <option value="key">削除</option>
</select>
パスワード <input type="password" name="delkey" size="8" [% ff %]>
<input type="submit" value=" 送信 " [% fm %]>
</form>
</div>

