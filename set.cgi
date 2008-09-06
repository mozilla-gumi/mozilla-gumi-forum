#! /usr/bin/perl

## WARNING!!!!
## ���Ƃ� cbbs �̐ݒ�t�@�C���Ƃ͑啝�ɈႢ�܂��B
## �R�����g���Q�l�ɂ��ĕҏW���Ă��������B
## $tmplVars{}�ɂȂ��Ă���ϐ��͂��̂����e���v���[�g�t�@�C���ֈړ����܂��B
## �S�Ă̕ϐ���$conf{}�Ɉڍs�\��ł��B
## �S�Ă̕ϐ���$conf{}�Ɉڍs��A�ݒ�t�@�C���̓e�L�X�g�x�[�X�ɂȂ�\��ł��B

#######################################################################
## MODIFICATION LOG
##
## Date       Author       Description
## ----       ------       -----------
## xx/01/2002 Ryuzi Kambe  Initial Release
##                         Customized Child Tree 5.1 for mozilla.gr.jp.
##                          1. Set color scheme
##                          2. Set/disabled some variables
##
## 03/02/2002 Gashu        Additional customization
##                          1. Set outliner images
##                          2. Changed styles to refer external CSS
##                              VARIABLE: ($STYLE)
##                          3. Changed description for fixed box
##                          4. Changed max length of title
##                              VARIABLE: ($t_max)
##                          5. Added related links(optional)
##                              VARIABLE: ($linkrel)
##                          6. Added additional help comments(optional)
##                              VARIABLE: ($helpadd)
##                          7. Added caption to main logo
##                              VARIABLE: ($talt)
##
## 22/02/2002 Gashu        Additional customization
##                          1. Enabled alternate style sheets
##                          2. Enabled some meta names
##                          3. Added a description about fixed font to Note.
##
## 08/03/2002 Gashu        Set titles for link item.
##
## 21/04/2005 Tooyama      Set titles for link item 2nd and more.
##
## 25/03/2006 Makoto       Additional customization
##                          1. Added custom header mode
##                              VARIABLE: ($custom_header_mode)
##                                        ($custom_header)
##
## 29/06/2006 Makoto       Delete "kanrimode = 2" description.
##                         (Bug-jp 5233)
##
#######################################################################

# �I�v�V�����͊�{�I�Ɉȉ��̂悤�ɂ���
#  0 : ���Ȃ��A�s�\
#  1 : ����A�\
#  1 �� not 0 ���Ӗ�����

our %conf;

#--- [��{�ݒ�] ----------------#
$met   = "POST";		# ���M�`��(POST or GET/�t�@�C���A�b�v���g���ꍇ��POST����)
    $tmplVars{'backurl'} = 'http://www.mozilla.gr.jp/';
#$backurl="http://www.mozilla.gr.jp";	# �߂�URL(http://�`��OK)
$TOPH = 1;			# �����\��(0=�X���b�h�^ 1=�c���[�^ 2=�g�s�b�N�^)
$max  = 100;			# �e�L���ő�ێ�����

#--- [�^�C�g���ݒ�] ------------#
##$title = "";		# �^�C�g�� => tmpl/head.tmpl
##$tface = "Times New Roman";	# �^�C�g���̃t�H���g
##$tsize = 6;			# �^�C�g���̃T�C�Y
##$tcolor= "#ffffff";		# �^�C�g���̐F(16�i��)
    $tmplVars{'t_img'} = 'file/logo.gif';
    $tmplVars{'twid'} = '186';
    $tmplVars{'thei'} = '67';
    $tmplVars{'talt'} = '������g�Z';
#$t_img= "file/logo.gif";			# �^�C�g���摜��URL�Ŏw��
#$twid = "186";			#  �V �̉���(�s�N�Z���w��)
#$thei = "67";			#  �V �̏c��(�@�V�@)
#$talt = "������g�Z";			#  �V �L���v�V����(�@�V�@)

