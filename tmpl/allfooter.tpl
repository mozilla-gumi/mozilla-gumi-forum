[% IF Bl != '' %]
  <div class="Caption01r">[[% Bl %]�O��[% footopt %][% Ble %]]
[% END %]
[% IF Nl != '' %]
  [% IF Bl != '' %]| [% ELSE %]<div class="Caption01r">[% END %]
  [[% Nl %]����[% footopt %][% Nle %]]</div>
[% ELSE %]
  [% IF Bl != '' %]</div>[% END %]
[% END %]
[% Plink %]
<hr>
<div class="Forms">
<form action="[% srch %]" method="[% met %]">
<strong>�����t�H�[��</strong><br>
<input type="hidden" name="andor" value="and">
<input type="hidden" name="logs" value="[% log %]">
[% nf %][% pf %]<input type="text" name="word" size="32" value="[% word %]">
<input type="submit" value="����">
�S�L���� [% NS %] �i�e [% total %]�A�ԐM [% RS %]�j ���猟��
</form></div>

<hr>
<div class="Forms">
<form action="[% cgi_f %]" method="[% met %]">
[% nf %][% pf %]
<strong>�폜 / �ҏW�t�H�[��</strong><br>
�L���ԍ� <input type="text" name="del" size="8" value="" [% ff %]>
<select name="mode">
  <option value="nam">�ҏW</option>
  <option value="key">�폜</option>
</select>
�p�X���[�h <input type="password" name="delkey" size="8" [% ff %]>
<input type="submit" value=" ���M " [% fm %]>
</form>
</div>

