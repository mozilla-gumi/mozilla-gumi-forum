<tr>
  <td><strong>��</strong></td>
  <td>OS
    <select name="OS" onchange="ChangeSelection(this, 'distri', 'Linux')">
      [% IF os %]
        <option selected="selected" value="[% os %]">[% os %]</option>
        <option value="Other">���̑�</option>
      [% ELSE %]
        <option selected="selected" value="Other">���̑�</option>
      [% END %]
      [% FOREACH cur = listos %]
        <option value="[% cur %]">[% cur %]</option>
      [%- END %]
    </select>
    <span id="Linux" style="display:none;"> �f�B�X�g���r���[�V����:</span>
    <span id="BSD" style="display:none;"> BSD:</span>
    <input type="text" name="OSver" id="OSver" size="10" style="display:none;">
    �u���E�U <select name="BROWSER">
      [% IF browser %]
        <option selected="selected" value="[% browser %]">[% browser %]</option>
        <option value="Other">���̑�</option>
      [% ELSE %]
        <option selected="selected" value="Other">���̑�</option>
      [% END %]
      [% FOREACH cur = listbrowser %]
        <option value="[% cur %]">[% cur %]</option>
      [%- END %]
    </select>
    MUA <select name="MUA">
      [% FOREACH cur = listmua %]
        <option value="[% cur %]">[% cur %]</option>
      [%- END %]
      <option selected="selected" value="">���̑�</option>
    </select>
  </td>
</tr>
