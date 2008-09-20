[% IF User.group_check('admin') == 1 %]
  <div class="kanri">
    <form action="[% cgi_f %]" method="[% met %]">[% nf %][% pf %]
      [% IF (i_mode != 0) || (mas_c != 0) %]
        モード
        <select name="mode">
          <option value="del">通常管理</option>
          <option value="ent">表示許可</select>
      [% ELSE %]
        <input type="hidden" name="mode" value="del">
      [% END %]
      管理パス
      <input type="password" name="pass" size="6" [% ff %]>
      <input type="submit" value="管理用" [% fm %]>
    </form>
  </div>
[% END %]
[% INCLUDE toolbar.inc.tpl %]
<div id="Credit">
<!--著作権表示 削除不可-->
- <a href="http://www.cj-c.com/"[% TGT %]>Child Tree</a> -<br>
</div>
</body></html>