#--- [�F�f�U�C���ݒ�] ----------#
$text = "#003366";		# �W�������F�w��(16�i��)
$bg   = "#C7D0D9";		# �w�i�F�̎w��  (�V)
$link = "blue";		# �������N�F�̎w��(�V)
$vlink= "purple";		# �������N�F�̎w��(�V)
##$ttb  = "#C7D0D9";		# �ėp�I�ȕ\�㕔�F(�V)
##$k_back="#FFFFFF";		# �L���̒��̔w�i�F(�V)
##$t_back="#E0ECF6";		# �L���薼�̔w�i�F(�V)
##$t_font="#008080";		# �L���薼�̕����F(�V)
##$res_f ="#666666";		# ���p�L���̐F    (�V)
##$kijino="#008080";		# �L��NO�̐F      (�V)
##$back = "";			# �w�i�摜��URL�Ŏw��(�����̏ꍇ�͋L�����Ȃ�)

#--- [�L�����e�Ɋւ���ݒ�] ----#
$topok= 1;			# �e�L�����e�͂���ł��\?(1=YES 0=�Ǘ��҂̂�)
$he_tp= 0;			# �ԐM��e�L�����e�҂݂̂̌����ɂ���?(1=YES 0=NO)
$r_max= 100;		# �ԐM�̌��x��(0 �ɂ���Ɩ�����)
$Res_i= 0;			# �L�����p��C�ӂɂ���?(1=�C�� 0=����)
$Res_T= 0;			# �e�L���𓊍e���ɕ��ׂ�?(1=YES 0=���X�ŐV��)
$AgSg = 1;			# ���X�̍ہA�L���ړ���C�ӂɂ���?(1=�C�� 0=����)
$EStmp= 1;			# �ҏW���ꂽ��^�C���X�^���v������?(1=YES 0=NO)
$UID  = 0;			# ID�@�\���g��?(1=YES 0=NO / �N�b�L�[�@�\�K�{)
$IDCol= "#FA8605";		# ID�@�\���g���ꍇ�̕\�������F
$wrap = "soft";			# �R�����g�t�H�[���̉��s�`��(soft=�蓮 or hard=����)
$tag  = 0;			# �^�O�̎g�p(YES=1 NO=0)
    $tmplVars{'use_post_edit'} = 0;         # ���e�̕ҏW�E�폜�t�H�[��
    $tmplVars{'use_password'} = 0;          # ���e���̃p�X���[�h�o�^�t�H�[��

#--- [�L���\���Ɋւ���ݒ�] ----#
$t_max= 128;			# �L���^�C�g���\�����x(����-���p40��/�S�p20��)
$AMark= '��';			# ���[���A�h���X�u������������(�摜�̏ꍇ��<img>��)
$SPAM = ' ';			# �A�h���X���W�\�t�g�΍�(�A�h���X�ɒǉ�����\������镶����)
$URLIM= "";			# URL�ɉ摜���g���ꍇ��http://�`�Ŏw��
$UI_Wi= "";			# �����p�̏ꍇ�摜����
$UI_He= "";			#      �V     �摜�c��(���c�����L�q)
$TGT  = "_blank";		# HOME�ȊO�̌f���O�ւ̃����N�^�[�Q�b�g

#--- [�L���^�C�g���̃w�b�_��ݒ�] -----------------------------------------------------------------
#       
# �摜=> <img>�^�O / �e�L�X�g=> ���Ȃǒ��ڏ���
# $hed_i �͒ʏ�L���p (�e�L�X�g��F�� / ��)
# $new_i �͐V���L���p (�e�L�X�g��F�m / NEW)
# $all_i �͈ꊇ�\���p (�e�L�X�g��F�� / ALL) => �c���[�\���p
# $up_i_ �͍X�V�L���p (�e�L�X�g��FUP / ��)  => �g�s�b�N/�X���b�h�\���p
#--------------------------------------------------------------------------------------------------
$hed_i= '<img src="file/hed.gif" height="15" width="15" border="0" alt="Message">';
$new_i= '<img src="file/new.gif" height="15" width="15" border="0" alt="New">';
$all_i= '<img src="file/all.gif" height="16" width="16" border="0" alt="All">';
$up_i_= '<img src="file/uph.gif" height="15" width="15" border="0" alt="Updated">';

