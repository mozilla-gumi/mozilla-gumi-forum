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
[% IF ! KLOG %]
<form action="[% srch %]" method="[% met %]">
<strong>�ߋ����O�Ɉړ����Ă��Ȃ��L���̌���</strong> : 
<input type="hidden" name="andor" value="and">
<input type="hidden" name="logs" value="[% log %]">
[% nf %]
<input type="hidden" name="KLOG" value="[% KLOG %]">
<input type="text" name="word" size="32" value="[% word %]">
<input type="submit" value="����">
�L���� [% NS %] �i�e [% total %]�A�ԐM [% RS %]�j ���猟��
</form>
[% END %]
<p>�ߋ����O�Ɉړ������X���b�h�̌����́A
<a href="srch.cgi">����</a>
���s�����Ƃ��ł��܂��B</p>
</div>

[% IF use_password != 0 %]
  <hr>
  <div class="Forms">
  <form action="[% cgi_f %]" method="[% met %]">[% nf %]
    <input type="hidden" name="KLOG" value="[% KLOG %]">
    <strong>�폜 / �ҏW�t�H�[��</strong><br>
    �L���ԍ� <input type="text" name="del" size="8" value="">
    <select name="mode">
      <option value="nam">�ҏW</option>
      <option value="key">�폜</option>
    </select>
    �p�X���[�h <input type="password" name="delkey" size="8">
    <input type="submit" value=" ���M ">
  </form>
  </div>
[% END %]
