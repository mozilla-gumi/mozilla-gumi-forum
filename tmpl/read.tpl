<table summary="topic">
  <tr><th>No[% namber %]�̋L��</th></tr>
</table>

<br />

[% IF range_err == 'wide' %]
  �����傫�����邽�� [% start_no %] - [% end_no %] �ɕύX���܂����B
[% ELSIF range_err == 'start_undef' %]
  �J�n�l�����w��̂��� [% start_no %] - [% end_no %] �ɕύX���܂����B
[% ELSIF range_err == 'end_undef' %]
  �I���l�����w��̂��� [% start_no %] - [% end_no %] �ɕύX���܂����B
[% ELSIF range_err == 'large_count' %]
  No �w�肪�������߂� 50 ���ȍ~�͔�\���ł��B
[% END %]

[% FOREACH out IN out_sort %]
  [% out %]
[% END %]
[% IF N.size > 0 %]
  <hr />
  <ul>
  [% FOREACH n_no IN N %]
    <li>No [% n_no %] �̋L���͌��݂̃��O���ɂ���܂���I</li>
    [% IF klog_s %]
      �� <a href="[% srch %]?[% no %]&amp;word=
      [%- n_no %]&amp;andor=and&amp;logs=all&amp;PAGE=
      [%- klog_h.0 %]&amp;ALL=1">�S�ߋ����O���� No [% n_no %] �̋L����T��</a>
    [% END %]
  [% END %]
  </ul>
[% END %]

<hr />

[% PROCESS htmlfoot.tpl %]