#--- [�`�F�b�N�{�b�N�X�ݒ�] ----#
$end_f = 1;			# �����`�F�b�N�{�b�N�X���g���H(1=YES 0=NO)
$end_c = 0;			# �����`�F�b�N�͊Ǘ��l�̂݉\�ɂ���?(1=YES 0=NO)
$end_e = 0;			# �����`�F�b�N���t������ԐM�s�ɂ���?(1=YES 0=NO)

# ���`�F�b�N���A�\�����镨(�^�O�� �摜�̎���<img>�^�O)
$end_ok= '<strong class="red">��!</strong>';

#--------------------------------------------------------------------------------------------------
# ���`�F�b�N�𑣂��R�����g(��: ����������`�F�b�N�I)
$end_m =<<"_END_";

��肪����������`�F�b�N���Ă�������

_END_


#--- [�c���[�\���ݒ�] ----------*
$TrON  = 1;			# �c���[�\�����g��?(1=YES 0=NO)
$a_max = 10;			# 1�y�[�W�\���c���[��
$obg   = "#E0ECF6";		# �e�L���̃c���[�w�i�F(�V)
$Keisen= 1;			# �r����\������?(1=YES 0=NO)
$K_I   = '<img src="file/ol_ver.gif" height="14" width="15" alt="|">';			# �r��(�A���^/�摜�̏ꍇ��<img>)
$K_T   = '<img src="file/ol_con.gif" height="14" width="15" alt="|-">';			# �r��(����^/ �V )
$K_L   = '<img src="file/ol_edg.gif" height="14" width="15" alt="L">';			# �r��(�I���^/ �V )
$K_SP  = '<img src="file/1pix.gif" height="1" width="15" alt="">';			# �r��(�X�y�[�X/ �V)
$zure  = 6;			# �c���[�̂��꒲��(�r��OFF�̏ꍇ�L��)

#--- [�g�s�b�N�\���ݒ�] --------*
$TpON  = 1;			# �g�s�b�N�\�����g��?(1=YES 0=NO)
$tab_m = 2;			# 1�y�[�W�\���e�[�u����
$tpmax = 10;			# �e�[�u��1����̕\���g�s�b�N��
$topic = 10;			# 1�g�s�b�N��1�y�[�W����̕\����
$tp_hi = 0;			# �g�s�b�N���e�̏����z��(1=�V���L���g�b�v 0=�e�g�s�b�N�g�b�v)
$tpend = 0;			# ���X��̕\�����e(0=�g�b�v 1=���X�����g�s�b�N)

#--- [�X���b�h�\���ݒ�] --------*
$ThON  = 1;			# �X���b�h�\�����g��?(1=YES 0=NO)
$alk_su= 5;			# �X���b�h�\���̍ۂ̐e�L���\������
$alk_rm= 5;			# 1�X���b�h���ɕ\�����郌�X�L����
$Top_t = 1;			# �L�����X�g��\������?(1=YES 0=NO)
$LiMax = 100;			# �L�����X�g�\���ő匏��
$ResHy = 5;			# ���X�\���̋�؂�P��

#--- [���[���ݒ�] --------------*
$t_mail= 0;			# �S���e�������Ƀ��[���ʒm����?(1=YES 0=NO)
$mymail= 0;			# �����̓��e���ʒm?(1=YES 0=NO)
$mailto= 'user@host.ne.jp';	# �����̃��[���A�h���X
$o_mail= 1;			# ���e�҂Ƀ��X�L���ʒm�@�\���g��?(1=YES 0=NO)
$s_mail= '/var/qmail/bin/sendmail';	# sendmail�p�X
$q_mail= 1;			# qmail�̏ꍇ1�ɂ���

#--- [�p�X���[�h�����ݒ�] ------#
$s_ret= 0;			# �L��������ۂ̐���(0=���Ȃ� 1=�����Ƃ� 2=����&�ǂނƂ�)
$s_pas= "7777";			# ��L��1or2�̏ꍇ�̃p�X���[�h(���p�p��2�����ȏ�)

#--- [�J�E���^�ݒ�] ------------#
$cou  = 1;			# �J�E���^�̐ݒu (1=YES 0=NO)
$fig  = 7;			# �J�E���^�̌���
#$c_co = "#38B52F";		# �e�L�X�g=> �e�L�X�g�̐F
$m_wid= 8;			# �摜=> �摜�̉��T�C�Y
$m_hei= 12;			#  �V => �摜�̏c�T�C�Y
$m_pas= "";			#  �V => �f�B���N�g���̃p�X(�g�p���Ȃ��ꍇ���̂܂�)
$c_f  = "../data/dat/ccount.dat";		# �J�E���^�t�@�C��
$cloc = "../data/dat/c.loc";		# �J�E���^���b�N�t�@�C��

#--- [�t�@�C�����ݒ�] ----------#
$cgi_f= "./cbbs.cgi";		# ���̃t�@�C��
if($ENV{HTTP_HOST} =~ /mozilla.gr.jp/){$cgi_f="./";}
$srch = "./srch.cgi";		# ����/�ߋ����O�{���pCGI
$log  = "../data/dat/cbbs_log.cgi";		# �L�^�t�@�C��
$lockf= "../data/dat/cbbs.loc";		# ���b�N�t�@�C��
$bup  =  0;			# �o�b�N�A�b�v���Ƃ�? (NO=0 YES=x(x �͍X�V�p�x����������))
$bup_f= "../data/dat/cbbs.bak";		# �o�b�N�A�b�v�t�@�C��
$locks = 1;			# �t�@�C�������b�N����?(1=YES 0=NO)

#--- [�V���L���ݒ�] ------------#
$new_t = 24;			# NEW/UP�A�C�R�������V���L���͉����Ԉȓ��̋L��?
$new_s = 10;			# �V���L����\������L����
$new_su= 1;			# �V���L���̃\�[�g��(1=�V�����قǏ� 0=1�̋t)

#--- [���������N�ݒ�] ----------#
$M_Rank= 0;			# �����L���O���擾?(1=YES 0=NO)
$RLOG  = "../data/dat/rank.dat";		# �����L���O���O
$RDEL  = 30;			# �����L���O����폜��������
$RBEST = 30;			# �����L���O�\����
$RLOCK = "../data/dat/rank.loc";		# �����L���O���b�N�t�@�C��(�g�p��56�s�ڂɈˑ�)

# �����x���ݒ� �E�ɍs���قǍ���(�ݒ肵�Ȃ��ꍇ�͋�s @RLv=(); �ɂ���)
@RLv   = ("��ʐl","�t���l","�R�c","�t�@�~���[","�x�e����","��䏊");
$RSPL  = 50;			# ���x���̋�؂�P��(�����l����50�񂲂ƂɃ��x���A�b�v)
$RGimg = "";			# �O���t�ɉ摜���g���ꍇ���̉摜��URL������
$RGhei = 7;			# �O���t�摜�̏c��
# �������N�O�ɂ���l�̖��O(�Ȃ��ꍇ�͋�s @NoRank=(); �ɂ���)
@NoRank= ("�Ǘ��l�̖��O","��イ����");

#--- [�����ݒ�] ----------------#
$Kyo_f = "#F9FF06";		# �����ꋭ���\���̔w�i�F
$Met   = "GET";			# �����̍ۂ̃f�[�^�󂯓n���`��(POST or GET)
@klog_h= (20,30,40,50);		# �����\������(���[�͉ߋ����O�\�������Ƃ��Ă����p)
$klog_a= 1;			# �S�ߋ����O������������?(1=YES 0=NO)

