<table summary="password">
<tr><th>�p�X���[�h�F��</th></tr>
<tr><th>*�������ނɂ̓p�X���[�h���K�v�ł�!<form action="[% cgi_f %]" method="[% met %]">
<input type="password" size="8" name="P">[% nf %]
<input type="submit" value=" �F�� ">
</form></th></tr></table>
[% IF s_ret == 1 %]
�L���̉{���͂ł��܂�(���[�h�I�����[)
<a href="[% cgi_f %]?P=R&amp;[% no %]">�L�����{������</a>
[% END %]

[% PROCESS htmlfoot.tpl %]
