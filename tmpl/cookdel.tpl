<h2>cookie�폜</h2>
<div class="ArtMain">
<SCRIPT language="JavaScript">
<!--
function Link(url) {
    if(confirm("�{���ɍ폜���Ă�OK�ł���?\n(�폜����Ɠ��e�͌��ɖ߂��܂���B)")){location.href=url;}
    else{location.href="#";}
}
//-->
</SCRIPT>
[% IF cookie_mode == 'ID' %]
  <h4>ID�폜����</h4>
[% ELSIF cookie_mode == 'ALL' %]
  <h4>cookie�폜����</h4>
[% END %]
[% msg %]
[% IF UID != '' %]
  <a href="#" onClick="Link('[% cgi_f %]?mode=cookdel&amp;mo=ID&amp;[% no %][% pp %]')">ID��cookie�̂ݍ폜</a>
[% END %]
<br>
<a href="#" onClick="Link('[% cgi_f %]?mode=cookdel&amp;mo=ALL&amp;[% no %][% pp %]')">���̌f���S�ʂ�cookie�폜</a><br>
mozilla�̏ꍇ�͍폜��mozilla���ċN������܂Ŕ��f����Ȃ������m��܂���</div>