#--- [�ߋ����O�֌W] ------------#
$klog_s= 1;			# �ߋ����O�@�\���g��?(1=YES 0=NO)
$klog_c= "../data/dat/klog.log";		# �ߋ����O���̃J�E���g�t�@�C��
$klog_d= "../data/dat/";			# �ߋ����O�����f�B���N�g��
$klog_l= 100;			# �ߋ����O�L�^ KB ��

#--- [RSS] ---#
    $conf{'rss'}     = 1;   # RSS�o�͂��邩 (1 : ����)
    $conf{'rss_num'} = 20;  # RSS�\���A�C�e���� (0 : ������)
    $conf{'rss_rev'} = 1;   # �V���L���\�[�g�� (1 : �V�����擪�A0 : �Â���)

#--------------------------------------------------------------------------------------------------
#                     [ �t�@�C���A�b�v�̐ݒ� ]
# �s�K�؂ȉ摜�̃A�b�v�̊Ď��ȂǁA�K�؂ȊǗ����K�v!!
# 1)@exn �̓A�b�v�\�t�@�C���g���q(�h�b�g(.)����L��/�K����������)
#     ��) .gif .txt .lzh .mid .mpeg .mp3 ��
# 2)@exi ��@exn��\������A�C�R���摜
#     �E�t�@�C���A�b�v����f�B���N�g��($i_dir)�ɓ����
#     �E�摜�̏ꍇ�� img �Ƃ����Ɖ摜���\�������
# 3)�t�@�C�����A�b�v����f�B���N�g���̃p�[�~�b�V������777 or 755
# 4)�摜�c���������擾�\�g���q�͈ȉ��̒ʂ�
#     (.gif/.GIF/.png/.PNG/.jpg/.jpeg/.JPG/.JPEG/.bmp/.BMP)
#--------------------------------------------------------------------------------------------------
$i_mode= 0;			# �t�@�C���A�b�v���[�h���g��?(1=YES 0=NO)

