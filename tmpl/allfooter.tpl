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
<strong>過去ログに移動していない記事の検索</strong> : 
<input type="hidden" name="andor" value="and">
<input type="hidden" name="logs" value="[% log %]">
[% nf %][% pf %]
<input type="text" name="word" size="32" value="[% word %]">
<input type="submit" value="検索">
記事数 [% NS %] （親 [% total %]、返信 [% RS %]） から検索
<p>過去ログに移動したスレッドの検索は、
<a href="http://forum.test.mozilla.gr.jp/srch.cgi">検索</a>
より行うことができます。</p>
</form></div>

[% IF use_password == 0 %]
  <hr>
  <div class="Forms">
  <form action="[% cgi_f %]" method="[% met %]">[% nf %][% pf %]
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
[% END %]
