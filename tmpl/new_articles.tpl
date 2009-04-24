[% PROCESS htmlhead.tpl
   htmltitle = "$new_t 時間以内に投稿されたメッセージ"
%]

<h2>[% new_t %]時間以内に投稿された新着記事</h2>
<div class="Caption03l">新着記事全 [% total %] 件中 [% Pg %] 〜 [% Pg2 %] 番目を表示</div>
<div class="Caption01c"><strong>全ページ</strong> / 
[% FOR i IN [ 0 .. page_ ] %]
    [% IF i == af %][<strong>[% i %]</strong>]
    [% ELSE %][<a href="[% cgi_f %]?mode=n_w&amp;page=[% i * new_s %]&amp;[% pp %]">[% i %]</a>]
    [% END %]
[% END %]
<br />
[ 
[% IF new_su == 0 %]
    <a href="[% cgi_f %]?mode=n_w&amp;s=1&amp;[% pp %]">新着順</a> / 古い順
[% ELSE %]
    新着順 / <a href="[% cgi_f %]?mode=n_w&amp;s=0&amp;[% pp %]">古い順</a>
[% END %]
 ]
<br>
</div>
<hr>

[% IF new_count > 0 %]
    [% FOREACH article = new_articles %][% article %]<br><hr>[% END %]</div>
    <div class="Caption01c"><strong>全ページ</strong> / 
    [% FOR i IN [ 0 .. page_ ] %]
        [% IF i == af %][<strong>[% i %]</strong>]
        [% ELSE %][<a href="[% cgi_f %]?mode=n_w&amp;page=[% i * new_s %]&amp;[% pp %]">[% i %]</a>]
        [% END %]
    [% END %]
[% ELSE %]
    新着記事はありません。
[% END %]

</div>

[% PROCESS htmlfoot.tpl %]
