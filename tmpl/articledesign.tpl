[% commode %]
<div class="ArtHead">
<a name="[% namber %]"><strong>[% d_may %]</strong></a><br>
<span class="ArtId">(#[% namber %]) [% resno %]</span>
</div>
<div class="postinfo">
<span class="name">[% name %] [% r %]</span>�̓��e :[% date %] [% url %]</div>
<div class="ArtComment">
[% IF userenv %](��: [% userenv %])<br>[% END %]
[% comment FILTER auto %]
</div>
<div class="Caption01r">[% end %]<br>
[% Pr %]
[% IF klog_def == 0 %]
  [% smsg %] / [% in %] 
  [% IF (mode == "al2") || (mode == "res") %]
    �`�F�b�N-<input type="radio" value="[% nam %]" name="del">
  [% ELSE %]
    [% IF use_post_edit != 0 %]
      <form action="[% cgi_f %]" method="[% met %]">
        <input type="hidden" name="del" value="[% namber %]">[% nf %][% pf %]
        �p�X���[�h <input type="password" name="delkey" size="8">
        <select name="mode">
          <option value="nam">�ҏW
          <option value="key">�폜
        </select>
        <input type="submit" value="���M">
      </form>
    [% END %]
  [% END %]
[% END %]
</div>
[% IF (type_def == 1) || (mode == "one") %]</div>[% END %]
[% IF mode == "n_w" %]</div>[% END %]
