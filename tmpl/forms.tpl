[% IF FORM_PV == "" %]
  <form action="[% cgi_f %]" method="[% met %]"
    [% IF multipart == 1 %]enctype="multipart/form-data"[% END %]
    name="post">
[% END %]
<ul>
  <li>���͓��e�Ƀ^�O�͗��p[% IF tag %]�\�ł��B[% ELSE %]�ł��܂���B[% END %]</li>
  [% PROCESS atcom.inc.tpl %]
</ul>
<input type="hidden" name="N" value="[% N_NUM %]">
<input type="hidden" name="mode" value="wri">
<input type="hidden" name="type" value="[% nams %]">
<input type="hidden" name="kiji" value="[% namber %]">
<input type="hidden" name="space" value="[% sp %]">
[% nf %][% pf %][% Hi %]

[% IF he_tp %]
  <h3>�g�s�b�N���쐬�������̃p�X���[�h�ł̂ݕԐM���ł��܂��B
    (�g�s�b�N�̍쐬�ɂ̓p�X���[�h���K�{�ł�)</h3>
[% END %]

<table class="Submittion" summary="form" border="0">
<tr>
  <td><strong>�����O</strong></td>
  <td>
    <input type="text" name="name" value="[% c_name %]" size="25"
      [% IF NMAX %]maxlength="[% NMAX %]"[% END %]>
    [% IF UID %]
      [ID:[% pUID %]]
      <!--
        ��<a href="[% cgi_f %]?mode=cookdel" [% TGT %]>����ID��j��</a>
      -->
    [% END %]
  </td>
</tr>
<tr>
  <td rowspan="2"><strong>E ���[��</strong></td>
  <td>
    <input type="text" name="email" value="[% c_email %]" size="40" maxlength="100" disabled="disabled">
  </td>
</tr>
  [% IF o_mail %][% PROCESS mbox %][% END %]
  [% uasel %]
<tr>
  <td><strong>�^�C�g��</strong></td>
  <td>
    <input type="text" name="d_may[% actime %]" size="40" value="[% ti %]" maxlength="100"
      [% IF TMAX %]maxlength="[% TMAX %]"[% END %]>
  </td>
</tr>
<tr>
  <td><strong>URL</strong></td>
  <td>
    <input type="text" name="url" value="http://[% c_url %]" size="70" maxlength="100">
  </td>
</tr>
<tr>
  <td colspan="2">
    <strong>�R�����g</strong>
    <input type="radio" name="pre" value="0" checked="checked">�������s
    <input type="radio" name="pre" value="1">�蓮���s�i�����t�H���g�j
    <br>
    <textarea id="comment" name="comment" rows="12" cols="75"
      [% IF BBFACE %]
        onselect="storeCaret(this);"
        onclick="storeCaret(this);"
        onkeyup="storeCaret(this);"
      [% END %]
    >[% IF com_nodisp %]�R�����g�\��: ������[% ELSE %][% com %][% END %]</textarea>
  </td>
</tr>
<!-- Auto-linkify -->
<tr>
  <td>���������N</td>
  <td>
    <span onclick="add_linkify('mozillazine-jp <id>');">MozillaZine-jp</span>
    /
    <span onclick="add_linkify('bug-jp <id>');">Bugzilla-jp</span>
    /
    <span onclick="add_linkify('bug-org <id>');">bmo (bugzilla.mozilla.org)</span>
    (�N���b�N�ő}��)
  </td>
</tr>
  [% IF multipart == 1 %][% PROCESS multipart_disp %][% END %]
  [% IF BBFACE %][% BBFACE %][% END %]
  [% IF hr %][% PROCESS hr_sel %][% END %]
  [% IF use_sel == 1 %][% PROCESS sel_sel %][% END %]
  [% IF use_txt == 1 %][% PROCESS txt_sel %][% END %]
  [% IF art_sort == 1 %][% PROCESS art_sort_sel %]
    [% ELSE %]<input type="hidden" name="AgSg" value="1">[% END %]
  [% IF use_password == 0 %]
    <input type="hidden" name="delkey" value="">
  [% ELSE %]
    <tr>
      <td><strong>�p�X���[�h</strong></td>
      <td>
        <input type="password" name="delkey" value="[% c_key %]" size="8">
          (���p8�����ȓ�[% KEY %])</td>
      </td>
    </tr>
  [% END %]
<tr>
  <td>�v���r���[</td>
  <td><input type="checkbox" name="PV" value="1" onclick="pvcheck();">
    ���̃`�F�b�N�{�b�N�X���`�F�b�N����ƁA���e�O�Ƀv���r���[���ł��܂�</td>
</tr>
  [% IF end_ok %]
    <tr>
      <td>[% end_ok %]</td>
      <td>
        [% IF end_c %][% end_ok %] �ɂȂ����炻�̎|�������Ă��������B[% END %]
        <input type="checkbox" name="end" value="1" [% PVC %]>[% end_m %]
      </td>
    </tr>
  [% END %]
  [% IF optH %]<input type="hidden" name="H" value="[% optH %]">[% END %]
  [% PROCESS show_captcha %]
<tr>
  <td colspan="2" align="right">
    <input type="submit" value=" �� �M ">
    <input type="reset" value="���Z�b�g">
  </td>
</tr>
</table>
</form>

<hr width="95%">


[% BLOCK hr_sel %]
  <tr>
    <td>�g���F</td>
    <td>
      [% FOREACH hr_c IN hr %]
        <input type="radio" name="hr" value="[% hr_c %]
          [% IF hr_c == hr_def %]checked="checked"[% END %]>
          <font color=[% hr_c %]">��</font>
      [% END %]
    </td>
  </tr>
[% END %]

[% BLOCK sel_sel %]
  <tr>
    <td>[% SEL_T %]</td>
    <td>
      <select name="sel">
      [% FOREACH sel_c IN sel %]
        <option value="[% sel_c %]" [% IF sel_c == sel_def %]selected="selected"[% END %]>
          [%- sel_c %]</option>
      [% END %]
      </select>
    </td>
  </tr>
[% END %]

[% BLOCK txt_sel %]
  <tr>
    <td>[% TXT_T %]</td>
    <td><input type="text" name="text" value="[% c_txt %] maxlength="[% TXT_Mx %]"
          size="[% TXT_Mx %]></td>
  </tr>
[% END %]

[% BLOCK art_sort_sel %]
  <tr>
    <td>�L���\�[�g</td>
    <td>
      <select name="AgSg">
        <option value="1">�グ��(age)</option>
        <option value="0">������(sage)</option>
      </select>
    </td>
  </tr>
[% END %]

[% BLOCK mbox %]
<tr>
  <td>
    * �֘A����ԐM�L�������[���Ŏ�M���܂���?
    <select name="send" disabled="disabled">
      <option value="0">������
      <option value="1" [% PVE %]>�͂�
   </select>
    * �A�h���X�̕\��
    <select name="pub" disabled="disabled">
      <option value="0">��\��
      <option value="1" [% IF c_pub %]selected="selected"[% END %]>�\��
    </select>
  </td>
</tr>
[% END %]


[% BLOCK show_captcha %]
<tr>
  <td>captcha</td>
  <td>
    <img src="./auca.cgi?[% md5sum %]" alt="input string in image" />
    <input type="text" name="auca" />
    <br />
    ��̉摜�F�؂̉摜�ɕ\������Ă��镶�� (2-8�̐�����������z�������p������) 
    ����͂��Ă��������B<br />
    �ǂݍ��݌�A��x��������60���Ԃ����L���ł͂���܂���B<br />
    <input type="hidden" name="aucamd5" value="[% md5sum %]" />
  </td>
</tr>
[% END %]

[% BLOCK multipart_disp %]
<tr>
  <td>File</td>
  <td>
    <input type="file" name="ups" size="60">
    <br>
    �A�b�v�\�g���q &gt;
    <!--
      �����I�Ɉꗗ���o����悤�ɂ��� - �z��̈���
    -->
    <br>
    1) �����̊g���q�͉摜�Ƃ��ĔF������܂��B<br>
    2) �摜�͏�����Ԃŏk���T�C�Y[% H2 %]�~[% W2 %]�s�N�Z���ȉ��ŕ\\������܂��B<br>
    3) �����t�@�C��������A�܂��̓t�@�C�������s�K�؂ȏꍇ�A<br>
    �@�@�t�@�C�����������ύX����܂��B<br>
    4) �A�b�v�\\�t�@�C���T�C�Y��1��<strong>[% max_fs %]KB</strong>(1KB=1024Bytes)�܂łł��B<br>
    5) �t�@�C���A�b�v���̓v���r���[�͗��p�ł��܂���B<br>
    [% IF SIZE %]
      6) �X���b�h���̍��v�t�@�C���T�C�Y:[[% SIZE %]/[% max_or %]KB] 
        <strong>�c��:[[% Rest %]KB]</strong>
    [% END %]
  </td>
</tr>
[% END %]
