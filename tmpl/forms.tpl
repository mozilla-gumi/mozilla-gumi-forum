[% IF FORM_PV == "" %]
  <form action="[% cgi_f %]" method="[% met %]"
    [% IF multipart == 1 %]enctype="multipart/form-data"[% END %]
    name="post">
[% END %]
<ul>
  <li>入力内容にタグは利用[% IF tag %]可能です。[% ELSE %]できません。[% END %]</li>
  [% PROCESS atcom.inc.tpl %]
</ul>
<input type="hidden" name="N" value="[% N_NUM %]">
<input type="hidden" name="mode" value="wri">
<input type="hidden" name="type" value="[% nams %]">
<input type="hidden" name="kiji" value="[% namber %]">
<input type="hidden" name="space" value="[% sp %]">
[% nf %][% pf %][% Hi %]

[% IF he_tp %]
  <h3>トピックを作成した時のパスワードでのみ返信ができます。
    (トピックの作成にはパスワードが必須です)</h3>
[% END %]

<table class="Submittion" summary="form" border="0">
<tr>
  <td><strong>お名前</strong></td>
  <td>
    <input type="text" name="name" value="[% c_name %]" size="25"
      [% IF NMAX %]maxlength="[% NMAX %]"[% END %]>
    [% IF UID %]
      [ID:[% pUID %]]
      <!--
        ←<a href="[% cgi_f %]?mode=cookdel" [% TGT %]>このIDを破棄</a>
      -->
    [% END %]
  </td>
</tr>
<tr>
  <td rowspan="2"><strong>E メール</strong></td>
  <td>
    <input type="text" name="email" value="[% c_email %]" size="40" maxlength="100" disabled="disabled">
  </td>
</tr>
  [% IF o_mail %][% PROCESS mbox %][% END %]
  [% uasel %]
<tr>
  <td><strong>タイトル</strong></td>
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
    <strong>コメント</strong>
    <input type="radio" name="pre" value="0" checked="checked">自動改行
    <input type="radio" name="pre" value="1">手動改行（等幅フォント）
    <br>
    <textarea id="comment" name="comment" rows="12" cols="75"
      [% IF BBFACE %]
        onselect="storeCaret(this);"
        onclick="storeCaret(this);"
        onkeyup="storeCaret(this);"
      [% END %]
    >[% IF com_nodisp %]コメント表示: 未許可[% ELSE %][% com %][% END %]</textarea>
  </td>
</tr>
<!-- Auto-linkify -->
<tr>
  <td>自動リンク</td>
  <td>
    <span onclick="add_linkify('mozillazine-jp <id>');">MozillaZine-jp</span>
    /
    <span onclick="add_linkify('bug-jp <id>');">Bugzilla-jp</span>
    /
    <span onclick="add_linkify('bug-org <id>');">bmo (bugzilla.mozilla.org)</span>
    (クリックで挿入)
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
      <td><strong>パスワード</strong></td>
      <td>
        <input type="password" name="delkey" value="[% c_key %]" size="8">
          (半角8文字以内[% KEY %])</td>
      </td>
    </tr>
  [% END %]
<tr>
  <td>プレビュー</td>
  <td><input type="checkbox" name="PV" value="1" onclick="pvcheck();">
    左のチェックボックスをチェックすると、投稿前にプレビューができます</td>
</tr>
  [% IF end_ok %]
    <tr>
      <td>[% end_ok %]</td>
      <td>
        [% IF end_c %][% end_ok %] になったらその旨も書いてください。[% END %]
        <input type="checkbox" name="end" value="1" [% PVC %]>[% end_m %]
      </td>
    </tr>
  [% END %]
  [% IF optH %]<input type="hidden" name="H" value="[% optH %]">[% END %]
  [% PROCESS show_captcha %]
<tr>
  <td colspan="2" align="right">
    <input type="submit" value=" 送 信 ">
    <input type="reset" value="リセット">
  </td>
</tr>
</table>
</form>

<hr width="95%">


[% BLOCK hr_sel %]
  <tr>
    <td>枠線色</td>
    <td>
      [% FOREACH hr_c IN hr %]
        <input type="radio" name="hr" value="[% hr_c %]
          [% IF hr_c == hr_def %]checked="checked"[% END %]>
          <font color=[% hr_c %]">■</font>
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
    <td>記事ソート</td>
    <td>
      <select name="AgSg">
        <option value="1">上げる(age)</option>
        <option value="0">下げる(sage)</option>
      </select>
    </td>
  </tr>
[% END %]

[% BLOCK mbox %]
<tr>
  <td>
    * 関連する返信記事をメールで受信しますか?
    <select name="send" disabled="disabled">
      <option value="0">いいえ
      <option value="1" [% PVE %]>はい
   </select>
    * アドレスの表示
    <select name="pub" disabled="disabled">
      <option value="0">非表示
      <option value="1" [% IF c_pub %]selected="selected"[% END %]>表示
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
    上の画像認証の画像に表示されている文字 (2-8の数字もしくはzを除く英小文字) 
    を入力してください。<br />
    読み込み後、一度もしくは60分間しか有効ではありません。<br />
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
    アップ可能拡張子 &gt;
    <!--
      将来的に一覧を出せるようにする - 配列の扱い
    -->
    <br>
    1) 太字の拡張子は画像として認識されます。<br>
    2) 画像は初期状態で縮小サイズ[% H2 %]×[% W2 %]ピクセル以下で表\示されます。<br>
    3) 同名ファイルがある、またはファイル名が不適切な場合、<br>
    　　ファイル名が自動変更されます。<br>
    4) アップ可能\ファイルサイズは1回<strong>[% max_fs %]KB</strong>(1KB=1024Bytes)までです。<br>
    5) ファイルアップ時はプレビューは利用できません。<br>
    [% IF SIZE %]
      6) スレッド内の合計ファイルサイズ:[[% SIZE %]/[% max_or %]KB] 
        <strong>残り:[[% Rest %]KB]</strong>
    [% END %]
  </td>
</tr>
[% END %]
