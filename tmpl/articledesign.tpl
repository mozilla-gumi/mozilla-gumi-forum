[% MD = BLOCK %][% IF htype == "N" -%]
[%- IF TOPH == 0 -%]
  mode=res&amp;namber=[% IF type %][% type %][% ELSE %][% namber %][% END %]
[%- ELSIF TOPH == 1 -%]
  mode=one&amp;namber=[% namber %]&amp;type=[% type %]&amp;space=[% space %]
[%- ELSIF TOPH == 2 -%]
  mode=al2&amp;namber=[% IF type %][% type %][% ELSE %][% namber %][% END %]&amp;space=[% space %]
[%- END %][%- END %]

[% IF htype == "T2" %]<br>[% END %]
[% IF (mode == "alk") && (type) %]
  <div class="ArtChild">
[% ELSIF ((mode == "al2") || (mode == "res")) && (type) %]
  </div><div class="ArtMain">
[% ELSE %]
  <div class="ArtMain">
[% END %]
<div class="ArtHead">
  <a name="[% namber %]">
    <strong>[% IF d_may == "" %][% notitle %][% ELSE %][% d_may %][% END %]</strong>
  </a>
  <br>
  <span class="ArtId">(#[% namber %]) 
    [% IF (htype == "T") || (htype == "T2") %] [% IF resno == 0 %]�e[% ELSE %][% resno %][% END %]�K�w
    [% ELSIF htype == "F" %] ���̃g�s�b�N[% IF resno == 0 %]�̐e[% ELSE %]��[% resno %]�Ԗڂ�[% END %]���e
    [% ELSIF (htype == "TR") || (htype == "TRES") %] [% IF resno == 0 %]�e�L��[% ELSE %]���̃X���b�h��[% resno %]�Ԗڂ̕ԐM[% END %]
    [% END %]
  </span>
</div>
<div class="postinfo">
<span class="name">[% name %] [% r %]</span>�̓��e :[% date %] [% url %]</div>
<div class="ArtComment">
[% IF userenv %](��: [% userenv %])<br>[% END %]
[% comment FILTER auto %]
</div>
<div class="Caption01r">[% end %]<br>
[% IF klog_def == 0 %]
  [% IF o_mail %][���[���]��/[% IF ((Se == 2) || (Se == 1)) %]ON[% ELSE %]OFF[% END %]]
  / [% INCLUDE reply_block %]
  [% IF (mode == "al2") || (mode == "res") %]
    �`�F�b�N-<input type="radio" value="[% nam %]" name="del">
  [% ELSIF use_post_edit != 0 %]
    <form action="[% cgi_f %]" method="[% met %]">
      <input type="hidden" name="del" value="[% namber %]">[% nf %]
      <input type="hidden" name="KLOG" value="[% KLOG %]">
      �p�X���[�h <input type="password" name="delkey" size="8">
      <select name="mode">
        <option value="nam">�ҏW
        <option value="key">�폜
      </select>
      <input type="submit" value="���M">
    </form>
  [% END %]
[% END %]
</div>
[% IF (type_def == 1) || (mode == "one") %]</div>[% END %]
[% IF mode == "n_w" %]</div>[% END %]


[% BLOCK reply_block %]
  [% IF (htype == "T") && (Res_i) %]
    <strong><a href="[% cgi_f %]?mo=1&amp;mode=one&amp;namber=[% namber %]&amp;type=[% type %]&amp;space=[% space %]&amp;[% pp %]#F">�L�����p</a></strong>
  [% ELSIF htype == "T2" %]
    [% IF type > 0 %][<a href="#[% ty %]">�e[% type %]</a>][% END %]
    <strong><a href="[% cgi_f %]?mode=one&amp;namber=[% nam %]&amp;type=[% ty %]&amp;space=[% sp %]&amp;[% pp %]">�ԐM</a></strong>
    [% IF Res_i %]
      / <strong><a href="[% cgi_f %]?mo=1&amp;mode=one&amp;namber=[% nam %]&amp;type=[% ty %]&amp;space=[% sp %]&amp;[% pp %]">���p�ԐM</a></strong>
    [% END %]
  [% ELSIF htype == "F" %]
    <a href="[% cgi_f %]?mode=al2&amp;mo=[% nam %]&amp;namber=[% namber %]&amp;space=[% sp %]&amp;rev=[% rev %]&amp;page=[% fp %]&amp;[% pp %]#F"><strong>���p�ԐM</strong></a>
    [% IF Res_i %]
      / <a href="[% cgi_f %]?mode=al2&amp;mo=[% nam %]&amp;namber=[% namber %]&amp;space=[% space %]&amp;rev=[% rev %]&amp;page=[% fp %]&amp;In=1&amp;[% pp %]#F"><strong>�ԐM</strong></a>
    [% END %]
  [% ELSIF htype == "N" %]
    <strong><a href="[% cgi_f %]?[% MD %]&amp;[% pp %]#F">�ԐM</a></strong>
    [% IF Res_i %]
      / <strong><a href="[% cgi_f %]?[% MD %]&amp;mo=[% namber %]&amp;[% pp %]#F">���p�ԐM</a></strong>
    [% END %]
  [% ELSIF htype == "TR" %]
    <a href="[% cgi_f %]?mode=res&amp;namber=[% nam %]&amp;type=[% type %]&amp;space=[% space %]&amp;mo=[% namber %]&amp;page=[% PNO %]&amp;[% pp %]#F"><strong>���p�ԐM</strong></a>
    [% IF Res_i %]
      / <a href="[% cgi_f %]?mode=res&amp;namber=[% nam %]&amp;type=[% type %]&amp;space=[% space %]&amp;mo=[% namber %]&amp;page=[% PNO %]&amp;In=1&amp;[% pp %]#F"><strong>�ԐM</strong></a>
    [% END %]
  [% ELSIF htype == "TRES" %]
    <a href="[% cgi_f %]?mode=res&amp;mo=[% nam %]&amp;namber=[% namber %]&amp;space=[% sp %]&amp;page=[% page %]&amp;[% pp %]#F"><strong>���p�ԐM</strong></a>
    [% IF Res_i %]
      / <a href="[% cgi_f %]?mode=res&amp;mo=[% nam %]&amp;namber=[% namber %]&amp;space=[% sp %]&amp;page=[% page %]&amp;In=1&amp;[% pp %]#F"><strong>�ԐM</strong></a>
    [% END %]
  [% END %]
[% END %]
