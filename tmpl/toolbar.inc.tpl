<div class="menubar">

<div class="Menu">
  [% IF topok == 1 %]
    <a class="Menu[% IF mode_id == 'newpost' %]Act[% END %]" href="[% cgi_f %]?mode=new&amp;[% no %][% pp %]">�V�K���e</a>
  [% END %]
  <a class="Menu[% IF mode_id == 'incoming' %]Act[% END %]" href="[% cgi_f %]?mode=n_w&amp;[% no %][% pp %]">�V���L��</a>
  [% IF TrON == 1 %]
    <a class="Menu[% IF mode_id == 'disp_tree' %]Act[% END %]" href="[% cgi_f %]?H=T&amp;[% no %][% pp %][% Wf %]">�c���[�\��</a>
  [% END %]
  [% IF ThON == 1 %]
    <a class="Menu[% IF mode_id == 'disp_thread' %]Act[% END %]" href="[% cgi_f %]?mode=alk&amp;[% no %][% pp %][% Wf %]">�X���b�h�\��</a>
  [% END %]
  [% IF TpON == 1 %]
    <a class="Menu[% IF mode_id == 'disp_topic' %]Act[% END %]" href="[% cgi_f %]?H=F&amp;[% no %][% pp %][% Wf %]">�g�s�b�N�\��</a>
  [% END %]
  [% IF M_Rank == 1 %]
    <a class="Menu[% IF mode_id == 'postrank' %]Act[% END %]" href="[% cgi_f %]?mode=ran&amp;[% no %][% pp %]">���������N</a>
  [% END %]
  [% IF i_mode == 1 %]
    <a class="Menu[% IF mode_id == 1 %]Act[% END %]" href="[% cgi_f %]?mode=f_a&amp;[% no %][% pp %]">�A�b�v�t�@�C���ꗗ</a>
  [% END %]
  <a class="Menu[% IF mode_id == 'search' %]Act[% END %]" href="[% srch %]?[% no %][% pp %]">����</a>
  [% IF klog_s == 1 %]
    <a class="Menu[% IF mode_id == 'oldlog' %]Act[% END %]" href="[% srch %]?mode=log&amp;[% no %][% pp %]">�ߋ����O</a>
  [% END %]
  [% IF in_group('admin') == 1 %]
    <a class="Menu[% IF mode_id == 'admin' %]Act[% END %]" href="./adminmenu.cgi">�Ǘ�</a>
  [% END %]
  [% IF user.uid != 0 %]
    <a class="Menu" href="login.cgi?logout=1">���O�A�E�g ([% user.name %])</a>
  [% ELSE %]
    <a class="Menu[% IF mode_id == 'login' %]Act[% END %]" href="login.cgi">���O�C��</a>
  [% END %]
  <a class="Menu[% IF mode_id == 'manual' %]Act[% END %]" href="[% cgi_f %]?mode=man&amp;[% no %][% pp %]">�w���v</a>
</div>

[% IF in_group('admin') == 1 %]
  <div class="Menu">
    <a class="Menu[% IF mode_adm == 'ip' %]Act[% END %]" href="editdenyip.cgi">IP</a>
    <a class="Menu[% IF mode_adm == 'word' %]Act[% END %]" href="editdenyword.cgi">Word</a>
    <a class="Menu[% IF mode_adm == 'count' %]Act[% END %]" href="editcounter.cgi">counter</a>
    <a class="Menu[% IF mode_adm == 'admin' %]Act[% END %]" href="managearticle.cgi">admin</a>
  </div>
[% END %]

</div>
