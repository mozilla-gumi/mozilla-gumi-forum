[% PROCESS htmlhead.tpl
   htmltitle = "スレッド表示 / $PAGE ページ"
%]

[% IF Top_t %]
    <li>[% new_t %]時間以内に作成されたスレッドは [% new_i %] で表示されます。</li>
    <li>[% new_t %]時間以内に更新されたスレッドは [% up_i_ %] で表示されます。</li>
[% END %]
[% PROCESS comtop.inc.tpl %]
</ul>

[% Henko %]

<hr>

[% IF cou %]
    <div class="Counter">[% counter %]</div>
    <br>
[% END %]

<div class="Caption03l">全 [% thread_total %] スレッド中 [% Pg %] ～ [% Pg2 %] 番目を表示</div>

<div class="Caption01r">親記事の表示順 :
[%- IF Res_T == 1 %]
    <a href="[% cgi_f %]?mode=alk&amp;W=W&amp;[% pp %]">返信最新順</a> /
    投稿順 /
    <a href="[% cgi_f %]?mode=alk&amp;W=R&amp;[% pp %]">記事数順</a>
[% ELSIF Res_T == 2 %]
    <a href="[% cgi_f %]?mode=alk&amp;W=W&amp;[% pp %]">返信最新順</a> /
    <a href="[% cgi_f %]?mode=alk&amp;W=T&amp;[% pp %]">投稿順</a> /
    記事数順
[% ELSE %]
    返信最新順 /
    <a href="[% cgi_f %]?mode=alk&amp;W=T&amp;[% pp %]">投稿順</a> /
    <a href="[% cgi_f %]?mode=alk&amp;W=R&amp;[% pp %]">記事数順</a>
[% END %]</div>

<div class="Caption01c"><strong>全ページ</strong> /
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
            <strong><a name="list">記事リスト</a></strong>
            ( )内の数字は返信数
        </div>
        [% List %]
    </div>
    <br>
[% END %]


