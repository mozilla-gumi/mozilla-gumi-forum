[% IF BG == "" %]
    [% PROCESS htmlhead.tpl
        htmltitle = "�G���["
    %]
[% END %]

<div class="ErrMsg">
[% adminerror = 0 %]
[% IF errmsg == 'noname' %]
  ���O�������͂ł��B�u���E�U�́m�߂�n�{�^�����g���Ă�����x���͂��Ă�������
[% ELSIF errmsg == 'nodmay' %]
  �^�C�g���������͂ł��B�u���E�U�́m�߂�n�{�^�����g���Ă�����x���͂��Ă�������
[% ELSIF errmsg == 'nocomment' %]
  ���e�������͂ł��B�u���E�U�́m�߂�n�{�^�����g���Ă�����x���͂��Ă�������
[% ELSIF errmsg == 'invalidemail' %]
  E-���[���̓��͓��e������������܂���B�悭�m�F���Ă��������B
  �u���E�U�́m�߂�n�{�^�����g���Ă�����x���͂��Ă�������
[% ELSIF errmsg == 'invaliddeleky' %]
  �p�X���[�h��8�����ȓ��ł��B��������ƃG���[���ł܂��B
  �u���E�U�́m�߂�n�{�^�����g���Ă�����x���͂��Ă�������
[% ELSIF errmsg == 'namelength' %]
  ���O�͔��p[% NMAX %]���ȓ��ł��肢���܂��B
  �u���E�U�́m�߂�n�{�^�����g���Ă�����x���͂��Ă�������
[% ELSIF errmsg == 'dmaylength' %]
  �^�C�g���͔��p[% TMAX %]���ȓ��ł��肢���܂��B
  �u���E�U�́m�߂�n�{�^�����g���Ă�����x���͂��Ă�������
[% ELSIF errmsg == 'commentlength' %]
  �R�����g�͔��p[% CMAX %]���ȓ��ł��肢���܂��B
  �u���E�U�́m�߂�n�{�^�����g���Ă�����x���͂��Ă�������
[% ELSIF errmsg == 'notxtt' %]
  [% TXT_T %]�������͂ł��B
  �u���E�U�́m�߂�n�{�^�����g���Ă�����x���͂��Ă�������
[% ELSIF errmsg == 'nodelkey' %]
  �g�s�b�N�ǉ��ɂ̓p�X���[�h���K�{�ł��B
  �u���E�U�́m�߂�n�{�^�����g���Ă�����x���͂��Ă�������
[% ELSIF errmsg == 'iprefused' %]
  ���Ȃ��̃A�N�Z�X��IP�A�h���X�́A�ߋ��Ɍf���^�c�ɏd��Ȏx����y�ڂ��s�ׂ��s����
  �Ȃǂ̗��R�ŋ��ۂ���Ă��܂��B [% COMipaddr %]
[% ELSIF errmsg == 'adminicon' %]
  �Ǘ��җp�A�C�R���͎g�p�ł��܂���B
[% ELSIF errmsg == 'nopass' %]
  �w�肳�ꂽ�L���ɂ̓p�X���[�h���ݒ肳��Ă��܂���B
[% ELSIF errmsg == 'invpass' %]
  �p�X���[�h�������͂��A���͂��ꂽ�p�X���[�h����v���܂���B
[% ELSIF errmsg == 'longmail' %]
  ���e���ꂽ���[���A�h���X���������܂��B
[% ELSIF errmsg == 'longurl' %]
  ���e���ꂽ URL ���������܂��B
[% ELSIF errmsg == 'invid' %]
  �폜���悤�Ƃ��Ă��铊�e�̓o�^ No �������͂������͖����ł��B
[% ELSIF errmsg == 'editinvid' %]
  �ҏW���悤�Ƃ��Ă��铊�e�� No �������͂������͖����ł��B
[% ELSIF errmsg == 'cookieoff' %]
  �u���E�U�� cookie ������������Ă��܂��B
  ���̏�Ԃł͂��̌f���ւ̓��e�͂ł��܂���B
  cookie �Ή��̃u���E�U�𗘗p���邩�Acookie ��L���ɂ��Ă��������B
[% ELSIF errmsg == 'twicepost' %]
  ������e��2�x�����������Ƃ��Ă��܂��B���d���e�͖����ł��B�Ċm�F���Ă��������B
[% ELSIF errmsg == 'notcreator' %]
  ���̃g�s�b�N�ւ̓g�s�b�N�̍쐬�҂݂̂��ԐM�ł��܂��B
[% ELSIF errmsg == 'uplimit' %]
  �A�b�v���[�h��������Ă���T�C�Y�𒴂���T�C�Y�̃t�@�C�����A�b�v���[�h���悤�Ƃ��Ă��܂��B
  �A�b�v���[�h����͖���������܂����B
[% ELSIF errmsg == 'oldlogs' %]
  �ߋ����O�ɂ͏������݂ł��܂���B
[% ELSIF errmsg == 'viaproxy' %]
  ProxyServer�o�R�ł͏������݂ł��܂���!
[% ELSIF errmsg == 'noflag' %]
  �A�b�v�ł��Ȃ��t�@�C���`���ł�!
[% ELSIF errmsg == 'upoverflow' %]
  �t�@�C���T�C�Y���傫�����܂�!
[% ELSIF errmsg == 'newpasserr' %]
  �p�X���[�h���Ⴂ�܂�!
[% ELSIF errmsg == 'novalidsetcgi' %]
  �ݒ�t�@�C����CGI�ɐݒ肳��Ă܂���!
[% ELSIF errmsg == 'invalidfile' %]
  ���̃t�@�C���͉{���ł��܂���!
[% ELSIF errmsg == 'invalidpass' %]
  �p�X���[�h���Ⴂ�܂�!
[% ELSIF errmsg == 'locked' %]
  LOCK is BUSY (���b�N��)
[% ELSIF errmsg == 'renerr' %]
  Rename Error
[% ELSIF errmsg == 'nobackup' %]
  �o�b�N�A�b�v���Ȃ��̂ŏC���s�\�ł�!
[% ELSIF errmsg == 'alreadyct' %]
  ���ł� ChildTree �p�ɂȂ��Ă��܂�!
[% ELSIF errmsg == 'captcha0' %]
  captcha�̐ݒ�G���[�ł��B
  [% adminerror = 1 %]
[% ELSIF errmsg == 'captcha-1' %]
  captcha�̗L���������؂�܂����B�ēx�擾���Ă��������B
[% ELSIF errmsg == 'captcha-2' %]
  captcha�̃R�[�h��������܂���B����captcha�͈�x�������p�ł��܂���B
[% ELSIF errmsg == 'captcha-3' %]
  captcha�̃R�[�h����v���܂���B
  ���̓t�H�[���������[�h����captcha���擾���Ȃ����Ă�蒼���Ă��������B
  captcha�ɂ́A2-9�̐�����a-y�܂ł̉p�������݂̂����p����Ă��܂��B
[% ELSIF errmsg == 'cannot_write' %]
  ���̃G���g���ɂ͏������݂ł��܂���B
[% ELSIF errmsg == 'cannot_write_oldlogs' %]
  ���̉ߋ����O�ɂ͏������݂ł��܂���B
[% ELSIF errmsg == 'captchaoth' %]
  ���m��captcha�Ɋւ���G���[�ł��B
  [% adminerror = 1 %]
[% ELSIF errmsg == 'edit_not_allowed' %]
  ���̃t�H�[�����ł͓��e�L���̕ҏW�E�폜�͋�����Ă��܂���B
[% ELSIF errmsg == 'range_undefined' %]
  �͈͂��w�肳��Ă��܂���B
[% ELSIF errmsg == 'disabled' %]
  ���̋@�\�͐ݒ�Ŗ����ɂ���Ă��܂��B
  �K�v�Ǝv����ꍇ�́A�Ǘ��҂܂Ŗ₢���킹�Ă��������B
[% ELSE %]
  ERROR - [% errmsg %]
[% END %]
</div>

[% IF adminerror == 1 %]
<div>
���̃G���[���o���Ƃ��ɂǂ̂悤�ȑ�������Ă������ƃG���[�R�[�h [% errmsg %] ���A
<a href="http://bugzilla.mozilla.gr.jp">bugzilla-jp</a> �Ƀo�O�Ƃ��ēo�^���Ă��������B
</div>
[% END %]

[% PROCESS htmlfoot.tpl %]

