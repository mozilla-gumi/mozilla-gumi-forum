<table summary="password">
<tr><th>パスワード認証</th></tr>
<tr><th>*書きこむにはパスワードが必要です!<form action="[% cgi_f %]" method="[% met %]">
<input type="password" size="8" name="P">[% nf %]
<input type="submit" value=" 認証 ">
</form></th></tr></table>
[% IF s_ret == 1 %]
記事の閲覧はできます(リードオンリー)
<a href="[% cgi_f %]?P=R&amp;[% no %]">記事を閲覧する</a>
[% END %]

[% PROCESS htmlfoot.tpl %]