# �����΃p�X/��΃p�X �Ńt�@�C���A�b�v����ꏊ(�t�@�C���A�b�v�p)
$i_dir = "../data/dat/file";

# ��http:// ��URL �Ńt�@�C���A�b�v����ꏊ(�t�@�C���\���p)
$i_Url = "http://moz.rsz.jp/forums/file";

# ��@exn �� @exi �͕K���y�A��
@exn= (".gif",".jpg",".jpeg",".png",".txt",".lzh",".zip",".mid",".mov",".tbz");
@exi= ("img","img","img","img","txt.gif","arc.gif","arc.gif","oto.gif","oto.gif","arc.gif");

$H2    = 250;			# �k�����[�h��img�̍ō��c��
$W2    = 250;			# �V ����
$img_h = 15;			# @exi(img�ȊO) $no_ent $no_img �̏c��
$img_w = 15;			# �V ���� (���肵�Ȃ��ꍇ�͗����L�����Ȃ�)
$ResUp = 1;			# ���X���t�@�C���A�b�v�\�ɂ���?(1=YES 0=NO)
$max_or= 5000;			# �e/���X�L���̍��v�t�@�C���T�C�Y���x(����1�̏ꍇ�d�v)
$max_fs= 1000;			# �ЂƂ̋L��������̃t�@�C���T�C�Y�̌��x
				# (�L���o�C�g(1KByte=1024Bytes)�w��)
$mas_c = 0;			# �t�@�C���\���͊Ǘ��҃`�F�b�N������?(1=File 2=File/�L�� 0=NO)
$no_ent= "no.gif";		# ����1�̏ꍇ�������܂ŕ\�������摜($i_dir�ɂ����)
$i_ico = "i.gif";		# �A�C�R�����[�h�̉摜��։摜(�V)
$LogDel= 1;			# �ߋ����O�ڍs���t�@�C�����폜����?(1=YES 0=NO)


