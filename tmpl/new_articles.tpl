[% PROCESS htmlhead.tpl
   htmltitle = "$new_t ���Ԉȓ��ɓ��e���ꂽ���b�Z�[�W"
%]

<h2>[% new_t %]���Ԉȓ��ɓ��e���ꂽ�V���L��</h2>
<div class="Caption03l">�V���L���S [% total %] ���� 
[% IF new_su == 0 %]
    [% total - Pg + 1 %] �` [% total - Pg2 + 1 %] 
[% ELSE %]
    [% Pg %] �` [% Pg2 %] 
[% END %]
�Ԗڂ�\��</div>
[% PROCESS navigation %]
<br />
[ 
[% IF new_su == 0 %]
    <a href="[% cgi_f %]?mode=n_w&amp;s=1&amp;page=[% Pg %]&amp;[% pp %]">�V����</a> / �Â���
[% ELSE %]
    �V���� / <a href="[% cgi_f %]?mode=n_w&amp;s=0&amp;page=[% Pg %]&amp;[% pp %]">�Â���</a>
[% END %]
 ]
<br>
</div>
<hr>

[% IF new_count > 0 %]
    [% FOREACH article = new_articles %][% article %]<br>[% END %]</div>
    [% PROCESS navigation %]
[% ELSE %]
    �V���L���͂���܂���B
[% END %]

</div>

[% PROCESS htmlfoot.tpl %]

[% BLOCK navigation %]
    <div class="Caption01c"><strong>�\���y�[�W</strong> : 
    [% FOR i IN [ 0 .. page_ ] %]
        [% IF i == af %][<strong>[% i %]</strong>]
        [% ELSE %][<a href="[% cgi_f %]?mode=n_w&amp;page=[% i * new_s %]&amp;s=[% new_su %]&amp;[% pp %]">[% i %]</a>]
        [% END %]
    [% END %]
[% END %]