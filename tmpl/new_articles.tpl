[% PROCESS htmlhead.tpl
   htmltitle = "$new_t 時間以内に投稿されたメッセージ"
%]

<h2>[% new_t %]時間以内に投稿された新着記事</h2>
<div class="Caption03l">新着記事全 [% total %] 件中 
[% IF new_su == 0 %]
    [% total - Pg + 1 %] ～ [% total - Pg2 + 1 %] 
[% ELSE %]
    [% Pg %] ～ [% Pg2 %] 
[% END %]
番目を表示</div>
[% PROCESS navigation %]
<br />
[ 
[% IF new_su == 0 %]
    <a href="[% cgi_f %]?mode=n_w&amp;s=1&amp;page=[% Pg %]&amp;[% pp %]">新着順</a> / 古い順
[% ELSE %]
    新着順 / <a href="[% cgi_f %]?mode=n_w&amp;s=0&amp;page=[% Pg %]&amp;[% pp %]">古い順</a>
[% END %]
 ]
<br>
</div>
<hr>

[% IF new_count > 0 %]
    [% FOREACH article = new_articles %][% article %]<br>[% END %]</div>
    [% PROCESS navigation %]
[% ELSE %]
    新着記事はありません。
[% END %]

</div>

[% PROCESS htmlfoot.tpl %]

[% BLOCK navigation %]
    <div class="Caption01c"><strong>表示ページ</strong> : 
    [% FOR i IN [ 0 .. page_ ] %]
        [% IF i == af %][<strong>[% i %]</strong>]
        [% ELSE %][<a href="[% cgi_f %]?mode=n_w&amp;page=[% i * new_s %]&amp;s=[% new_su %]&amp;[% pp %]">[% i %]</a>]
        [% END %]
    [% END %]
[% END %]