#--- [�t�H�[���X�^�C���ݒ�]-----#
$fss  = 0;			# �t�H�[���̃X�^�C���V�[�g���p(1=YES 0=NO)

# ��̍��ڂ� 1 �̏ꍇ�ݒ�
# �킩��Ȃ��ꍇ�͏����ݒ�̂܂�
# $fst=StyleSheet $on/$off=JavaScrip
#--------------------------------------------------------------------------------------------------
$fst=<<"SS_";
<STYLE TYPE="text/css">
<!--
-->
</STYLE>
SS_
# ���͍폜�s��-------------------------------------------------------------------------------------
# �� �}�E�X��������Ƃ���A�t�H�[�J�X���������̓���
#$on= "backgroundColor='#FDE8B5'\;";

# �� �}�E�X���ǂ����Ƃ���A�t�H�[�J�X�����������̓���
#$off="backgroundColor='#FFFFFF'\;";

#--- [�A�C�R���ݒ�] -------------------------------------------------------------------------------
# @ico1 => �t�@�C���� (xxx.gif/yyy.jpg ��)
# @ico2 => �A�C�R���� (�˂�/���� ��)
# @ico1 @ico2 �͕K���y�A�� �����ꍇ�́A�J���}(,)�̑O��ŉ��sOK
# @ico3 => �L���w�b�_�t�@�C���� (xxx.gif/yyy.jpg ��)
#          �L���w�b�_�ɃA�C�R���𔽉f������
#          @ico1 �Ɠ������p�ӂ���Brandam/master�������ʒu�ɓ����
#          �L���w�b�_�摜���炢�̏����߂̉摜��p��
#          �g��Ȃ��ꍇ�͋�s�� @ico3=(); ��
# [�Ǘ��҃A�C�R��] ����/�Ō�ɐݒ�ς� @ico1 �� master ��ݒ肷��(@ico2 �������Đݒ�)
# [�����_���@�\]   ����/�Ōォ��2�Ԗڂɐݒ�ς� @ico1 �� randam ��ݒ肷��(�V)
#--------------------------------------------------------------------------------------------------
$Icon   = 0;			# �A�C�R���@�\���g��?(1=YES 0=NO)
# �A�C�R���@�\�͈ꎞ�폜�ς�
$IconDir= "./icon";		# �摜�̂���f�B���N�g��(URL�ł�OK/�Ō�̃X���b�V���͏Ȃ�)

@ico1 = ('rob6.gif','rob2.gif','panda.gif','neko2.gif','mouse.gif','coara.gif','qes.gif','randam','master');
@ico2 = ('�z�C�[�����{','����胍�{','�ς�','�ӂƂ߃l�R','�˂���','������','�^��˂�','�����_��','�Ǘ��җp');
@ico3 = ('rob6_m.gif','rob2_m.gif','panda_m.gif','neko2_m.gif','mouse_m.gif','coara_m.gif','qes_m.gif','randam','master');


$IconHei= "32";			# �摜�̏c��(�s�N�Z���w��)
$IconWid= "32";			# �摜�̉���(�V) �T�C�Y�����肵�Ȃ��ꍇ �����L�����Ȃ�
$I_Hei_m= "15";			# @ico3�̏c��(�s�N�Z���w��)
$I_Wid_m= "15";			# @ico3�̉���(�V) �T�C�Y�����肵�Ȃ��ꍇ �����L�����Ȃ�
$Ico_h  = 4;			# �A�C�R���ꗗ�ŉ��s�����鐔
$Ico_w  = 100;			# �A�C�R���ꗗ�̕\����(�s�N�Z���w��)
$Ico_kp = 10;			# �A�C�R���ꗗ/�t�@�C���A�b�v�ꗗ�̉��y�[�W��
$Ico_k  = "ktai.gif";		# �g�ђ[������̃A�C�R��(�g��Ȃ��ꍇ�͋L�����Ȃ�)
$Ico_km = "ktai_m.gif";		# �g�ђ[������̃~�j�A�C�R��(�V)

