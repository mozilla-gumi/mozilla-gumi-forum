[% PROCESS htmlhead.tpl
   htmltitle = "�X���b�h�\�� / $PAGE �y�[�W"
%]

[% IF Top_t %]
    <li>[% new_t %]���Ԉȓ��ɍ쐬���ꂽ�X���b�h�� [% new_i %] �ŕ\������܂��B</li>
    <li>[% new_t %]���Ԉȓ��ɍX�V���ꂽ�X���b�h�� [% up_i_ %] �ŕ\������܂��B</li>
[% END %]
[% PROCESS comtop.inc.tpl %]
</ul>

[% Henko %]

<hr>

[% IF cou %]
    <div class="Counter">[% counter %]</div>
    <br>
[% END %]

<div class="Caption03l">�S [% thread_total %] �X���b�h�� [% Pg %] �` [% Pg2 %] �Ԗڂ�\��</div>

<div class="Caption01r">�e�L���̕\���� :
[%- IF Res_T == 1 %]
    <a href="[% cgi_f %]?mode=alk&amp;W=W&amp;[% pp %]">�ԐM�ŐV��</a> /
    ���e�� /
    <a href="[% cgi_f %]?mode=alk&amp;W=R&amp;[% pp %]">�L������</a>
[% ELSIF Res_T == 2 %]
    <a href="[% cgi_f %]?mode=alk&amp;W=W&amp;[% pp %]">�ԐM�ŐV��</a> /
    <a href="[% cgi_f %]?mode=alk&amp;W=T&amp;[% pp %]">���e��</a> /
    �L������
[% ELSE %]
    �ԐM�ŐV�� /
    <a href="[% cgi_f %]?mode=alk&amp;W=T&amp;[% pp %]">���e��</a> /
    <a href="[% cgi_f %]?mode=alk&amp;W=R&amp;[% pp %]">�L������</a>
[% END %]</div>

<div class="Caption01c"><strong>�S�y�[�W</strong> /
[% FOR i IN [ 0 .. page_ ] %]
    [% IF i == af %][<strong>[% i %]</strong>]
    [% ELSE %][<a href="[% cgi_f %]?mode=alk&amp;page=[% i * alk_su %]&amp;[% pp %][% Wf %]">[% i %]</a>]
    [% END %]
[% END %]
</div>
<hr class="Hidden">
<br>

[% IF Top_t %]
    <div class="ArtList">
        <div class="Caption01List">
            <strong><a name="list">�L�����X�g</a></strong>
            ( )���̐����͕ԐM��
        </div>
        [% List %]
    </div>
    <br>
[% END %]


