<html><head>
[% INCLUDE 'style.inc.tpl' %]
[% fsi %]
<!--[% ver %]-->
<title>�SBBS�ŐV�X�V�L�� [All BBS New Subject]</title>
<meta http-equiv="Content-type" content="text/html; charset=Shift_JIS"></head>
<body text=[% text %] link=[% link %] vlink=[% vlink %] bgcolor=[% bg %]
[% IF back %] background=[% back %][% END %]
>
<table summary="update" width="100%"><tr>
<th>�SBBS�ŏI�X�V�L��</th></tr></table><br>
<ul>
<li>Child Tree �ɐݒ肳��Ă���BBS�̍ŏI�X�V�L����\�����܂��B</li>
<li>BBS�^�C�g�����N���b�N����Ƃ��̌f���ցA�e�L���^�C�g�����N���b�N����Ƃ��̋L���Q�֔�т܂��B</li>
</ul>
<table summary="list" width="95%" border="1"><tr><th>BBS�^�C�g��</th>
<th>�ŐV�X�V���ꂽ�e�L���^�C�g��</th><th>�L����</th><th>�X�V��</th><th>�X�V����</th></tr>

[% FOREACH res = resources %]
<tr>
  <th><a href="[% res.cgi_f %]?[% res.no %]">[% res.title %]</a></th>
  <td align="center">
    <span class="ArtId">[[% res.namber %]]
    <a href="[% res.cgi_f %]?[% res.MD %]&amp;[% res.no %]">
    <strong>[% res.d_may %]</strong></a></span></td>
  <th>[% res.N %]</th>
  <th>[% res.Name %]</th>
  <td align="center">[% res.date %]</td>
</tr>
[% END %]

</table>