#--- [�Ǘ��җp�A�C�R��] --------#
# -> ���̃A�C�R���Ɠ����f�B���N�g���ɓ����(�摜���͏�̐ݒ�Ɉˑ�)
# -> @mas_i = �Ǘ��p�A�C�R���t�@�C����
# -> @mas_m = �w�b�_�p�~�j�A�C�R���t�@�C����
# -> @mas_p = �p�X���[�h ���e���폜�L�[�ɓ���� �g�������ŕ����̊Ǘ��҃A�C�R�����g�p��
@mas_i= ('master.gif','rob6.gif');
@mas_m= ('masmin.gif','rob6_m.gif');
@mas_p= ('7777','8888');

#--- [�I�𕶎��F��ݒ�] --------#
# -> �����F�I�����g�p����ꍇ�ݒ�
# -> �ݒ���@�� @fonts = ('#xxxxxx','#yyyyyy','#zzzzzz') �Ƃ�������
@fonts= ('black','blue','green','aqua','red','pink','yellow');

#--- [�I��g���F��ݒ�] --------#
# -> �g���F�I�����g�p����ꍇ�ݒ�
# -> �ݒ���@�� @hr = ('#xxxxxx','#yyyyyy','#zzzzzz') �Ƃ�������
@hr   = ();

# �{���������Ȃ�IP�A�h���X(����/�ŏ���3��؂���w��) �����悤�ɂ����ł��w��\
@ips=("xxx.xxx.xxx","yyy.yyy.yyy","zzz.zzz.zzz");

$Proxy= 0;			# proxy�T�[�o�o�R���Ə������݂����Ȃ��ꍇ1

$NMAX = 50;			# ���O�̓��͌��x(�������Ȃ��ꍇ��0/���p������)
$TMAX = 100;			# �^�C�g�����͌��x( �V )
$CMAX = 10000;			# �R�����g���x( �V )

#--- [�Z���N�g/�e�L�X�g�ݒ�] ---#
# ���ꂼ��ЂƂ��ݒ�ł��܂��B
#-------------------------------#
$SEL_F = 1;			# �Z���N�g�t�H�[�����g��? (0=NO 1=YES)
$SEL_T = "�L�����e";		# �t�H�[���̗p�r����
$SEL_C = 0;			# �N�b�L�[�ɕۑ�����?(0=NO 1=YES)
$SEL_R = 0;			# �g�p�͐e�L���̂�?(0=NO 1=YES)
# �I�����̐ݒ�
@SEL   = ("(�I�����Ă�������)","����","����","�o�O��","����(������)",,"����(��薢����)","���","�⑫","�I�t�g�s");

$TXT_F = 0;			# �e�L�X�g�t�H�[�����g��? (0=NO 1=YES)
$TXT_T = "CGI��";		# �t�H�[���̗p�r����
$TXT_C = 1;			# �N�b�L�[�ɕۑ�����?(0=NO 1=YES)
$TXT_H = 0;			# ���͕K�{���ڂɂ���?(0=NO 1=YES)
$TXT_Mx= 30;			# ���͌��x(�������/���p30����)
$TXT_R = 0;			# �g�p�͐e�L���̂�?(0=NO 1=YES)

$TS_Pr = 1;			# �L�����\���ʒu(0=�^�C�g���O 1=�R�����g�O 2=�R�����g��)
				# (��L�Z���N�g/�e�L�X�g�Ƃ������ʒu�ɒu����܂�)


###added by victory , 2nd Tooyama
$notitle = '�薼���ݒ�';	#�^�C�g�������̏ꍇ�ɕt������^�C�g��
$noname = '���O���ݒ�';		#���O�����̏ꍇ�ɕt�����閼�O
$kanrimode = 1;		#�Ǘ����[�h�\��/��\�� 0:��\�� 1:�\��
$tdsep=' / ';
$klogext='.klog.cgi';
$atchange='-nosp@m.';

