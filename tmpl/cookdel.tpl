<h2>cookie削除</h2>
<div class="ArtMain">
<SCRIPT language="JavaScript">
<!--
function Link(url) {
    if(confirm("本当に削除してもOKですか?\n(削除すると内容は元に戻せません。)")){location.href=url;}
    else{location.href="#";}
}
//-->
</SCRIPT>
[% IF cookie_mode == 'ID' %]
  <h4>ID削除完了</h4>
[% ELSIF cookie_mode == 'ALL' %]
  <h4>cookie削除完了</h4>
[% END %]
[% msg %]
[% IF UID != '' %]
  <a href="#" onClick="Link('[% cgi_f %]?mode=cookdel&amp;mo=ID&amp;[% no %][% pp %]')">IDのcookieのみ削除</a>
[% END %]
<br>
<a href="#" onClick="Link('[% cgi_f %]?mode=cookdel&amp;mo=ALL&amp;[% no %][% pp %]')">この掲示板全般のcookie削除</a><br>
mozillaの場合は削除後mozillaを再起動するまで反映されないかも知れません</div>

