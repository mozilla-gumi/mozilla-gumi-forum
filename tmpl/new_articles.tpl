[% PROCESS htmlhead.tpl
   htmltitle = "$new_t ���Ԉȓ��ɓ��e���ꂽ���b�Z�[�W"
%]

<h2>[% new_t %]���Ԉȓ��ɓ��e���ꂽ�V���L��</h2>
<div class="Caption03l">�V���L���S [% total %] ���� [% Pg %] �` [% Pg2 %] �Ԗڂ�\��</div>
<div class="Caption01c"><strong>�S�y�[�W</strong> / 
[% FOR i IN [ 0 .. page_ ] %]
    [% IF i == af %][<strong>[% i %]</strong>]
    [% ELSE %][<a href="[% cgi_f %]?mode=n_w&amp;page=[% i * new_s %]&amp;[% pp %]">[% i %]</a>]
    [% END %]
[% END %]
<br />
[ 
[% IF new_su %]
    �V���� / <a href="[% cgi_f %]?mode=n_w&amp;s=0&amp;[% pp %]">�Â���</a>
[% ELSE %]
    <a href="[% cgi_f %]?mode=n_w&amp;s=1&amp;[% pp %]">�V����</a> / �Â���
[% END %]
 ]
<br>
</div>
<hr>

[% IF new_count > 0 %]
    [% FOREACH article = new_articles %][% article %]<br><hr>[% END %]</div>
    <div class="Caption01c"><strong>�S�y�[�W</strong> / 
    [% FOR i IN [ 0 .. page_ ] %]
        [% IF i == af %][<strong>[% i %]</strong>]
        [% ELSE %][<a href="[% cgi_f %]?mode=n_w&amp;page=[% i * new_s %]&amp;[% pp %]">[% i %]</a>]
        [% END %]
    [% END %]
[% ELSE %]
    �V���L���͂���܂���B
[% END %]

</div>

[% PROCESS htmlfoot.tpl %]