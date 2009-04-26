#! /usr/bin/perl

require './common.pl';

&d_code_;

Forum->template->set_vars('mode_id', 'search');

$set[0] = "./set.cgi";
$SetUpFile = $set[0];
require $SetUpFile;

$ag = $ENV{'HTTP_USER_AGENT'};
if ($logs) {
    unless (($logs eq "$log" || $logs=~ /^[\d]+$/ || $logs eq "all" || $logs eq "recent")) {
        Forum->error->throw_error_user('invalidfile');
    }
}
$SL = "$klog_d\/1$klogext";

if ($mode eq "log") {
    &log_;
} elsif ($mode eq "del") {
    &del_;
} else {
    &srch_;
}

exit;

##---
# d_code_ - decode CGI input / WILL BE REMOVED IN FUTURE
sub d_code_ {
    my %params;
    my ($name, $value);
    my $guess;
    %params = $obj_cgi->Vars;
    while (($name, $value) = each(%params)) {
        $guess = Encode::Guess::guess_encoding($value);
        unless (ref $guess) {
        } else {
            $value = $guess->decode($value);
            $value = Encode::encode('sjis', $value);
        }
        $value =~ s/&/&amp\;/g;
        $value =~ s/</\&lt\;/g;
        $value =~ s/>/\&gt\;/g;
        $value =~ s/\"/\&quot\;/g;
        $value =~ s/<>/\&lt\;\&gt\;/g;
        $value =~ s/<!--(.|\n)*-->//g;

        $FORM{$name} = $value;
        if ($name eq 'del') { push(@d_,$value); }
    }
    $word = $FORM{'word'};
    $andor = $FORM{'andor'};
    $mode = $FORM{'mode'};
    $logs = $FORM{'logs'};
    $FORM{'N'} =~ s/([^0-9,])*?//g;
    my $neq = $FORM{'N'};
    $Neq = '';
    $Neq = "&amp;
    N = $neq" if ($neq);
    undef $neq;
}
#--------------------------------------------------------------------------------------------------------------------
# [�����@�\&�\��]
# -> �����t�H�[���̕\���ƁA�������ʂ̕\���������Ȃ�(srch_)
#
sub srch_ {
    print Forum->cgi->header();

    $klog_h = $klog_h[0];
    if ($FORM{"PAGE"}) {
        $klog_h = $FORM{"PAGE"};
    }
    my $logcount = 0;
    if ($klog_s && (-e $SL)) {
        open(NO, $klog_c);
        $logcount = <NO>;
        close(NO);
    }
    if ($FORM{"bigmin"}) {
        $BM = 0;
    } else {
        $BM = 1;
    }
    Forum->template->set_vars('logcount', $logcount);
    Forum->template->set_vars('andor', $andor);
    Forum->template->set_vars('srch', $srch);
    Forum->template->set_vars('word', $word);
    Forum->template->set_vars('klog_s', $klog_s);
    Forum->template->set_vars('log', $log);
    Forum->template->set_vars('logs', $logs);
    Forum->template->set_vars('FORM-KYO', $FORM{'KYO'});
    Forum->template->set_vars('klog_h', \@klog_h);
    Forum->template->set_vars('KH', $KH);
    Forum->template->set_vars('FORM-ALL', $FORM{'ALL'});
    Forum->template->set_vars('BM', $BM);
    Forum->template->process('search_result.tmpl', \%tmplVars);



    if ($word ne "") {
        $word =~ s/�@/ /g;
        $word =~ s/\t/ /g;
        @key_ws= split(/ /,$word);
        if($logs eq "all"){
            $Stert=0; if($FORM{'N'}){($N,$S)=split(/\,/,$FORM{'N'}); $Stert=$N;} $End=$n-1;
            if ($klog_a==0) {
                Forum->error->throw_error_user('not_able_to_search_all');
            }
        } else {
            $Stert = 0;
            $End = 0;
        }
        @new=(); $Next=0;
        foreach ($Stert..$End) {
            if($logs eq "all"){$I=$_+1; $IT="$I$klogext"; $Log="$klog_d\/$IT"; $notopened="�ߋ����O$I";}
            elsif($logs eq 'recent'){$Log=$log; $notopened="���s���O";}
            elsif($logs eq $log){$Log=$log; $notopened="���s���O";}
            else{$Log="$klog_d\/$logs$klogext"; $notopened="���O$logs";}
            Forum->template->set_vars('file', $Log);
            open(DB,$Log) || Forum->error->throw_error_user('cannot_open_logfile');
            while ($Line=<DB>) {
                $hit = 0;
                if($FORM{"ALL"}){
                    ($nam,$date,$name,$email,$d_may,$comment,
                        $url,$font,$ico,$type,$del,$ip) = split(/<>/,$Line);
                    if($word==$nam || $word==$type){$hit=1;}
                }else{
                    foreach $key_w (@key_ws){
                        if($key_w =~ /[\x80-\xff]/){$jflag = 1;}else{$jflag = 0;}
                        $key_w=~ s/^&$/&amp\;/g;
                        $key_w=~ s/^<$/\&lt\;/g;
                        $key_w=~ s/^>$/\&gt\;/g;
                        $key_w=~ s/^\"$/\&quot\;/g;
                        if ($jflag) {
                            if(index($Line, $key_w) >= 0){$hit=1;}else{$hit=0;}
                        } else {
                            if($BM){if($Line =~ /$key_w/i){$hit=1;}else{$hit=0;}}
                            else{if($Line =~ /$key_w/){$hit=1;}else{$hit=0;}}
                        }
                        if($hit){if($andor eq "or"){last;}}else{if($andor eq "and"){$hit=0; last;}}
                    }
                }
                if($hit){push(@new,"$IT<>$Line");}
                if($#new+1 >= 200 && $logs eq "all"){$Next=$I+1;}
            }
            close(DB);
            if($Next){last;}
        }
    }
    $count=@new;
    if($logs eq "$log"){@new=reverse(@new);}
    if($count > 0){
        $word=~ s/([^0-9A-Za-z_])/"%".unpack("H2",$1)/ge;
        $word=~ tr/ /+/;
        $total=@new;
        $page_=int(($total-1)/$klog_h);
        if($FORM{'page'} eq ""){$page=0;}else{$page=$FORM{'page'};}

        $end_data=@new-1;
        $page_end=$page+($klog_h-1);
        if($page_end >= $end_data){$page_end=$end_data;}
        $Pg=$page+1; $Pg2=$page_end+1;
        print"<div class=\"Caption03l\">$count ���� $Pg �` $Pg2 ���ڂ�\\��</div>";
        if($Next || $N){
            $NLog="<div class=\"Caption01c\">�q�b�g�����������̂�";
            if($N){$N++; $NLog.="�ߋ����O$N"; $fromto="�ߋ����O$N";}else{$NLog.="�ߋ����O1"; $fromto="�ߋ����O1";}
            if($I>1 && $I>$N){$NLog.="�`$I "; $fromto.="�`$I ";}
            $NLog.="�̌�������"; $fromto .="��";
            if($n>$I){
                $NLog.=" / <strong><a href=\"$srch?mode=srch&amp;logs=$logs&amp;word=$word&amp;andor=$andor&amp;KYO=$FORM{'KYO'}&amp;PAGE=$klog_h&amp;N=$I,$Stert\">";
                $NLog.="�ߋ����O$Next���炳��Ɍ�����</a></strong>\n";
            }
        }
        print"$NLog\n</div>\n";
        $nl=$page_end + 1;
        $bl=$page - $klog_h;
        if($bl >= 0){
            $Bl ="<a href=\"$srch?mode=srch&amp;logs=$logs&amp;page=$bl&amp;word=$word&amp;andor=$andor&amp;KYO=$FORM{'KYO'}&amp;PAGE=$klog_h$Neq\">";
            $Ble="</a>";
        }
        if($page_end ne $end_data){
            $Nl ="<a href=\"$srch?mode=srch&amp;logs=$logs&amp;page=$nl&amp;word=$word&amp;andor=$andor&amp;KYO=$FORM{'KYO'}&amp;PAGE=$klog_h$Neq\">";
            $Nle="</a>";
        }
        $Plink="<div class=\"Caption01c\"><strong>$fromto�S�y�[�W</strong> /\n"; $a=0;
        $a=0;
        for($i=0;$i<=$page_;$i++){
            $af=$page/$klog_h;
            if($i != 0){$Plink.=" ";}
            if($i eq $af){$Plink.="[<strong>$i</strong>]\n";}
            else{
                $Plink.="[<a href=\"$srch?mode=srch&amp;logs=$logs&amp;page=$a";
                $Plink.="&amp;word=$word&amp;andor=$andor&amp;KYO=$FORM{'KYO'}&amp;PAGE=$klog_h$Neq\">$i</a>]\n";
            }
            $a+=$klog_h;
        }
        $Plink.="$Nl$Nle\n</div>";
        print <<"_KT_";
$Plink
<form action="$srch" method="$Met"><input type="hidden" name="mode" value="del">
<input type="hidden" name="logs" value="$logs">
_KT_

    foreach ($page .. $page_end) {
        ($IT,$nam,$date,$name,$email,$d_may,$comment,$url,
            $sp,$e,$type,$del,$ip,$tim,$Se) = split(/<>/,$new[$_]);
        ($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
        ($ICON,$ICO,$font,$hr)=split(/\|/,$TXT);
        ($txt,$sel,$yobi)=split(/\|\|/,$SEL);
        if($date eq ""){next;}
        $Pr="";
        if($ico){
            if($Ent==0 && $fimg){$fimg=$no_ent;}
            if(-s "$i_dir/$ico"){$Size= -s "$i_dir/$ico";}else{$Size=0;}
            $KB=int($Size/1024); if($KB==0){$KB=1;}
            if($Size){
                if($Size && $fimg ne $no_ent){$Alt=" alt=\"$ico/$KB\KB\"";}else{$Alt="";}
                if($fimg eq $no_ent){$A=0;}
                elsif($fimg eq "img"){
                    $Pr.="<a href=\"$i_Url/$ico\"$TGT><img src='$i_Url/$i_ico' border=0$Alt>";
                    $A=1;
                }else{$Pr.="<a href=\"$i_Url/$ico\"$TGT>";$A=1;}
                if($img_h eq "" && $fimg ne img){$Pr.="<img src=\"$i_Url/$fimg\" border=0$Alt>";}
                elsif($img_h ne "" && $fimg ne img){$Pr.="<img src=\"$i_Url/$fimg\" height=$img_h width=$img_w border=0$Alt>";}
                $AEND="";
                if($A){$AEND="$ico</a>/";}
                $Pr="$Pr"."<br>$AEND $KB\KB\n";
            }
        }
        if($hr eq ""){$hr=$ttb;}
        if($type > 0){$t_com="�L��No.$type �ւ̕ԐM\n"; $KK="$type";}else{$t_com="�e�L��\n"; $KK="$nam";}
        if($d_may eq ""){$d_may="$notitle";}
        if($email && $Se < 2){$name ="$name <a href=\"mailto:$email\">$AMark</a>";}
        if($url){
            if($URLIM){
                if($UI_Wi){$UIWH=" width=\"$UI_Wi\" height=\"$UI_He\">";}
                $i_or_t="<img src=\"$URLIM\"$UIWH>";
            }else{$i_or_t="http://$url";}
            $url="<a href=\"http://$url\"$TGT>$i_or_t</a>";
        }
        if($Icon && $comment=~/<br>\(�g��\)$/){$ICO="$Ico_k";}
        if($ICO ne ""){
            if($IconHei){$WH=" height=\"$IconHei\" width=\"$IconWid\"";}
            $ICO="<img src=\"$IconDir\/$ICO\"$WH>";
        }
        if($txt){$Txt="$TXT_T:[$txt]�@";}else{$Txt="";}
        if($sel){$Sel="$SEL_T:[$sel]�@";}else{$Sel="";}
        if($yobi){$yobi="[ID:$yobi]";}
        if($Txt || $Sel ||($Txt && $Sel)){
            if($TS_Pr==0){$d_may="$Txt$Sel/"."$d_may";}
            elsif($TS_Pr==1){$comment="$Txt<br>$Sel<br>"."$comment";}
            elsif($TS_Pr==2){$comment.="<br>$Txt<br>$Sel";}
        }
        if($comment=~ /^<pre>/){$comment=~ s/<br>/\n/g;}
        $comment="<!--C-->$comment";
        if($IT ne "" && $logs eq "all"){
            $IT=~s/$klogext//; $IT=~s/^\n//; $IT=~s/\.txt$//; $PLL="�ߋ����O$IT��� /"; $IT="&KLOG=$IT";
        }else{$IT="";}
        if ($FORM{"KYO"}) {
            if ($comment =~ /<\/pre>/) {
                $comment =~ s/(>|\n)((&gt;|��|>)[^\n]*)/$1<font color=$res_f>$2<\/font>/g;
            } else {
                $comment =~ s/>((&gt;|��|>)[^<]*)/><font color=$res_f>$1<\/font>/g;
            }
            Encode::from_to($comment, 'sjis', 'euc-jp');
            foreach $KEY (@key_ws) {
                Encode::from_to($KEY, 'sjis', 'euc-jp');
                $comment =~ s/$KEY/<b STYLE="background-color:$Kyo_f\;">$KEY<\/b>/g;
                if ($BM) {
                    $comment =~ s/($KEY)/<b STYLE="background-color:$Kyo_f\;">$1<\/b>/ig;
                } else {
                    $comment =~ s/$KEY/<b STYLE="background-color:$Kyo_f\;">$KEY<\/b>/g;
                }
            }
            Encode::from_to($comment, 'euc-jp', 'sjis');
        } else {
            &auto_($comment);
        }
        if($o_mail){$Smsg="[���[���]��/";if($Se==2 || $Se==1){$Smsg.="ON]\n";}else{$Smsg.="OFF]\n";}}
        if($e){$e=" END /";}
        if($logs eq $log){
            if($TOPH==0){$MD="mode=res&amp;namber="; if($type){$MD.="$type";}else{$MD.="$nam";}}
            elsif($TOPH==1){$MD="mode=one&amp;namber=$nam&amp;type=$type&amp;space=$sp";}
            elsif($TOPH==2){$MD="mode=al2&amp;namber="; if($type){$MD.="$type";}else{$MD.="$nam";}}
            $L=" <a href=\"$cgi_f?$MD\">�g�s�b�N�\\���ƕԐM</a> /";
        }
        print <<"_HITCOM_";
<div class="ArtMain">
<div class="ArtHead">
<a name="$namber"><strong>$d_may</strong></a><br>
<span class="ArtId">(#$nam) $ResNo</span>
</div>
<div class="postinfo">
<span class="name">$name $R</span>�̓��e :$date<br>
$url</div>
<div class="ArtComment">$comment</div>
<div class="Caption01r">$end<br>
$Pr
$Smsg
$t_com /$e$L$PLL
<a href="$cgi_f?mode=al2&amp;namber=$KK&amp;$IT"$TGT>�֘A�L���\\��</a>
�`�F�b�N/<input type="checkbox" name="del" value="$nam"></div></div><br>
_HITCOM_



    }
    print qq!<hr class="Hidden"><div class="Caption01r">\n!;
    if($Bl){print"[ $Bl�O��$klog_h��$Ble ]\n";}
    if($Nl){if($Bl){print" | ";} print"[ $Nl����$klog_h��$Nle ]\n";}
print "</div><hr>$Plink\n$NLog";
    if($kanrimode){
    print <<"_KF_";
<div align=right>�p�X���[�h/<input type=password name=pas size=4>
<input type=submit value="�Ǘ��ҍ폜�p"></form></div>
_KF_
    }
}elsif($count == 0 && $word){print qq!<div class="Caption03l">�Y������L���͂���܂���ł����B</div>!;}
    Forum->template->process('htmlfoot.tpl', \%tmplVars);
}
#--------------------------------------------------------------------------------------------------------------------
# [URL�������N��]
# -> �R�����g���A�����N�E�����F�ȂǏ���(auto_)
#
sub auto_ {
if($_[0]=~/<\/pre>/){$_[0]=~ s/(>|\n)((&gt;|��|>)[^\n]*)/$1$2/g;}
else{$_[0]=~ s/>((&gt;|��|>)[^<]*)/><span class="Quoted">$1<\/span>/g;}
$_[0]=~ s/([^=^\"]|^)((http|ftp|https)\:[\w\.\~\-\/\?\&\+\=\:\@\%\;\#\,\|]+)/$1<a href="$2"$TGT>$2<\/a>/g;
$_[0]=~ s/([^\w^\.^\~^\-^\/^\?^\&^\+^\=^\:^\%^\;^\#^\,^\|]+)(No|NO|no|No.|NO.|no.|&gt;&gt;|����|>>)([0-9\,\-]+)/$1<a href=\"$cgi_f?mode=red&amp;namber=$3\"$TGT>$2$3<\/a>/g;
{$_[0]=~ s/&gt;([^<]*)/<span class="Quoted">&gt;$1<\/span>/g;}
}


##---
# hed_ - output HTML header (w/ HTTP header)
sub hed_ {
    my ($title) = @_;
    print Forum->cgi->header();
    Forum->template->set_vars('htmltitle', $title);
    Forum->template->set_vars('KLOG', $KLOG);
    Forum->template->process('htmlhead.tpl', \%tmplVars);
}

##---
# log_ - output old log list
sub log_ {
    my $n;
    Forum->template->set_vars('mode_id', 'oldlog');
    if (-e $SL) {
        open(NO, $klog_c);
        $n = <NO>;
        close(NO);
        Forum->template->set_vars('logcount', $n);
    } else {
        Forum->error->throw_error_user('no_avail_oldlog');
    }
    Forum->template->set_vars('srch', $srch);
    print Forum->cgi->header();
    Forum->template->process('oldlog_list.tmpl', \%tmplVars);
    exit;
}

##---
# del_ - delete routine for old logs
sub del_ {
    if (Forum->user->validate_password_admin($FORM{'pas'}) != 1) {
        Forum->error->throw_error_user('invalidpass');
    }
    if ($logs eq $log) {
        Forum->error->throw_error_user('cannot_open_curfile');
    }
    $logs = "$klog_d/$logs";
    Forum->template->set_vars('file', $logs);
    open(DB,$logs) || Forum->error->throw_error_user('cannot_open_logfile');
    @mens = <DB>;
    close(DB);
    @CAS = ();
    foreach $mens (@mens) {
        $castam = 0;
        $mens =~ s/\n//g;
        ($nam, $date, $name, $email, $d_may, $comment, $url,
            $sp, $e, $type, $del, $ip) = split(/<>/, $mens);
        foreach $word (@d_) {
            if ($word eq "$nam") {
                $mens = "";
                $castam = 1;
            }
        }
        if ($mens eq "") {
            $n = "";
        } else {
            $n = "\n";
        }
        push (@CAS, "$mens$n");
    }
    open (DB, ">$logs");
    print DB @CAS;
    close(DB);
    &log_();
}
