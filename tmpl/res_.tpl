[% plink = BLOCK %]
  <div class="Caption01c">
    [% IF page_ > 0 %] <strong>���̃X���b�h�̃y�[�W</strong> : 
      [%- FOREACH page_no IN [0 .. page_] %]
        [% IF page_no == cur_page %]
          [<strong>[% page_no %]</strong>]
        [% ELSE %]
          [<a href="[% cgi_f %]?mode=res&amp;namber=[% form_namber %]&amp;page=
            [%- ResHy * page_no %]&amp;[% no %][% pp %]">[% page_no %]</a>]
        [% END %]
      [% END %]
    [% ELSE %]
      <strong>���̃X���b�h�̑S�L����\����</strong>
    [% END %]
  </div>
[% END %]

<form action="[% cgi_f %]" method="POST">
<br>
[% IF page %]
  <div class="Caption03l">�X���b�h���S [% total %] �ԐM�� [% page %] �` [% page_end %] ���ڂ�\��</div>
[% ELSE %]
  <div class="Caption03l">�X���b�h���S [% total %] �ԐM���A�e�L������� [% page_end %] ���ڂ܂ł�\��</div>
[% END %]
[% plink %]
[% IF Dk %]
  [% Dk %] ���̍폜�L�����\�� <br />
[% END %]
<br>
<hr class="Hidden">
[% FOREACH article IN article_html %]
  [% article %]
[% END %]
[% IF use_post_edit != 0 %]
  <div class="Forms">
  <input type="hidden" name="no" value="0">
  <strong>�폜 / �ҏW�t�H�[��</strong><br>
  �`�F�b�N�����L����
  <select name="mode">
    <option value="nam">�ҏW
    <option value="key">�폜
  </select>
  �p�X���[�h <input type="password" name="delkey" size="8">
  <input type="submit" value="���M">
  </div>
  <hr />
[% END %]
</form>
[% IF TrON %]
  <div class="Caption01r">[ <a href="[% cgi_f %]?mode=all&amp;namber=
    [%- form_namber %]&amp;space=0&amp;type=0&amp;[% no %][% pp %]">
    [% all_i %] ���̃X���b�h���c���[�ňꊇ�\��</a> ]
  </div>
[% END %]

[% IF bl >= 0 %]
  <div class="Caption01r">[
  <a href="[% cgi_f %]?mode=res&amp;namber=[% form_namber %]&amp;page=[% bl %]&amp;[% no %][% pp %]">
  �O�̕ԐM[% ResHy %]��</a> ]
[% END %]
[% IF page_end != end_data %]
  [% IF bl >= 0 %] | [% ELSE %]<div class="Caption01r">[% END %]
  [ <a href="[% cgi_f %]?mode=res&amp;namber=[% form_namber %]&amp;page=[% page_end + 1 %]&amp;[% no %][% pp %]">
    ���̕ԐM[% ResHy %]��</a> ]
  </div>
[% ELSE %]
  </div>
[% END %]
[% plink %]
<hr>
<a name="F"><h2>���̃X���b�h�ɏ�������</h2></a>
[% IF r_max && (total > r_max) %]
  <h3>�ԐM���̌��x�𒴂����̂ŕԐM�ł��܂���B(�ԐM�����x: [% r_max %] ���݂̕ԐM��: [% total %])</h3>
  �� <strong><a href="[% cgi_f %]?mode=new&amp;[% no %][% pp %]">[�X���b�h�̐V�K�쐬]</a></strong>
[% ELSE %]
  [% IF En && end_e %][% end_ok %] / �ԐM�s��[% END %]
[% END %]
