[% IF User.group_check('admin') == 1 %]
  <div class="kanri">
    <form action="[% cgi_f %]" method="[% met %]">[% nf %][% pf %]
      [% IF (i_mode != 0) || (mas_c != 0) %]
        ���[�h
        <select name="mode">
          <option value="del">�ʏ�Ǘ�</option>
          <option value="ent">�\������</select>
      [% ELSE %]
        <input type="hidden" name="mode" value="del">
      [% END %]
      �Ǘ��p�X
      <input type="password" name="pass" size="6" [% ff %]>
      <input type="submit" value="�Ǘ��p" [% fm %]>
    </form>
  </div>
[% END %]
[% INCLUDE toolbar.inc.tpl %]
<div id="Credit">
<!--���쌠�\�� �폜�s��-->
- <a href="http://www.cj-c.com/"[% TGT %]>Child Tree</a> -<br>
</div>
</body></html>
