#!/usr/local/bin/perl

require './common.pl';

use Forum::Captcha;

#------------------------------------------
my $ver = "Child Tree v8.92 (modified)";# (�c���[���f����)
#------------------------------------------
# Copyright(C) ��イ����
# E-Mail:ryu@cj-c.com
# W W W :http://www.cj-c.com/
#------------------------------------------

#---[�ݒ�t�@�C��]-------------------------

my @set;
# �����悤�ɂ����ł����₹�܂��B
# [ ]���̐������g��CGI�ɃA�N�Z�X����Ƃ��̐ݒ�t�@�C���œ��삵�܂��B
# $set[12] �̐ݒ�t�@�C�����g���ꍇ: http://www.---.com/cgi-bin/cbbs.cgi?no=12
$set[0]="./set.cgi";
#if (!($ENV{SCRIPT_FILENAME} =~ /forums/)) {
#    $set[1]="./set_kanri.cgi";
#    $set[2]="./set_color.cgi";
#    $set[3]="./set_forums.cgi";
#    $set[4]="./set_viewdel.cgi";
#}
my @NW;
my @ips;

# �r��IP/�֎~������ݒ�t�@�C��
my $IpFile = "../data/cbbs/IpAcDeny.cgi";
my $NWFile = "../data/cbbs/WordDeny.cgi";

# ---[�r��IP/�֎~������ǂݍ���]-------------------------------------------------------------------------------------
if (-e $NWFile) {
    open(DE, "$NWFile");
    while (<DE>) {push(@NW, $_); }
    close(DE);
}
if (-e $IpFile) {
    open(DE, "$IpFile");
    while (<DE>) {push(@ips, $_); }
    close(DE);

    $match=0;
    foreach (@ips) {
        $_=~ s/\n//;
        $_ =~ s/\./\\\./g;
        if ($ENV{'REMOTE_ADDR'}=~ /^$_/) {
            $match=1;
            last;
        }
    }
    if ($match) {
        &er_('iprefused');
    }
}
# ---[�ݒ�t�@�C���ǂݍ���]------------------------------------------------------------------------------------------
$res_r=1;
&d_code_;
if (($set[$no]) && (-e $set[$no])) {
    $SetUpFile="$set[$no]";
} else {
    $SetUpFile="$set[0]";
    undef($no);
} require $SetUpFile;
#else{&er_('novalidsetcgi');}
if ($no && ($mode ne "all_v") &&
    (Forum->config->GetParam('admin_pass') eq '')) {
#if ($no && ($mode ne "all_v") && !$pass) {
    $no="no=$no";
}
$nf= "<input type=\"hidden\" name=\"no\" value=\"$no\">\n";
# ---[�t�H�[���X�^�C���V�[�g�ݒ�]------------------------------------------------------------------------------------
$ag=$ENV{'HTTP_USER_AGENT'};
if ($fss && $ag =~ /IE|Netscape6/) {
    $fm=" onmouseover=\"this.style.$on\" onmouseout=\"this.style.$off\"";
    $ff=" onFocus=\"this.style.$on\" onBlur=\"this.style.$off\"";
    $fsi="$fst";
}
# ---[�ȈՃp�X���[�h�����֘A]----------------------------------------------------------------------------------------
if ($s_ret) {
    if ($FORM{"P"} eq "") {
        &get_("P");
    }
    $P=$FORM{"P"};
    $pf="<input type=\"hidden\" name=\"P\" value=\"$P\">\n";
    $pp="&P=$P";
} else {
    $pf="";
    $pp="";
}
if ($FORM{'KLOG'}) {
    $KLOG=$FORM{'KLOG'};
    $TrON=0;
    $TpON=1;
    $ThON=0;
    $TOPH=2;
    unless($KLOG=~ /^[\d]+/) {
        &er_('invalidfile');
    }
    $log="$klog_d\/$KLOG$klogext";
    $pp.="&KLOG=$KLOG";
    $pf.="<input type=\"hidden\" name=\"KLOG\" value=\"$KLOG\">\n";
}
if ($s_ret && $P eq "" && ($mode eq "alk"||$mode eq "")) {
    &pas_;
}
if ($s_ret==2 && $P eq "R") {
    &er_('invalidpass');
}
if ($s_ret && $P ne "R") {
    if ($P ne "$s_pas") {
        &er_('invalidpass');
    } else {
        &set_("P");
    }
}
# ---[�T�u���[�`���̓ǂݍ���/�\���m��]-------------------------------------------------------------------------------
if (($conf{'rss'} eq 1) && ($mode eq 'RSS')) {&RSS; }
if ($mode eq "all_v") {&a_;}
if ($mode eq "ffs") {&freeform_;}
if ($mode eq "bma") {&bma_;}
if ($mode eq "Den") {&Den_;}
if ($mode eq "ent") {&ent_;}
if ($mode eq "man") {&man_;}
if ($mode eq "n_w") {&n_w_;}
if ($mode eq "wri") {&wri_;}
if ($mode eq "del") {&del_;}
if ($mode eq "s_d") {&s_d_;}
if ($mode eq "nam") {&hen_;} # edit post
if ($mode eq "h_w") {&h_w_;}
if ($mode eq "new") {&new_;}
if ($mode eq "all") {&all_;}
if ($mode eq "al2") {&all2;}
if ($mode eq "res") {&res_;}
if ($mode eq "key") {&key_;} # delete post
if ($mode eq "one") {&one_;}
if ($mode eq "ran") {&ran_;}
if ($mode eq "f_a") {&f_a_;}
if ($mode eq "img") {&img_;}
if ($mode eq "red") {&read;}
if ($mode eq "cmin") {&set_("M");}
if ($mode eq "cookdel") {&cookdel;}

unless(-e $log) {
    if ($KLOG eq "") {&l_m($log);}
}
unless(-e $c_f) {
    if ($cou) {&l_m($c_f);}
}
unless(-e $RLOG) {
    if ($M_Rank) {&l_m($RLOG);}
}
if ($W) {$Wf = "&W=$W"; }
if ($H) {$Hf = "&H=$H"; }
if ($W eq "W") {$Res_T = 0; }
elsif ($W eq "T") {$Res_T = 1; }
elsif ($W eq "R") {$Res_T = 2; }
if ($mode eq "alk") {&alk_;}
if ($H eq "F") {&html2_;}
elsif ($H eq "T") {&html_;}
elsif ($H eq "N") {&alk_;}
if ($TOPH == 1) {&html_; }
elsif ($TOPH==2) {&html2_;}
else {&alk_; }
exit;