@bbsmile=qw[
	:D			icon_biggrin.gif	Very_Happy			:D
	:\)			icon_smile.gif		Smile				:)
	:\(			icon_sad.gif		Sad					:(
	:oops:		icon_redface.gif	Embarassed			:oops:
	:o			icon_surprised.gif	Surprised			:o
	:shock:		icon_eek.gif		Shocked				:shock:
	:\?			icon_confused.gif	Confused			:?
	8\)			icon_cool.gif		Cool				8)
	:lol:		icon_lol.gif		Laughing			:lol:
	:x			icon_mad.gif		Mad					:x
	:P			icon_razz.gif		Razz				:P
	:cry:		icon_cry.gif		Crying_or_Very_sad	:cry:
	:evil:		icon_evil.gif		Evil_or_Very_Mad	:evil:
	:twisted:	icon_twisted.gif	Twisted_Evil		:twisted:
	:roll:		icon_rolleyes.gif	Rolling_Eyes		:roll:
	:wink:		icon_wink.gif		Wink				:wink:
	:!:			icon_exclaim.gif	Exclamation			:!:
	:ques:		icon_question.gif	Question			:ques:
	:idea:		icon_idea.gif		Idea				:idea:
	:arrow:		icon_arrow.gif		Arrow				:arrow:
	:\|			icon_neutral.gif	Neutral				:|
	:mrgreen: 	icon_mrgreen.gif	Mr.Green			:mrgreen:
];

$BBFACE=1;
$smiledir='smiles/';
$useragent = $ENV{HTTP_USER_AGENT};
$useragent =~ s/</&lt;/;
$useragent =~ s/>/&gt;/;
if($BBFACE){
	$BBFACE = '<tr><td title="ON�ɂ���Ɠ��e��摜�ɕϊ����܂�">';
    $BBFACE .= '�X�}�C���[<input id="smile" name="smile" type="hidden" value="ON"></td><td>';
	for ($_ = 0; $_ < scalar(@bbsmile); $_ +=4) {
		$BBFACE .= "\n";
		$BBFACE .= '<img onclick="emoticon(' . "'$bbsmile[$_]'" . ')" src="' . "$smiledir$bbsmile[$_+1]" . '" border="0" alt="' . $bbsmile[$_+2] . '" title="' . $bbsmile[$_+2] . '" class="bbsmile" />';
	}
	$BBFACE .= "<br>\n <span onclick=\"emoticon('UA')\" title=\"�N���b�N�Ńe�L�X�g�G���A�ɓ\\��t�����܂�\">$useragent</span></td>\n</tr>";
}

sub smile_encode{
	$smile_pre = '<img src="' . $smiledir;

	for ($_ = 0; $_ < scalar(@bbsmile); $_ +=4) {
		$smile_aft = '" alt="' . $bbsmile[$_+2] . '">';
		$comment =~ s/ $bbsmile[$_] / $smile_pre$bbsmile[$_+1]$smile_aft /g;
	}
}

sub smile_decode{
	$smile_pre = '<img src="' . $smiledir;

	for ($_ = 0; $_ < scalar(@bbsmile); $_ +=4) {
		$smile_aft = '" alt="' . $bbsmile[$_+2] . '">';
		$com =~ s/$smile_pre$bbsmile[$_+1]$smile_aft/$bbsmile[$_+3]/g;
	}
}

$use_col=0;		#�L���̕����F�w��Ƃ��̕\���ւ̓K�p 0:
if(!$use_col){@fonts=();}
$ua_select=1;

$target_blank =0;		#�V���������J�����邩�ǂ����B0:off ���Ȃ��ꍇ�͎���3�s�Ŗ��E���܂��B
if($target_blank){
$TGT  = ' target="_blank"';		# HOME�ȊO�̌f���O�ւ̃����N�^�[�Q�b�g
}else{$TGT="";}




1;#�폜�s��
