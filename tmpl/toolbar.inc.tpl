<hr class="Hidden">
<div class="Menu">
  [% IF topok == 1 %]
    <a class="Menu[% IF curT == 3 %]Act[% END %]" href="[% cgi_f %]?mode=new&amp;[% no %][% pp %]">�V�K���e</a>
  [% END %]
  <a class="Menu[% IF curT == 2 %]Act[% END %]" href="[% cgi_f %]?mode=n_w&amp;[% no %][% pp %]">�V���L��</a>
  [% IF TrON == 1 %]
    <a class="Menu[% IF curT == 5 %]Act[% END %]" href="[% cgi_f %]?H=T&amp;[% no %][% pp %][% Wf %]">�c���[�\��</a>
  [% END %]
  [% IF ThON == 1 %]
    <a class="Menu[% IF curT == 4 %]Act[% END %]" href="[% cgi_f %]?mode=alk&amp;[% no %][% pp %][% Wf %]">�X���b�h�\��</a>
  [% END %]
  [% IF TpON == 1 %]
    <a class="Menu[% IF curT == 7 %]Act[% END %]" href="[% cgi_f %]?H=F&amp;[% no %][% pp %][% Wf %]">�g�s�b�N�\��</a>
  [% END %]
  [% IF M_Rank == 1 %]
    <a class="Menu[% IF curT == 6 %]Act[% END %]" href="[% cgi_f %]?mode=ran&amp;[% no %][% pp %]">���������N</a>
  [% END %]
  [% IF i_mode == 1 %]
    <a class="Menu[% IF curT == 1 %]Act[% END %]" href="[% cgi_f %]?mode=f_a&amp;[% no %][% pp %]">�A�b�v�t�@�C���ꗗ</a>
  [% END %]
  <a class="Menu" href="[% srch %]?[% no %][% pp %]">����</a>
  [% IF klog_s == 1 %]
    <a class="Menu" href="[% srch %]?mode=log&amp;[% no %][% pp %]">�ߋ����O</a>
  [% END %]
  [% IF in_group('admin') == 1 %]
    <a class="Menu" href="./?mode=del">�Ǘ��p</a>
  [% ELSE %]
    <a class="Menu" href="login.cgi">���O�C��</a>
  [% END %]
<a class="Menu[% IF curT == 1 %]Act[% END %]" href="[% cgi_f %]?mode=man&amp;[% no %][% pp %]">�w���v</a>
</div>
<hr>

