[% plink = BLOCK %]
  <div class="Caption01c">
    [% IF page_ > 0 %] <strong>このスレッドのページ</strong> : 
      [%- FOREACH page_no IN [0 .. page_] %]
        [% IF page_no == cur_page %]
          [<strong>[% page_no %]</strong>]
        [% ELSE %]
          [<a href="[% cgi_f %]?mode=res&amp;namber=[% form_namber %]&amp;page=
            [%- ResHy * page_no %]&amp;[% no %][% pp %]">[% page_no %]</a>]
        [% END %]
      [% END %]
    [% ELSE %]
      <strong>このスレッドの全記事を表示中</strong>
    [% END %]
  </div>
[% END %]

<form action="[% cgi_f %]" method="POST">
<br>
[% IF page %]
  <div class="Caption03l">スレッド内全 [% total %] 返信中 [% page %] ～ [% page_end %] 件目を表示</div>
[% ELSE %]
  <div class="Caption03l">スレッド内全 [% total %] 返信中、親記事および [% page_end %] 件目までを表示</div>
[% END %]
[% plink %]
[% IF Dk %]
  [% Dk %] 件の削除記事を非表示 <br />
[% END %]
<br>
<hr class="Hidden">
[% FOREACH article IN article_html %]
  [% article %]
[% END %]
[% IF use_post_edit != 0 %]
  <div class="Forms">
  <input type="hidden" name="no" value="0">
  <strong>削除 / 編集フォーム</strong><br>
  チェックした記事を
  <select name="mode">
    <option value="nam">編集
    <option value="key">削除
  </select>
  パスワード <input type="password" name="delkey" size="8">
  <input type="submit" value="送信">
  </div>
  <hr />
[% END %]
</form>
[% IF TrON %]
  <div class="Caption01r">[ <a href="[% cgi_f %]?mode=all&amp;namber=
    [%- form_namber %]&amp;space=0&amp;type=0&amp;[% no %][% pp %]">
    [% all_i %] このスレッドをツリーで一括表示</a> ]
  </div>
[% END %]

[% IF bl >= 0 %]
  <div class="Caption01r">[
  <a href="[% cgi_f %]?mode=res&amp;namber=[% form_namber %]&amp;page=[% bl %]&amp;[% no %][% pp %]">
  前の返信[% ResHy %]件</a> ]
[% END %]
[% IF page_end != end_data %]
  [% IF bl >= 0 %] | [% ELSE %]<div class="Caption01r">[% END %]
  [ <a href="[% cgi_f %]?mode=res&amp;namber=[% form_namber %]&amp;page=[% page_end + 1 %]&amp;[% no %][% pp %]">
    次の返信[% ResHy %]件</a> ]
  </div>
[% ELSE %]
  </div>
[% END %]
[% plink %]
<hr>
<a name="F"><h2>このスレッドに書きこむ</h2></a>
[% IF r_max && (total > r_max) %]
  <h3>返信数の限度を超えたので返信できません。(返信数限度: [% r_max %] 現在の返信数: [% total %])</h3>
  → <strong><a href="[% cgi_f %]?mode=new&amp;[% no %][% pp %]">[スレッドの新規作成]</a></strong>
[% ELSE %]
  [% IF En && end_e %][% end_ok %] / 返信不可[% END %]
[% END %]