#--------------------------------------------------------------------------------------------------------------------
# [�L���f�U�C��] 
# -> �L���𓝈�f�U�C���ŕ\��(design)
#
sub design ($$$$$$$$$$$$$$$$$$$$$$$$$$$) {
    my ($namber, $date, $name, $email, $d_may, $comment_, $url, $space, 
        $end, $type, $delkey, $ip, $tim, $ico, $Ent, $fimg, $mini, 
        $icon, $font, $hr, $txt, $sel, $yobi, $Se, $ResNo, $htype, 
        $hanyo) = @_;
    @_ = ();
    my ($comment, $userenv) = split('\t', $comment_);
    my $email =~ s/@/$atchange/;

    $HTML = "";
    $commode = '<div class="ArtMain">';
    if (($mode eq "alk") && ($type)) {
        $commode = '<div class="ArtChild">';
    }
    if ((($mode eq "al2") || ($mode eq "res")) && ($type)) {
        $commode = '</div><div class="ArtMain">';
    }
    if ($font eq "") {$font = $text; }
    if ($hr eq "") {$hr = $ttb; }
    if ($d_may eq "") {$d_may = "$notitle"; }
    if ($Icon && $comment =~ /<br>\(�g��\)$/) {$icon = "$Ico_k"; }
    if ($icon ne "") {
        if ($IconHei) {$WH = " height=\"$IconHei\" width=\"$IconWid\""; }
        $icon = "<img src=\"$IconDir\/$icon\"$WH>";
    }
    if ((! $name) || ($name eq ' ') || ($name eq '�@')) {$name = $noname; }
    if ($txt) {$Txt = "$TXT_T:[$txt]�@"; }
    else {$Txt = ""; }
    if ($sel) {$Sel = "$SEL_T:[$sel]�@"; }
    else {$Sel = ""; }
    if ($yobi) {$yobi = "[ID:$yobi]"; }
    if ($end) {$end = "$end_ok"; }
    if ($email && ($Se < 2)) {
        $email = "<a href=\"mailto:$SPAM$email\">$AMark</a>";
    } else {
        $email = "";
    }
    if ($url) {
        if ($URLIM) {
            if ($UI_Wi) {$UIWH = " width=\"$UI_Wi\" height=\"$UI_He\""; }
            $i_or_t = "<img src=\"$URLIM\" border=\"0\"$UIWH>";
        } else {
            $i_or_t = "http://$url";
        }
        $url="<br><a href=\"http://$url\"$TGT>$i_or_t</a>";
    }
    if ($Txt || $Sel || ($Txt && $Sel)) {
        if ($TS_Pr == 0) {$d_may = "$Txt$Sel/" . "$d_may"; }
        elsif ($TS_Pr == 1) {$comment = "$Txt<br>$Sel<br>" . "$comment"; }
        elsif ($TS_Pr == 2) {$comment .= "<br>$Txt<br>$Sel"; }
    }
    if (Forum->user->validate_password_admin($FORM{'pass'}) != 0) {
#    if ($FORM{"pass"} && ($FORM{"pass"} eq $pass)) {
        $Ent = 1;
        $url = "";
    }
    if (($mas_c == 2) && ($Ent == 0)) {
        $comment = "�R�����g�\\��:������";
    }
    if ($o_mail) {
        $Smsg = "[���[���]��/";
        if (($Se == 2) || ($Se == 1)) {
            $Smsg .= "ON]\n";
        } else {
            $Smsg .= "OFF]\n";
        }
    }
    if ($ico && $i_mode) {
        $Pr = "";
        &size();
        $Pr = "<tr><td align=\"center\">$Pr</td></tr>\n";
        $SIZE += $Size;
    } else { 
        $Pr = "";
    }
    $agsg = "";
    $UeSt = "";
    $Pre = "";
    if ($ResNo == 0) {$ResNo = "�e"; }
#--------------------------------------------------------
    if ($htype eq "T") {
        $ResNo = "$ResNo�K�w";
        $Border = 1;
        $Twidth = 90;
        if ($Res_i) {
            $IN = "<strong><a href=\"$cgi_f?mo=1&amp;mode=one&amp;namber=$namber&amp;type=$type&amp;space=$space&amp;$no$pp#F\">�L�����p</a></strong>";
        }
    } elsif ($htype eq "T2") {
        $ResNo = "$ResNo�K�w";
        $Border = 1;
        $Twidth = 90;
        $IN = "<strong><a href=\"$cgi_f?mode=one&amp;namber=$nam&amp;type=$ty&amp;space=$sp&amp;$no$pp\">�ԐM</a></strong>";
        if ($Res_i) {
            $IN .= "/<strong><a href=\"$cgi_f?mo=1&amp;mode=one&amp;namber=$nam&amp;type=$ty&amp;space=$sp&amp;$no$pp\">���p�ԐM</a></strong>\n";
        }
        $VNo = $namber;
        $OTL = "";
        if ($type > 0) {
            $UeSt .= "$b_ ";
            $OTL = " <a href=\"#$ty\">�e $type </a> /";
        } else {
            $UeSt .= "�e�L���@/ ";
        }
        if ($n_) {
            $UeSt .= "$n_ </a>\n";
        } else {
            $UeSt .= "�ԐM����\n";
        }
        if ($OTL) {
            $IN = "[$OTL]\n" . $IN;
        }
        $HTML .= "<br>";
    } elsif ($htype eq "F") {
        $VNo++;
        $ResNo = "���̃g�s�b�N�� $ResNo �Ԗڂ̓��e";
        $Border = 0;
        $Twidth = 90;
        $IN = "<a href=\"$cgi_f?mode=al2&amp;mo=$nam&amp;namber=$FORM{'namber'}&amp;space=$sp&amp;rev=$rev&amp;page=$fp&amp;$no$pp#F\"><strong>���p�ԐM</strong></a>";
        if ($Res_i) {$IN .= "/<a href=\"$cgi_f?mode=al2&amp;mo=$nam&amp;namber=$FORM{'namber'}&amp;space=$space&amp;rev=$rev&amp;page=$fp&amp;In=1&amp;$no$pp#F\"><strong>�ԐM</strong></a>";}
        if ($VNo == 1) {
            $sg = $VNo + 1;
            $agsg = "\&nbsp\;\&nbsp\;<a href=\"#$sg\">��</a><a href=\"#1\">��</a>";
        } elsif ($VNo >= $topic) {
            $ag = $VNo - 1;
            $agsg = "<a href=\"#$ag\">��</a>�@<a href=\"#1\">��</a>";
        } else {
            $ag = $VNo - 1;
            $sg = $VNo + 1;
            $agsg="<a href=\"#$ag\">��<a href=\"#$sg\">��<a href=\"#1\">��</a>";
        }
    } elsif ($htype eq "N") {
        $ResNo = "";
        $Border = 1;
        $Twidth = 90;
        if ($TOPH == 0) {
            $MD = "mode=res&amp;namber=";
            if ($type) {$MD .= "$type"; }
            else {$MD .= "$namber"; }
        } elsif ($TOPH == 1) {
            $MD = "mode=one&amp;namber=$namber&amp;type=$type&amp;space=$space";
        } elsif ($TOPH == 2) {
            $MD = "mode=al2&amp;namber=";
            if ($type) {$MD .= "$type"; }
            else {$MD .= "$namber"; }
            $MD .= "&amp;space=$space";
        }
        $IN = "<strong><a href=\"$cgi_f?$MD&amp;$no$pp#F\">�ԐM</a></strong>";
        if ($Res_i) {
            $IN .= "/<strong><a href=\"$cgi_f?$MD&amp;mo=$namber&amp;$no$pp#F\">���p�ԐM</a></strong>\n";
        }
    } elsif ($htype eq "P") {
        $ResNo = "";
        $Border = 1;
        $Twidth = 90;
        if ($hanyo eq "randam") {$icon = "�A�C�R��<br>�����_��"; }
    } elsif ($htype eq "TR") {
        if ($ResNo eq "�e") {
            $ResNo = "�e�L��";
            $Twidth = 100;
        } else {
            $ResNo = "���̃X���b�h�� $ResNo �Ԗڂ̕ԐM";
            $Twidth = 90;
        }
        $Border = 0;
        $IN = "<a href=\"$cgi_f?mode=res&amp;namber=$nam&amp;type=$type&amp;space=$space&amp;mo=$namber&amp;page=$PNO&amp;$no$pp#F\"><strong>���p�ԐM</strong></a>";
        if ($Res_i) {
            $IN .= "/<a href=\"$cgi_f?mode=res&amp;namber=$nam&amp;type=$type&amp;space=$space&amp;mo=$namber&amp;page=$PNO&amp;In=1&amp;$no$pp#F\"><strong>�ԐM</strong></a>";
        }
    } elsif ($htype eq "TRES") {
        $Border = 0;
        $Twidth = 90;
        $VNo++;
        if ($ResNo eq "�e") {
            $ResNo = "�e�L��";
        } else {
            $ResNo = "���̃X���b�h�� $ResNo �Ԗڂ̕ԐM";
        }
        if ($VNo == 1) {
            $sg = $VNo + 1;
            $agsg = "\&nbsp\;\&nbsp\;<a href=\"#$sg\">��</a><a href=\"#1\">��</a>";
        } elsif ($VNo >= $topic) {
            $ag = $VNo - 1;
            $agsg = "<a href=\"#$ag\">��</a>�@<a href=\"#1\">��</a>";
        } else {
            $ag = $VNo - 1;
            $sg = $VNo + 1;
            $agsg = "<a href=\"#$ag\">��<a href=\"#$sg\">��<a href=\"#1\">��</a>";
        }
        $IN = "<a href=\"$cgi_f?mode=res&amp;mo=$nam&amp;namber=$FORM{'namber'}&amp;space=$sp&amp;page=$page&amp;$no$pp#F\"><strong>���p�ԐM</strong></a>";
        if ($Res_i) {
            $IN .= "/<a href=\"$cgi_f?mode=res&amp;mo=$nam&amp;namber=$FORM{'namber'}&amp;space=$sp&amp;page=$page&amp;In=1&amp;$no$pp#F\"><strong>�ԐM</strong></a>"
        }
    }

    $tmplVars{'commode'} = $commode;
    $tmplVars{'namber'} = $namber;
    $tmplVars{'d_may'} = $d_may;
    $tmplVars{'resno'} = $ResNo;
    $tmplVars{'name'} = $name;
    $tmplVars{'r'} = $R;
    $tmplVars{'date'} = $date;
    $tmplVars{'url'} = $url;
    $tmplVars{'comment'} = $comment;
    $tmplVars{'end'} = $end;
    $tmplVars{'pr'} = $Pr;
    $tmplVars{'mode'} = $mode;
    $tmplVars{'smsg'} = $Smsg;
    $tmplVars{'in'} = $IN;
    $tmplVars{'nam'} = $nam;
    $tmplVars{'cgi_f'} = $cgi_f;
    $tmplVars{'met'} = $met;
    $tmplVars{'nf'} = $nf;
    $tmplVars{'pf'} = $pf;
    $tmplVars{'ff'} = $ff;
    $tmplVars{'fm'} = $fm;
    $tmplVars{'font'} = $font;
    $tmplVars{'use_col'} = $use_col;
    $tmplVars{'userenv'} = $userenv;
    if ($KLOG) {$tmplVars{'klog_def'} = 1; } else {$tmplVars{'klog_def'} = 0; }
    if ($type) {$tmplVars{'type_def'} = 1; } else {$tmplVars{'type_def'} = 0; }
    $HTML_2 = "";
    $obj_template->process('articledesign.tpl', \%tmplVars, \$HTML_2);
    $HTML .= $HTML_2;
}
#--------------------------------------------------------------------------------------------------------------------
# [�g�s�b�N�ꗗ�\��]
# -> �g�s�b�N���ꗗ�\��(html2_)
#
sub html2_ {
    @NEW = ();
    @RES = ();
    %R = ();
    %RES = ();
    $RS = 0;
    if ($FORM{'page'}) {
        $page = $FORM{'page'};
    } else {
        $page = 0;
    }
    open(LOG,"$log") || &er_("Can't open $log");
    while (<LOG>) {
        ($namber,$date,$name,$email,$d_may,$comment,$url,
        $space,$end,$type,$del,$ip,$tim) = split(/<>/,$_);
        $email =~ s/@/$atchange/;
        if($type){
            if ($tim eq "") {$tim = "$TIM"; }
            $tim = sprintf("%011d", $tim);
            $RS++;
            if ($R{$type}) {$R{$type}++; }
            else {$R{$type} = 1; }
            if(($OyaCount > $page+($tab_m*$tpmax) || $page > $OyaCount+1) &&
               $Res_T==0 && $tim=~/[\d]+/) {
                next;
            }
            if($date){$RES{$type}.="$tim<>$_";}
        }else{
            if($tim eq ""){$tim="$TIM";} $tim=sprintf("%011d",$tim);
            if($Res_T==2){$tim=$R{$namber}; $tim=sprintf("%05d",$tim);}
            push(@NEW,"$tim<>$_"); $OyaCount=@NEW;
        }
        $TIM=$tim;
    }
    close(LOG);

    if($Res_T){@NEW=sort(@NEW); @NEW=reverse(@NEW);}
    $total=@NEW; $NS=$total+$RS; @lines=();
    $PAGE=$page/($tpmax*2);
    &hed_("All Topic / Page: $PAGE");
    $Pg=$page+1; $Pg2=$page+$tpmax*$tab_m;
    if($Pg2 >= $total){$Pg2=$total;}
    $obj_template->process('comtop.inc.tpl');

    $tmplVars{'new_t'} = $new_t;
    $tmplVars{'new_i'} = $new_i;
    $tmplVars{'up_i_'} = $up_i_;
    $tmplVars{'henko'} = $Henko;
    $obj_template->process('topiclist.tpl', \%tmplVars);

    if($i_mode){&minf_("F");}

    $end_data=@NEW-1;
    $page_end=$page+($tpmax*$tab_m-1);
    if($page_end >= $end_data){$page_end=$end_data;}
    $page_=int(($total-1)/($tpmax*$tab_m));
    $view =$tpmax*$tab_m;
    $nl = $page_end + 1;
    $bl = $page - $view;
    if($bl >= 0){
        $Bl="<a href=\"$cgi_f?H=F&amp;page=$bl&amp;$no$pp$Wf\">"; $Ble="</a>";
    }else{
        $Bl=""; $Ble="";
    }
    if($page_end ne $end_data){
        $Nl="<a href=\"$cgi_f?H=F&amp;page=$nl&amp;$no$pp$Wf\">"; $Nle="</a>";
    }else{
        $Nl=""; $Nle="";
    }
    if($cou){&con_;}
    print"<div class=\"Caption03l\">�S $total �g�s�b�N�� $Pg �` $Pg2 ��\\��</div>\n";
    $Plink="$Bl$Ble\n"; $a=0;
    for($i=0;$i<=$page_;$i++){
        $af=$page/($tpmax*$tab_m);
        if($i != 0){$Plink.=" ";}
        if($i eq $af){
            $Plink.="[<strong>$i</strong>]\n";
        }else{
            $Plink.="[<a href=\"$cgi_f?page=$a&amp;H=F&amp;$no$pp$Wf\">$i</a>]\n";}
            $a+=$tpmax*$tab_m;
        }
        $Plink.="$Nl$Nle\n";
        if($Res_T==1){
            $OJ1="<a href=\"$cgi_f?H=F&amp;W=W&amp;$no$pp\">�ԐM�ŐV��</a>";
            $OJ2="���e��";
            $OJ3="<a href=\"$cgi_f?H=F&amp;W=R&amp;$no$pp\">�L������</a>";
        } elsif($Res_T==2){
            $OJ1="<a href=\"$cgi_f?H=F&amp;W=W&amp;$no$pp\">�ԐM�ŐV��</a>";
            $OJ2="<a href=\"$cgi_f?H=F&amp;W=T&amp;$no$pp\">���e��</a>";
            $OJ3="�L������";
        }else{
            $OJ1="�ԐM�ŐV��";
            $OJ2="<a href=\"$cgi_f?H=F&amp;W=T&amp;$no$pp\">���e��</a>";
            $OJ3="<a href=\"$cgi_f?H=F&amp;W=R&amp;$no$pp\">�L������</a>";
        }
        print"<div class=\"Caption01r\">�e�L���̏��� [ $OJ1 / $OJ2 / $OJ3 ]</div>\n";
        $Plink="<div class=\"Caption01c\"><strong>�S�y�[�W</strong> / $Plink</div>\n";
        print $Plink;
        $k=0; $q=0;
        if($k){$p=$tab_m-$i; $page+=$tpmax*$p; last;}
        if($topok){$TP="<th width=\"13\%\">�g�s�b�N�쐬��</th>";}
        if($he_tp==0){$SK="<th width=\"13\%\">�ŏI������</th>";}
        if($end_f){$EE='<th width="5%">��</th>';}
        $TableChange=0;
        foreach ($page .. $page_end) {
            ($T,$namber,$date,$name,$email,$d_may,$comment,$url,
             $space,$end,$type,$del,$ip,$tim,$Se) = split(/<>/,$NEW[$_]);
            ($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
            ($ICON,$ICO,$font,$hr)=split(/\|/,$TXT);
            ($txt,$sel,$yobi)=split(/\|\|/,$SEL);
            $email =~ s/@/$atchange/;
            if($TableChange==0){
                print"<br><table class=\"Topics\" summary=\"topic\" align=\"center\" width=\"90\%\" border><tr>\n";
                if($SEL_F){print"<th>$SEL_T</th>";}
                if($TXT_F){print"<th>$TXT_T</th>";}
                print"<th width=\"46\%\">�g�s�b�N�^�C�g��</th><th width=\"8\%\">�L����</th>$TP$SK<th width=\"15\%\">�ŏI�X�V</th>$EE</tr>\n";
            }
            $TableChange++;
            if($i_mode){
                $File=0; $Size=0;
                if($ico){$File++; $Size+=-s "$i_dir/$ico";}
            }
            if(($time_k-$tim) > $new_t*3600){$news="$hed_i";}else{$news="$new_i";}
            if($yobi){$yobi="[ID:$yobi]";}
            if((!$name)||($name eq ' ')||($name eq '�@')){$name=$noname;}
            if($email && $Se < 2){$name="$name <a href=\"mailto:$SPAM$email\">$AMark</a>";}
            if($d_may eq ""){$d_may="$notitle";}
            if(length($d_may)>$t_max){$d_may=substr($d_may,0,($t_max-2)); $d_may="$d_may..";}
            $reok="<br>"; $date=substr($date,5,16);
            $ksu=1; $BeTime=0;
            @RES= split(/\n/,$RES{$namber}); @RES=sort(@RES);
            foreach $lines(@RES) {
                ($T,$rnam,$rd,$rname,$rmail,$rdm,$rcom,$rurl,
                 $rsp,$re,$rtype,$del,$ip,$rtim,$rSe) = split(/<>/,$lines);
                $rmail =~ s/@/$atchange/;
                if($namber eq "$rtype"){
                    ($Ip,$ico,$Ent,$fimg,$rTXT,$rSEL,$R)=split(/:/,$ip);
                    ($rtxt,$rsel,$rid)=split(/\|\|/,$rSEL);
                    if($SEL_R==0){$sel="$rsel";} if($TXT_R==0){$txt=$rtxt;}
                    if($rid){$rid="<br>[ID:$rid]";}
                    if($i_mode){if($ico){$File++; $Size+=-s "$i_dir/$ico";}}
                    $ksu++;
                    if($BeTime < $rtim || $tim !~/[\d]+/){
                        if($rmail && $rSe < 2){$rn="$rname <a href=\"mailto:$SPAM$rmail\">$AMark</a>";}
                        else{$rn="$rname";}
                        $rdd=substr($rd,5,16);
                        if($re){$reok="$end_ok";}else{$reok="<br>";}
                        if(($time_k-$rtim)>$new_t*3600){$news="$hed_i";}else{$news="$up_i_";}
                        $BeTime=$rtim;
                    }
                    if($R{$namber}==($ksu-1)){last;}
                }
            }
            if($rdd eq ""){$rdd="$date";}
            if($rn eq "") {$rn="$name$yobi";}
            if($topok){$TP2="<td align=\"center\">$name$yobi</td>";}
            if($he_tp==0){$SK2="<td align=\"center\">$rn$rid</td>";}
            if($Size){$KB=int($Size/1024); if($KB==0){$KB=1;}}
            $FL="<br>��<span class=\"ArtId\">#$namber</span>�@[�쐬��:$date]";
            if($File && $Size){$FL.="�@[File:$File -$KB\KB]";}
            if($topic < $ksu){
                $a=0; $PG_=int(($ksu-1)/$topic); $RP="";
                for($j=0;$j<=$PG_;$j++){
                    $RP.="<a href=\"$cgi_f?mode=al2&amp;namber=$namber&amp;page=$a&amp;rev=$tp_hi&amp;$no$pp$Wf\">$j</a>\n";
                    $a+=$topic;
                }
                if($FL){$FL.="�@[ $RP]";}else{$FL="<br>�@<small>[ $RP]";}
            }
            if(@ico3 && $Icon && ($ICON ne "" || $comment=~/<br>\(�g��\)$/)){
                if($I_Hei_m){$WHm=" width=\"$I_Wid_m\" height=\"$I_Hei_m\"";}
                if($ICON ne ""){if($ICON=~ /m/){$ICON=~ s/m//; $mICO=$mas_m[$ICON];}else{$mICO=$ico3[$ICON];}}
            elsif($Icon && $comment=~/<br>\(�g��\)$/){$mICO="$Ico_km";}
            $news.="<img src=\"$IconDir\/$mICO\" border=\"0\"$WHm>";
        }
        if($TXT_F){if($txt){$Txt="<td>$txt</td>";}else{$Txt="<td>/</td>";}}
        if($SEL_F){if($sel){$Sel="<td>$sel</td>";}else{$Sel="<td>/</td>";}}
        $ksu=$R{$namber}+1;
        print"<tr>$Sel$Txt<td align=\"left\">";
        print"<a href=\"$cgi_f?mode=al2&amp;namber=$namber&amp;rev=$r&amp;$no$pp\">$news <strong>$d_may</strong></a>$FL</td>";
        print"<td align=\"center\">$ksu��</td>$TP2$SK2<td align=\"center\"><small>$rdd</small></td>";
        if($end_f){print"<td align=\"center\">$reok</td>";}
        print"</tr>\n";
        $rdd=""; $rn=""; $rid="";
        if($tpmax <= $TableChange || $_ >= $total-1){print"</table><br>\n"; $TableChange=0;}
    }
    &allfooter("�g�s�b�N$view");
    &foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [�R�����g���p]
# -> �g�s�b�N/�X���b�h�\���̍ۂ̈��p����(comin_)
#
sub comin_{
    if ($sp==0) {$re = 1; }
    elsif ($sp>0) {$re = $sp / 15 + 1; }
    if ($d_may eq "") {$d_may = $notitle; }
    if ($d_may =~ /^Re\[/) {
        $resuji = index("$d_may" , "\:");
        $d_may =~ s/\:\ //;
        $d_may = substr($d_may, $resuji);
    }
    $ti = "Re[$re]: $d_may";
    $space = $sp;
    ($com, $com_) = split('\t', $com);
    if ($FORM{'In'} eq "") {
        $com = "��No$nam�ɕԐM($na����̋L��)<br>$co";
        $com =~ s/<br>/\n&gt; /g;
        $com =~ s/&gt; &gt; /&gt;&gt;/g;
    }
    $com =~ s/&nbsp;/ /g;
    $com =~ s/	//g;
    $com =~ s/\t//g;
    $com =~ s/\	//g;
    $FORM{"type"} = $ty;
    $type = $ty;
    $namber = $nam;
}
#--------------------------------------------------------------------------------------------------------------------
# [�g�s�b�N���e�\��]
# -> �g�s�b�N���e��\��(all2)
#
sub all2 {
    if ($FORM{'rev'} ne "") {$rev = $FORM{'rev'}; }
    else {$rev = $tp_hi; }
    if ($space eq "") {$space = 0; }
    $SP = $space + 15;
@TOP=(); $k=0; $Dk=0; $On=0; $En=0; $O2=0; $TitleHed="";
open(DB,"$log");
while (<DB>) {
    ($nam,$da,$na,$mail,$d_may,$co,$ur,
        $sp,$end,$ty,$de,$ip,$time)=split(/<>/,$_);
    if(($ty==0 && $FORM{"namber"} eq "$nam")||($ty != 0 && $FORM{"namber"} eq $ty)){
        if($rev){
            ($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
            if($ico && -s "$i_dir/$ico"){$SIZE+= -s "$i_dir/$ico";}else{$SIZE+=0;}
        }
        if($space < $sp && $On==0 && $O2==0){$N_NUM=$nam; $On=1;}
        if($space eq $sp && $O2==0 && $mo ne $nam){$On=0; $N_NUM="";}
        if($time){
            $time=sprintf("%011d",$time);
            push(@TOP,"$time<>$_"); if($end){$En=1;}
        }else{$Dk++;}
        $namb=$nam; $k++; $TitleHed=$d_may;
        if($mo){if($mo eq $nam){$On=1; $O2=1; &comin_;}}else{if($k==1){$On=1; $O2=1; &comin_;}}
    }else{if($k && $KLOG eq ""){last;}}
}
close(DB);
@TOP=sort(@TOP);
if($rev){@TOP=reverse(@TOP);}
$fhy ='<h2><a name="F">���̃g�s�b�N�ɏ�������</a></h2>';
if($KLOG){$fhy="";}
$total=@TOP;
if($FORM{'page'} eq ''){$page=0;}else{$page=$FORM{'page'};}
$PAGE=$page/$topic;
&hed_("One Topic All View / $TitleHed / Page: $PAGE","1");
if($cou){&con_;}
if($rev){
    print"$fhy\n";
    if($r_max && ($total-1) >= $r_max){
        print"<h3>�ԐM���̌��x�𒴂����̂ŕԐM�ł��܂���B<br>(�ԐM�����x:$r_max ���݂̕ԐM�L����:$total)</h3>\n";
        print" �� <strong><a href=\"$cgi_f?mode=new&amp;$no$pp\">[�g�s�b�N�̐V�K�쐬]</a></strong>";
        }else{if($En && $end_e){print"$end_ok / �ԐM�s��";
    }else{&forms_("F");}}
}
$page_=int(($total-1)/$topic);
$end_data=@TOP-1;
$page_end=$page+($topic-1);
if($page_end >= $end_data){$page_end=$end_data;}
$Pg=$page+1; $Pg2=$page_end+1;
$nl=$page_end+1; 
$bl=$page-$topic;
if($page_end ne $end_data){$Nl="<a href=\"$cgi_f?mode=al2&amp;namber=$FORM{'namber'}&amp;page=$nl&amp;rev=$rev&amp;$no$pp\">"; $Nle="</a>";}
if($bl >= 0){$Bl="<a href=\"$cgi_f?mode=al2&amp;namber=$FORM{'namber'}&amp;page=$bl&amp;rev=$rev&amp;$no$pp\">"; $Ble="</a>";}
print "<form action=\"$cgi_f\" method=\"$met\">\n";
print"<div class=\"Caption03l\">�g�s�b�N���S $total �L������ $Pg �` $Pg2 �Ԗڂ�\\��</div>\n";
if($rev == 0){
    print"<div class=\"Caption01r\"><strong>[ <a href=\"$cgi_f?mode=al2&amp;namber=$FORM{'namber'}&amp;rev=1&amp;$no$pp\">";
    print"�ŐV�L���y�ѕԐM�t�H�[�����g�s�b�N�g�b�v��</a> ]</strong><br></div>\n";
}elsif($rev){
    print"<div class=\"Caption01r\"><strong>[ <a href=\"$cgi_f?mode=al2&amp;namber=$FORM{'namber'}&amp;rev=0&amp;$no$pp\">�e�L�����g�s�b�N�g�b�v��</a> ]</strong><br></div>\n";
}
$Plink="<div class=\"Caption01c\"><strong>���̃g�s�b�N�̑S�y�[�W</strong> / "; $a=0;
for($i=0;$i<=$page_;$i++){
    $af=$page/$topic;
    if($i != 0){$Plink.=" ";}
    if($i eq $af){$Plink.="[<strong>$i</strong>]\n";}else{$Plink.="[<a href=\"$cgi_f?mode=al2&amp;namber=$FORM{'namber'}&amp;page=$a&amp;rev=$rev&amp;$no$pp\">$i</a>]\n";}
    $a+=$topic;
}
$Plink.="</div>";
print"$Plink<br>";
if($Dk){print"($Dk���̍폜�L�����\\��)<br>";}
print"\n";
$i=0; $ToNo=$page; $SIZE=0;
foreach ($page .. $page_end) {
    ($T,$nam,$date,$name,$email,$d_may,$comment,$url,
        $sp,$end,$ty,$del,$ip,$tim,$Se) = split(/<>/,$TOP[$_]);
    ($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
    ($ICON,$ICO,$font,$hr)=split(/\|/,$TXT);
    ($txt,$sel,$yobi)=split(/\|\|/,$SEL);
    $ToNo++;
    if($rev){$fp=0;}else{$fp=$topic*$page_;}
    &design($nam,$date,$name,$email,$d_may,$comment,$url,$sp,$end,$ty,$del,$Ip,$tim,$ico,
        $Ent,$fimg,$ICON,$ICO,$font,$hr,$txt,$sel,$yobi,$Se,$ToNo,"F","");
    print"$HTML\n";
}
if($TrON){$TrLink="<div class=\"Caption01r\">[ <a href=\"$cgi_f?mode=all&namber=$FORM{'namber'}&space=0&type=0&$no$pp\">$all_i ���̃g�s�b�N���c���[�ňꊇ�\\��</a> ]</div>";}
print <<"_HTML_";
<hr>
<div class="Forms">
<input type="hidden" name="no" value="0">
<strong>�폜 / �ҏW�t�H�[��</strong><br>
�`�F�b�N�����L����
<select name="mode">
<option value="nam">�ҏW
<option value="key">�폜
</select>
�p�X���[�h <input type="password" name="delkey"size="8"$ff>
<input type="submit" value="���M" $fm>
</div>
</form>
_HTML_
print"<hr>\n$TrLink\n";
if($Bl){print"<div class=\"Caption01r\">[ $Bl�O�̃g�s�b�N���e$topic��$Ble ]";}
if($Nl){if($Bl){print" | ";}else{print "<div class=\"Caption01r\">";} print"[ $Nl���̃g�s�b�N���e$topic��$Nle ]</div>";}else{print "</div>";}
print"$Plink\n<hr>\n";
$Ta=$total-1;
if($r_max && $Ta > $r_max){
    print"<h3>�ԐM���̌��x�𒴂����̂ŕԐM�ł��܂���B</h3>(�ԐM�����x:$r_max ���݂̕ԐM��:$Ta)";
    print" �� <strong><a href=\"$cgi_f?mode=new&amp;$no$pp\">[�g�s�b�N�̐V�K�쐬]</a></strong><br>";
}else{
    if($En && $end_e){print"<h3>$end_ok / �ԐM�s��</h3><br>";}
    else{
        if($total <= ($page+$topic) && $rev==0){
            print"$fhy";
            &forms_("F");
        }elsif($total >= ($page+$topic) && $rev==0){
            $page=$i-1; $a-=$topic;
            print"<div class=\"Caption01r\">[ <a href=\"$cgi_f?mode=al2&amp;namber=$FORM{'namber'}&amp;page=$a&amp;$no$pp#F\">���̃g�s�b�N�̕ԐM�t�H�[����</a> ]</div>";
        }
    }
}
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [�c���[�L���\��]
# -> �c���[�̋L����\������(one_)
#
sub one_ {
@TREE=();
open(LOG,"$log") || &er_("Can't open $log");
while ($Line = <LOG>) {
    ($nam,$date,$name,$email,$d_may,$comment,$url,
        $sp,$end,$ty,$del,$ip,$tim) = split(/<>/,$Line);
    if(($type==0 && ($nam eq $namber || $ty eq $namber))||($type && ($nam eq $type || $ty eq $type))){
    $kiji_exist=1;
        if($ty){
            if($Keisen){
                $SPS=$sp/15; $Lg=0; $Tg=0; $S="";
                if($SP){
                    if($SP > $SPS){if($L[$SPS]){$Tg=1; $L[$SP]="";}else{$Lg=1; $L[$SP]="";}}
                    elsif($SP==$SPS && $L[$SPS]){$Tg=1;}elsif($SP < $SPS){$Lg=1;}
                }else{$Lg=1;}
                if($SPS > 1){foreach(2..$SPS){$_--; if($L[$_]){$S.="$K_I";}else{$S.="$K_SP";}}}
                $SP=$sp/15;
                if($SP==1){@L=(); $L[$SP]=1;}else{$L[$SP]=1;}
                if($Lg){$Line="<tt>$S$K_L</tt><>$Line";}
                elsif($Tg){$Line="<tt>$S$K_T</tt><>$Line";}
            }else{$Line="<>$Line";}
            if($date){unshift(@TREE,$Line);}
        }else{unshift(@TREE,"<>$Line"); $SP=0; @L=(); if($tim=~/[\d]+/){last;}}
    }
}
close(LOG);
$rs=0; $i=0; $ON=0; $Tree=""; $SP=0; $F=0;
foreach $lines (@TREE) {
    ($Sen,$nam,$date,$name,$email,$d_may,$comment,$url,
        $sp,$end,$ty,$del,$ip,$tim,$Se)=split(/<>/,$lines);
    ($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
    ($ICON,$ICO,$font,$hr)=split(/\|/,$TXT);
    ($txt,$sel,$yobi)=split(/\|\|/,$SEL);
    if($namber eq "$nam" && $namber ne $ty) {
    $kiji_exist=1;
        if($d_may eq ""){$d_may="$notitle";}
        &hed_("One Message View / $d_may","1");
        $com="$comment";
        $com=~ s/<br>/\n&gt; /g; $com=~ s/&gt; &gt; /&gt;&gt;/g; $com="&gt; $com";
        if($sp==0){$re=1;}elsif($sp>0){$re=$sp/15+1;}
        if($d_may=~ /^Re\[/){
            $resuji=index("$d_may" , "\:");
            $d_may=~ s/\:\ //;
            $d_may=substr($d_may,$resuji);
        }
        $ti="Re[$re]: $d_may";
        if($i==0){$i=1;}
        $ResNo=$sp/15;
        &design($nam,$date,$name,$email,$d_may,$comment,$url,$sp,$end,$ty,$del,$Ip,$tim,$ico,
            $Ent,$fimg,$ICON,$ICO,$font,$hr,$txt,$sel,$yobi,$Se,$ResNo,"T");
        print"$HTML\n";
        print'<br><table class="Topics border" summary="beforeafter">';
        print"\n<tr align=\"center\"><th>�O�̋L��(���ɂȂ����L��)</th>\n";
        print"<th>���̋L��(���̋L���̕ԐM)</th></tr>\n";
    }
    if($end){$end="$end_ok"; $En=1;}
    if($d_may eq ""){$d_may="$notitle";}
    $date=substr($date,2,19);
    if(($time_k-$tim)>$new_t*3600){$news="$hed_i";}else{$news="$new_i";}
    if($txt){$Txt="$TXT_T:[$txt]�@";}else{$Txt="";}
    if($sel){$Sel="$SEL_T:[$sel]�@";}else{$Sel="";}
    if($Txt || $Sel ||($Txt && $Sel)){if($TS_Pr==0){$d_may="$Txt$Sel/"."$d_may";}}
    if(@ico3 && $Icon && ($ICON ne "" || $comment=~/<br>\(�g��\)$/)){
        if($I_Hei_m){$WHm=" width=\"$I_Wid_m\" height=\"$I_Hei_m\"";}
        if($ICON ne ""){if($ICON=~ /m/){$ICON=~ s/m//; $mICO=$mas_m[$ICON];}else{$mICO=$ico3[$ICON];}}
        elsif($Icon && $comment=~/<br>\(�g��\)$/){$mICO="$Ico_km";}
        $news.="<img src=\"$IconDir\/$mICO\" border=\"0\"$WHm>";
    }
    if($yobi){$yobi="[ID:$yobi]";}
    if(length($d_may)>$t_max){$d_may=substr($d_may,0,($t_max-2)); $d_may="$d_may..";}
if((!$name)||($name eq ' ')||($name eq '�@')){$name=$noname;}
    if($email && $Se < 2){$name="$name <a href=\"mailto:$email\">$AMark</a>";}
    if($ico && $i_mode){$Pr=""; &size(1); $Pr=" "."$Pr"; $SIZE+=$Size;}else{$Pr="";}
    $psp=$space+15;$nsp=$space-15;
    if(($namber eq "$ty" || $type eq "$nam" || $type eq "$ty") && $ON==0){
        if($rs && $sp <= $space && $type){$ON=1;}
        if($sp eq $nsp && $nam < $namber && $i != 1){
            $b_="<a href=\"$cgi_f?mode=one&amp;namber=$nam&amp;type=$ty&amp;space=$sp&amp;$no$pp\">$d_may</a>\n/$name <small>$yobi</small>$Pr";
        }elsif($type == 0){$b_="�e�L��";}
        if($sp eq $psp && $nam > $namber && $i == 1){
            $n_.="<a href=\"$cgi_f?mode=one&amp;namber=$nam&amp;type=$ty&amp;space=$sp&amp;$no$pp\">$d_may</a>\n/$name <small>$yobi</small>$Pr<br>";
            $N_NUM=$nam;
        }
        if($i==1){$rs=1;}
    }
    $im=""; $im2=""; $im3="";
    if($sp > $SP && $F){$N_NUM=$nam;}
    if($sp eq $SP && $F){$F=0;}
    if($N_NUM eq $nam && $F==0){$F=1; $SP=$sp;}
    if($nam eq $namber){$im="<strong class=\"Highlight\">";$im2="";$im3=" *���݂̋L��<\/strong>";$ii=1;}
    if($Keisen){$Tree.="$Sen";}
    else{

        $spz=$sp/15*$zure;
        $Tree.="." x $spz;

    }
    $Tree.="$im<a href=\"$cgi_f?mode=one&amp;namber=$nam&amp;type=$ty&amp;space=$sp&amp;$no$pp\">$news $d_may</a>\n";
    $Tree.="/ $name :$date <span class=\"ArtId\">(#$nam)</span>$im2 $end$Pr$im3</td></tr><tr><td colspan=\"2\" nowrap>\n";
}
if(!$kiji_exist){$kiji_exist=2; if($TOPH==1){&html_;}elsif($TOPH==2){&html2_;}else{&alk_;}}else{
print"<tr><td valign=\"top\" width=\"50\%\">$b_</td><td width=\"50\%\">\n";
if($n_){print"$n_\n";}else{print"�ԐM����\n";}
print <<"_HTML_";
�@</td></tr>
</table>
<br>
<h2>��L�֘A�c���[</h2>
<table summary="tree" class="Tree">

<tr><td colspan="2">
_HTML_

print "$Tree\n";
$total=@TREE-1;
if($type>0){$a_="$type";}elsif($type==0){$a_="$namber";}
if($TpON){$TpLink=" / <a href=\"$cgi_f?mode=al2&amp;namber=$a_&amp;rev=$r&amp;$no$pp\">��L�c���[���g�s�b�N�\\��</a>\n";}
print <<"_TREE_";
</td></tr></table><!--dum-->
<div class="Caption01r">
[ <a href="$cgi_f?mode=all&amp;namber=$a_&amp;type=0&amp;space=0&amp;$no$pp">$all_i ��L�c���[���ꊇ�\\��</a>
$TpLink ]</div>
<br><hr><h2><a name="F">��L�̋L���֕ԐM</a></h2>
_TREE_
if ($r_max && ($total >= $r_max)) {
    print"<h3>�ԐM���̌��x�𒴂����̂ŕԐM�ł��܂���B</h3>\n(�ԐM�����x:$r_max ���݂̕ԐM��:$total)";
    print" <strong><a href=\"$cgi_f?mode=new&amp;$no$pp\">[�c���[�̐V�K�쐬]</a></strong>\n";
} else {
    if ($En && $end_e) {print "$end_ok / �ԐM�s��"; }
    if ($vRSS eq 'RSS') {}
    else{&forms_("T"); }
}
&foot_;
}
}
#--------------------------------------------------------------------------------------------------------------------
# [�c���[�\��]
# -> �c���[�̈ꗗ��\������(html_)
#
sub html_ {
    @NEW = ();
    @RES = ();
    @SEN = ();
    $SP = 0;
    %RES = ();
    %R = ();
    if ($FORM{'page'}) {
        $page = $FORM{'page'};
    } else {
        $page = 0;
    }
    open(LOG, "$log") || &er_("Can't open $log");
    while ($Line = <LOG>) {
        ($namber,$date,$name,$email,$d_may,$comment,$url,
            $space,$end,$type,$del,$ip,$tim) = split(/<>/, $Line);
        if (($namber !~ /^[0-9]*$/) || ($type !~ /^[0-9]*$/)) {next; }
        if ($type) {
            $RS++;
            if ($R{$type}) {
                $R{$type}++;
            } else {
                $R{$type} = 1;
            }
            if (($OyaCount > $page+$a_max || $page > $OyaCount+1) &&
                 $Res_T==0 &&
                 $tim=~/[\d]+/) {
                next;
            }
            if ($date) {
                if ($Keisen) {
                    $SPS = $space / 15;
                    $Lg=0;
                    $Tg=0;
                    $S="";
                    if ($SP) {
                        if ($SP > $SPS) {
                            if ($L[$SPS]) {
                                $Tg=1; $L[$SP]="";
                            } else {
                                $Lg=1; $L[$SP]="";
                            }
                        } elsif ($SP==$SPS && $L[$SPS]) {
                            $Tg=1;
                        } elsif ($SP < $SPS) {
                            $Lg=1;
                        }
                    } else {
                        $Lg=1;
                    }
                    if ($SPS > 1) {
                        foreach (2..$SPS) {
                            $_--;
                            if ($L[$_]) {
                                $S .= "$K_I";
                            } else {
                                $S .= "$K_SP";
                            }
                        }
                    }
                    $SP=$space/15;
                    if($SP==1){@L=(); $L[$SP]=1;}else{$L[$SP]=1;}
                    if($Lg){$Line="<tt>$S$K_L</tt><>$Line";}
                    elsif($Tg){$Line="<tt>$S$K_T</tt><>$Line";}
                } else {
                    $Line="<>$Line";
                }
                $RES{$type}="$Line".$RES{$type};
            }
        } else {
            if($tim eq ""){$tim="$TIM";} $tim=sprintf("%011d",$tim);
            if($Res_T==2){$tim=$R{$namber}; $tim=sprintf("%05d",$tim);}
            push(@NEW,"$tim<>$Line"); $SP=0; @L=(); $OyaCount=@NEW;
        }
        $TIM=$tim;
    }
    close(LOG);

if($Res_T){@NEW=sort(@NEW); @NEW=reverse(@NEW);}
@lines=(); $total=@NEW; $NS=$total+$RS;
$PAGE=$FORM{"page"}/$a_max;
&hed_("All Tree / Page: $PAGE");

$page_=int(($total-1)/$a_max);
$end_data=@NEW-1;
$page_end=$page + ($a_max - 1);
if($page_end >= $end_data){$page_end=$end_data;}
$Pg=$page+1; $Pg2=$page_end+1;
$nl=$page_end + 1;
$bl=$page - $a_max;
if($bl >= 0){$Bl="<a href=\"$cgi_f?page=$bl&amp;H=T&amp;$no$pp$Wf\">"; $Ble="</a>";}else{$Bl=""; $Ble="";}
if($page_end ne $end_data){$Nl="<a href=\"$cgi_f?page=$nl&amp;H=T&amp;$no$pp$Wf\">";$Nle="</a>";}else{$Nl=""; $Nle="";}
    $obj_template->process('comtop.inc.tpl');
print <<"_HTML_";
<li>$new_t���Ԉȓ��̋L���� $new_i �ŕ\\������܂��B</li>
<li>$all_i ���N���b�N����Ƃ��̃c���[���ꊇ�ŕ\\�����܂��B</li>
</ul>$Henko<hr>
_HTML_
if($i_mode){&minf_("T");}
if($cou){&con_;}
print"<div class=\"Caption03l\">�S $total �c���[�� $Pg �` $Pg2 �Ԗڂ�\\��</div>\n";
$Plink="<div class=\"Caption01c\"><strong>�S�y�[�W</strong> /\n"; $a=0;
for($i=0;$i<=$page_;$i++){
    $af=$page/$a_max;
    if($i != 0){$Plink.=" ";}
    if($i eq $af){$Plink.="[<strong>$i</strong>]\n";}else{$Plink.="[<a href=\"$cgi_f?page=$a&amp;H=T&amp;$no$pp$Wf\">$i</a>]\n";}
    $a+=$a_max;
}
$Plink.="</div>\n";
if($Res_T==1){$OJ1="<a href=\"$cgi_f?H=T&amp;W=W&amp;$no$pp\">�ԐM�ŐV��</a>"; $OJ2="���e��"; $OJ3="<a href=\"$cgi_f?H=T&amp;W=R&amp;$no$pp\">�L������</a>";}
elsif($Res_T==2){$OJ1="<a href=\"$cgi_f?H=T&amp;W=W&amp;$no$pp\">�ԐM�ŐV��</a>"; $OJ2="<a href=\"$cgi_f?H=T&amp;W=T&amp;$no$pp\">���e��</a>"; $OJ3="�L������";}
else{$OJ1="�ԐM�ŐV��"; $OJ2="<a href=\"$cgi_f?H=T&amp;W=T&amp;$no$pp\">���e��</a>"; $OJ3="<a href=\"$cgi_f?H=T&amp;W=R&amp;$no$pp\">�L������</a>";}
print"<div class=\"Caption01r\">�e�L���̏��� [ $OJ1 / $OJ2 / $OJ3 ]</div>\n";
print"$Plink\n<hr class=\"Hidden\">\n";
foreach ($page .. $page_end) {
    ($T,$namber,$date,$name,$email,$d_may,$comment,$url,
        $space,$end,$type,$del,$ip,$tim,$Se)=split(/<>/,$NEW[$_]);
        $email =~ s/@/$atchange/;
    if(($time_k - $tim) > $new_t*3600){$news="$hed_i";}else{$news="$new_i";}
if((!$name)||($name eq ' ')||($name eq '�@')){$name=$noname;}
    if($email && $Se < 2){$name="$name <a href=\"mailto:$SPAM$email\">$AMark</a>";}
    ($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
    ($ICON,$ICO,$font,$hr)=split(/\|/,$TXT);
    ($txt,$sel,$yobi)=split(/\|\|/,$SEL);
    if(@ico3 && $Icon && ($ICON ne "" || $comment=~/<br>\(�g��\)$/)){
        if($I_Hei_m){$WHm=" width=\"$I_Wid_m\" height=\"$I_Hei_m\"";}
        if($ICON ne ""){if($ICON=~ /m/){$ICON=~ s/m//; $mICO=$mas_m[$ICON];}else{$mICO=$ico3[$ICON];}}
        elsif($Icon && $comment=~/<br>\(�g��\)$/){$mICO="$Ico_km";}
        $news.="<img src=\"$IconDir\/$mICO\" border=\"0\"$WHm>";
    }
    if($ico && $i_mode){$Pr=""; &size(1); $Pr=" "."$Pr";}else{$Pr="";}
    if($d_may eq ""){$d_may="$notitle";}
    if($yobi){$yobi="[ID:$yobi]";}
    if($txt){$Txt="$TXT_T:[$txt]�@";}else{$Txt="";}
    if($sel){$Sel="$SEL_T:[$sel]�@";}else{$Sel="";}
    if($Txt || $Sel ||($Txt && $Sel)){if($TS_Pr==0){$d_may="$Txt$Sel/"."$d_may";}}
    if(length($d_may)>$t_max){$d_may=substr($d_may,0,($t_max-2));$d_may="$d_may.."; }
    $date=substr($date,2,19);
if((!$name)||($name eq ' ')||($name eq '�@')){$name=$noname;}
    print <<"_HTML_";
<br>
<table class="Tree" summary="Tree" cellspacing="0" cellpadding="0" border="0">
<tr><td class="Highlight" width="1\%">
<a href="$cgi_f?mode=all&amp;namber=$namber&amp;type=$type&amp;space=$space&amp;$no$pp">$all_i</a></td>
<td class="Highlight" width="99\%"><a href="$cgi_f?mode=one&amp;namber=$namber&amp;type=$type&amp;space=$space&amp;$no$pp">$news $d_may</a>
/ $name :$date $yobi<span class="ArtId">(#$namber)</span> $Pr
_HTML_

    $res=0;
    @RES= split(/\n/,$RES{$namber});
    foreach $lines(@RES) {
        ($Sen,$rnam,$rd,$rname,$rmail,$rdm,$rcom,$rurl,
            $rsp,$re,$rtype,$del,$ip,$rtim,$M) = split(/<>/,$lines);
        $rmail =~ s/@/$atchange/;
        if($re ne ""){$re="$end_ok";}
        if($namber eq "$rtype"){
            if(($time_k-$rtim)>$new_t*3600){$news="$hed_i";}else{$news="$new_i";}
            if($rmail && $M < 2){$rname="$rname <a href=\"mailto:$SPAM$rmail\">$AMark</a>";}
            $rd=substr($rd,2,19);
            ($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
            ($rICON,$ICO,$font,$hr)=split(/\|/,$TXT);
            ($txt,$sel,$yobi)=split(/\|\|/,$SEL);
            if(@ico3 && $Icon &&($rICON ne "" || $rcom=~/<br>\(�g��\)$/)){
                if($I_Hei_m){$WHm=" width=\"$I_Wid_m\" height=\"$I_Hei_m\"";}
                if($rICON ne ""){if($rICON=~ /m/){$rICON=~ s/m//; $mrICO=$mas_m[$rICON];}else{$mrICO=$ico3[$rICON];}}
                elsif($Icon && $rcom=~/<br>\(�g��\)$/){$mrICO="$Ico_km";}
                $news.="<img src=\"$IconDir\/$mrICO\" border=\"0\"$WHm>";
            }
            if($ico && $i_mode){$Pr=""; &size(1); $Pr=" "."$Pr";}else{$Pr="";}
            if($rdm eq ""){$rdm="$notitle"; }
            if($yobi){$yobi="[ID:$yobi]";}
            if($txt){$Txt="$TXT_T:[$txt]�@";}else{$Txt="";}
            if($sel){$Sel="$SEL_T:[$sel]�@";}else{$Sel="";}
            if($Txt || $Sel ||($Txt && $Sel)){if($TS_Pr==0){$rdm="$Txt$Sel/"."$rdm";}}
            if(length($rdm)>$t_max){$rdm=substr($rdm,0,($t_max-2)); $rdm="$rdm..";}
            print "</td></tr><tr><td></td><td nowrap>\n";
            if($Keisen){print"$Sen";}
            else{
                $rspz=$rsp/15*$zure;
                print "." x $rspz;
            }
            print"<a href=\"$cgi_f?mode=one&amp;namber=$rnam&amp;type=$rtype&amp;space=$rsp&amp;$no$pp\">$news $rdm</a>\n";
if((!$rname)||($rname eq ' ')||($rname eq '�@')){$rname=$noname;}
            print"/ $rname :$rd <span class=\"ArtId\">(#$rnam)</span> $re$Pr\n";
            $res++;
            if($R{$namber}==$res){last;}
        }
    }
    print "</td></tr></table>\n";
}
print "<hr width=\"95%\">\n";
&allfooter("�c���[$a_max");
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [�c���[�ꊇ�\��]
# -> �c���[�̊֘A�L����\������(all_)
#
sub all_ {
@TREE=();
open(DB,"$log");
while ($Line = <DB>) {
    ($nam,$date,$name,$email,$d_may,$comment,$url,
        $sp,$end,$ty,$del,$ip,$tim) = split(/<>/,$Line);
    if(($type==0 && ($nam eq $namber || $ty eq $namber))||($type && ($nam eq $type || $ty eq $type))){
        if($ty){
            if($Keisen){
                $SPS=$sp/15; $Lg=0; $Tg=0; $S="";
                if($SP){
                    if($SP > $SPS){if($L[$SPS]){$Tg=1; $L[$SP]="";}else{$Lg=1; $L[$SP]="";}}
                    elsif($SP==$SPS && $L[$SPS]){$Tg=1;}elsif($SP < $SPS){$Lg=1;}
                }else{$Lg=1;}
                if($SPS > 1){foreach(2..$SPS){$_--; if($L[$_]){$S.="$K_I";}else{$S.="$K_SP";}}}
                $SP=$sp/15;
                if($SP==1){@L=(); $L[$SP]=1;}else{$L[$SP]=1;}
                if($Lg){$Line="<tt>$S$K_L</tt><>$Line";}
                elsif($Tg){$Line="<tt>$S$K_T</tt><>$Line";}
            }else{$Line="<>$Line";}
            if($date){unshift(@TREE,$Line);}
        }else{unshift(@TREE,"<>$Line"); $SP=0; @L=(); if($tim=~/[\d]+/){last;}}
    }
}
close(DB);
&hed_("One Tree All Message");
if($cou){&con_;}
print<<"_ALLTOP_";
<div class="Caption03l">�c���[�ꊇ�\\��$IcCom</div>
<table class="Tree" summary="tree">
<tr><td>
_ALLTOP_

$ALLTREE="";
foreach $line (@TREE) {
    ($Sen,$nam,$date,$name,$email,$d_may,$comment,$url,
        $sp,$end,$ty,$del,$ip,$tim,$Se) = split(/<>/,$line);
    if($end ne ""){$end="$end_ok";}
    if(($ty == 0 && $namber eq "$nam")||($ty != 0 && $namber eq $ty)){
        ($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
        ($ICON,$ICO,$font,$hr)=split(/\|/,$TXT);
        ($txt,$sel,$yobi)=split(/\|\|/,$SEL);
        $n_="";
        $rs=0;$i=0;
        foreach $Line (@TREE) {
            ($S,$n,$d,$na,$e,$dm,$c,$u,$s,$e,$t) = split(/<>/,$Line);
            if($nam eq $n){$i=1;}
            if(($t==0 && $namber eq "$n")||($t != 0 && $namber eq $t)){
                if($rs && $sp eq "$s"){last;}
                $psp=$sp+15;$nsp=$sp-15;
                if($s eq $nsp && $nam > $n && $i != 1){$b_="<a href=\"\#$n\">��[ $n ]</a> / ";}
                if($s eq $psp && $nam < $n && $i == 1){$n_.="<a href=\"\#$n\">��[ $n ]</a>\n";}
            }
        if($i==1){$rs=1;}
        }
        $ResNo=$sp/15;
        &design($nam,$date,$name,$email,$d_may,$comment,$url,$sp,$end,$ty,$del,$Ip,$tim,$ico,
            $Ent,$fimg,$ICON,$ICO,$font,$hr,$txt,$sel,$yobi,$Se,$ResNo,"T2");
        $ALLTREE.="$HTML";
if((!$name)||($name eq ' ')||($name eq '�@')){$name=$noname;}
        $email =~ s/@/$atchange/;
        if($email && $Se < 2){$name="$name <a href=\"mailto:$email\">$AMark</a>";}
        if(($time_k-$tim)>$new_t*3600){$news = "$hed_i";}else{$news="$new_i";}
        if($d_may eq ""){$d_may = "$notitle";}
        $date=substr($date,2,19);
        if($Keisen){print"$Sen";}
        else{

            $spz=$sp/15*$zure;
            print "." x $spz;

        }
        if($yobi){$yobi="[ID:$yobi]";}
        if($txt){$Txt="$TXT_T:[$txt]�@";}else{$Txt="";}
        if($sel){$Sel="$SEL_T:[$sel]�@";}else{$Sel="";}
        if($Txt || $Sel ||($Txt && $Sel)){if($TS_Pr==0){$d_may="$Txt$Sel/"."$d_may";}}
        if(length($d_may)>$t_max){$d_may=substr($d_may,0,($t_max-2));$d_may="$d_may..";}
        if(@ico3 && $Icon && ($ICON ne "" || $comment=~/<br>\(�g��\)$/)){
            if($I_Hei_m){$WHm=" width=\"$I_Wid_m\" height=\"$I_Hei_m\"";}
            if($ICON ne ""){if($ICON=~ /m/){$ICON=~ s/m//; $mICO=$mas_m[$ICON];}else{$mICO=$ico3[$ICON];}}
            elsif($Icon && $comment=~/<br>\(�g��\)$/){$mICO="$Ico_km";}
            $news.="<img src=\"$IconDir\/$mICO\" border=\"0\"$WHm>";
        }
        if($i_mode && $ico){$Pr=""; &size(1); $Pr=" "."$Pr"; $CookOn="";}else{$Pr="";}
if((!$name)||($name eq ' ')||($name eq '�@')){$name=$noname;}
        print"<a href=\"#$nam\">$news $d_may</a>\n";
        print"/$name ($date) $yobi<span class=\"ArtId\">(#$nam)</span> $end$Pr</td></tr><tr><td>\n";
    }
}
print"</td></tr></table><br>\n";
print"$ALLTREE</div>";
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [�V���L���\��]
# -> �V���L����\������(n_w_)
#
sub n_w_ {
@NEW=();
open(DB,"$log");
while (<DB>) {
    ($nam,$date,$name,$email,$d_may,$comment,$url,
        $sp,$end,$ty,$del,$ip,$tim,$Se) = split(/<>/,$_);
    if(($time_k - $tim) <= $new_t*3600){push(@NEW,"$tim<>$_<>");}
}
close(DB);

&hed_("New Message");
$total=@NEW;
$page_=int(($#NEW)/$new_s);
if($FORM{'page'} eq ''){$page=0;}else{$page=$FORM{'page'};}
$end_data=@NEW-1;
$page_end=$page + ($new_s - 1);
if($page_end >= $end_data) { $page_end = $end_data; }
$Pg=$page+1; $Pg2=$page_end+1;
$nl = $page_end + 1;
$bl = $page - $new_s;
if($bl >= 0){$Bl="<a href=\"$cgi_f?page=$bl&amp;mode=n_w&amp;$no$pp\">"; $Ble="</a>";}
if($page_end ne $end_data){$Nl="<a href=\"$cgi_f?page=$nl&amp;mode=n_w&amp;$no$pp\">"; $Nle="</a>";}
print <<"_FTOP_";
<h2>$new_t���Ԉȓ��ɓ��e���ꂽ�V���L��</h2>
<div class="Caption03l">�V���L���S $total ���� $Pg �` $Pg2 �Ԗڂ�\\��</div>
<div class="Caption01c"><strong>�S�y�[�W</strong> / 
_FTOP_

$Plink="$Bl$Ble\n";$a=0;
for($i=0;$i<=$page_;$i++){
    $af=$page/$new_s;
    if($i != 0){$Plink.=" ";}
    if($i eq $af){$Plink.="[<strong>$i</strong>]\n";}else{$Plink.="[<a href=\"$cgi_f?mode=n_w&amp;page=$a&amp;$no$pp\">$i</a>]\n";}

    $a+=$new_s;
}
$Plink.="$Nl$Nle";
if($FORM{"s"} ne ""){$new_su=$FORM{"s"};}
if($new_su){$SL1="�V����"; $SL2="<a href=\"$cgi_f?mode=n_w&amp;s=0&amp;$no$pp\">�Â���</a>";}
else{$SL1="<a href=\"$cgi_f?mode=n_w&amp;s=1&amp;$no$pp\">�V����</a>"; $SL2="�Â���";}
print"$Plink<br>[ $SL1 / $SL2 ]<br>\n</div><hr>\n";
if(@NEW){
    @NEW=sort @NEW;
    if($new_su){@NEW=reverse(@NEW);}
    foreach ($page..$page_end) {
    $divdiv=$page;
        ($Tim,$nam,$date,$name,$email,$d_may,$comment,$url,
            $sp,$end,$ty,$del,$ip,$tim,$Se) = split(/<>/,$NEW[$_]);
        ($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
        ($ICON,$ICO,$font,$hr)=split(/\|/,$TXT);
        ($txt,$sel,$yobi)=split(/\|\|/,$SEL);
        &design($nam,$date,$name,$email,$d_may,$comment,$url,$sp,$end,$ty,$del,$Ip,$tim,$ico,
            $Ent,$fimg,$ICON,$ICO,$font,$hr,$txt,$sel,$yobi,$Se,$ResNo,"N");
        if($divdiv != $page_end){print"$HTML<br>\n<hr>"; $divdiv++;}else{print"$HTML</div><br>\n<hr>"; undef $divdiv;}
    }
    print"<div class=\"Caption01c\"><strong>�S�y�[�W</strong> / ";
    print"$Plink<br></div>\n";
}else{print"�V���L���͂���܂���B</div>\n";}
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [���O�������ݏ���]
# -> ���O�ɋL������������(wri_)
#
sub wri_ {
    if ($s_ret && ($P ne "$s_pas")) {&er_('invpass');}
    if ($KLOG) {&er_('oldlogs');}
    &check_;
    if ($FORM{"PV"} && ($FLAG == 0)) {
        &hed_("Preview","1");
        $c_name=$name; $c_email=$email; $ti=$d_may; $c_txt=$txt; $c_sel=$sel;
        $c_ico=$CICO; $c_hr=$hr; $c_font=$font; $c_key=$delkey;
        $com=$comment; $com=~ s/<br>/\n/g;
        if (($com =~ /^<pre>/) && ($com =~ /<\/pre>$/)) {$Z = " checked"; }
        else {$T = " checked"; }
        $c_url = $url;
        if ($i_mode && ($ResUp || (($ResUp == 0) && ($sp == 0)))) {
            $FORM_E = " enctype=\"multipart/form-data\"";
        } else {$FORM_E = ""; }
        if ($tag) {
            $comment =~ s/\&lt\;/</g;
            $comment =~ s/\&gt\;/>/g;
            $comment =~ s/\&quot\;/\"/g;
            $comment =~ s/<>/\&lt\;\&gt\;/g;
        }
        $comment=~ s/\\t//g;
        $comment .= "\t$userenv";
        &design("",$date,$name,$email,$d_may,$comment,$url,$space,$end,$type,$delkey,$ip,$tim,"",
            "","","",$ICO,$font,$hr,$txt,$sel,$yobi,$send,"","P",$CICO);
        if ($AgSg) {
            if ($FORM{"AgSg"}) {$HTML .= "�L���\\�[�g:�グ��(age)"; }
            else {$HTML .= "�L���\\�[�g:������(sage)"; }
        }
        print<<"_PV_";
<h2>�v���r���[</h2>
$HTML
<form action="$cgi_f" method="$met"$FORM_E>
<input type="submit" value="���M O K" $fm> / <strong>[<a href="#F">��������</a>]</strong>
<br><a name="F"></a>
<h2>�� �������� ��</h2>
_PV_
        &forms_($H);
        &foot_;
    }
    my $obj_captcha = new Forum::Captcha;
    my $aucares = $obj_captcha->check($ccauth, $ccmd5);
    if ($aucares eq 0) {
        &er_('captcha0');
    } elsif ($aucares eq -1) {
        &er_('captcha-1');
    } elsif ($aucares eq -2) {
        &er_('captcha-2');
    } elsif ($aucares eq -3) {
        &er_('captcha-3');
    } elsif ($aucares ne 1) {
        &er_('captchaoth');
    }

if($FORM{'URL'}){
    ($KURL,$Ag) = split(/::/,$FORM{'URL'});
    $comment.="<br>(�g��)";
}
if($UID){
    if($Ag){$pUID=$Ag;}else{&get_("I");}
    if($pUID eq "n"){&er_('cookieoff');}
}
&set_; &cry_;
if($pUID){&set_("I","$pUID");}
if($tag){
    $comment=~ s/\&lt\;/</g;
    $comment=~ s/\&gt\;/>/g;
    $comment=~ s/\&quot\;/\"/g;
    $comment=~ s/<>/\&lt\;\&gt\;/g;
}
if($locks){&lock_("$lockf");}
if($M_Rank){&rank;}
open(LOG,"$log") || &er_("Can't open $log");
@lines = <LOG>;
close(LOG);
$NOWTIME=time; &time_($NOWTIME);
if($bup){&backup_;}
($knum,$kd,$kname,$kem,$ksub,$kcom)=split(/<>/,$lines[0]);
$namber=$knum+1;
if($kd eq "" && $kcom eq ""){shift(@lines);}
if($mas_c){$E=0;}else{$E=1;}
$oya=0; @new=(); $SeMail=""; $WR=0; $R=~ s/:/�F/g; $SIZE=0;
$txt=~ s/\:/�F/g; $sel=~ s/\:/�F/g; $txt=~ s/\|\|/�b�b/g; $sel=~ s/\|\|/�b�b/g; 
if($file){$SIZE+=-s "$i_dir/$file";}
if($o_mail){if($send && $FORM{'pub'}==0){$send=2;}elsif($send==0 && $FORM{'pub'}==0){$send=3;}}
if($smile){&smile_encode($comment);}
$new_="$namber<>$date<>$name<>$email<>$d_may<>$comment\t$userenv<>$url<>$space<>$end<>$type<>$epasswd<>";
$new_.="$Ip:$file:$E:$TL:$ICON\|$ICO\|$font\|$hr\|:$txt\|\|$sel\|\|$pUID\|\|:$R:<>$time_k<>$send<>\n";
#new_ = ���e�f�[�^�A$lines = ���O�A@new=�o�̓f�[�^
$res_process=0; $MAIL_TO="";
if ($res_r==1 && $type != 0) {
    @r_data=();
    foreach (0 .. $#lines) {
        $resres=0;
        ($nam,$d,$na,$mail,$d_m,$com,$u,$s,$e,$ty,$de,$ip,$tim,$sml) = split(/<>/,$lines[$_]);
        $sml=~ s/\n/0/;
        ($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
        ($comment_tmp,$userenv) = split("\t",$com);
 		if($name eq $na && $comment eq $comment_tmp){&er_('twicepost',"1");}
        if(($FORM{'N'} eq $nam)&&(!$res_process)){	push(@r_data,$new_); $oya=1; $resres=1; $res_process=1;}
        if($ty == 0 && $nam eq "$type"){
            if($i_mode && $ico){$SIZE+=-s "$i_dir/$ico";}
            if($sml==2 || $sml==1){if($SeMail !~ /$mail/){$SeMail[$MAIL_TO]=$mail; $MAIL_TO++;}}
#			if($sml==2 || $sml==1){if($SeMail !~ /$mail/){if($q_mail){$SeMail.=" $mail";}else{$SeMail.=",$mail";}}}
            $new_line="$lines[$_]";
            if($he_tp){&cryma_($de); if($ok eq "n"){&er_('notcreator',"1");}}
            if(($nam eq "$kiji" && $oya==0) && $FORM{'N'} eq ""){push(@r_data,$new_); $oya=1;}
            $resres=1; $res_process=1;
            if($FORM{"AgSg"}==0){push(@new,@r_data); push(@new,$new_line);}
        }elsif($ty eq "$type"){
            if($i_mode && $ico){$SIZE+=-s "$i_dir/$ico";}
            if($sml==2 || $sml==1){if($SeMail !~ /$mail/){$SeMail[$MAIL_TO]=$mail; $MAIL_TO++;}}
#			if($sml==2 || $sml==1){if($SeMail !~ /$mail/){if($q_mail){$SeMail.=" $mail";}else{$SeMail.=",$mail";}}}
            if(($nam eq "$kiji" && $oya==0)||($ty eq "$kiji" && $oya==0 && $space > 15) && $FORM{'N'} eq ""){
                push(@r_data,$new_); $oya=1;
            }
            push(@r_data,$lines[$_]);
            if($he_tp){&cryma_($de); if($ok eq "n"){&er_('notcreator',"1");}}
            $resres=1; $res_process=1;
        }
        if($resres == 0){push(@new,$lines[$_]);}
    }
    if($FORM{"AgSg"}){unshift(@new,$new_line); unshift(@new,@r_data);}
}else{
    $h=0; $ON=0; @KLOG=();
    foreach (0 .. $#lines) {
        ($nam,$d,$na,$mail,$d_m,$com,$u,$s,$e,$ty,$de,$ip,$tim,$sml)=split(/<>/,$lines[$_]);
        ($IP,$i,$E)=split(/:/,$ip);
        if($name eq $na && $comment eq $com){ &er_('twicepost',"1"); }
        $sml =~ s/\n/0/;
        if($ty==0){$h++;}
        if($FORM{'N'} eq $nam){push(@new,$new_); $oya=1; if(!$res_process){$res_process=1;}}
        if($nam eq "$kiji" && $FORM{'N'} eq ""){
            if($i_mode && $i){$SIZE+=-s "$i_dir/$i";}
            if($sml==2 || $sml==1){if($SeMail !~ /$mail/){$SeMail[$MAIL_TO]=$mail; $MAIL_TO++;}}
#			if($sml==2 || $sml==1){if($SeMail !~ /$mail/){if($q_mail){$SeMail.=" $mail";}else{$SeMail.=",$mail";}}}
            if(!$res_process){push(@new,$new_);$res_process=1;}
            $oya=1;
        }
        if($ON){
            if($i && -e "$i_dir/$i" && $LogDel){unlink("$i_dir/$i");}
            if($klog_s){unshift(@KLOG,$lines[$_]);}else{if($i_mode==0){last;}}
        }else{push(@new,$lines[$_]);}
        if($h >= $max-1){$ON=1;}
    }
}
if($SIZE && $max_or < int($SIZE/1024)){&er_('uplimit',"1");}
if($type==0 || $oya==0){unshift(@new,$new_);}
elsif($oya){unshift(@new,"$namber<><><><><><><><><>$namber<><><><><>\n");}

open(LOG,">$log") || &er_("Can't write $log","1");
print LOG @new;
close(LOG);
if($i_mode){&get_("M"); &set_("M");}
if($klog_s && @KLOG){&log_;}
if(-e $lockf){rmdir($lockf);}
if($t_mail || $o_mail){&mail_;}
if($H eq "F" && $tpend && $type){$FORM{"namber"}=$type; $space=0; &all2;}
    if ($conf{'rss'} eq 1) {&RSS; }
}
#--------------------------------------------------------------------------------------------------------------------
# [�L���ꊇ�폜]
# -> �L���t�H�[�}�b�g�������Ȃ�(s_d_)
#
sub s_d_ {
    if($s_ret && $P ne "$s_pas"){&er_('invpass');}
    if (Forum->user->validate_password_admin($FORM{'pass'}) == 0) {
        &er_('invpass');
    }
#    if($FORM{'pass'} ne "$pass"){&er_('invpass');}

    open(DB,">$log");
    print DB "";
    close(DB);
    $msg="<h3>�t�H�[�}�b�g����</h3>"; &del_;
}
#--------------------------------------------------------------------------------------------------------------------
# [cookie���s]
# -> cookie�𔭍s����(set_)
#
sub set_ {
    if($_[0] eq "I"){$kday=1826;}else{$kday=30;}
    ($secg,$ming,$hourg,$mdayg,$mong,$yearg,$wdayg,$ydayg,$isdstg) = gmtime(time + $kday*24*60*60);
$yearg += 1900;
if($secg  < 10){$secg ="0$secg"; }
if($ming  < 10){$ming ="0$ming"; }
if($hourg < 10){$hourg="0$hourg";}
if($mdayg < 10){$mdayg="0$mdayg";}
$month = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')[$mong];
$youbi = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')[$wdayg];
$date_gmt = "$youbi, $mdayg\-$month\-$yearg $hourg:$ming:$secg GMT";
if($SEL_C){$Csel=",sel:$sel";}else{$Csel="";}
if($TXT_C){$Ctxt=",txt:$txt";}else{$Ctxt="";}
$cook="name\:$name\,email\:$email\,url\:$url\,delkey\:$delkey\,pub\:$FORM{'pub'}\,ico\:$CICO\,font\:$font\,hr\:$hr$Csel$Ctxt";
if($_[0] eq "P"){print"Set-Cookie: $s_pas=$s_pas; expires=$date_gmt\n";}
elsif($_[0] eq "M"){print"Set-Cookie: Cmin=$FORM{'min'}; expires=$date_gmt\n";}
elsif($_[0] eq "I"){print"Set-Cookie: UID=$_[1]; expires=$date_gmt\n";}
else{print "Set-Cookie: CBBS=$cook; expires=$date_gmt\n";}
}
#--------------------------------------------------------------------------------------------------------------------
# [cookie�擾]
# -> cookie���擾����(get_)
#
sub get_ { 
    $cookies = $ENV{'HTTP_COOKIE'};
    @pairs = split(/;/, $cookies);
    foreach $pair (@pairs) {
        ($NAME, $value) = split(/=/, $pair);
        $NAME =~ s/ //g;
        $DUMMY{$NAME} = $value;
    }
    if ($_[0] eq "P") {
        if ($DUMMY{"$s_pas"}) {$FORM{"P"} = $DUMMY{"$s_pas"}; }
    } elsif ($_[0] eq "M") {
        if ($DUMMY{'Cmin'}) {$FORM{"min"} = $DUMMY{'Cmin'}; }
        else {$FORM{"min"} = 0; }
    } elsif ($_[0] eq "I") {
        if ($DUMMY{'UID'}) {$pUID = $DUMMY{'UID'}; }
        else {$pUID="n"; }
    } else {
        @pairs = split(/,/, $DUMMY{'CBBS'});
        foreach $pair (@pairs) {
            ($name, $value) = split(/:/, $pair);
            $COOKIE{$name} = $value;
        }
        $c_name  = $COOKIE{'name'};
        $c_email = $COOKIE{'email'};
        $c_url   = $COOKIE{'url'};
        $c_key   = $COOKIE{'delkey'};
        $c_pub   = $COOKIE{'pub'};
        $c_ico   = $COOKIE{'ico'};
        $c_font  = $COOKIE{'font'};
        $c_hr    = $COOKIE{'hr'};
        if ($SEL_C) {$c_sel = $COOKIE{'sel'}; }
        if ($TXT_C) {$c_txt = $COOKIE{'txt'}; }
    }
}
#--------------------------------------------------------------------------------------------------------------------
# [���Ԑݒ�]
# -> ���Ԃ�ݒ肷��(time_)
#
sub time_ {
    $ENV{'TZ'} = "JST-9";
    if ($_[0]) {$time_k = $_[0]; }
    else {$time_k = time; }
    ($sec, $min, $hour, $mday, $mon, $year, $wday) = localtime($time_k);
    $year += 1900;
    $mon++;
    if ($mon  < 10) {$mon  = "0$mon"; }
    if ($mday < 10) {$mday = "0$mday";}
    if ($hour < 10) {$hour = "0$hour";}
    if ($min  < 10) {$min  = "0$min"; }
    if ($sec  < 10) {$sec  = "0$sec"; }
    $week = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat') [$wday];
    $date = "$year\/$mon\/$mday\($week\) $hour\:$min\:$sec";
}
#--------------------------------------------------------------------------------------------------------------------
# [�Ǘ��p�y�[�W]
# -> �Ǘ����[�h��\������(del_)
#
sub del_ {
    if (Forum->user->validate_password_admin($FORM{'pass'}) == 0) {
        &er_('invpass');
    }
#if($FORM{'pass'} ne "$pass"){ &er_('invpass'); }
&hed_("Editor");
@NEW=(); $RES=(); $FSize=0; $RS=0; @lines=(); %R=();
open(DB,"$log");
while ($Line=<DB>) {
    if($FORM{"mode2"} eq "Backup"){push(@lines,$Line);}
    ($namber,$date,$name,$email,$d_may,$comment,$url,
        $space,$end,$type,$delk,$ip,$tim) = split(/<>/,$Line);
    ($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
    if($i_mode && $ico){$FSize+= -s "$i_dir/$ico";}
    if($type){
        if($Keisen){
            $SPS=$space/15; $Lg=0; $Tg=0; $S="";
            if($SP){
                if($SP > $SPS){if($L[$SPS]){$Tg=1; $L[$SP]="";}else{$Lg=1; $L[$SP]="";}}
                elsif($SP==$SPS && $L[$SPS]){$Tg=1;}elsif($SP < $SPS){$Lg=1;}
            }else{$Lg=1;}
            if($SPS > 1){foreach(2..$SPS){$_--; if($L[$_]){$S.="$K_I";}else{$S.="$K_SP";}}}
            $SP=$space/15;
            if($SP==1){@L=(); $L[$SP]=1;}else{$L[$SP]=1;}
            if($Lg){$Line="<tt>$S$K_L</tt><>".$Line;}
            elsif($Tg){$Line="<tt>$S$K_T</tt><>".$Line;}
        }else{$Line="0<>$Line";}
        if($date){$R{$type}="$Line".$R{$type}; $RS++;}
    }else{push(@NEW,$Line); $SP=0; @L=();}
}
close(DB);
if($FORM{"mode2"} eq "Backup"){&backup_; $msg="<h3>�o�b�N�A�b�v����</h3>"; @lines=();}
elsif($FORM{"mode2"} =~/\d/){
    open(NO,">$c_f") || &er_("Can't write $c_f","1");
    print NO $FORM{"mode2"};
    close(NO);
    $msg="<h3>�J�E���^�l�ҏW����</h3>";
}elsif($FORM{"mode2"} eq "LockOff"){
    $msg="<h3>���b�N��������</h3>";
    if(-e $lockf){rmdir($lockf); $msg.="($lockf����)";}else{$msg.="($lockf����)";}
    if(-e $cloc){rmdir($cloc);   $msg.="($cloc����)"; }else{$msg.="($cloc����)";}
}
$total=@NEW; $NS=$RS+$total;
$page_=int(($total-1)/$a_max);
if(-s $log){$l_size=int((-s $log)/1024);}else{$l_size=0;}
if($topok==0){$NewMsg="<li><a href=\"$cgi_f?mode=new&amp;$no&amp;pass=$FORM{'pass'}$pp\">�Ǘ��p�V�K�쐬</a>\n";}
if($i_mode || $mas_c){
    if($FSize){$FSize=int($FSize/1024); $FileSize="<br>�A�b�v�t�@�C�����v�T�C�Y�F$FSize\KB";}else{$FSize=0;}
    $FP ="<form action=\"$cgi_f\" method=\"$met\"$TGT>\n";
    $FP.="<strong>[�摜/�L���\\������]</strong><br><input type=\"hidden\" name=\"mode\" value=\"ent\">$nf$pf\n";
    $FP.="<input type=\"hidden\" name=\"pass\" value=\"$FORM{'pass'}\"><input type=\"submit\" value=\"�\\�����V�X�e��\"></form>\n";
}
if($bup){$BUL="/�o�b�N�A�b�v";}
print <<"_HTML_";
<h2>�Ǘ����[�h</h2>
<ul>
<li>���݂̃��O�̃T�C�Y�F$l_size\KB�@�L�����F$NS(�e/$total �ԐM/$RS)$FileSize</li>
<li>�L����ҏW�������ꍇ�A���̋L���̃^�C�g�����N���b�N�B</li>
<li>�폜�������L���Ƀ`�F�b�N�����u�폜�v�{�^���������ĉ������B</li>
<li>�L��No�̉���IP�A�h���X���N���b�N����Ɣr��IP���[�h�֏��𑗂�܂��B</li>
<li>�c���[�폜������ƃc���[���Ռ`�����������܂��B</li>
<li>�L���폜�́A���̋L���ɑ΂���ԐM���Ȃ��ꍇ�͊��S�폜�ɂȂ�܂��B<br>
���̋L���ɑ΂���ԐM������ꍇ�͊��S�ɍ폜���ꂸ�폜�L���ɂȂ�܂��B</li>
<li>�폜�L���́u�L�����S�폜�v���`�F�b�N����Ɗ��S�ɏ����܂��B</li>
<li><a href="#FMT">���b�N����/���O������/�t���[�t�H�[���C��/���O�R���o�[�g$BUL</a>
$NewMsg</li>
</ul>
<form action="$cgi_f" method="$met"$TGT>$nf$pf
<input type="hidden" name="mode" value="Den"><input type="hidden" name="pass" value="$FORM{'pass'}">
<strong>[�r��IP/�֎~�����ǉ�]</strong><br>
_HTML_
print '<input type="submit" value="�r���ݒ�ǉ�"></form>';
print "$FP";
if($cou){
    open(NO,"$c_f") || &er_("Can't open $c_f");
    $cnt = <NO>;
    close(NO);
    print <<"_BUP_";
<form action="$cgi_f" method=$met>$nf$pf
<input type="hidden" name="mode" value="del"><input type="hidden" name="pass" value="$FORM{'pass'}">
<strong>[�J�E���^�l�ҏW]</strong><br>
_BUP_
print '�J�E���g��/<input type="text" name="mode2" value="' . $cnt . '" size="7"><input type="submit" value="�ҏW" ' . "\"></form>\n";
}
print <<"_HTML_";
$msg
<form action=\"$cgi_f\" method="$met">$nf$pf
<input type="hidden" name="mode" value="key"><input type="hidden" name="mo" value="1">
<input type="hidden" name="pass" value="$FORM{'pass'}"><input type="hidden" name="page" value="$FORM{"page"}">
<hr>
_HTML_
if($FORM{'page'} eq ''){$page=0;}else{$page=$FORM{'page'};}
$end_data=@NEW - 1;
$page_end=$page + ($a_max - 1);
if($page_end >= $end_data){$page_end=$end_data;}
$nl=$page_end + 1;
$bl=$page - $a_max;
if($bl >= 0){$Bl="<a href=\"$cgi_f?mode=del&amp;page=$bl&amp;pass=$FORM{'pass'}&amp;$no$pp\">"; $Ble="</a>";}
if($page_end ne $end_data){$Nl="<a href=\"$cgi_f?mode=del&amp;page=$nl&amp;pass=$FORM{'pass'}&amp;$no$pp\">"; $Nle="</a>";}
$Plink="<div class=\"Caption01c\"><strong>�S�y�[�W</strong> $Bl$Ble /\n\n";
$a=0;
for($i=0;$i<=$page_;$i++){
    $af=$page/$a_max;
    if($i != 0){$Plink.=" ";}
    if($i eq $af){$Plink.="[<strong>$i</strong>]\n";}else{$Plink.="[<a href=\"$cgi_f?page=$a&amp;mode=del&amp;pass=$FORM{'pass'}&amp;$no$pp\">$i</a>]\n";}
    $a+=$a_max;
}
$Plink.="$Nl$Nle\n</div>";
print"$Plink\n";

#test
foreach ($page .. $page_end) {
    ($namber,$date,$name,$email,$d_may,$comment,$url,
        $space,$end,$type,$delkey,$Ip) = split(/<>/,$NEW[$_]);
    ($ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$Ip);
    ($txt,$sel,$yobi)=split(/\|\|/,$SEL);
    if($ico){$ico=" [File:<a href=\"$i_Url\/$ico\"$TGT>$ico</a>]";}
if((!$name)||($name eq ' ')||($name eq '�@')){$name=$noname;}
    if($email ne ""){$name = "<a href=\"mailto:$email\">$name</a>";}
    if($d_may eq ""){$d_may= "$notitle";}
    if($yobi){$yobi=" [ID:$yobi]";}
    if(length($d_may)>$t_max){$d_may=substr($d_may,0,($t_max-2));$d_may="$d_may..";}
    $date=substr($date,2,19);
print '<table class="Tree" summary="Tree" cellspacing="0" cellpadding="0" border="0">';
print '<tr><td><input type="radio" name="kiji" value="';
print $namber;
print '>�c���[�폜</td><td class="Highlight">' . "\n" . '<input type="checkbox" name="del" value="' . "$namber\">\n";
    print <<"_HTML_";
<a href="$cgi_f?mode=nam&amp;pass=$FORM{'pass'}&amp;kiji=$namber&amp;mo=1&amp;$no$pp">$d_may</a>
/ $name :$date <span class="ArtId">(#$namber)</span>
[<a href="$cgi_f?mode=Den&amp;pass=$FORM{"pass"}&amp;mo=$ip"$TGT>$ip</a>]$ico
</td></tr>
_HTML_

##H=T
#foreach ($page .. $page_end) {
#	($T,$namber,$date,$name,$email,$d_may,$comment,$url,
#		$space,$end,$type,$del,$ip,$tim,$Se)=split(/<>/,$NEW[$_]);
#	if(($time_k - $tim) > $new_t*3600){$news="$hed_i";}else{$news="$new_i";}
#if((!$name)||($name eq ' ')||($name eq '�@')){$name=$noname;}
#	if($email && $Se < 2){$name="$name <a href=\"mailto:$SPAM$email\">$AMark</a>";}
#	($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
#	($ICON,$ICO,$font,$hr)=split(/\|/,$TXT);
#	($txt,$sel,$yobi)=split(/\|\|/,$SEL);
#	if(@ico3 && $Icon && ($ICON ne "" || $comment=~/<br>\(�g��\)$/)){
#		if($I_Hei_m){$WHm=" width=\"$I_Wid_m\" height=\"$I_Hei_m\"";}
#		if($ICON ne ""){if($ICON=~ /m/){$ICON=~ s/m//; $mICO=$mas_m[$ICON];}else{$mICO=$ico3[$ICON];}}
#		elsif($Icon && $comment=~/<br>\(�g��\)$/){$mICO="$Ico_km";}
#		$news.="<img src=\"$IconDir\/$mICO\" border=\"0\"$WHm>";
#	}
#	if($ico && $i_mode){$Pr=""; &size(1); $Pr=" "."$Pr";}else{$Pr="";}
#	if($d_may eq ""){$d_may="$notitle";}
#	if($yobi){$yobi="[ID:$yobi]";}
#	if($txt){$Txt="$TXT_T:[$txt]�@";}else{$Txt="";}
#	if($sel){$Sel="$SEL_T:[$sel]�@";}else{$Sel="";}
#	if($Txt || $Sel ||($Txt && $Sel)){if($TS_Pr==0){$d_may="$Txt$Sel/"."$d_may";}}
#	if(length($d_may)>$t_max){$d_may=substr($d_may,0,($t_max-2));$d_may="$d_may.."; }
#	$date=substr($date,2,19);
#if((!$name)||($name eq ' ')||($name eq '�@')){$name=$noname;}
#	print <<"_HTML_";
#<br>
#<table class="Tree" summary="Tree" cellspacing="0" cellpadding="0" border="0">
#<tr><td class="Highlight" width="1\%">
#<a href="$cgi_f?mode=all&amp;namber=$namber&amp;type=$type&amp;space=$space&amp;$no$pp">$all_i</a></td>
#<td class="Highlight" width="99\%"><a href="$cgi_f?mode=one&amp;namber=$namber&amp;type=$type&amp;space=$space&amp;$no$pp">$news $d_may</a>
#/ $name :$date $yobi<span class="ArtId">(#$namber)</span> $Pr
#_HTML_

#---kanri
#foreach ($page .. $page_end) {
#	($namber,$date,$name,$email,$d_may,$comment,$url,
#		$space,$end,$type,$delkey,$Ip) = split(/<>/,$NEW[$_]);
#	($ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$Ip);
#	($txt,$sel,$yobi)=split(/\|\|/,$SEL);
#	if($ico){$ico=" [File:<a href=\"$i_Url\/$ico\"$TGT>$ico</a>]";}
#if((!$name)||($name eq ' ')||($name eq '�@')){$name=$noname;}
#	if($email ne ""){$name = "<a href=\"mailto:$email\">$name</a>";}
#	if($d_may eq ""){$d_may= "$notitle";}
#	if($yobi){$yobi=" [ID:$yobi]";}
#	if(length($d_may)>$t_max){$d_may=substr($d_may,0,($t_max-2));$d_may="$d_may..";}
#	$date=substr($date,2,19);
#print '<input type="radio" name="kiji" value="' . $namber . '" ';
#print '>�c���[�폜<br><input type="checkbox" name="del" value="' . "$namber\">\n";
#	print <<"_HTML_";
#<a href="$cgi_f?mode=nam&amp;pass=$FORM{'pass'}&amp;kiji=$namber&amp;mo=1&amp;$no$pp">$d_may</a>
#/ $name :$date <span class="ArtId">(#$namber)</span>
#[<a href="$cgi_f?mode=Den&amp;pass=$FORM{"pass"}&amp;mo=$ip"$TGT>$ip</a>]$ico</small><br>
#_HTML_

##test
    $res=0;
    @RES=split(/\n/,$R{$namber});
    foreach $lines(@RES) {
        ($Sen,$rnam,$rd,$rname,$rmail,$rdm,$rcom,$rurl,
            $rsp,$re,$rtype,$rde,$rIp,$tim,$Se) = split(/<>/,$lines);
        ($rip,$ico,$Ent,$fimg,$TXT,$rSEL,$R)=split(/:/,$rIp);
        ($txt,$sel,$ryobi)=split(/\|\|/,$rSEL);
        if ($namber eq "$rtype"){
            if($rmail){$rname="<a href=\"mailto:$rmail\">$rname</a>";}
            if($rd_may eq ""){$rd_may="$notitle";}
            if(length($rdm)>$t_max){$rdm=substr($rdm,0,($t_max-2));$rdm="$rdm..";}
            $rd=substr($rd,2,19); if($re){$re="$end_ok";}
            if($ico){$ico=" [File:<a href='$i_Url\/$ico'$TGT>$ico</a>]";}
            if($ryobi){$ryobi=" [ID:$ryobi]";}
            print "<tr><td></td><td>\n";
            if($Keisen){print"$Sen";}
            else{
                $rspz=$rsp/15*$zure;
                print "." x $rspz;
            }
#			print"<a href=\"$cgi_f?mode=one&amp;namber=$rnam&amp;type=$rtype&amp;space=$rsp&amp;$no$pp\">$news $rdm</a>\n";
if((!$rname)||($rname eq ' ')||($rname eq '�@')){$rname=$noname;}
            $res++;
            if($R{$namber}==$res){last;}
#	print "</td></tr></table>\n";

#---H=T

#	$res=0;
#	@RES= split(/\n/,$RES{$namber});
#	foreach $lines(@RES) {
#		($Sen,$rnam,$rd,$rname,$rmail,$rdm,$rcom,$rurl,
#			$rsp,$re,$rtype,$del,$ip,$rtim,$M) = split(/<>/,$lines);
#		if($re ne ""){$re="$end_ok";}
#		if($namber eq "$rtype"){
#			if(($time_k-$rtim)>$new_t*3600){$news="$hed_i";}else{$news="$new_i";}
#			if($rmail && $M < 2){$rname="$rname <a href=\"mailto:$SPAM$rmail\">$AMark</a>";}
#			$rd=substr($rd,2,19);
#			($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
#			($rICON,$ICO,$font,$hr)=split(/\|/,$TXT);
#			($txt,$sel,$yobi)=split(/\|\|/,$SEL);
#			if(@ico3 && $Icon &&($rICON ne "" || $rcom=~/<br>\(�g��\)$/)){
#				if($I_Hei_m){$WHm=" width=\"$I_Wid_m\" height=\"$I_Hei_m\"";}
#				if($rICON ne ""){if($rICON=~ /m/){$rICON=~ s/m//; $mrICO=$mas_m[$rICON];}else{$mrICO=$ico3[$rICON];}}
#				elsif($Icon && $rcom=~/<br>\(�g��\)$/){$mrICO="$Ico_km";}
#				$news.="<img src=\"$IconDir\/$mrICO\" border=\"0\"$WHm>";
#			}
#			if($ico && $i_mode){$Pr=""; &size(1); $Pr=" "."$Pr";}else{$Pr="";}
#			if($rdm eq ""){$rdm="$notitle"; }
#			if($yobi){$yobi="[ID:$yobi]";}
#			if($txt){$Txt="$TXT_T:[$txt]�@";}else{$Txt="";}
#			if($sel){$Sel="$SEL_T:[$sel]�@";}else{$Sel="";}
#			if($Txt || $Sel ||($Txt && $Sel)){if($TS_Pr==0){$rdm="$Txt$Sel/"."$rdm";}}
#			if(length($rdm)>$t_max){$rdm=substr($rdm,0,($t_max-2)); $rdm="$rdm..";}
#			print "</td></tr><tr><td></td><td nowrap>\n";
#			if($Keisen){print"$Sen";}
#			else{
#				$rspz=$rsp/15*$zure;
#				print "." x $rspz;
#			}
#			print"<a href=\"$cgi_f?mode=one&amp;namber=$rnam&amp;type=$rtype&amp;space=$rsp&amp;$no$pp\">$news $rdm</a>\n";
#if((!$rname)||($rname eq ' ')||($rname eq '�@')){$rname=$noname;}
#			print"/ $rname :$rd <span class=\"ArtId\">(#$rnam)</span> $re$Pr\n";
#			$res++;
#			if($R{$namber}==$res){last;}
#		}
#	}
#	print "</td></tr></table>\n";
#}

#---kanri
#	@RES=split(/\n/,$R{$namber});
#	foreach $lines(@RES) {
#		($Sen,$rnam,$rd,$rname,$rmail,$rdm,$rcom,$rurl,
#			$rsp,$re,$rtype,$rde,$rIp,$tim,$Se) = split(/<>/,$lines);
#		($rip,$ico,$Ent,$fimg,$TXT,$rSEL,$R)=split(/:/,$rIp);
#		($txt,$sel,$ryobi)=split(/\|\|/,$rSEL);
#		if ($namber eq "$rtype"){
#			if($rmail){$rname="<a href=\"mailto:$rmail\">$rname</a>";}
#			if($rd_may eq ""){$rd_may="$notitle";}
#			if(length($rdm)>$t_max){$rdm=substr($rdm,0,($t_max-2));$rdm="$rdm..";}
#			$rd=substr($rd,2,19); if($re){$re="$end_ok";}
#			if($ico){$ico=" [File:<a href='$i_Url\/$ico'$TGT>$ico</a>]";}
#			if($ryobi){$ryobi=" [ID:$ryobi]";}
#			if($Keisen){print"$Sen";}
#			else{
#				$rspz=$rsp/15*$zure;
#				print "." x $rspz;
#			}
#if((!$rname)||($rname eq ' ')||($rname eq '�@')){$rname=$noname;}
#}
            print <<"_HTML_";
<input type="checkbox" name="del" value="$rnam">
<a href="$cgi_f?mode=nam&amp;pass=$FORM{'pass'}&amp;kiji=$rnam&amp;mo=1&amp;no=$no$pp">$rdm</a>
/ $rname :$rd $ryobi <span class="ArtId">(#$rnam)</span>
[<a href="$cgi_f?mode=Den&amp;pass=$FORM{"pass"}&amp;mo=$rip"$TGT>$rip</a>]$ico $re</td></tr>
_HTML_
            }

        }
        print "</table><br>\n";
#	print"<hr width=\"90\%\">";
    }

    $tmplVars{'Bl'} = $Bl;
    $tmplVars{'a_max'} = $a_max;
    $tmplVars{'Ble'} = $Ble;
    $tmplVars{'Nl'} = $Nl;
    $tmplVars{'Nle'} = $Nle;
    $tmplVars{'Plink'} = $Plink;
    $tmplVars{'ttb'} = $ttb;
    $tmplVars{'cgi_f'} = $cgi_f;
    $tmplVars{'met'} = $met;
    $tmplVars{'FORM'} = \%FORM;
    $tmplVars{'no'} = $no;
    $tmplVars{'pp'} = $pp;
    if ( -e $lockf ) {$tmplVars{'lockf'} = $lockf; }
    if ( -e $cloc ) {$tmplVars{'cloc'} = $cloc; }
    $tmplVars{'log'} = $log;
    $tmplVars{'bup'} = $bup;
    if ($bup) {
        if ( -e $bup_f ) {
            $tmplVars{'bup_f'} = $bup_f;
            $bl = ( -M $bup_f );
            $tmplVars{'bh'} = sprintf("%.1f", 24 * $bl);
            $tmplVars{'bl'} = sprintf("%.2f", $bl);
            $tmplVars{'bs'} = int(( -s $bup_f ) / 1024);
            $Nb = $bup - $bl;
            $tmplVars{'Nh'} = sprintf("%.1f", $Nb * 24);
        }
        $tmplVars{'met'} = $met;
        $tmplVars{'nf'} = $nf;
        $tmplVars{'pf'} = $pf;
        $tmplVars{'bc'} = $bc;
        $tmplVars{'Nb'} = $Nb;
        $tmplVars{'Nh'} = $Nh;
    }

    print '</ul><input type="checkbox" name="kiji" value="A" ' . "\">�L�����S�폜<br>\n";
    print '<input type="submit" value=" �� �� " ' . "\">\n";
    print '<input type="reset" value="���Z�b�g" ' . "\"></form>\n";
    print "<strong>";
    if($Bl){print"<div class=\"Caption01r\">[ $Bl�O�̕ԐM$a_max��$Ble ]\n";}
    if($Nl){if($Bl){print"| ";}else{print "<div class=\"Caption01r\">";} print"[ $Nl���̕ԐM$a_max��$Nle ]\n</div>\n";}else{print "</div>";}
    print <<"_HTML_";
</strong><br>$Plink
<SCRIPT language="JavaScript">
<!--
function Link(url) {
    if(confirm("�{���Ɏ��s���Ă�OK�ł���?\\n(���s����Ɠ��e�͌��ɖ߂��܂���!)")){location.href=url;}
    else{location.href="#FMT";}
}
//-->
</SCRIPT>
<a name="FMT"><hr width="95\%"></a>
*JavaScript �� ON�ɂ��Ă�������*
<table summary="lock" border="1" bordercolor="$ttb" width="90\%">
<tr><td colspan="2"><form action="$cgi_f" method="$met"><strong>[���b�N�t�@�C���̉���(�폜)]</strong><ul>
<input type="button" value="���b�N����" onClick="Link('$cgi_f?mode=del&amp;pass=$FORM{"pass"}&amp;mode2=LockOff&amp;$no$pp')">
<li>���b�N�t�@�C�����ǂ����Ă��폜����Ȃ��ꍇ�Ɏ����Ă��������B��肪�����ꍇ�͂��܂�g��Ȃ��ŉ�����<ul>
_HTML_
    if(-e $lockf){print"<li>���C�����O($lockf):���b�N��\n";}
    if(-e $cloc){print"<li>�J�E���^���O($cloc):���b�N��\n";}
    print<<"_HTML_";
</ul><li>���b�N���̃��O�������Ă��A���[�U�����쒆�̏ꍇ������܂��B���΂炭�l�q�����Ď��s���Ă��������B
</ul></form></td></tr>
<tr valign="top"><td>
<form action="$cgi_f" method="$met">
<strong>[���O�t�H�[�}�b�g(������)]</strong>
<ul><input type="button" value="�t�H�[�}�b�g" onClick="Link('$cgi_f?mode=s_d&amp;pass=$FORM{"pass"}&amp;$no$pp')"><br>
<li>�t�@�C���A�b�v�@�\\��ON�̏ꍇ�A�\\�������[�h�Ńt�@�C�������ׂč폜���s�Ȃ��Ă�������!
</ul></form>
</td><td>
<form action="$cgi_f" method="$met">
<strong>[�t���[�t�H�[���C��]</strong>
<ul><input type="button" value="�C������" onClick="Link('$cgi_f?mode=ffs&amp;mo=1&amp;pass=$FORM{"pass"}&amp;$no$pp')"><br>
<li>�����R�[�h��̕s��C�����܂��B�����������N�����ꍇ�͕ҏW�ŏC�����Ă��������B<br>
<li>�O�̂��߃o�b�N�A�b�v������Ă������Ƃ������߂��܂�(v7.0��������t���[�t�H�[�����g�p\���Ă���ꍇ)
</ul></form>
</td></tr><tr valign="top"><td>
<form action="$cgi_f" method="$met">
<strong>[���O�R���o�[�g]</strong>
<ul><input type="button" value="I-BOARD" onClick="Link('$cgi_f?mode=ffs&amp;mo=I-BOARD&amp;pass=$FORM{"pass"}&amp;$no$pp')"> /
<input type="button" value="UPP-BOARD" onClick="Link('$cgi_f?mode=ffs&amp;mo=UPP-BOARD&amp;pass=$FORM{"pass"}&amp;$no$pp')"><br>
<li>I-BOARD�V���[�Y �������� UPP-BOARD �̃��O�� ChildTree �p�ɃR���o�[�g���܂��B<br>
<li>�R���o�[�g����ƌ��ɖ߂��̂͑�ςȂ̂Œ���! �{�^�����ԈႦ�Ȃ���!<br>
<li>�L���͂��ׂĐV���L�������ƂȂ�܂��B<br>
<li>�R���o�[�g�Ώۃ��O:[$log]<br>
</ul></form>
</td><td>
_HTML_
    if($bup) {
        if(-e $bup_f){
            $bl=(-M $bup_f); $bh=sprintf("%.1f",24*$bl); $bl=sprintf("%.2f",$bl); $bs=int((-s $bup_f)/1024);
            $bc="����($bs\KB / $bl��(��$bh����)�O)"; $Nb=$bup-$bl; $Nh=sprintf("%.1f",$Nb*24);
        } else {$bc="����";}
        print <<"_BUP_";
<form action="$cgi_f" method="$met">$nf$pf
<input type="hidden" name="mode" value="del"><input type="hidden" name="pass" value="$FORM{'pass'}">
<strong>[�o�b�N�A�b�v]</strong>
<ul><input type="button" value="���O���C��" onClick="Link('$cgi_f?mode=bma&amp;pass=$FORM{"pass"}&amp;$no$pp')">
/ <input type="submit" value="Backup" name="mode2"><br>
<li>[Backup]�{�^�����N���b�N����ƌ��݂̃��O���o�b�N�A�b�v���܂��B
<li>�o�b�N�A�b�v�@\�\\���g�p���Ă���l�̂ݏC���\\�ł��B<br>
<li>�o�b�N�A�b�v$bc
<li>���̃o�b�N�A�b�v�� $Nb��(��$Nh����)��
</ul></form>
_BUP_
    }
    print"</td></tr></table>\n";
    &foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [�L���ҏW]
# -> �L���ҏW�̃t�H�[�����o��(hen_)
#
sub hen_ {
    if ($KLOG) {&er_('oldlogs'); }
    if ($mo eq "") {
#        if ($FORM{'del'} eq "") {&er_('invid'); }
#        if ($delkey eq "") {&er_('invpass'); }
#        $kiji = $FORM{'del'};
        &er_('edit_not_allowed');
    } elsif ($mo == 1) {
        if (Forum->user->validate_password_admin($FORM{'pass'}) == 0) {
            &er_('invpass');
        }
#        if ($FORM{'pass'} ne "$pass") {&er_('invpass'); }
    }
    open(DB,"$log");
    while ($line=<DB>) {
        ($namber,$d,$name,$email,$d_may,$comment,$url,
            $s,$end,$t,$de,$i,$ti,$sml) = split(/<>/,$line);
        ($comment,$userenv) = split("\t",$comment);
        if($d eq ""){next;}
        if($kiji eq "$namber"){
            if($mo eq ""){
                if($de eq "") { &er_('nopass'); }
                &cryma_($de);
                if (Forum->user->validate_password_admin($delkey) != 0) {
                    $ok = 'm';
                }
#                if($delkey eq "$pass"){$ok="m";}
                if($ok eq "n"){ &er_('invpass'); }
                $hen_l = "$cgi_f?$no$pp";
                $Lcom = "";
            } else {
                $hen_l = "$cgi_f?mode=del&amp;pass=$FORM{'pass'}&amp;$no$pp";
                $Lcom = "�Ǘ����[�h��";
            }
            if ($s && $end_f && (($end_c == 0) ||
                 (Forum->user->validate_password_admin($FORM{'pass'}) != 0)) &&
                $t) {
#            if ($s && $end_f && (($end_c == 0) || ($FORM{'pass'} eq $pass)) && $t) {
                if ($end) {$C = " checked"; }
                $end_form = <<"_ENDBOX_";
$end_ok BOX
<input type="checkbox" name="end" value="1" $C>
$end_m
_ENDBOX_
            }
            if ($FORM{'pass'} eq "") {$FORM{'pass'} = $delkey; }
            &hed_("Message Edit");
            $comment =~ s/<br>/\n/g;
            if (($comment =~ /<pre>/) && ($comment =~ /<\/pre>$/)) {
                $Z = " checked";
                $comment =~ s/<pre>//g;
                $comment =~ s/<\/pre>//g;
            } else {
                $T = " checked";
            }
            if ($o_mail) {
                if (($sml == 1) || ($sml == 2)) {$Y = " selected"; }
                if ($sml < 2) {$Pch = " selected"; }
                $Mbox= <<_MAIL_;
<tr><td colspan="2">
 *�֘A���郌�X�L�������[���Ŏ�M���܂���? <select name="send">
<option value="1"$Y>�͂�
<option value="0">������
</select> 
 �A�h���X <select name="pub">
<option value="0">��\\��
<option value="1"$Pch>�\\��
</select></td></tr>
_MAIL_
            }
            if ($tag) {
                $comment =~ s/</\&lt\;/g;
                $comment =~ s/>/\&gt\;/g;
            }
            ($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R) = split(/:/,$i);
            print <<"_HTML_";
<h2>�L��No[$namber] �̕ҏW</h2>
$msg
<form action="$cgi_f" method="$met" name="post">$nf$pf
<input type="hidden" name="pass" value="$FORM{'pass'}">
<input type="hidden" name="mode" value="h_w">
<input type="hidden" name="namber" value="$namber"><input type="hidden" name="mo" value="$mo">
<table class="Submittion" summary="form">
<tr><td><strong>�����O</strong></td><td>
<input type="text" name="name" value="$name" size="20" maxlength="100"></td></tr>
<tr><td><strong>E ���[��</strong></td><td>
<input type="text" name="email" value="$email" size="40" maxlength="100"></td></tr>
$Mbox
_HTML_
            if ($ua_select) {
                if (Forum->user->validate_password_admin($FORM{'pass'}) != 0) {
#                if ($FORM{'pass'} eq "$pass") {
                    if ($userenv) {
                        print "<input type=\"hidden\" value=\"$userenv\">";
                    }
                } else {
                    &UAsel;
                }
            }
            print "<tr><td><strong>�^�C�g��</strong></td><td>";
            print "<input type=\"text\" name=\"d_may$actime\" size=\"40\" value=\"$d_may\" maxlength=\"100\"></td></tr>";
            print "<tr><td><strong>URL</strong></td><td><input type=\"text\" name=\"url\" value=\"http://$url\" size=\"60\" maxlength=\"100\"></td></tr>";
            print "<tr><td colspan=\"2\"><strong>�R�����g</strong>";
            print "�ʏ탂�[�h/<input type=\"radio\" name=\"pre\" value=\"0\" $T>";
            print "�}�\\���[�h/<input type=\"radio\" name=\"pre\" value=\"1\" $Z>";
            $com=$comment;
            &smile_decode($com);

            print '(�K���ɉ��s�����ĉ�����)<br>' . "\n" . '<textarea name="comment" rows="15" cols="80" ';
            if ($BBFACE) {
                print ' onselect="storeCaret(this);" onclick="storeCaret(this);" onkeyup="storeCaret(this);"';
            }
            print ">$com</textarea></td></tr>";
            if ($BBFACE) {print "$BBFACE"; }

            ($ICON,$ICO,$font,$hr)=split(/\|/,$TXT);
            ($txt,$sel,$yobi)=split(/\|\|/,$SEL);
            if($font){
                print "<tr><td>�����F</td><td>\n";
                foreach (0 .. $#fonts) {
                    if($font eq ""){$font="$fonts[0]";}
                    print"<input type=\"radio\" name=\"font\" value=\"";
                    if($font eq "$fonts[$_]"){print"$fonts[$_]\" checked><span class=\"col_$fonts[$_]\">��</span>\n";}
                    else{print"$fonts[$_]\"><span class=\"col_$fonts[$_]\">��</span>\n";}
                }
                print"</td></tr>";
            }
            if($hr){
                print"<tr><td>�g���F</td><td>\n";
                foreach (0 .. $#hr) {
                    if($hr eq ""){$cr="$hr[0]";}
                    print "<input type=\"radio\" name=\"hr\" value=\"";
                    if($hr eq "$hr[$_]"){print"$hr[$_]\" checked><font color=\"$hr[$_]\">��</font>\n";}
                    else{print"$hr[$_]\"><font color=\"$hr[$_]\">��</font>\n";}
                }
                print"</td></tr>";
            }
            if($ICON ne ""){
                if($CICO){$ICO=$CICO;}
                print"<tr><td>Icon</td><td> <select name=\"Icon\">\n";
                foreach(0 .. $#ico1) {
                    if($ICO eq $ico1[$_]){print"<option value=\"$_\" selected>$ico2[$_]\n";}
                    else{print"<option value=\"$_\">$ico2[$_]\n";}
                }
                print"</select> <small>(�摜��I��/";
                print"<a href=\"$cgi_f?mode=img&amp;$no$pp\"$TGT>�T���v���ꗗ</a>)</small></td></tr>\n";
            }
            if($sel){
                print"<tr><td>$SEL_T</td><td> <select name=\"sel\">\n";
                foreach(0 .. $#SEL) {
                    if($sel eq "$SEL[$_]"){print"<option value=\"$SEL[$_]\" selected>$SEL[$_]\n";}
                    else{print"<option value=\"$SEL[$_]\">$SEL[$_]\n";}
                }
                print"</select></td></tr>\n";
            }
            if($txt){
                print"<tr><td>$TXT_T</td><td>/\n";
                print"<input type=\"text\" name=\"txt\" value=\"$txt\" maxlength=\"$TXT_Mx\">\n";
                print"</td></tr>";
            }
            print<<"_HTML_";
<tr><td colspan="2"><br>$end_form</td></tr>
</td></tr><tr><td colspan="2" align="right"><input type="submit" value=" �� �W " >
_HTML_
            print "<input type=\"reset\" value=\"���Z�b�g\"></td></tr></table></form></ul><hr width=\"95\%\">";
            if($i_mode){
                if($ico){
                    &size;
                    print<<"_DEL_";
�E��������t�@�C���폜�ł��܂��B<br>
<table summary="delete" width="90\%">$Pr</table>
<form action="$cgi_f">$nf$pf
<input type="hidden" name="mode" value="h_w"><input type="hidden" name="pass" value="$FORM{"pass"}">
<input type="hidden" name="IMD" value="$namber"><input type="submit" value="�t�@�C�����폜">
</form><hr width="95\%">
_DEL_
                }elsif($s==0 || ($s && $ResUp)){
                    print<<"_DEL_";
<ul>
�E��������t�@�C���A�b�v�ł��܂��B<br>
<form action="$cgi_f" method="$met" enctype="multipart/form-data">$nf$pf
_DEL_
                    print 'File <input type="file" name="ups" size="60" ' . "\"$ff>�@<input type=\"submit\" value=\"���M\">";
                    print '<ul>�A�b�v�\\�g���q=&gt;';
                    foreach (0..$#exn) {
                    if($exi[$I] eq "img"){$EX="<strong>$exn[$_]</strong>";}else{$EX="$exn[$_]";}
                    print"/$EX"; $I++;
                }
                print<<"_DEL_";
<br>
1) �����̊g���q�͉摜�Ƃ��ĔF������܂��B<br>
2) �摜�͏�����Ԃŏk���T�C�Y$H2�~$W2�s�N�Z���ȉ��ŕ\\������܂��B<br>
3) �����t�@�C��������A�܂��̓t�@�C�������s�K�؂ȏꍇ�A<br>
�@�@�t�@�C�����������ύX����܂��B<br>
4) �A�b�v�\\�t�@�C���T�C�Y��1��<strong>$max_fs\KB</strong>(1KB=1024Bytes)�܂łł��B<br></ul>
<input type="hidden" name="mode" value="h_w"><input type="hidden" name="pass" value="$FORM{"pass"}">
<input type="hidden" name="UP" value="$namber"><input type="hidden" name="UPt" value="$t">
<input type="hidden" name="mo" value="$mo"></form></ul><hr width="95\%">
_DEL_
                }
            }
            last;
        }
    }
    close(DB);
    &foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [�p�X���[�h�Í���]
# -> �p�X���[�h���Í�������(cry_)
#
sub cry_ {
    $time = time;
    ($p1, $p2) = unpack("C2", $time);
    $wk = $time / (60*60*24*7) + $p1 + $p2 - 8;
    @saltset = ('a'..'z','A'..'Z','0'..'9','.','/');
    $nsalt = $saltset[$wk % 64] . $saltset[$time % 64];
    $epasswd = crypt($FORM{'delkey'}, $nsalt);
}
#--------------------------------------------------------------------------------------------------------------------
# [�p�X���[�h���]
# -> �p�X���[�h���Í������}�b�`���O(cryma_)
#
sub cryma_ {
    if($de =~ /^\$1\$/){ $crptkey=3; }else{ $crptkey=0; }
    $ok = "n";
    if(crypt($FORM{'delkey'}, substr($de,$crptkey,2)) eq $de){$ok = "y";}
}
#--------------------------------------------------------------------------------------------------------------------
# [�폜����]
# -> �L���̍폜����(key_)
#
sub key_ {
    if ($mo eq "") {
#        if ($FORM{'del'} eq "") {&er_('invid'); }
#        if ($delkey eq "") {&er_('invpass'); }
        &er_('edit_not_allowed');
    } elsif ($mo == 1) {
        if (Forum->user->validate_password_admin($FORM{'pass'}) == 0) {
            &er_('invpass');
        }
#        if ($FORM{'pass'} ne $pass) {&er_('invpass'); }
    }
    if ($locks) {&lock_("$lockf"); }
    open(DB, "$log") || &er_("Can't open $log");
    @CAS = ();
    $dok = 0;
    $OYA = 0;
    $SP = "";
    while ($mens = <DB>) {
        $mens =~ s/\n//g;
        $Pdel = 0;
        ($nam, $d, $na, $mail, $d_, $com, $url, $sp, $e, $ty, $de, $ip, $ti)
            = split(/<>/, $mens);
        if ($d eq "") {
            push(@CAS, "$mens\n");
            $OYA = 1;
            next;
        }
        foreach $namber (@d_) {
            if ($namber eq "$nam") {
                if ($mo eq "") {
                    if (($de eq "") && ($dok == 0)) {&er_('nopass', "1"); }
                    &cryma_($de);
                    if (Forum->user->validate_password_admin($delkey) != 0) {
                        $ok = 'm';
                    }
#                    if ($delkey eq "$pass") {$ok = "m"; }
                    if (($ok eq "n") && ($dok == 0)) {&er_('invpass',"1"); }
                }
                &delcollect;
                if (($SP < $sp) || ($SP == $sp) || ($SP eq "")) {$Pdel = 1; }
                $mens = "";
                $dok = 1;
                ($I, $ico, $E, $fi, $TX, $S, $R) = split(/:/, $ip);
                if ($ico && (-e "$i_dir/$ico")) {unlink("$i_dir/$ico"); }
            }
        }
        if (($kiji ne "") && (($kiji eq "$nam") || ($kiji eq "$ty"))) {$mens = ""; }
        $n = "\n";
        if (($mens eq "") && ($kiji eq "") && ($Pdel == 0)) {
            if ($mo || ($ok eq "m")) {$Dm = "(�Ǘ���)"; }
            else {$Dm = "(���e��)"; }
            $mens = "$nam<>$d<><><>�i�폜�j<>���̋L����$Dm�폜����܂���<><>$sp<><>$ty<><><>$ti<><>";
        } elsif (($mens eq "") && (($kiji ne "") || $Pdel)) {
            $mens = "";
            $n = "";
            if ($OYA == 0) {
                $mens = "$nam<><><><><><><><><>$nam<><><><><>";
                $n = "\n";
            }
        }
        $OYA = 1;
        $SP = $sp;
        push(@CAS, "$mens$n");
    }
    close(DB);

    open (DB,">$log");
    print DB @CAS;
    close(DB);
    if (-e $lockf) {rmdir($lockf); }
    if ($mo) {
        $msg = "<h3>�폜����</h3>";
        &del_;
    } else {
        $mode = "";
    }
    if ($conf{'rss'} eq 1) {&RSS; }
}
#--------------------------------------------------------------------------------------------------------------------
# [�ҏW�L���u��]
# -> �ҏW���e��u��������(h_w_)
#
sub h_w_ {
    if($KLOG){&er_('oldlogs');}
    if ((Forum->user->validate_password_admin($FORM{'pass'}) == 0) && $mo) {
        &er_('invpass');
    }
#if($FORM{'pass'} ne "$pass" && $mo){&er_('invpass');}
    ($comment,$com_)= split('\t',$comment);
if($E_[0] eq "" && $I_[0] eq ""){
    $delkey=$FORM{'pass'}; &check_;
    if($tag){
        $comment=~ s/\&lt\;/</g;
        $comment=~ s/\&gt\;/>/g;
        $comment=~ s/\&quot\;/\"/g;
        $comment=~ s/<>/\&lt\;\&gt\;/g;
    }
}
    $comment=~ s/\t//g;
if($locks){&lock_("$lockf");}
if($FORM{"pre"}){$comment="<pre>$comment</pre>";}
@new=(); $flag=0; $SIZE=0;
open(DB,"$log");
while ($line=<DB>) {
    $line =~ s/\n//g;
    ($knam,$k,$kname,$kemail,$kd_may,$kcomment,$kurl,
        $ks,$ke,$kty,$kd,$ki,$kt,$sml) = split(/<>/,$line);
    if($k eq ""){push (@new,"$line\n"); next;}
    if($namber eq "$knam") {
        if($mo eq ""){
            $de=$kd; $FORM{'delkey'}=$FORM{'pass'};
            &cryma_($epasswd);
            if (Forum->user->validate_password_admin($FORM{'pass'}) != 0) {
                $ok = 'm';
            }
#            if($FORM{"pass"} eq $pass){$ok="m";}
            if($ok eq "n"){ &er_('invpass',"1"); }
        }
        if($EStmp){
            &time_("");
            $EditCom="$date �ҏW";
            if($mo || $ok eq "m"){$EditCom.="(�Ǘ���)";}else{$EditCom.="(���e��)";}
            if($comment !~ /([0-9][0-9]):([0-9][0-9]):([0-9][0-9]) �ҏW/){$EditCom.="<br><br>";}else{$EditCom.="<br>";}
            $comment=$EditCom.$comment."\t".$userenv;
        }
        ($KI,$Kico,$E,$Kfi,$KTX,$KS,$KR)=split(/:/,$ki);
        ($Ktxt,$Ksel,$Kyobi)=split(/\|\|/,$KS);
        if($o_mail){if($send && $FORM{'pub'}==0){$send=2;}elsif($send==0 && $FORM{'pub'}==0){$send=3;}}
        $line="$namber<>$k<>$name<>$email<>$d_may<>$comment<>$url<>$ks<>$end<>$kty<>$kd";
        $line.="<>$KI:$Kico:$E:$Kfi:$ICON|$ICO|$font|$hr|:$txt\|\|$sel\|\|$Kyobi\|\|:$KR:<>$kt<>$send<>";
        $flag = 1;
    }elsif(@E_){
        ($KI,$Kico,$E,$Kfi,$KTX,$KS,$KR)=split(/:/,$ki);
        $EF=0;
        foreach $ENT (@E_){if($ENT eq $knam){$EF=1; if($E){$EE=0;}else{$EE=1;} last;}}
        if($EF){
            if($mo eq ""){
                $de=$kd; $FORM{'delkey'}=$FORM{'pass'};
                &cryma_($epasswd);
                if($ok eq "n"){ &er_('invpass',"1"); }
            }
            $line="$knam<>$k<>$kname<>$kemail<>$kd_may<>$kcomment<>$kurl<>$ks<>$ke<>$kty<>$kd<>$KI:$Kico:$EE:$Kfi:$KTX:$KS:$KR:<>$kt<>$sml<>";
            $flag=1;
        }
    }elsif(@I_){
        ($KI,$Kico,$E,$Kfi,$KTX,$KS,$KR)=split(/:/,$ki);
        $EF=0;
        foreach $ENT (@I_){if($ENT eq $knam){$EF=1;last;}}
        if($EF){
            if($mo eq ""){
                $de=$kd; $FORM{'delkey'}=$FORM{'pass'};
                &cryma_($epasswd);
                if($ok eq "n"){ &er_('invpass',"1"); }
            }
            if($Kico && -e "$i_dir/$Kico"){unlink("$i_dir/$Kico");}
            $Kico=""; $E=0; $Kfi="";
 			$line="$knam<>$k<>$kname<>$kemail<>$kd_may<>$kcomment<>$kurl<>$ks<>$ke<>$kty<>$kd<>$KI:$Kico:$EE:$Kfi:$KTX:$KS:$KR:<>$kt<>$sml<>";
            $flag=1;
        }
    }elsif($FORM{'UP'}){
        $UPt=$FORM{'UPt'}; $UP=$FORM{'UP'};
        ($KI,$Kico,$E,$Kfi,$KTX,$KS,$KR)=split(/:/,$ki);
        if($UPt){if($UPt eq $kty && $Kico){$SIZE+= -s "$i_dir/$Kico";}}
        else{if($UP eq $kty && $Kico){$SIZE+= -s "$i_dir/$Kico";}}
        if($UP eq $knam){
            if($mo eq ""){
                $de=$kd; $FORM{'delkey'}=$FORM{'pass'};
                &cryma_($epasswd);
                if($ok eq "n"){ &er_('invpass',"1"); }
            }
 			if($mas_c){$E=0;}else{$E=1;}
            $SIZE+=-s "$i_dir/$file";
            $line="$knam<>$k<>$kname<>$kemail<>$kd_may<>$kcomment<>$kurl<>$ks<>$ke<>$kty<>$kd<>$KI:$file:$E:$TL:$KTX:$KS:$KR:<>$kt<>$sml<>";
            $flag=1;
        }
    }
    push(@new,"$line\n");
}
close(DB);
if($SIZE && $max_or < int($SIZE/1024)){&er_('uplimit',"1");}
if($flag==0){&er_('editinvid',"1");}
if($flag==1){
    open (DB,">$log");
    print DB @new;
    close(DB);
}
if(-e $lockf){rmdir($lockf);}
if(@E_ || @I_ || $FORM{'UP'}){
    if($mo && (@E_ || @I_)){&ent_;}
    else{
        if(@I_){$msg="<h3>�t�@�C���폜</h3>"; $FORM{"del"}=$I_[0];}
        elsif($FORM{'UP'}){$msg="<h3>�t�@�C���A�b�v����</h3>$Henko"; if($mo){$kiji=$FORM{'UP'};}else{$FORM{"del"}=$FORM{'UP'};}}
        $delkey=$FORM{"pass"}; &hen_;
    }
}elsif($mo){$msg="<h3>�ҏW����</h3>"; &del_;}
else{$msg="<h3>�ȉ��̂悤�ɕҏW����</h3>"; $delkey=$FORM{"pass"}; $FORM{"del"}=$namber; &hen_;}
    if ($conf{'rss'} eq 1) {&RSS; }
}
#--------------------------------------------------------------------------------------------------------------------
# [�r��IP/�֎~�����ǉ�]
# -> �r��IP/�֎~�����ǉ��V�X�e��(Den_)
#
sub Den_ {
    if (Forum->user->validate_password_admin($FORM{'pass'}) == 0) {
        &er_('invpass');
    }
#if($FORM{'pass'} ne "$pass"){&er_('invpass');}
($m,$Log)=split(/:/,$FORM{"m"});
if($m eq "Make"){
    open(DB,">$Log") || &er_("Can't make $Log");
    print DB "";
    close(DB);
    chmod(0666,"$Log");
}elsif($m eq "Add"){
    $FORM{'u'}=~ s/\&lt\;/</g; $FORM{'u'}=~ s/\&gt\;/>/g;
    open(OUT,">>$Log");
    print OUT "$FORM{'u'}\n";
    close(OUT);
    $msd="<h3>$Log�֓o�^����</h3>";
}elsif($m eq "Del"){
    open(DB,"$Log");
    @deny = <DB>;
    close(DB);
    @NEW = ();$F=0;
    foreach $b (@deny) {
        $b =~ s/\n//g;
        foreach $u (@d_) {if($u eq "$b"){$F=1; last;}}
        if($F){$F=0; next;}
        push(@NEW,"$b\n");
    }
    open (DB,">$Log");
    print DB @NEW;
    close(DB);
    $msd="<h3>$Log���폜����</h3>";
}
&hed_("Deny IP/Word Editor");
print<<"_HTML_";
<table summary="deny" width="95\%"><tr><th>�r��IP/�֎~������ݒ胂�[�h</th></tr></table>$msd
<ul>
<li>�w�肵�������܂܂�Ă���Ƃ��ꂼ��r������܂��B</li>
<li><strong>[�r��IP?]</strong> IP�A�h���X��4���ō\\������Ă���A�ʏ�4���ڂ��A�N�Z�X���ɕς��܂��B����āA3���ڂ܂ł��w�肵�܂��B<br>
��) 127.0.0.1 ��r���������ꍇ�� 127.0.0. �Ǝw�肷��B192.168.0.1 �� 192.168.0. (*)������IP�͐�΂ɐݒ肵�Ȃ�!</li>
<li><strong>[�֎~������?]</strong> �g�p���ꂽ���Ȃ���������w�肵�܂��B�啶���������͋�ʂ���܂��B<br>
��) ��`�L����URL���w��B�^�O���J�n�^�O�̈ꕔ &lt;img &lt;font ���B</li>
</ul>
_HTML_
@Deny=("$IpFile","$NWFile");
@Dcom=("�r��IP","�֎~������");
foreach(0..1){
    if($mo){if($_==0){$mo=~ s/(\d+\.\d+\.\d+\.)(\d+)/$1/;}else{$mo="";}}
    if(-e "$Deny[$_]"){
        open(DB,"$Deny[$_]") || &er_("Can't open $Deny[$_]");
        @deny = <DB>;
        close(DB);
# deleted $pass from html form : non needed : $pass => --pass--
        print<<"_EDIT_";
<hr><strong>�� $Dcom[$_]�̒ǉ�</strong>
<form action="$cgi_f" method="$met"><input type="hidden" name="mode" value="Den">$nf$pf
<input type="hidden" name="pass" value="--pass--"><input type="hidden" name="m" value="Add:$Deny[$_]">
$Dcom[$_] /<input type="text" name="u" size="25" value="$mo"> (��/cj-c.com)
_EDIT_
        print<<"_EDIT_";
<input type="submit" value="�� ��">
</form><strong>�� $Deny[$_] �ɓo�^�ς݂�$Dcom[$_]</strong>
<form action="$cgi_f" method="$met"><input type="hidden" name="mode" value="Den">$nf$pf
<input type="hidden" name="pass" value="--pass--"><input type="hidden" name="m" value="Del:$Deny[$_]">
_EDIT_
        foreach(0..$#deny){
            $deny[$_]=~ s/\n//g; $deny[$_]=~ s/</\&lt\;/g; $deny[$_]=~ s/>/\&gt\;/g;
            print"<input type=\"checkbox\" name=\"del\" value=\"$deny[$_]\">- $deny[$_]<br>\n";
        }
        print '<br><input type="submit" value="�� ��" ' . "\"><input type=\"reset\" value=\"���Z�b�g\"></form></ul>\n";
    }else{
        print<<"_EDIT_";
<hr><br><strong>�� $Dcom[$_]�ݒ������t�@�C���̍쐬</strong><ul>
<li>$Dcom[$_]��ݒ肷��t�@�C��($Deny[$_])���Ȃ��̂ŃI�����C���Őݒ肷��ꍇ�A���̃t�@�C�����쐬����K�v������܂��B</li>
<li>����CGI�̂���f�B���N�g���ɍ쐬���܂�(���̃f�B���N�g���̃p�[�~�b�V������777or755 �ł���K�v������܂�)�B</li>
<li>�����ł��܂��쐬�ł��Ȃ��ꍇ�͓����t�@�C����FTP����쐬���Ă�������(�p�[�~�b�V����:666)</li>
</ul>
<form action="$cgi_f" method="$met"><input type="hidden" name="mode" value="Den">$nf$pf
<input type="hidden" name="pass" value="--pass--"><input type="hidden" name="m" value="Make:$Deny[$_]">
<input type="submit" value="$Deny[$_] ���쐬����">
</form>
_EDIT_
    }
}
print"<hr width=\"95\%\">\n";
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [���b�N����]
# -> �t�@�C�����b�N����(lock_)
#
sub lock_ {
    $lflag = 0;
    foreach (1 .. 5) {
        if (($tmp = mkdir($_[0], 0755))) {
            $lflag = 1;
            last;
        } else {
            sleep(1);
        }
    }
    if ($lflag == 0) {
        if (-e $_[0]) {
            rmdir($_[0]);
        }
        &er_('locked' ,"1");
    }
}
#--------------------------------------------------------------------------------------------------------------------
# [�J�E���^����]
# -> �J�E���g�A�b�v����(con_)
#
sub con_ {
    if($mode eq "" || $mode eq "alk"){
        if($locks){&lock_("$cloc");}
        open(NO,"$c_f") || &er_("Can't open $c_f","1");
        $cnt = <NO>;
        close(NO);
        if($FORM{'mode'} eq "" && $FORM{'page'} eq "" && $ENV{'HTTP_REFERER'} !~ /$cgi_f/) {
            $cnt++;
            open(NO,">$c_f") || &er_("Can't write $c_f","1");
            print NO $cnt;
            close(NO);
        }
        if(-e $cloc){rmdir($cloc);}
        while(length($cnt) < $fig){$cnt="0".$cnt;}
        @cnts = split(//,$cnt);
        if($m_pas){foreach(0..$#cnts){print"<img src=\"$m_pas/$cnts[$_]\.gif\" width=\"$m_wid\" height=\"$m_hei\">";}}
        else{print "<div class=\"Counter\">$cnt</div>";}
        print"<br>\n";
    }
}
#--------------------------------------------------------------------------------------------------------------------
# [�G���[�\��]
# -> �G���[�̓��e��\������(er_)
#
sub er_ {
    if (-e $lockf && $_[1]==1) {rmdir($lockf); }
    if (-e $cloc && $_[1]==1) {rmdir($cloc); }
    if (-e "$i_dir/$file") {unlink("$i_dir/$file"); }
    if ($FORM{"URL"}) {
        ($KURL, $Ag) = split(/::/, $FORM{'URL'});
    }
    if ($BG eq "") {&hed_("Error"); }
    $tmplVars{'errmsg'} = $_[0];
    $obj_template->process('error.tpl', \%tmplVars);
    &foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [�ߋ����O]
# -> �ߋ����O�ւ̏�������(log_)
#
sub log_ {
    open(NO,"$klog_c") || &er_("Can't open $klog_c");
    $n = <NO>;
    close(NO);

    $klog_f = "$klog_d\/$n$klogext";
    unless(-e $klog_f){ &l_m($klog_f);}

    $klog_size=$klog_l*1024;
    if(-s $klog_f > $klog_size) {&log_up;}

    open(LOG,">>$klog_f") || &er_("Can't write $klog_f");
    print LOG @KLOG;
    close(LOG);
}
#--------------------------------------------------------------------------------------------------------------------
# [�J�E���g�A�b�v]
# -> �ߋ����O�ԍ��̃J�E���g�A�b�v(log_up)
#
sub log_up {
    $n++;

    open(NUM,">$klog_c") || &er_("Can't write $klog_c");
    print NUM "$n";
    close(NUM);

    $klog_f="$klog_d\/$n$klogext";
    &l_m($klog_f);
}
#--------------------------------------------------------------------------------------------------------------------
# [���O����]
# -> ���O�������������܂�(l_m)
#
sub l_m {
    open(DB,">$_[0]") || &er_("Can't make $_[0]");
    print DB "";
    close(DB);

    chmod(0666,"$_[0]");
}
#--------------------------------------------------------------------------------------------------------------------
# [�o�b�N�A�b�v����]
# -> �ȈՃo�b�N�A�b�v����(backup_)
#
sub backup_{
    unless(-e $bup_f){&l_m($bup_f);}
    if(-M "$bup_f" > $bup || $FORM{"mode2"} eq "Backup"){
        open(LOG,">$bup_f") || &er_("Can't write $bup_f");
        print LOG @lines;
        close(LOG);
    }
}
#--------------------------------------------------------------------------------------------------------------------
# [�C������]
# -> �o�b�N�A�b�v�t�@�C�����l�[������(bma_)
#
sub bma_ {
    if (Forum->user->validate_password_admin($FORM{'pass'}) == 0) {
        &er_('invpass');
    }
#    if($FORM{'pass'} ne "$pass"){&er_('invpass');}
    if(-e $lockf){rmdir($lockf);}
    if(-e $bup_f){rename ($bup_f,$log) || &er_('renerr');}
    else{&er_('nobackup', "1");}
    $msg="<h3>�C������</h3>"; &del_;
}
#--------------------------------------------------------------------------------------------------------------------
# [�X���b�h�\��]
# -> �X���b�h�`���ŋL���̈ꗗ��\������(alk_)
#
sub alk_ {
$thread_oya=0;
if($FORM{'page'} eq ''){$page = 0;}else{$page=$FORM{'page'};}
@NEW=(); @RES=(); $List=""; $news=""; $On=1; %N=(); %d=(); %n=(); $RS=0; $K=1; $TOya=0;
open(LOG,"$log") || &er_("Can't open $log");
while (<LOG>) {
    ($namber,$date,$name,$email,$d_may,$comment,$url,
        $space,$end,$type,$del,$ip,$tim) = split(/<>/,$_);
    if($type){
        if($On){if(($time_k-$tim)>$new_t*3600){$n{$type}="$hed_i";}else{$n{$type}="$up_i_"; $On=0;}}
        $tim=sprintf("%011d",$tim); if($date){$R{$type}.="$tim<>$_";} $N{$type}++; $RS++;
    }else{
        if($n{$namber} eq ""){if(($time_k-$tim)>$new_t*3600){$n{$namber}="$hed_i";}else{$n{$namber}="$new_i";}}
        if($tim eq ""){$tim="$TIM";} $tim=sprintf("%011d",$tim);
        if($Res_T==2){$tim=$N{$namber}; $tim=sprintf("%05d",$tim);}
        push(@NEW,"$tim<>$_");
        ($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
        ($ICON,$ICO,$font,$hr)=split(/\|/,$TXT);
        ($txt,$sel,$yobi)=split(/\|\|/,$SEL);
        if($txt){$Txt="$TXT_T:[$txt]�@";}else{$Txt="";}
        if($sel){$Sel="$SEL_T:[$sel]�@";}else{$Sel="";}
        if($d_may eq ""){$d{$namber}=$notitle;}else{$d{$namber}=$d_may;}
        if($Txt || $Sel ||($Txt && $Sel)){if($TS_Pr==0){$d{$namber}="$Txt$Sel/"."$d{$namber}";}}
        if($N{$namber} eq ""){$N{$namber}=0;}
        if($Top_t && $Res_T==0 && $Rno < $LiMax){
            $Rno++; $PAH=$alk_su*$K; if(($PAH) < $Rno){$PAL="&amp;page=$PAH"; $K++;} $L_3=$Rno-1;
            if(($page+$alk_su)>=$Rno && ($page)<$Rno){$List.="<a href=\"#$TOya\">$n{$namber}$d{$namber}($N{$namber})</a> |\n"; $TOya++;}
            else{$List.="<a href=\"$cgi_f?mode=res&amp;namber=$namber&amp;page=&amp;$no$pp\">$n{$namber}$d{$namber}($N{$namber})</a> |\n";}
        }
        $news=""; $On=1;
    }
    $TIM=$tim;
}
close(LOG);

$PAGE=$page/$alk_su;
&hed_("All Thread / Page: $PAGE");
if($Res_T){
    @NEW=sort(@NEW); @NEW=reverse(@NEW);
    if($Top_t){
        foreach (0..$#NEW){
            if($Rno > $LiMax){last;}
            ($T,$namber,$date,$name,$email,$d_may,$comment,$url,
                $space,$end,$type,$del,$ip,$tim) = split(/<>/,$NEW[$_]);
            $Rno++; $PAH=$alk_su*$K; if(($PAH) < $Rno){$PAL="&amp;page=$PAH"; $K++;} $L_3=$Rno-1;
            if(($page+$alk_su)>=$Rno && ($page)<$Rno){$List.="<a href=\"#$L_3\">$n{$namber}$d{$namber}($N{$namber})</a> |\n";}
            else{$List.="<a href=\"$cgi_f?mode=res&amp;namber=$namber&amp;page=&amp;$no$pp\">$n{$namber}$d{$namber}($N{$namber})</a> |\n";}
        }
    }
}
if($Top_t){
    print "<li>$new_t���Ԉȓ��ɍ쐬���ꂽ�X���b�h�� $new_i �ŕ\\������܂��B</li>\n";
    print "<li>$new_t���Ԉȓ��ɍX�V���ꂽ�X���b�h�� $up_i_ �ŕ\\������܂��B</li>\n";
}

    $obj_template->process('comtop.inc.tpl');
print"</ul>$Henko<hr>";
if($cou){&con_;}
if($i_mode){&minf_("N");}
$total=@NEW; $NS=$RS+$total;
$page_=int(($total-1)/$alk_su);
$end_data=@NEW-1;
$page_end=$page+($alk_su-1);
if($page_end >= $end_data){$page_end = $end_data;}
$Pg=$page+1; $Pg2=$page_end+1;
$nl=$page_end+1;
$bl=$page-$alk_su;
if($bl >= 0){$Bl="<a href=\"$cgi_f?mode=alk&amp;page=$bl&amp;$no$pp$Wf\">"; $Ble="</a>";}
if($page_end ne $end_data){$Nl="<a href=\"$cgi_f?mode=alk&amp;page=$nl&amp;$no$pp$Wf\">"; $Nle="</a>";}
print"<div class=\"Caption03l\">�S $total �X���b�h�� $Pg �` $Pg2 �Ԗڂ�\\��</div>\n";

$Plink="<div class=\"Caption01c\"><strong>�S�y�[�W</strong> /\n"; $a=0;
$a=0;
for($i=0;$i<=$page_;$i++){
    $af=$page/$alk_su;
    if($i != 0){$Plink.=" ";}
    if($i eq $af){$Plink.="[<strong>$i</strong>]\n";}else{$Plink.="[<a href=\"$cgi_f?mode=alk&amp;page=$a&amp;$no$pp$Wf\">$i</a>]\n";}
    $a+=$alk_su;
}
$Plink.="</div>\n";
$Plink.='<hr class="Hidden">';
if($Res_T==1){$OJ1="<a href=\"$cgi_f?mode=alk&amp;W=W&amp;$no$pp\">�ԐM�ŐV��</a>\n"; $OJ2="���e��"; $OJ3="<a href=\"$cgi_f?mode=alk&amp;W=R&amp;$no$pp\">�L������</a>\n";}
elsif($Res_T==2){$OJ1="<a href=\"$cgi_f?mode=alk&amp;W=W&amp;$no$pp\">�ԐM�ŐV��</a>\n"; $OJ2="<a href=\"$cgi_f?mode=alk&amp;W=T&amp;$no$pp\">���e��</a>"; $OJ3="�L������\n";}
else{$OJ1="�ԐM�ŐV��"; $OJ2="<a href=\"$cgi_f?mode=alk&amp;W=T&amp;$no$pp\">���e��</a>\n"; $OJ3="<a href=\"$cgi_f?mode=alk&amp;W=R&amp;$no$pp\">�L������</a>\n";}
print"<div class=\"Caption01r\">�e�L���̏��� [ $OJ1 / $OJ2 / $OJ3 ]</div>\n";
print"$Plink<br>\n";
if($Top_t){
    print"<div class=\"ArtList\">\n<div class=\"Caption01List\">\n\n";
    print"<strong><a name=\"list\">�L�����X�g</a></strong> ( )���̐����͕ԐM��</div>\n$List\n</div><br>\n";
}
$LinkNo="";
foreach ($page .. $page_end) {
    ($T,$nam,$date,$name,$email,$d_may,$comment,$url,
        $sp,$end,$ty,$del,$ip,$tim,$Se) = split(/<>/,$NEW[$_]);
    ($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
    ($ICON,$ICO,$font,$hr)=split(/\|/,$TXT);
    ($txt,$sel,$yobi)=split(/\|\|/,$SEL);
    &design($thread_oya,$date,$name,$email,$d_may,$comment,$url,$sp,$end,$ty,$del,$Ip,$tim,$ico,
        $Ent,$fimg,$ICON,$ICO,$font,$hr,$txt,$sel,$yobi,$Se,"","TR");
    print"<hr><br>\n";
if(($thread_oya>0)&&(!$type)){print"</div>\n</div>\n";}
if($type){print"</div>\n";}
    print"$HTML";
    @RES=split(/\n/,$R{$nam}); $PNO=0;
    @RES=sort(@RES);
    if(@RES){
        $Rn=$alk_rm; $RC=@RES; $Pg=$RC-$alk_rm+1; if($Pg<=0){$Pg=1;}
        print"<hr><div class=\"Caption01l\">�S�ԐM $RC ���� $Pg �` $RC �Ԗڂ�\\��</div><br>\n";
        $RC_=int($RC/$ResHy);
        $res=0; $Dk=0; $ResNo=$Pg-1; $PgSt=$Pg-1; $PgEd=$RC-1;
        foreach ($PgSt..$PgEd) {
            ($T,$rnam,$rd,$rname,$rmail,$rdm,$rcom,$rurl,
                $rsp,$re,$rtype,$del,$rip,$rtim,$Se)=split(/<>/,$RES[$_]);
            if($nam eq "$rtype"){
                $ResNo++;
                ($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$rip);
                ($ICON,$ICO,$font,$hr)=split(/\|/,$TXT);
                ($txt,$sel,$yobi)=split(/\|\|/,$SEL);
                $PNO=int($ResNo/$ResHy)*$ResHy;
                &design($rnam,$rd,$rname,$rmail,$rdm,$rcom,$rurl,$rsp,$re,$rtype,$del,$Ip,$rtim,$ico,
                    $Ent,$fimg,$ICON,$ICO,$font,$hr,$txt,$sel,$yobi,$Se,$ResNo,"TR");
                print"<hr class=\"Hidden\">\n$HTML";
            }
            if($ResNo==$N{$nam}){last;}
        }
        if($RC){
#			if($Top_t){print"<hr><a href=\"#list\">���L�����X�g</a> /\n";}
            print"<hr><div class=\"Caption01r\">�ԐM�p�X���b�h�\\��\n";
            $a=0;
            for($i=0;$i<=$RC_;$i++){
                if($i){$St=$i*$ResHy; $En=$St+$ResHy-1; if($RC+1<=$En){$En=$RC;}}
                else{$En=$ResHy-1; if($RC<$En){$En=$RC;} $St="�e";}
                print"[<a href=\"$cgi_f?mode=res&amp;namber=$nam&amp;rev=$r&amp;page=$a&amp;$no$pp\">$St �` $En</a>]\n";
                $a+=$ResHy;
            }
            if($Dk){print"<br>($Dk���͍폜�L��)\n";}
            print "</div>";
        }
    }
    $LinkNo=$nam;
    print"</div>\n";
    $thread_oya++;
}
print"<hr>\n";
&allfooter("�X���b�h$alk_su");
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [�摜���擾]
# -> �t�@�C�����摜�̏ꍇ�A�t�@�C����ǂݍ���ŕ����擾���܂��B����ȊO�̃A�C�R���\���������Ȃ��܂�(size)
# -> �Ƃقق̃��E���W���Q�l�ɂ����Ă��������܂��� => http://tohoho.wakusei.ne.jp/
#
sub size {
if($Ent==0 && $fimg){$fimg=$no_ent; $A=0;}
if($_[0]){$FORM{"min"}=2;}else{if($CookOn eq ""){&get_("M"); $CookOn=1;}}
$A=0; $I=0;
if($fimg eq "img" && $FORM{'min'}==0){
    $Cg=1; $Wn=$W2; $Hn=$H2; $IW=0; $IH=0;
    if($ico=~/.gif$/i){ #GIF
        open(GIF,"$i_dir/$ico");
        binmode(GIF);
        seek(GIF,6,0);
        read(GIF,$size,4);
        close(GIF);
        ($IW,$IH)=unpack("vv",$size);
    }elsif($ico=~/.png$/i){ #PNG
        open(PNG,"$i_dir/$ico");
        binmode(PNG);
        seek(PNG,16,0);
        read(PNG,$Pw,4);
        read(PNG,$Ph,4);
        close(PNG);
        $PW=unpack("H*",$Pw);$IW=hex($PW);
        $PH=unpack("H*",$Ph);$IH=hex($PH);
    }elsif($ico=~/.jpg$|.jpeg$/i){ #JPEG
        open(JPG,"$i_dir/$ico");
        binmode(JPG);
        read(JPG,$Top,2);
        while (JPG) {
            read(JPG,$Top,4);
            ($mark,$Cell,$Lar)=unpack("aan",$Top);
            if($mark ne "\xFF"){$IW=0; $IH=0; last;}
            elsif((ord($Cell) >= 0xC0) && (ord($Cell) <= 0xC3)){
                read(JPG,$Top,5); ($IH, $IW)=unpack("xn2",$Top); last;
            }else{read(JPG,$Top,($Lar-2));}
        }
        close(JPG);
    }elsif($ico=~/.bmp$/i){ #BMP
        open(BMP,"$i_dir/$ico");
        binmode(BMP);
        seek(BMP,18,0);
        read(BMP,$size,8);
        close(BMP);
        ($IW,$IH)=unpack("V2",$size);
    }
    if($IW && $IH){
        if($IW > $Wn){$IK=$Wn*$IH;$kH=int($IK/$IW);$kW=$Wn;$Cg=0;}
        if($Cg && $IH > $Hn){$IK=$Hn*$IW;$kW=int($IK/$IH);$kH=$Hn;$Cg=0;}
        elsif($Cg==0 && $kH > $Hn){$IK=$Hn*$kW;$kW=int($IK/$kH);$kH=$Hn;}
        $Pr.="<small>$IW�~$IH";
        if($Cg){$kW=$IW;$kH=$IH;}
        else{$Pr.=" =\&gt\; $kW�~$kH";}
        $Pr.="</small><br>\n";
    }else{$kW=$W2;$kH=$H2;}
}
if($FORM{'min'}==1){$HW="";}elsif($FORM{'min'}==2){$I=1;}else{$HW=" width=\"$kW\" height=\"$kH\"";}
if(-s "$i_dir/$ico"){$Size= -s "$i_dir/$ico";}else{$Size=0;}
$KB=int($Size/1024); if($KB==0){$KB=1;}
if($Size){
    if($Size && $_[0] && $fimg ne $no_ent){$Alt=" alt=\"$ico/$KB\KB\"";}else{$Alt="";}
    if($fimg eq $no_ent){$A=0;}
    elsif($fimg eq "img"){
        if($I){$Pr.="<a href=\"$i_Url/$ico\"$TGT><img src=\"$i_Url/$i_ico\" border=\"0\"$Alt>"; $A=1;}
        else{$Pr.="<a href=\"$i_Url/$ico\"$TGT><img src='$i_Url/$ico' border=1$HW$Alt>"; $A=1;}
    }else{$Pr.="<a href=\"$i_Url/$ico\"$TGT>";$A=1;}
    if($img_h eq "" && $fimg ne img){$Pr.="<img src=\"$i_Url/$fimg\" border=\"0\"$Alt>";}
    elsif($img_h ne "" && $fimg ne img){$Pr.="<img src=\"$i_Url/$fimg\" height=\"$img_h\" width=\"$img_w\" border=\"0\"$Alt>";}
    $AEND="";
    if($_[0] eq ""){
        if($A){$AEND="$ico</a>/";}
        $Pr="$Pr"."<br>$AEND<small>$KB\KB</small>\n";
    }else{if($A){$AEND="</a>";} $Pr.="$AEND\n";}
}
}
#--------------------------------------------------------------------------------------------------------------------
# [���V�X�e��]
# -> �A�b�v�t�@�C��/�L���̕\������^���܂�(ent_)
#
sub ent_ {
    if (Forum->user->validate_password_admin($FORM{'pass'}) == 0) {
        &er_('invpass');
    }
#if($FORM{'pass'} ne "$pass"){&er_('invpass');}
&hed_("Permit");
print <<"_ENT_";
<table summary="allow"><tr><th>�t�@�C��/�L���\\������</th></tr></table><br>
<a href="$cgi_f?$no$pp"> �f���ɖ߂�</a> / <a href="$cgi_f?mode=del&amp;pass=$FORM{"pass"}&amp;$no$pp">�ʏ�Ǘ����[�h</a>
������/�����ɂ���t�@�C�����`�F�b�N���A�{�^���������ĉ������B
�t�@�C���폜���`�F�b�N���ă{�^���������ƃt�@�C���݂̂��폜�ł��܂��B
�L���݂̂̕\\�����͈�x���ς݂ɂ���ƁA�����ɖ߂��܂���!

<form action="$cgi_f" method="$met">$nf$pf
<input type="hidden" name="mode" value="ent"><input type="hidden" name="pass" value="$FORM{"pass"}">
<select name="check">
<option value="1">�S�����L���`�F�b�N
<option value="2">�S���ϋL���`�F�b�N
<option value="0">�`�F�b�N���͂���
_ENT_
print <<"_ENT_";
<input type="submit" value="���s"></form><br>
<form action="$cgi_f" method="$met">$nf$pf
<input type="hidden" name="mode" value="h_w"><input type="hidden" name="mo" value="1">
<input type="hidden" name="pass" value="2"$FORM{"pass"}">
_ENT_
$i=0; $k=0;
open(LOG,"$log") || &er_("Can't open $log");
while ($line=<LOG>) {
    ($nam,$date,$name,$email,$d_may,$comment,$url,
        $sp,$end,$ty,$del,$ip,$tim,$Se)=split(/<>/,$line);
    if($date eq ""){next;}
    ($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
    if($ico || ($Ent==0 && $mas_c==2)){
        if($i==0){
            print"<table summary=\"check\" width=\"95\%\"><tr>";
            print"<th>���`�F�b�N</th><th>���e�ҏ��</th><th>�R�����g</th><th>�t�@�C�����</th><th>�t�@�C���폜</th></tr>\n";
        }
        $check="";	
        if($Ent){$eok="��"; if($FORM{"check"}==2){$check=" checked";}}
        else{$eok="<span class=\"red\">�~</span>"; if($FORM{"check"}==1){$check=" checked";}}
        if($ty){$Re="($ty���X)";}else{$Re="";}
if((!$name)||($name eq ' ')||($name eq '�@')){$name=$noname;}
        if($email){$name="<a href=\"mailto:$email\">$name</a>";}
        if($url){$url="/<a href=\"http://$url\"$TGT>HP</a>";}
        if(-s "$i_dir/$ico"){$Size = -s "$i_dir/$ico";}else{$Size = 0;}
        $comment =~ s/<br>/ /g; $TB=1;
        if($tag){ $comment =~ s/</&lt;/g; $comment =~ s/>/&gt;/g; }
        if(length($comment) > 100){
            $comment=substr($comment,0,98); $comment=$comment . '..';
            $comment.="<a href=\"$cgi_f?mode=one&amp;namber=$nam&amp;pass=$FORM{'pass'}&amp;$no$pp\"$TGT>�S��</a>";
        }
        if($k){$BG=""; $k=0;}else{$BG=""; $k=1;}
        print <<"_ENT_";
<tr$BG><th><input type="checkbox" name="ENT" value="$nam$check">-$eok</th>
<td nowrap>#$nam $Re<br>��$name [$Ip]<br>
��<small>($date$url)</small></td>
<td>$comment<a href="$cgi_f?mode=one&amp;namber=$nam&amp;$no$pp"$TGT></a></td>
<td><a href="$i_Url/$ico"$TGT>$ico</a><br>($Size\Bytes)</td>
_ENT_
print "<th><input type=\"checkbox\" name=\"IMD\" value=\"$nam\"></th></tr>";
    $i++;
    if($i==30){print"</table>"; $i=0; $TB=0;}
    }else{next;}
}
close(LOG);
if($TB){print"</table>";}
print "<br><input type=\"submit\" value=\"����/������ �t�@�C���폜\"></form>\n";
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [�\���`��]
# -> �A�b�v�t�@�C���\���`���̕ύX�Ȃ�(minf_)
#
sub minf_ {
if($FORM{"min"} eq ""){&get_("M");}
if($FORM{"min"}==1){$S="";$S2=" selected";$S3="";}
elsif($FORM{"min"}==2){$S="";$S2="";$S3=" selected";}
else{$S2="";$S=" selected";$S3="";}
print"<form action=\"$cgi_f\" method=\"$met\">$nf$pf";
if($mas_c){print"�E�\\�������o��܂Ńt�@�C����<img src=\"$i_Url/$no_ent\">�ŕ\\������܂��B<br>\n";}
if($_[0]){print"<input type=\"hidden\" name=\"H\" value=\"$_[0]\">";}
print <<"_KEY_";
<input type="hidden" name="page" value="$page"><input type="hidden" name="mode" value="cmin">
�E�L�����̉摜�\\���`��<select name="min">
<option value="0"$S>$W2�~$H2�ȉ��ɏk��
<option value="1"$S2>������
<option value="2"$S3>�A�C�R��
_KEY_
print <<"_KEY_";
</select><input type="submit" value="�� �X" $fm>
</form>
_KEY_
}
#--------------------------------------------------------------------------------------------------------------------
# [�A�b�v�t�@�C���ꗗ]
# -> �A�b�v���ꂽ�t�@�C�����ꗗ�ŕ\�����܂�(f_a_)
#
sub f_a_ {
&hed_("All Up File");
print <<"_ENT_";
<h2>�t�@�C���ꗗ</h2>
<a href="$cgi_f?$no$pp"> �f���ɖ߂�</a>
 �A�b�v���ꂽ�t�@�C���݂̂̈ꗗ�ł��B
_ENT_
@ICO=();
open(LOG,"$log") || &er_("Can't open $log");
while (<LOG>) {
    ($namber,$date,$name,$email,$d_may,$comment,$url,
        $space,$end,$type,$del,$ip,$tim) = split(/<>/,$_);
    ($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
    if($ico){push(@ICO,"$_");}
}
close(LOG);

@NEW=(); $FS=0; $KL="";
$page_=int($#ICO/$Ico_kp);
if($page_){
    $KL.='<hr size="1" width="80%">�y�[�W�ړ� / ';
    if($FORM{'page'}){$page=$FORM{'page'};}else{$page=0;}
    $page_end=$page+($Ico_kp-1);
    if($page_end > $#ICO){$page_end=$#ICO;}
    for($i=0;$i<=$page_;$i++){
        $af=$page/$Ico_kp;
        if($i != 0){$KL.="| ";}
        if($i eq $af){$KL.="<strong>$i</strong>\n";}else{$KL.="<a href=\"$cgi_f?mode=f_a&amp;page=$a&amp;$no$pp\">$i</a>\n";}
        $a+=$Ico_kp;
    }
    $KL.='<hr size="1" width="80%">';
}else{$page=0; $page_end=$#ICO;}
$i=0; print"$KL";
foreach ($page..$page_end) {
    ($nam,$date,$name,$email,$d_may,$comment,$url,
        $sp,$end,$ty,$del,$ip,$tim,$Se)=split(/<>/,$ICO[$_]);
    ($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
    if($i==0){print"<table summary=\"filelist\" width=\"90\%\">\n";}
    $TB=1;
    if($i_mode && $ico){$Pr=""; &size;}else{$Pr="";}
    if($Size==0){next;}
    $FS=$FS+$Size;
    if($TOPH==0){$MD="mode=res&amp;namber="; if($ty){$MD.="$ty";}else{$MD.="$nam";}}
    elsif($TOPH==1){$MD="mode=one&amp;namber=$nam&amp;type=$ty&amp;space=$sp";}
    elsif($TOPH==2){$MD="mode=al2&amp;namber="; if($ty){$MD.="$ty";}else{$MD.="$nam";}}
    print"<tr><td align=\"center\"><br><table summary=\"follow\"><tr><td align=\"center\">$Pr</td></tr></table><br>\n";
    print"<strong>[<a href=\"$cgi_f?$MD&amp;$no$pp\">�ԐM�y�[�W</a>]</strong><br></td></tr>\n";
    $i++;
    if($i==30){print"</table>"; $i=0; $TB=0;}
}
if($TB){print"</table>";}
$FS=int($FS/1024);
print "<br>���v�t�@�C���T�C�Y/$FS\KB$KL\n";
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [�t���[�t�H�[���C��]
# -> �ȑO�̕����R�[�h��̕s��C���ƃ��O�R���o�[�g(freeform_)
#
sub freeform_{
    if (Forum->user->validate_password_admin($FORM{'pass'}) == 0) {
        &er_('invpass');
    }
#    if ($FORM{'pass'} ne "$pass") {&er_('invpass'); }
    if ($locks) {&lock_($lockf); }
    @NEW = ();
    $T = time;
    $DmyNo = 0;
    open(DB, "$log");
    while ($lines = <DB>) {
        ($namber,$date,$name,$email,$d_may,$comment,$url,
            $space,$end,$type,$del,$ip,$tim,$S) = split(/<>/,$lines);
        if ($date eq "") {push(@NEW, $lines); next; }
        else {$lines =~ s/\n//g; }
        if ($mo == 1) {
            ($Ip, $ico, $Ent, $fimg, $TXT, $SEL, $R) = split(/:/, $ip);
            if($SEL !~/\|\|\|\|/){
                ($txt,$sel,$yobi)=split(/\|/,$SEL);
                $new_ = "$namber<>$date<>$name<>$email<>$d_may<>$comment<>$url<>$space<>$end<>$type<>$del<>";
                $new_ .= "$Ip:$ico:$Ent:$fimg:$TXT:$txt\|\|$sel\|\|$yobi\|\|:$R:<>$tim<>$S<>\n";
            } else {push(@NEW, $lines); next; }
        } elsif ($mo eq "I-BOARD") {
            if ($space =~ /[A-Za-z\#]+/) {
                ($font,$hr)=split(/\;/,$space);
                if($ip=~ /:/){($ip,$ID,$Sex,$Old,$Rank,$T)=split(/:/,$ip);}
                if($type){$sp=15;}else{$sp=0;}
                if($DmyNo <= $namber){$DmyNo=$namber;}
                $new_="$namber<>$date<>$name<>$email<>$d_may<>$comment<>$url<>$sp<><>$type<>$del<>";
                $new_.="$ip\::1::\|$end\|$font\|$hr\|:$Old\|\|$Sex\|\|$ID\|\|:$Rank:<>$T<>$tim<>\n"; $T--;
            }else{&er_('alreadyct',"1");}
        }elsif($mo eq "UPP-BOARD"){
            if($space =~/[A-Za-z\#]+/){
                ($font,$hr)=split(/\;/,$space);
                if($type){$sp=15;}else{$sp=0;}
                if($DmyNo <= $namber){$DmyNo=$namber;}
                if($end){foreach(0..$#exn){if($end=~ /$exn[$_]$/ || $end=~ /\U$exn[$_]\E$/){$TL=$exi[$_]; last;}}}
                $new_="$namber<>$date<>$name<>$email<>$d_may<>$comment<>$url<>$sp<><>$type<>$del<>";
                $new_.="$ip:$end:$tim:$TL:\|\|$font\|$hr\|:\|\|\|\|\|\|::<>$T<>$tim<>\n"; $T--;
            }else{&er_('alreadyct', "1");}
        }
        push(@NEW,$new_);
    }
    close(DB);
    if($DmyNo){unshift(@NEW,"$DmyNo<><><><><><><><><>$DmyNo<><><><><>\n");}
    open (DB,">$log");
    print DB @NEW;
    close(DB);
    if(-e $lockf){rmdir($lockf);}
    $msg="<h3>�C������</h3>"; &del_;
}
#--------------------------------------------------------------------------------------------------------------------
# [���e�`�F�b�N]
# -> �t�H�[�����e���`�F�b�N(check_)
#
sub check_ {
    my ($envkey, $envvalue);
    &check_proxy();
    if ($i_mode && $UP) {
        $FLAG = 0;
        foreach (0..$#exn) {
            if ($file =~ /$exn[$_]$/i) {
                $FLAG = 1;
                $TAIL = $exn[$_];
                $TL = $exi[$_];
                last;
            }
        }
        if ($FLAG == 0) {&er_('noflag'); }
        if (-e "$i_dir/$file") {
            $TIME = time;
            $file = "$TIME$TAIL";
            $Henko = "<h3>�����t�@�C�������������߁A$file�ɕύX���܂���</h3>";
        } elsif ($file =~ /[^\w\-\.]/) {
            $TIME = time;
            $file = "$TIME$TAIL";
            $Henko = "<h3>�t�@�C�������s�K�؂��������߁A$file�ɕύX���܂���</h3>";
        }
        $MaxSize = $max_fs * 1024;
        if ($Fsize > $MaxSize) {&er_('upoverflow'); }
        if (open(OUT, "> $i_dir/$file")) {
            binmode(OUT);
#            print OUT substr($Read, $Pos2, $Fsize);
            print OUT $Read;
            close(OUT);
        }
        chmod(0666, "$i_dir/$file");
    }
    #if($kanrimode>1){$tag=1;}

    $tmplVars{'NMAX'} = $NMAX;
    $tmplVars{'TMAX'} = $TMAX;
    $tmplVars{'CMAX'} = $CMAX;
    if ($FORM{'UP'} eq "") {
        if ($name eq '') {&er_('noname'); }
        if ($d_may eq '') {&er_('nodmay'); }
        if ($comment eq '') {&er_('nocomment'); }
        if ($email && ($email !~ /(.*)\@(.*)\.(.*)/)) {&er_('invalidemail'); }
        if ($email && ($email !~ /^[\w@\.\-_]+$/)) {&er_('invalidemail'); }
        if ((length($delkey) > 8) && ($mode ne 'h_w')) {&er_('invaliddelkey'); }
        if ($NMAX && ($NMAX < length($name))) {&er_('namelength'); }
        if ($TMAX && ($TMAX < length($d_may))) {&er_('dmaylength'); }
        if ($CMAX && ($CMAX < length($comment))) {&er_('commentlength'); }
        if ($TXT_H && $TXT_F && ($txt eq '') &&
            (($TXT_R == 0) || $TXT_R && ($type == 0))) {&er_('notxtt'); }
        if ($he_tp && ($delkey eq '') && ($FORM{'pass'} eq ''))
            {&er_('nodelkey'); }
        if ($FORM{"pre"}) {$comment = "<pre>$comment</pre>"; }
        if ($FORM{"dmay"}) {$d_may = $FORM{"dmay"}; }
        if ($d_may eq "") {$d_may = "$notitle"; }
        $Ip = $ENV{'REMOTE_ADDR'};
        if ($ICON ne "") {
            $ICO = $ico1[$ICON];
            if ($ICO eq "randam") {
                srand;
                $randam = $#ico1;
                $ICON  = int(rand($randam));
                $ICO = $ico1[$ICON];
                if (($ICO eq "") || ($ICO eq "randam") || ($ICO eq "master")) {
                    foreach (0..$#ico1) {
                        if (($ico1[$_] ne "randam") && ($ico1[$_] ne "master")) {
                            $ICO = $ico1[$_];
                            $ICON = $_;
                        }
                    }
                }
                $CICO = "randam";
            } elsif ($ICO eq "master") {
                $ICO_F = 0;
                if ($mode eq "h_w") {$delkey = $FORM{'pass'}; }
                foreach (0..$#mas_p) {
                    if ($mas_p[$_] eq $delkey) {
                        $ICO = $mas_i[$_];
                        $ICO_F = 1;
                        $ICON = "m$_";
                        last;
                    }
                }
                if ($ICO_F == 0) {&er_('adminicon'); }
                $CICO = "master";
            } else {$CICO = $ICO; }
        }
    }
}

################################################################################

##------------------------------------------------------------------------------
# check_proxy - check for proxy
#  vars : 
#  tmpl : 
#  rets : none (exit on defined($Proxy) and accessed via proxy
sub check_proxy {
    if ($Proxy) {
        while (($envkey, $envvalue) = each(%ENV)) {
            if (($envkey =~ /proxy|squid/i) ||
                ($envvalue =~ /proxy|squid/i)) {
                &er_('viaproxy');
            }
        }
    }
}

##------------------------------------------------------------------------------
# allfooter - footer for listing all
#  vars : footopt
#  tmpl : allfooter.tpl
#  rets : none
sub allfooter ($) {
    $tmplVars{'footopt'} = $_[0];
    $tmplVars{'Bl'} = $Bl;
    $tmplVars{'Ble'} = $Ble;
    $tmplVars{'Nl'} = $Nl;
    $tmplVars{'Nle'} = $Nle;
    $tmplVars{'Plink'} = $Plink;
    $tmplVars{'srch'} = $srch;
    $tmplVars{'met'} = $met;
    $tmplVars{'log'} = $log;
    $tmplVars{'nf'} = $nf;
    $tmplVars{'pf'} = $pf;
    $tmplVars{'word'} = $word;
    $tmplVars{'NS'} = $NS;
    $tmplVars{'total'} = $total;
    $tmplVars{'RS'} = $RS;
    $tmplVars{'cgi_f'} = $cgi_f;
    $tmplVars{'ff'} = $ff;
    $tmplVars{'fm'} = $fm;
    $obj_template->process('allfooter.tpl', \%tmplVars);
}

##------------------------------------------------------------------------------
# man_ - display manual
#  vars : none
#  tmpl : man.tpl
#  rets : none
sub man_ {
    &hed_("Help");
    $tmplVars{'TrON'} = $TrON;
    $tmplVars{'TpON'} = $TpON;
    $tmplVars{'ThON'} = $ThON;
    $tmplVars{'all_i'} = $all_i;
    $tmplVars{'alk_su'} = $alk_su;
    $tmplVars{'alk_rm'} = $alk_rm;
    $tmplVars{'new_t'} = $new_t;
    $tmplVars{'new_i'} = $new_i;
    $tmplVars{'M_Rank'} = $M_Rank;
    $tmplVars{'i_mode'} = $i_mode;
    $tmplVars{'klog_s'} = $klog_s;
    $tmplVars{'max'} = $max;
    $tmplVars{'r_max'} = $r_max;
    $tmplVars{'end_f'} = $end_f;
    $tmplVars{'end_c'} = $end_c;
    $tmplVars{'end_ok'} = $end_ok;
    $tmplVars{'UID'} = $UID;
    $tmplVars{'SPAM'} = $SPAM;
    $tmplVars{'max_fs'} = $max_fs;
    $tmplVars{'up_i_'} = $up_i_;
    $tmplVars{'hed_i'} = $hed_i;
    $obj_template->process('man.tpl', \%tmplVars);
    &foot_;
}
##------------------------------------------------------------------------------
# new_ - show form for posting new
#  vars : 
#  tmpl : new.h2.tpl
#  rets : none
sub new_ {
    if (($topok == 0) &&
        (Forum->user->validate_password_admin($FORM{'pass'}) == 0)) {
#    if ($topok == 0 && ($FORM{'pass'} ne "$pass")) {
        &er_('newpasserr');
    }
    &hed_("Write New Message", "1");
    $tmplVars{'TrON'} = $TrON;
    $tmplVars{'TpON'} = $TpON;
    $tmplVars{'ThON'} = $ThON;
    $obj_template->process('new.h2.tpl', \%tmplVars);
    &forms_;
    &foot_;
}
##------------------------------------------------------------------------------
# hed_ - generate html header
#  vars : 
#  tmpl : htmlhead.tpl
#  rets : none
sub hed_ {
#    print "Content-type: text/html; charset=Shift_JIS\n\n";
    print Forum->cgi->header();
    if ($UID && ($_[1] == 1)) {
        &get_("I");
        if ($pUID eq "n") {
            $pUID = "";
            @UID = ('a'..'z','A'..'Z','0'..'9');
            srand;
            $pUID .= "$UID[int(rand(62))]"; $pUID .= "$UID[int(rand(62))]";
            $pUID .= "$UID[int(rand(62))]"; $pUID .= "$UID[int(rand(62))]";
            $pUID .= "$UID[int(rand(62))]"; $pUID .= "$UID[int(rand(62))]";
            $pUID .= "$UID[int(rand(62))]"; $pUID .= "$UID[int(rand(62))]";
            &set_("I", "$pUID");
        }
        if ($pUID eq "n") {$pUID="�����s"; }
    }
    $tmplVars{'fsi'} = $fsi;
    $tmplVars{'htmltitle'} = $_[0];
    $tmplVars{'text'} = $text;
    $tmplVars{'link'} = $link;
    $tmplVars{'vlink'} = $vlink;
    $tmplVars{'bg'} = $bg;
    $tmplVars{'back'} = $back;

    $curT = 0;
    if ($mode eq "man")      {$curT = 1; }
    elsif ($mode eq "n_w")   {$curT = 2; }
    elsif ($mode eq "one")   {$curT = 5; }
    elsif ($mode eq "new")   {$curT = 3; }
    elsif ($mode eq "alk")   {$curT = 4; }
    elsif ($mode eq "all")   {$curT = 5; }
    elsif ($mode eq "al2")   {$curT = 7; }
    elsif ($mode eq "ran")   {$curT = 6; }
    elsif ($mode eq "res")   {$curT = 4; }
    elsif ($mode eq "f_a")   {$curT = 8; }
    elsif ($mode eq "" || $mode eq "wri") {
        if ($H) {
            if ($H eq "T") {$curT = 5; }
            elsif ($H eq "F") {$curT = 7; }
            elsif ($H eq "N") {$curT = 4; }
        } else {
            if ($TOPH == 1) {$curT = 5; }
            elsif ($TOPH == 2) {$curT = 7; }
            else {$curT = 4; }
        }
    }
    $tmplVars{'curT'} = $curT;
    $tmplVars{'klog_s'} = $klog_s;
    $tmplVars{'M_Rank'} = $M_Rank;
    $tmplVars{'topok'} = $topok;
    $tmplVars{'TrON'} = $TrON;
    $tmplVars{'TpON'} = $TpON;
    $tmplVars{'ThON'} = $ThON;
    $tmplVars{'i_mode'} = $i_mode;
    $tmplVars{'srch'} = $srch;
    $tmplVars{'no'} = $no;
    $tmplVars{'pp'} = $pp;
    $tmplVars{'Wf'} = $Wf;
    $tmplVars{'cgi_f'} = $cgi_f;
    $tmplVars{'kiji_exist'} = $kiji_exist;
    if ($KLOG) {
        $tmplVars{'KLOG'} = $KLOG;
    }
    $obj_template->process('htmlhead.tpl', \%tmplVars);
}

##------------------------------------------------------------------------------
# foot_ - generates html footer
#  vars : 
#  tmpl : htmlfoot.tpl
sub foot_ {
    $tmplVars{'kanrimode'} = $kanrimode;
    $tmplVars{'cgi_f'} = $cgi_f;
    $tmplVars{'met'} = $met;
    $tmplVars{'nf'} = $nf;
    $tmplVars{'ff'} = $ff;
    $tmplVars{'pf'} = $pf;
    $tmplVars{'i_mode'} = $i_mode;
    $tmplVars{'mas_c'} = $mas_c;
    $tmplVars{'TGT'} = $TGT;
    $obj_template->process('htmlfoot.tpl', \%tmplVars);
    exit;
}

##------------------------------------------------------------------------------
# d_code_ - decodes input data
#  vars : 
#  tmpl : 
sub d_code_ {
    my %params;
    my $file;
    my $curNW;
    my ($vkey, $valarr, @values, $value);
    $file = "";
    if ($ENV{'CONTENT_LENGTH'} &&
        ($ENV{'CONTENT_TYPE'} =~ /^multipart\/form-data/)) {
        # form upload : ups
        $filename = $obj_cgi->param('ups');
        $Read = "";
        while (<$filename>) {$Read .= $_; }
        $Fsize = length($Read);
    }
    %params = $obj_cgi->Vars;
    while (($vkey, $valarr) = each(%params)) {
        if ($vkey eq 'ups') {next; }
        @values = split("\0", $valarr);
        foreach $value (@values) {
            if ($value !~ /[\x00-\x7E]*/) {
                $value = encode('shiftjis', decode('Guess', $value));
            }
            if ($vkey ne 'del') {
                foreach $curNW (@NW) {
                    $curNW =~ s/\n//;
                    if (index($value, $curNW) >= 0) {
                        $curNW =~ s/</\&lt\;/g;
                        $curNW =~ s/>/\&gt\;/g;
                        &er_("�u$curNW�v�͎g�p�ł��܂���!");
                    }
                }
            }
            $value =~ s/&/&amp\;/g;
            $value =~ s/</\&lt\;/g;
            $value =~ s/>/\&gt\;/g;
            $value =~ s/\"/\&quot\;/g;
            $value =~ s/<>/\&lt\;\&gt\;/g;
            $value =~ s/<!--(.|\n)*-->//g;
            if ($vkey =~ /^d_may[\d]/) {$vkey='d_may'; }
            $FORM{$vkey} = $value;
            if ($vkey eq 'del') {push(@d_,$value); }
            if ($vkey eq 'ENT') {push(@E_,$value); }
            if ($vkey eq 'IMD') {push(@I_,$value); }
        }
    }
    $actime = time();
    $d_may = $FORM{'d_may'}; $d_may =~ s/\x0D\x0A|\x0D|\x0A//g;
    $name  = $FORM{'name'}; $name =~ s/\x0D\x0A|\x0D|\x0A//g;
    $OS    = $FORM{'OS'}; $OS =~ s/\///g;
    $BROWSER = $FORM{'BROWSER'};
    $BROWSER =~ s/\///g;
    $MUA  = $FORM{'MUA'};
    $MUA =~ s/\///g;
    $userenv = $FORM{'userenv'};
    if (!$userenv) {
        $userenv = $OS;
        if ($BROWSER) {$userenv = "$userenv/$BROWSER"; }
        if ($MUA) {$userenv = "$userenv/$MUA"; }
    }
    $comment = $FORM{'comment'};
    $comment =~ s/\x0D\x0A/<br>/g;
    $comment =~ s/\x0D/<br>/g;
    $comment =~ s/\x0A/<br>/g;
    $comment =~ s/\t//g;
    $comment =~ s/^(<br>)*//g;
    $comment =~ s/(<br>)*$//g;
    $email = $FORM{'email'};
    if (length($email) > 100) {
        &er_('longmail');
    }
    $email =~ s/\x0D\x0A|\x0D|\x0A//g;
    $url  = $FORM{'url'};
    if (length($url) > 1000) {
        &er_('longurl');
    }
    $url =~ s/\x0D\x0A|\x0D|\x0A//g;
    $url =~ s/^http\:\/\///;
    $mode = $FORM{'mode'};
    $end  = $FORM{'end'};
    $space= $FORM{'space'};
    $kiji = $FORM{'kiji'};
    $namber=$FORM{'namber'};
    $namber=~s/\D//g;
    $type = $FORM{'type'};
    $delkey=$FORM{"delkey"};
    $mo    =$FORM{"mo"};
    $send = $FORM{"send"};
    $no    =$FORM{"no"};
    $W     =$FORM{"W"};
    $H     =$FORM{"H"};
    $txt   =$FORM{"txt"};
    $vRSS  =$FORM{"RSS"};
    $sel=$FORM{"sel"};
    $ICON  =$FORM{"Icon"};
    $hr=$FORM{"hr"};
    $font=$FORM{"font"};
    $smile = 1 if($FORM{"smile"});
    $ccauth = $FORM{'auca'};
    $ccmd5 = $FORM{'aucamd5'};
    &time_;
}

##------------------------------------------------------------------------------
# pas_ - password checker
#  vars : 
#  tmpl : 
sub pas_ {
    &hed_("Pass Input");
    $tmplVars{'cgi_f'} = $cgi_f;
    $tmplVars{'met'} = $met;
    $tmplVars{'ff'} = $ff;
    $tmplVars{'nf'} = $nf;
    $tmplVars{'fm'} = $fm;
    $tmplVars{'no'} = $no;
    $tmplVars{'s_ret'} = $s_ret;
    $obj_template->process('password.tpl', \%tmplVars);
    &foot_;
}

##------------------------------------------------------------------------------
# forms_ - show comment forms
#  vars : 
#  tmpl : 
sub forms_ {
    if ($s_ret && ($P ne "$s_pas")) {&er_('cannot_write'); }
    elsif ($KLOG) {&er_('cannot_write_oldlogs'); }

    my $obj_captcha = new Forum::Captcha;
    $tmplVars{'md5sum'} = $obj_captcha->generate($obj_config->GetParam('captcha_length'));

    if ($FORM{'PV'}) {
        $N_NUM = $FORM{"N"};
        $nams = $type;
        $namber = $kiji;
        $sp = $space;
        if ($FORM{'pub'}) {$c_pub = 1; }
        if ($FORM{'end'}) {$PVC = " checked"; }
#        if ($FORM{'send'}) {$PVE = " selected"; }
    } else {
        &get_;
        if ($FORM{'type'} eq "") {$sp = 0; }
        elsif ($FORM{'type'} == 0) {$sp = 15; }
        elsif ($FORM{'type'} > 0) {$sp = $space + 15; }
        if ($namber eq "") {$namber = 0; }
        if ($FORM{'type'} > 0) {$nams = $type; }
        elsif ($FORM{'type'} == 0) {$nams = $namber; }
        $T = " checked";
    }

    $tmplVars{'o_mail'} = $o_mail;
    $tmplVars{'PVE'} = $PVE;
    $tmplVars{'c_pub'} = $c_pub;

    $com =~ s/<pre>//g;
    $com =~ s/<\/pre>//g;
    if ($tag) {
        $com =~ s/</&lt;/g;
        $com =~ s/>/&gt;/g;
    }
    if (($mas_c == 2) && ($Ent == 0)) {
        $tmplVars{'com_nodisp'} = 1;
    }
    if ($Res_i && ($mo eq "") && ($FORM{'PV'} eq "")) {$com = ""; }
    if ($i_mode && ($ResUp || (($ResUp == 0) && ($sp == 0)))) {
#        foreach (0..$#exn) {
#            if($exi[$I] eq "img"){$EX="<strong>$exn[$_]</strong>";}else{$EX="$exn[$_]";}
#            $FI.="/$EX"; $I++;
#        }
        if($ResUp && $sp){
            $SIZE = int($SIZE/1024);
            $tmplVars{'SIZE'} = $SIZE;
            $tmplVars{'max_or'} = $max_or;
            $tmplVars{'Rest'} = $max_or - $SIZE;
        }
        $tmplVars{'multipart'} = 1;
        $tmplVars{'H2'} = $H2;
        $tmplVars{'W2'} = $W2;
        $tmplVars{'max_fs'} = $max_fs;
    } else {
        $tmplVars{'multipart'} = 0;
    }
    $tmplVars{'FORM_PV'} = $FORM{'PV'};
    $tmplVars{'cgi_f'} = $cgi_f;
    $tmplVars{'met'} = $met;
    $tmplVars{'tag'} = $tag;
    $tmplVars{'N_NUM'} = $N_NUM;
    $tmplVars{'nams'} = $nams;
    $tmplVars{'namber'} = $namber;
    $tmplVars{'sp'} = $sp;
    $tmplVars{'nf'} = $nf;
    $tmplVars{'pf'} = $pf;
    $tmplVars{'Hi'} = $Hi;
    $tmplVars{'he_tp'} = $he_tp;
    $tmplVars{'c_name'} = $c_name;
    $tmplVars{'c_email'} = $c_email;
    $tmplVars{'c_url'} = $c_url;
    $tmplVars{'ff'} = $ff;
    $tmplVars{'NMAX'} = $NMAX;
    $tmplVars{'TMAX'} = $TMAX;
    $tmplVars{'UID'} = $UID;
    $tmplVars{'pUID'} = $pUID;
    $tmplVars{'TGT'} = $TGT;
    if ($ua_select) {
        $tmplVars{'uasel'} = &UAsel;
    } else {
        $tmplVars{'uasel'} = '';
    }
    $tmplVars{'actime'} = $actime;
    $tmplVars{'ti'} = $ti;

    ($com, $com_) = split('\t', $com);
    $com =~ s/\t/ /g;
    $com =~ s/&nbsp;/ /g;
    &smile_decode($com);
    $tmplVars{'com'} = $com;
    $tmplVars{'BBFACE'} = $BBFACE;
    $tmplVars{'FI'} = $FI;

    if (@fonts) {
        if ($c_font eq '') {$c_font = $font[0]; }
        $tmplVars{'fonts'} = \@fonts;
        $tmplVars{'font_def'} = $c_font;
    }
    if (@hr) {
        if ($c_hr eq '') {$c_hr = $hr[0]; }
        $tmplVars{'hr'} = \@hr;
        $tmplVars{'hr_def'} = $c_hr;
    }
    if (($SEL_F && ($SEL_R == 0)) || ($SEL_F && $SEL_R && ($sp == 0))) {
        $tmplVars{'use_sel'} = 1;
        $tmplVars{'SEL_T'} = $SEL_T;
        $tmplVars{'sel'} = \@SEL;
        if ($c_sel eq '') {$c_sel = $SEL[0]; }
        $tmplVars{'sel_def'} = $c_sel;
    } else {
        $tmplVars{'use_sel'} = 0;
    }
    if (($TXT_F && ($TXT_R == 0)) || ($TXT_F && $TXT_R && ($sp == 0))) {
        $tmplVars{'use_txt'} = 1;
        $tmplVars{'TXT_T'} = $TXT_T;
        $tmplVars{'c_txt'} = $c_txt;
        $tmplVars{'TXT_Mx'} = $TXT_Mx;
    } else {
        $tmplVars{'use_txt'} = 0;
    }
    if ($AgSg && ($sp > 0)) {$tmplVars{'art_sort'} = 1; }
    else {$tmpl{'art_sort'} = 0; }
    $tmplVars{'c_key'} = $c_key;
    $tmplVars{'key'} = $key;
    $tmplVars{'optH'} = $_[0];
    if (($space ne "") && ($end_f == 1)) {
        $tmplVars{'end_ok'} = $end_ok;
        $tmplVars{'end_c'} = $end_c;
        $tmplVars{'end_m'} = $end_m;
        $tmplVars{'PVC'} = $PVC;
    }
    $obj_template->process('forms.tpl', \%tmplVars);
}

##------------------------------------------------------------------------------
# img_ - list icon images sample
#  vars : 
#  tmpl : img_.tpl
sub img_ {
  &hed_("All Icon");
  my $iconCnt = 0;
  my $pageCnt = int($#ico1 / $Ico_kp);
  my $pageCur = 0;
  my ($iconStart, $iconEnd);
  if ($pageCnt > 0) {
    if ($FORM{'page'} > 0) {$pageCur = $FORM{'page'}; }
    if ($pageCur > $pageCnt) {$pageCur = 0; }
    $iconStart = $pageCur * $Ico_kp;
    $iconEnd   = $iconStart + $Ico_kp - 1;
  } else {
    $iconStart = 0;
    $iconEnd = $#ico1;
  }

  $tmplVars{'page_cnt'} = $pageCnt;
  $tmplVars{'page_cur'} = $pageCur;
  $tmplVars{'icon_start'} = $iconStart;
  $tmplVars{'icon_end'} = $iconEnd;
  $tmplVars{'icon_1'} = \@ico1;
  $tmplVars{'icon_2'} = \@ico2;
  $tmplVars{'icon_master'} = \@mas_i;
  $tmplVars{'icon_dir'} = $IconDir;
  $tmplVars{'cgi_f'} = $cgi_f;
  $tmplVars{'no'} = $no;
  $tmplVars{'pp'} = $pp;
  $tmplVars{'icon_1'} = \@ico1;
  $obj_template->process('img_.tpl', \%tmplVars);
  &foot_;
}

##------------------------------------------------------------------------------
# a_ - display all boards in database
#  vars : 
#  tmpl : a_.tpl
sub a_ {
#    print "Content-type: text/html\n\n";
    print Forum->cgi->header();

    $tmplVars{'fsi'} = $fsi;
    $tmplVars{'text'} = $text;
    $tmplVars{'link'} = $link;
    $tmplVars{'vlink'} = $vlink;
    $tmplVars{'bg'} = $bg;
    $tmplVars{'ver'} = $ver;
    if ($back ne '') {$tmplVars{'back'} = $back; }

    my @resItems;
    foreach (0..$#set) {
        if (! $set[$_]) {next; }
        unless(-e $set[$_]) {next; }
        require "$set[$_]";
        $no = $_;
        @RES = ();
        $N = 0;
        open (LOG, "$log") || &er_("Can't open $log");
        while (<LOG>) {
            ($namber, $date, $name, $email, $d_may, $comment, $url, $space,
             $end, $type, $del, $ip, $tim) = split(/<>/, $_);
            if ($tim eq "") {next; }
            if ($type) {
                $ti = sprintf("%011d", $tim);
                if ($date) {
                    unshift(@RES, "$ti<>$name<>$tim<>");
                }
                $N++;
            } else {
                $ti = sprintf("%011d", $tim);
                if ($date) {
                    unshift(@RES, "$ti<>$name<>$tim<>");
                }
                $N++;
                last;
            }
        }
        close(LOG);
        @lines = ();
        @RES = sort(@RES);
        @RES = reverse(@RES);
        if (@RES) {
            ($Ti, $Name, $Tim) = split(/<>/, $RES[0]);
            if ($TOPH == 0) {$MD = "mode=res&amp;namber=$namber&amp;page=0"; }
            elsif ($TOPH == 1) {$MD = "mode=all&amp;namber=$namber&amp;type=0&amp;space=0"; }
            elsif ($TOPH == 2) {$MD = "mode=al2&amp;namber=$namber"; }
            &time_($Tim);
        } else {
            $namber = "#";
            $d_may = "����������ޤ���!";
            $date = "/";
            $MD = "";
            $Name = "/";
        }
        if ((! $Name) || ($Name eq ' ') || ($Name eq '��')) {
            $Name = $noname;
        }
        my %resOne;
        $resOne{'title'}  = $title;
        $resOne{'cgi_f'}  = $cgi_f;
        $resOne{'no'}     = $no;
        $resOne{'namber'} = $namber;
        $resOne{'MD'}     = $MD;
        $resOne{'d_may'}  = $d_may;
        $resOne{'N'}      = $N;
        $resOne{'Name'}   = $Name;
        $resOne{'date'}   = $date;
        push(@resItems, \%resOne);
    }

    $tmplVars{'resources'} = \@resItems;
    $obj_template->process('a_.tpl', \%tmplVars);

    &foot_;
}

##------------------------------------------------------------------------------
# cookdel - delete cookie
#  vars : 
#  tmpl : cookdel.tpl
sub cookdel{
    if ($mo eq "ID") {
        print"Set-Cookie: UID=; expires=Sunday, 1-Jun-2001 00:00:00 GMT\n";
    } elsif ($mo eq "ALL") {
        print"Set-Cookie: $s_pas=; expires=Sunday, 1-Jun-2001 00:00:00 GMT\n";
        print"Set-Cookie: Cmin=; expires=Sunday, 1-Jun-2001 00:00:00 GMT\n";
        print"Set-Cookie: UID=; expires=Sunday, 1-Jun-2001 00:00:00 GMT\n";
        print"Set-Cookie: CBBS=; expires=Sunday, 1-Jun-2001 00:00:00 GMT\n";
    }
    &hed_("cookie Delete");
    $tmplVars{'msg'} = $msg;
    $tmplVars{'cookie_mode'} = $mo;
    $tmplVars{'UID'} = $UID;
    $tmplVars{'cgi_f'} = $cgi_f;
    $tmplVars{'no'} = $no;
    $tmplVars{'pp'} = $pp;
    $obj_template->process('cookdel.tpl', \%tmplVars);
    &foot_;
}

##------------------------------------------------------------------------------
# read - read articles
#  vars : 
#  tmpl : read.tpl
sub read {
    if ($namber =~ /,/) {
        @N = split(/\,/, $namber);
        if ($#N > 50) {
            splice(@N, 50);
            $range_err = 'large_count';
        }
    } elsif ($namber =~ /-/) {
        my ($St, $En) = split(/-/, $namber);
        my ($tmpVal, $range_err);
        if ($St > $En) {
            $tmpVal = $En;
            $En = $St;
            $St = $tmpVal;
        }
        if (($En - $St) > 50) {
            $En = $St + 49;
            $range_err = 'wide';
        }
        if (($St eq '') && ($En eq '')) {
            &er_('range_undefined');
        } elsif ($St eq '') {
            $range_err = 'start_undef';
            $St = $En - 10;
        } elsif ($En eq '') {
            $range_err = 'end_undef';
            $En = $St + 10;
        }
        foreach ($St .. $En) {unshift(@N, $_); }
        $tmplVars{'range_err'} = $range_err;
        $tmplVars{'start_no'} = $St;
        $tmplVars{'end_no'} = $En;
    } else {
        @N = ($namber);
    }

    $N = @N;
    &hed_("No$namber �̋L���\\��");
    $tmplVars{'namber'} = $namber;
    $tmplVars{'MSG'} = $MSG;

    $FLAG = 0;
    my %outArray;
    my @outSort = ();
    open (LOG, "$log") || &er_("Can't open $log");
    while ($lines = <LOG>) {
        ($nam, $date, $name, $email, $d_may, $comment, $url,
        $sp, $end, $ty, $del, $ip, $tim, $Se) = split(/<>/, $lines);
        $i = 0;
        $HTML = "";
        foreach $namber (@N) {
            if (($namber eq "$nam") && ($namber ne $ty)) {
                ($Ip, $ico, $Ent, $fimg, $TXT, $SEL, $R) = split(/:/, $ip);
                ($ICON, $ICO, $font, $hr) = split(/\|/, $TXT);
                ($txt, $sel, $yobi) = split(/\|\|/, $SEL);
                &design($nam, $date, $name, $email, $d_may, $comment, $url, $sp, $end,
                        $ty, $del, $Ip, $tim, $ico, $Ent, $fimg, $ICON, $ICO, $font,
                        $hr, $txt, $sel, $yobi, $Se, "" ,"N");
                $tim = sprintf("%011d", $tim);
                $outArray{$tim} = $HTML;
                $FLAG++;
                last;
            }
            $i++;
        }
        if ($HTML) {splice(@N, $i, 1); }
        if (@N) {next; } else {last; }
    }
    close(LOG);
    foreach (sort keys %outArray) {
        push(@outSort, $outArray{$_});
    }
    $tmplVars{'out_sort'} = \@outSort;
    @N = reverse(@N);
    $tmplVars{'N'} = \@N;
    $tmplVars{'klog_s'} = $klog_s;
    $tmplVars{'klog_h'} = $klog_h;

    $tmplVars{'srch'} = $srch;
    $obj_template->process('read.tpl', \%tmplVars);
    &foot_;
}

##------------------------------------------------------------------------------
# res_ - show replies for thread
#  vars : 
#  tmpl : res_.tpl
sub res_ {
    if ($space eq "") {$space = 0; }
    $SP = $space + 15;
    @TOP = ();
    $k = 0;
    $Dk = 0;
    $On = 0;
    $En = 0;
    $O2 = 0;
    $TitleHed = "";
    open(DB, "$log");
    while (<DB>) {
        ($nam, $da, $na, $mail, $d_may, $co, $ur, $sp, $end, $ty,
         $de, $ip, $time) = split(/<>/, $_);
        if ((($ty == 0) && ($FORM{"namber"} eq "$nam")) ||
            (($ty != 0) && ($FORM{"namber"} eq $ty))) {
            if (($space < $sp) && ($On == 0) && ($O2 == 0)) {
                $N_NUM = $nam;
                $On = 1;
            }
            if (($space eq $sp) && ($O2 == 0) && ($mo ne $nam)) {
                $On = 0;
                $N_NUM = "";
            }
            if ($time) {
                $time = sprintf("%011d", $time);
                push(@TOP, "$time<>$_");
                if ($end) {$En = 1; }
            } else {
                $Dk++;
            }
            $namb = $nam;
            $k++;
            $TitleHed = $d_may;
            if ($mo) {
                if ($mo eq $nam) {
                    $On = 1;
                    $O2 = 1;
                    &comin_;
                }
            } else {
                if ($k == 1) {
                    $On = 1;
                    $O2 = 1;
                    &comin_;
                }
            }
        } else {
            if ($k && ($time =~ /[\d]+/)) {last; }
        }
    }
    close(DB);

    @TOP = sort(@TOP);
    $total = @TOP - 1;
    if ($FORM{'page'} eq '') {
        $page = 0;
    } else {
        $page = $FORM{'page'};
    }
    $PAGE = $page / $ResHy;
    &hed_("One Thread Res View / $TitleHed / Page: $PAGE", "1");
    $page_ = int($total / $ResHy);
    $end_data = @TOP-1;
    $page_end = $page + ($ResHy - 1);
    if ($page_end >= $end_data) {$page_end = $end_data; }
    $tmplVars{'cgi_f'} = $cgi_f;
    $tmplVars{'total'} = $total;
    $tmplVars{'page'} = $page;
    $tmplVars{'page_end'} = $page_end;
    $tmplVars{'cur_page'} = $page / $ResHy;
    $tmplVars{'ResHy'} = $ResHy;
    $tmplVars{'page_'} = $page_;
    $tmplVars{'form_namber'} = $FORM{'namber'};
    $tmplVars{'no'} = $no;
    $tmplVars{'pp'} = $pp;
    $tmplVars{'Dk'} = $Dk;
    $i = 0;
    $ToNo = $page;
    $SIZE = 0;
    my @article_html;
    foreach ($page .. $page_end) {
        ($T, $nam, $date, $name, $email, $d_may, $comment, $url, $sp, $end,
         $ty, $del, $ip, $tim, $Se) = split(/<>/, $TOP[$_]);
        ($Ip, $ico, $Ent, $fimg, $TXT, $SEL, $R) = split(/:/, $ip);
        ($ICON, $ICO, $font, $hr) = split(/\|/, $TXT);
        ($txt, $sel, $yobi) = split(/\|\|/, $SEL);
        &design($nam, $date, $name, $email, $d_may, $comment, $url, $sp, $end, $ty,
            $del, $Ip, $tim, $ico, $Ent, $fimg, $ICON, $ICO, $font, $hr, $txt, $sel,
            $yobi, $Se, $ToNo, "TRES");
        push(@article_html, $HTML);
        $ToNo++;
    }
    $tmplVars{'article_html'} = \@article_html;
    $tmplVars{'TrON'} = $TrON;
    $tmplVars{'all_i'} = $all_i;

    $bl = $page - $ResHy;
    $tmplVars{'bl'} = $bl;
    $tmplVars{'end_data'} = $end_data;

    if ($mo eq "") {$com = ""; }

    $tmplVars{'r_max'} = $r_max;
    $tmplVars{'total'} = $total;
    $tmplVars{'En'} = $En;
    $tmplVars{'end_e'} = $end_e;
    $tmplVars{'end_ok'} = $end_ok;
    $obj_template->process('res_.tpl', \%tmplVars);
    if (! ($r_max && ($total > $r_max))) {
        if (! ($En && $end_e)) {
            &forms_("N");
        }
    }
    &foot_;
}


################################################################################
# DELETED SUB ROUTINES

##------------------------------------------------------------------------------
# rank - counts commit ranking
#  vars : 
#  tmpl : 
sub rank {
    return;
}

##------------------------------------------------------------------------------
# ran_ - display commit ranking
#  vars : 
#  tmpl : 
sub ran_ {
    &er_('disabled');
}

##------------------------------------------------------------------------------
# mail_ - sending e-mail for forum commits
#  vars : 
#  tmpl : 
sub mail_ {
    return;
}

################################################################################
# SHOULD BE MOVED TO TT ROUTINES
