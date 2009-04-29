#! /usr/bin/perl

require './common.pl';

use Forum::Captcha;
use Forum::CGI;
use Forum::MigUtils;

my @set;
$set[0]="./set.cgi";
my @NW;
my @ips;

my $IpFile = Forum::Constants::LOCATIONS()->{'ipdeny'};
my $NWFile = Forum::Constants::LOCATIONS()->{'worddeny'};

# ---[排除IP/禁止文字列読み込み]-------------------------------------------------------------------------------------
if (-e $NWFile) {
    open(DE, $NWFile);
    while (<DE>) {push(@NW, $_); }
    close(DE);
}
if (-e $IpFile) {
    open(DE, $IpFile);
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
# ---[設定ファイル読み込み]------------------------------------------------------------------------------------------
$res_r=1;
&d_code_;

$SetUpFile = $set[0];
require $SetUpFile;

# ---[フォームスタイルシート設定]------------------------------------------------------------------------------------
$pf="";
$pp="";

if ($FORM{'KLOG'}) {
    $KLOG=$FORM{'KLOG'};
    $tmplVars{'TrON'}=0;
    $tmplVars{'TpON'}=1;
    $tmplVars{'ThON'}=0;
    $TOPH=2;
    unless($KLOG=~ /^[\d]+/) {
        &er_('invalidfile');
    }
    $log="$klog_d\/$KLOG$klogext";
    $pp = "&KLOG=$KLOG";
    $pf = "<input type=\"hidden\" name=\"KLOG\" value=\"$KLOG\">\n";
    $tmplVars{'KLOG'} = $KLOG;
}

Forum->template->set_vars('TS_Pr', $TS_Pr);
Forum->template->set_vars('TXT_T', $TXT_T);
Forum->template->set_vars('SEL_T', $SEL_T);
Forum->template->set_vars('cgi_f', $cgi_f);
Forum->template->set_vars('end_ok', $end_ok);
Forum->template->set_vars('notitle', $notitle);
Forum->template->set_vars('noname', $noname);
Forum->template->set_vars('atchange', $atchange);
Forum->template->set_vars('pp', $pp);

$mode_id = '';
if ($mode eq "man")      {$mode_id = 'manual'; }
elsif ($mode eq "n_w")   {$mode_id = 'incoming'; }
elsif ($mode eq "one")   {$mode_id = 'disp_tree'; }
elsif ($mode eq "new")   {$mode_id = 'newpost'; }
elsif ($mode eq "alk")   {$mode_id = 'disp_thread'; }
elsif ($mode eq "all")   {$mode_id = 'disp_tree'; }
elsif ($mode eq "al2")   {$mode_id = 'disp_topic'; }
elsif ($mode eq "ran")   {$mode_id = 'postrank'; }
elsif ($mode eq "res")   {$mode_id = 'disp_thread'; }
elsif ($mode eq "f_a")   {$mode_id = 8; }
elsif ($mode eq "" || $mode eq "wri") {
    if ($H) {
        if ($H eq "T") {$mode_id = 'disp_tree'; }
        elsif ($H eq "F") {$mode_id = 'disp_topic'; }
        elsif ($H eq "N") {$mode_id = 'disp_thread'; }
    } else {
        if ($TOPH == 1) {$mode_id = 'disp_tree'; }
        elsif ($TOPH == 2) {$mode_id = 'disp_topic'; }
        else {$mode_id = 'disp_thread'; }
    }
}
Forum->template->set_vars('mode_id', $mode_id);

# ---[サブルーチンの読み込み/表示確定]-------------------------------------------------------------------------------
if ($mode eq "cmin") {&set_("M");}
if (($conf{'rss'} eq 1) && ($mode eq 'RSS')) {&RSS; }
if ($mode eq "ent") {&ent_;} # EXIT (foot_)
if ($mode eq "man") {&man_;} # EXIT
if ($mode eq "n_w") {&n_w_;} # EXIT (foot_)
if ($mode eq "wri") {&wri_;}
if ($mode eq "nam") {&hen_;} # edit post / EXIT (foot_)
if ($mode eq "h_w") {&h_w_;}
if ($mode eq "new") {&new_;}
if ($mode eq "all") {&all_;}
if ($mode eq "al2") {&all2;}
if ($mode eq "res") {&res_;}
if ($mode eq "key") {&key_;} # delete post
if ($mode eq "one") {&one_;}
if ($mode eq "ran") {&ran_;}
if ($mode eq "img") {&img_;}
if ($mode eq "red") {&read;}
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
$tmplVars{'Wf'} = $Wf;
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
# [記事デザイン] 
# -> 記事を統一デザインで表示(design)
#
sub design ($$$$$$$$$$$$$$$$$$$$$$$$$$$) {
    my ($namber, $date, $name, $email, $d_may, $comment_, $url, $space, 
        $end, $type, $delkey, $ip, $tim, $ico, $Ent, $fimg, $mini, 
        $icon, $font, $hr, $txt, $sel, $yobi, $Se, $ResNo, $htype, 
        $hanyo) = @_;

    $Pr = "";

    Forum->template->set_vars('namber', $namber);
    Forum->template->set_vars('date', $date);
    Forum->template->set_vars('name', $name);
    Forum->template->set_vars('email', $email);
    Forum->template->set_vars('d_may', $d_may);
    Forum->template->set_vars('comment_', $comment_);
    Forum->template->set_vars('url', $url);
    Forum->template->set_vars('space', $space);
    Forum->template->set_vars('end', $end);
    Forum->template->set_vars('type', $type);
    # delkey
    # ip
    # tim
    # ico
    Forum->template->set_vars('Ent', $Ent);
    # fimg
    # mini
    # icon
    # hr
    Forum->template->set_vars('font', $font);
    Forum->template->set_vars('txt', $txt);
    Forum->template->set_vars('sel', $sel);
    # yobi
    Forum->template->set_vars('Se', $Se);
    Forum->template->set_vars('resno', $ResNo);
    Forum->template->set_vars('htype', $htype);
    # hanyo

    Forum->template->set_vars('Res_i', $Res_i);
    Forum->template->set_vars('mode', $mode);

    Forum->template->set_vars('r', $R);
    Forum->template->set_vars('nam', $nam);
    Forum->template->set_vars('ty', $ty);
    Forum->template->set_vars('sp', $sp);
    Forum->template->set_vars('rev', $rev);
    Forum->template->set_vars('fp', $fp);
    Forum->template->set_vars('PNO', $PNO);
    Forum->template->set_vars('o_mail', $o_mail);
    Forum->template->set_vars('mas_c', $mas_c);
    if ($KLOG) {$tmplVars{'klog_def'} = 1; } else {$tmplVars{'klog_def'} = 0; }
    if ($type) {$tmplVars{'type_def'} = 1; } else {$tmplVars{'type_def'} = 0; }
    $HTML = '';
    $obj_template->process('articledesign.tpl', \%tmplVars, \$HTML);
    return $HTML;
}
#--------------------------------------------------------------------------------------------------------------------
# [トピック一覧表示]
# -> トピックを一覧表示(html2_)
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
    $tmplVars{'henko'} = $Henko;
    $obj_template->process('topiclist.tpl', \%tmplVars);

    $end_data=@NEW-1;
    $page_end=$page+($tpmax*$tab_m-1);
    if($page_end >= $end_data){$page_end=$end_data;}
    $page_=int(($total-1)/($tpmax*$tab_m));
    $view =$tpmax*$tab_m;
    $nl = $page_end + 1;
    $bl = $page - $view;
    if($bl >= 0){
        $Bl="<a href=\"$cgi_f?H=F&amp;page=$bl&amp;$pp$Wf\">"; $Ble="</a>";
    }else{
        $Bl=""; $Ble="";
    }
    if($page_end ne $end_data){
        $Nl="<a href=\"$cgi_f?H=F&amp;page=$nl&amp;$pp$Wf\">"; $Nle="</a>";
    }else{
        $Nl=""; $Nle="";
    }
    if($cou){
        print "<div class=\"Counter\">" . &con_() . "</div><br>\n";
    }
    print"<div class=\"Caption03l\">全 $total トピック中 $Pg ～ $Pg2 を表\示</div>\n";
    $Plink="$Bl$Ble\n"; $a=0;
    for($i=0;$i<=$page_;$i++){
        $af=$page/($tpmax*$tab_m);
        if($i != 0){$Plink.=" ";}
        if($i eq $af){
            $Plink.="[<strong>$i</strong>]\n";
        }else{
            $Plink.="[<a href=\"$cgi_f?page=$a&amp;H=F&amp;$pp$Wf\">$i</a>]\n";}
            $a+=$tpmax*$tab_m;
        }
        $Plink.="$Nl$Nle\n";
        if($Res_T==1){
            $OJ1="<a href=\"$cgi_f?H=F&amp;W=W&amp;$pp\">返信最新順</a>";
            $OJ2="投稿順";
            $OJ3="<a href=\"$cgi_f?H=F&amp;W=R&amp;$pp\">記事数順</a>";
        } elsif($Res_T==2){
            $OJ1="<a href=\"$cgi_f?H=F&amp;W=W&amp;$pp\">返信最新順</a>";
            $OJ2="<a href=\"$cgi_f?H=F&amp;W=T&amp;$pp\">投稿順</a>";
            $OJ3="記事数順";
        }else{
            $OJ1="返信最新順";
            $OJ2="<a href=\"$cgi_f?H=F&amp;W=T&amp;$pp\">投稿順</a>";
            $OJ3="<a href=\"$cgi_f?H=F&amp;W=R&amp;$pp\">記事数順</a>";
        }
        print"<div class=\"Caption01r\">親記事の順番 [ $OJ1 / $OJ2 / $OJ3 ]</div>\n";
        $Plink="<div class=\"Caption01c\"><strong>全ページ</strong> / $Plink</div>\n";
        print $Plink;
        $k=0; $q=0;
        if($k){$p=$tab_m-$i; $page+=$tpmax*$p; last;}
        if($topok){$TP="<th width=\"13\%\">トピック作成者</th>";}
        if($he_tp==0){$SK="<th width=\"13\%\">最終発言者</th>";}
        if($end_f){$EE='<th width="5%">状況</th>';}
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
                print"<th width=\"46\%\">トピックタイトル</th><th width=\"8\%\">記事数</th>$TP$SK<th width=\"15\%\">最終更新</th>$EE</tr>\n";
            }
            $TableChange++;
            if(($time_k-$tim) > $new_t*3600){$news="$hed_i";}else{$news="$new_i";}
            if($yobi){$yobi="[ID:$yobi]";}
            if((!$name)||($name eq ' ')||($name eq '　')){$name=$noname;}
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
            $FL="<br>└<span class=\"ArtId\">#$namber</span>　[作成日:$date]";
            if($File && $Size){$FL.="　[File:$File -$KB\KB]";}
            if($topic < $ksu){
                $a=0; $PG_=int(($ksu-1)/$topic); $RP="";
                for($j=0;$j<=$PG_;$j++){
                    $RP.="<a href=\"$cgi_f?mode=al2&amp;namber=$namber&amp;page=$a&amp;rev=$tp_hi&amp;$pp$Wf\">$j</a>\n";
                    $a+=$topic;
                }
                if($FL){$FL.="　[ $RP]";}else{$FL="<br>　<small>[ $RP]";}
            }
            if(@ico3 && $Icon && ($ICON ne "" || $comment=~/<br>\(携帯\)$/)){
                if($I_Hei_m){$WHm=" width=\"$I_Wid_m\" height=\"$I_Hei_m\"";}
                if($ICON ne ""){if($ICON=~ /m/){$ICON=~ s/m//; $mICO=$mas_m[$ICON];}else{$mICO=$ico3[$ICON];}}
            elsif($Icon && $comment=~/<br>\(携帯\)$/){$mICO="$Ico_km";}
            $news.="<img src=\"$IconDir\/$mICO\" border=\"0\"$WHm>";
        }
        if($TXT_F){if($txt){$Txt="<td>$txt</td>";}else{$Txt="<td>/</td>";}}
        if($SEL_F){if($sel){$Sel="<td>$sel</td>";}else{$Sel="<td>/</td>";}}
        $ksu=$R{$namber}+1;
        print"<tr>$Sel$Txt<td align=\"left\">";
        print"<a href=\"$cgi_f?mode=al2&amp;namber=$namber&amp;rev=$r&amp;$pp\">$news <strong>$d_may</strong></a>$FL</td>";
        print"<td align=\"center\">$ksu件</td>$TP2$SK2<td align=\"center\"><small>$rdd</small></td>";
        if($end_f){print"<td align=\"center\">$reok</td>";}
        print"</tr>\n";
        $rdd=""; $rn=""; $rid="";
        if($tpmax <= $TableChange || $_ >= $total-1){print"</table><br>\n"; $TableChange=0;}
    }
    &allfooter("トピック$view");
    &foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [コメント引用]
# -> トピック/スレッド表示の際の引用処理(comin_)
#
sub comin_{
    ($com, $com_) = split('\t', $com);
    if ($FORM{'In'} eq "") {
        $com = "■No$namに返信($naさんの記事)<br>$co";
        $com =~ s/<br>/\n&gt; /g;
        $com =~ s/&gt; &gt; /&gt;&gt;/g;
    }
    $com =~ s/&nbsp;/ /g;
    $com =~ s/\t//g;
    $FORM{"type"} = $ty;
    $type = $ty;
    $namber = $nam;
}
#--------------------------------------------------------------------------------------------------------------------
# [トピック内容表示]
# -> トピック内容を表示(all2)
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
        if ($mo) {
            if ($mo eq $nam) {
                $On = 1;
                $O2 = 1;
                &rep_title();
                &comin_;
            }
        } else {
            if ($k == 1) {
                $On=1;
                $O2=1;
                &rep_title();
                &comin_;
            }
        }
    }else{if($k && $KLOG eq ""){last;}}
}
close(DB);
@TOP=sort(@TOP);
if($rev){@TOP=reverse(@TOP);}
$fhy ='<h2><a name="F">このトピックに書きこむ</a></h2>';
if($KLOG){$fhy="";}
$total=@TOP;
if($FORM{'page'} eq ''){$page=0;}else{$page=$FORM{'page'};}
$PAGE=$page/$topic;
&get_uid();
&hed_("One Topic All View / $TitleHed / Page: $PAGE");
if($cou){
        print "<div class=\"Counter\">" . &con_() . "</div><br>\n";
}
if($rev){
    print"$fhy\n";
    if($r_max && ($total-1) >= $r_max){
        print"<h3>返信数の限度を超えたので返信できません。<br>(返信数限度:$r_max 現在の返信記事数:$total)</h3>\n";
        print" → <strong><a href=\"$cgi_f?mode=new&amp;$pp\">[トピックの新規作成]</a></strong>";
        }else{if($En && $end_e){print"$end_ok / 返信不可";
    }else{&forms_("F");}}
}
$page_=int(($total-1)/$topic);
$end_data=@TOP-1;
$page_end=$page+($topic-1);
if($page_end >= $end_data){$page_end=$end_data;}
$Pg=$page+1; $Pg2=$page_end+1;
$nl=$page_end+1; 
$bl=$page-$topic;
if($page_end ne $end_data){$Nl="<a href=\"$cgi_f?mode=al2&amp;namber=$FORM{'namber'}&amp;page=$nl&amp;rev=$rev&amp;$pp\">"; $Nle="</a>";}
if($bl >= 0){$Bl="<a href=\"$cgi_f?mode=al2&amp;namber=$FORM{'namber'}&amp;page=$bl&amp;rev=$rev&amp;$pp\">"; $Ble="</a>";}
print "<form action=\"$cgi_f\" method=\"$met\">\n";
print"<div class=\"Caption03l\">トピック内全 $total 記事中の $Pg ～ $Pg2 番目を表\示</div>\n";
if($rev == 0){
    print"<div class=\"Caption01r\"><strong>[ <a href=\"$cgi_f?mode=al2&amp;namber=$FORM{'namber'}&amp;rev=1&amp;$pp\">";
    print"最新記事及び返信フォームをトピックトップへ</a> ]</strong><br></div>\n";
}elsif($rev){
    print"<div class=\"Caption01r\"><strong>[ <a href=\"$cgi_f?mode=al2&amp;namber=$FORM{'namber'}&amp;rev=0&amp;$pp\">親記事をトピックトップへ</a> ]</strong><br></div>\n";
}
$Plink="<div class=\"Caption01c\"><strong>このトピックの全ページ</strong> / "; $a=0;
for($i=0;$i<=$page_;$i++){
    $af=$page/$topic;
    if($i != 0){$Plink.=" ";}
    if($i eq $af){$Plink.="[<strong>$i</strong>]\n";}else{$Plink.="[<a href=\"$cgi_f?mode=al2&amp;namber=$FORM{'namber'}&amp;page=$a&amp;rev=$rev&amp;$pp\">$i</a>]\n";}
    $a+=$topic;
}
$Plink.="</div>";
print"$Plink<br>";
if($Dk){print"($Dk件の削除記事を非表\示)<br>";}
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
if($tmplVars{'TrON'}){$TrLink="<div class=\"Caption01r\">[ <a href=\"$cgi_f?mode=all&namber=$FORM{'namber'}&space=0&type=0&$pp\">$all_i このトピックをツリーで一括表\示</a> ]</div>";}
print"</div><hr>\n$TrLink\n";
if($Bl){print"<div class=\"Caption01r\">[ $Bl前のトピック内容$topic件$Ble ]";}
if($Nl){if($Bl){print" | ";}else{print "<div class=\"Caption01r\">";} print"[ $Nl次のトピック内容$topic件$Nle ]</div>";}else{print "</div>";}
print"$Plink\n<hr>\n";
$Ta=$total-1;
if($r_max && $Ta > $r_max){
    print"<h3>返信数の限度を超えたので返信できません。</h3>(返信数限度:$r_max 現在の返信数:$Ta)";
    print" → <strong><a href=\"$cgi_f?mode=new&amp;$pp\">[トピックの新規作成]</a></strong><br>";
}else{
    if($En && $end_e){print"<h3>$end_ok / 返信不可</h3><br>";}
    elsif($KLOG){print"<h3>返信不可</h3><br>";}
    else{
        if($total <= ($page+$topic) && $rev==0){
            print"$fhy";
            &forms_("F");
        }elsif($total >= ($page+$topic) && $rev==0){
            $page=$i-1; $a-=$topic;
            print"<div class=\"Caption01r\">[ <a href=\"$cgi_f?mode=al2&amp;namber=$FORM{'namber'}&amp;page=$a&amp;$pp#F\">このトピックの返信フォームへ</a> ]</div>";
        }
    }
}
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [ツリー記事表示]
# -> ツリーの記事を表示する(one_)
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
        &get_uid();
        &hed_("One Message View / $d_may");
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
        print"\n<tr align=\"center\"><th>前の記事(元になった記事)</th>\n";
        print"<th>次の記事(この記事の返信)</th></tr>\n";
    }
    if($end){$end="$end_ok"; $En=1;}
    if($d_may eq ""){$d_may="$notitle";}
    $date=substr($date,2,19);
    if(($time_k-$tim)>$new_t*3600){$news="$hed_i";}else{$news="$new_i";}
    if($txt){$Txt="$TXT_T:[$txt]　";}else{$Txt="";}
    if($sel){$Sel="$SEL_T:[$sel]　";}else{$Sel="";}
    if($Txt || $Sel ||($Txt && $Sel)){if($TS_Pr==0){$d_may="$Txt$Sel/"."$d_may";}}
    if(@ico3 && $Icon && ($ICON ne "" || $comment=~/<br>\(携帯\)$/)){
        if($I_Hei_m){$WHm=" width=\"$I_Wid_m\" height=\"$I_Hei_m\"";}
        if($ICON ne ""){if($ICON=~ /m/){$ICON=~ s/m//; $mICO=$mas_m[$ICON];}else{$mICO=$ico3[$ICON];}}
        elsif($Icon && $comment=~/<br>\(携帯\)$/){$mICO="$Ico_km";}
        $news.="<img src=\"$IconDir\/$mICO\" border=\"0\"$WHm>";
    }
    if($yobi){$yobi="[ID:$yobi]";}
    if(length($d_may)>$t_max){$d_may=substr($d_may,0,($t_max-2)); $d_may="$d_may..";}
if((!$name)||($name eq ' ')||($name eq '　')){$name=$noname;}
    if($email && $Se < 2){$name="$name <a href=\"mailto:$email\">$AMark</a>";}
    $psp=$space+15;$nsp=$space-15;
    if(($namber eq "$ty" || $type eq "$nam" || $type eq "$ty") && $ON==0){
        if($rs && $sp <= $space && $type){$ON=1;}
        if($sp eq $nsp && $nam < $namber && $i != 1){
            $b_="<a href=\"$cgi_f?mode=one&amp;namber=$nam&amp;type=$ty&amp;space=$sp&amp;$pp\">$d_may</a>\n/$name <small>$yobi</small>$Pr";
        }elsif($type == 0){$b_="親記事";}
        if($sp eq $psp && $nam > $namber && $i == 1){
            $n_.="<a href=\"$cgi_f?mode=one&amp;namber=$nam&amp;type=$ty&amp;space=$sp&amp;$pp\">$d_may</a>\n/$name <small>$yobi</small>$Pr<br>";
            $N_NUM=$nam;
        }
        if($i==1){$rs=1;}
    }
    $im=""; $im2=""; $im3="";
    if($sp > $SP && $F){$N_NUM=$nam;}
    if($sp eq $SP && $F){$F=0;}
    if($N_NUM eq $nam && $F==0){$F=1; $SP=$sp;}
    if($nam eq $namber){$im="<strong class=\"Highlight\">";$im2="";$im3=" *現在の記事<\/strong>";$ii=1;}
    if($Keisen){$Tree.="$Sen";}
    else{

        $spz=$sp/15*$zure;
        $Tree.="." x $spz;

    }
    $Tree.="$im<a href=\"$cgi_f?mode=one&amp;namber=$nam&amp;type=$ty&amp;space=$sp&amp;$pp\">$news $d_may</a>\n";
    $Tree.="/ $name :$date <span class=\"ArtId\">(#$nam)</span>$im2 $end$Pr$im3</td></tr><tr><td colspan=\"2\" nowrap>\n";
}
if(!$kiji_exist){$kiji_exist=2; if($TOPH==1){&html_;}elsif($TOPH==2){&html2_;}else{&alk_;}}else{
print"<tr><td valign=\"top\" width=\"50\%\">$b_</td><td width=\"50\%\">\n";
if($n_){print"$n_\n";}else{print"返信無し\n";}
print <<"_HTML_";
　</td></tr>
</table>
<br>
<h2>上記関連ツリー</h2>
<table summary="tree" class="Tree">

<tr><td colspan="2">
_HTML_

print "$Tree\n";
$total=@TREE-1;
if($type>0){$a_="$type";}elsif($type==0){$a_="$namber";}
if($tmplVars{'TpON'}){$TpLink=" / <a href=\"$cgi_f?mode=al2&amp;namber=$a_&amp;rev=$r&amp;$pp\">上記ツリーをトピック表\示</a>\n";}
print <<"_TREE_";
</td></tr></table><!--dum-->
<div class="Caption01r">
[ <a href="$cgi_f?mode=all&amp;namber=$a_&amp;type=0&amp;space=0&amp;$pp">$all_i 上記ツリーを一括表\示</a>
$TpLink ]</div>
<br><hr><h2><a name="F">上記の記事へ返信</a></h2>
_TREE_
if ($r_max && ($total >= $r_max)) {
    print"<h3>返信数の限度を超えたので返信できません。</h3>\n(返信数限度:$r_max 現在の返信数:$total)";
    print" <strong><a href=\"$cgi_f?mode=new&amp;$pp\">[ツリーの新規作成]</a></strong>\n";
} else {
    if ($En && $end_e) {print "$end_ok / 返信不可"; }
    if ($vRSS eq 'RSS') {}
    else{&forms_("T"); }
}
&foot_;
}
}
#--------------------------------------------------------------------------------------------------------------------
# [ツリー表示]
# -> ツリーの一覧を表示する(html_)
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
if($bl >= 0){$Bl="<a href=\"$cgi_f?page=$bl&amp;H=T&amp;$pp$Wf\">"; $Ble="</a>";}else{$Bl=""; $Ble="";}
if($page_end ne $end_data){$Nl="<a href=\"$cgi_f?page=$nl&amp;H=T&amp;$pp$Wf\">";$Nle="</a>";}else{$Nl=""; $Nle="";}
    $obj_template->process('comtop.inc.tpl');
print <<"_HTML_";
<li>$new_t時間以内の記事は $new_i で表\示されます。</li>
<li>$all_i をクリックするとそのツリーを一括で表\示します。</li>
</ul>$Henko<hr>
_HTML_
if($cou){
        print "<div class=\"Counter\">" . &con_() . "</div><br>\n";
}
print"<div class=\"Caption03l\">全 $total ツリー中 $Pg ～ $Pg2 番目を表\示</div>\n";
$Plink="<div class=\"Caption01c\"><strong>全ページ</strong> /\n"; $a=0;
for($i=0;$i<=$page_;$i++){
    $af=$page/$a_max;
    if($i != 0){$Plink.=" ";}
    if($i eq $af){$Plink.="[<strong>$i</strong>]\n";}else{$Plink.="[<a href=\"$cgi_f?page=$a&amp;H=T&amp;$pp$Wf\">$i</a>]\n";}
    $a+=$a_max;
}
$Plink.="</div>\n";
if($Res_T==1){$OJ1="<a href=\"$cgi_f?H=T&amp;W=W&amp;$pp\">返信最新順</a>"; $OJ2="投稿順"; $OJ3="<a href=\"$cgi_f?H=T&amp;W=R&amp;$pp\">記事数順</a>";}
elsif($Res_T==2){$OJ1="<a href=\"$cgi_f?H=T&amp;W=W&amp;$pp\">返信最新順</a>"; $OJ2="<a href=\"$cgi_f?H=T&amp;W=T&amp;$pp\">投稿順</a>"; $OJ3="記事数順";}
else{$OJ1="返信最新順"; $OJ2="<a href=\"$cgi_f?H=T&amp;W=T&amp;$pp\">投稿順</a>"; $OJ3="<a href=\"$cgi_f?H=T&amp;W=R&amp;$pp\">記事数順</a>";}
print"<div class=\"Caption01r\">親記事の順番 [ $OJ1 / $OJ2 / $OJ3 ]</div>\n";
print"$Plink\n<hr class=\"Hidden\">\n";
foreach ($page .. $page_end) {
    ($T,$namber,$date,$name,$email,$d_may,$comment,$url,
        $space,$end,$type,$del,$ip,$tim,$Se)=split(/<>/,$NEW[$_]);
        $email =~ s/@/$atchange/;
    if(($time_k - $tim) > $new_t*3600){$news="$hed_i";}else{$news="$new_i";}
if((!$name)||($name eq ' ')||($name eq '　')){$name=$noname;}
    if($email && $Se < 2){$name="$name <a href=\"mailto:$SPAM$email\">$AMark</a>";}
    ($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
    ($ICON,$ICO,$font,$hr)=split(/\|/,$TXT);
    ($txt,$sel,$yobi)=split(/\|\|/,$SEL);
    if(@ico3 && $Icon && ($ICON ne "" || $comment=~/<br>\(携帯\)$/)){
        if($I_Hei_m){$WHm=" width=\"$I_Wid_m\" height=\"$I_Hei_m\"";}
        if($ICON ne ""){if($ICON=~ /m/){$ICON=~ s/m//; $mICO=$mas_m[$ICON];}else{$mICO=$ico3[$ICON];}}
        elsif($Icon && $comment=~/<br>\(携帯\)$/){$mICO="$Ico_km";}
        $news.="<img src=\"$IconDir\/$mICO\" border=\"0\"$WHm>";
    }
    if($d_may eq ""){$d_may="$notitle";}
    if($yobi){$yobi="[ID:$yobi]";}
    if($txt){$Txt="$TXT_T:[$txt]　";}else{$Txt="";}
    if($sel){$Sel="$SEL_T:[$sel]　";}else{$Sel="";}
    if($Txt || $Sel ||($Txt && $Sel)){if($TS_Pr==0){$d_may="$Txt$Sel/"."$d_may";}}
    if(length($d_may)>$t_max){$d_may=substr($d_may,0,($t_max-2));$d_may="$d_may.."; }
    $date=substr($date,2,19);
if((!$name)||($name eq ' ')||($name eq '　')){$name=$noname;}
    print <<"_HTML_";
<br>
<table class="Tree" summary="Tree" cellspacing="0" cellpadding="0" border="0">
<tr><td class="Highlight" width="1\%">
<a href="$cgi_f?mode=all&amp;namber=$namber&amp;type=$type&amp;space=$space&amp;$pp">$all_i</a></td>
<td class="Highlight" width="99\%"><a href="$cgi_f?mode=one&amp;namber=$namber&amp;type=$type&amp;space=$space&amp;$pp">$news $d_may</a>
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
            if(@ico3 && $Icon &&($rICON ne "" || $rcom=~/<br>\(携帯\)$/)){
                if($I_Hei_m){$WHm=" width=\"$I_Wid_m\" height=\"$I_Hei_m\"";}
                if($rICON ne ""){if($rICON=~ /m/){$rICON=~ s/m//; $mrICO=$mas_m[$rICON];}else{$mrICO=$ico3[$rICON];}}
                elsif($Icon && $rcom=~/<br>\(携帯\)$/){$mrICO="$Ico_km";}
                $news.="<img src=\"$IconDir\/$mrICO\" border=\"0\"$WHm>";
            }
            if($rdm eq ""){$rdm="$notitle"; }
            if($yobi){$yobi="[ID:$yobi]";}
            if($txt){$Txt="$TXT_T:[$txt]　";}else{$Txt="";}
            if($sel){$Sel="$SEL_T:[$sel]　";}else{$Sel="";}
            if($Txt || $Sel ||($Txt && $Sel)){if($TS_Pr==0){$rdm="$Txt$Sel/"."$rdm";}}
            if(length($rdm)>$t_max){$rdm=substr($rdm,0,($t_max-2)); $rdm="$rdm..";}
            print "</td></tr><tr><td></td><td nowrap>\n";
            if($Keisen){print"$Sen";}
            else{
                $rspz=$rsp/15*$zure;
                print "." x $rspz;
            }
            print"<a href=\"$cgi_f?mode=one&amp;namber=$rnam&amp;type=$rtype&amp;space=$rsp&amp;$pp\">$news $rdm</a>\n";
if((!$rname)||($rname eq ' ')||($rname eq '　')){$rname=$noname;}
            print"/ $rname :$rd <span class=\"ArtId\">(#$rnam)</span> $re$Pr\n";
            $res++;
            if($R{$namber}==$res){last;}
        }
    }
    print "</td></tr></table>\n";
}
print "<hr width=\"95%\">\n";
&allfooter("ツリー$a_max");
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [ツリー一括表示]
# -> ツリーの関連記事を表示する(all_)
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
if($cou){
        print "<div class=\"Counter\">" . &con_() . "</div><br>\n";
}
print<<"_ALLTOP_";
<div class="Caption03l">ツリー一括表\示$IcCom</div>
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
                if($s eq $nsp && $nam > $n && $i != 1){$b_="<a href=\"\#$n\">▲[ $n ]</a> / ";}
                if($s eq $psp && $nam < $n && $i == 1){$n_.="<a href=\"\#$n\">▼[ $n ]</a>\n";}
            }
        if($i==1){$rs=1;}
        }
        $ResNo=$sp/15;
        &design($nam,$date,$name,$email,$d_may,$comment,$url,$sp,$end,$ty,$del,$Ip,$tim,$ico,
            $Ent,$fimg,$ICON,$ICO,$font,$hr,$txt,$sel,$yobi,$Se,$ResNo,"T2");
        $ALLTREE.="$HTML";
if((!$name)||($name eq ' ')||($name eq '　')){$name=$noname;}
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
        if($txt){$Txt="$TXT_T:[$txt]　";}else{$Txt="";}
        if($sel){$Sel="$SEL_T:[$sel]　";}else{$Sel="";}
        if($Txt || $Sel ||($Txt && $Sel)){if($TS_Pr==0){$d_may="$Txt$Sel/"."$d_may";}}
        if(length($d_may)>$t_max){$d_may=substr($d_may,0,($t_max-2));$d_may="$d_may..";}
        if(@ico3 && $Icon && ($ICON ne "" || $comment=~/<br>\(携帯\)$/)){
            if($I_Hei_m){$WHm=" width=\"$I_Wid_m\" height=\"$I_Hei_m\"";}
            if($ICON ne ""){if($ICON=~ /m/){$ICON=~ s/m//; $mICO=$mas_m[$ICON];}else{$mICO=$ico3[$ICON];}}
            elsif($Icon && $comment=~/<br>\(携帯\)$/){$mICO="$Ico_km";}
            $news.="<img src=\"$IconDir\/$mICO\" border=\"0\"$WHm>";
        }
if((!$name)||($name eq ' ')||($name eq '　')){$name=$noname;}
        print"<a href=\"#$nam\">$news $d_may</a>\n";
        print"/$name ($date) $yobi<span class=\"ArtId\">(#$nam)</span> $end$Pr</td></tr><tr><td>\n";
    }
}
print"</td></tr></table><br>\n";
print"$ALLTREE</div>";
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [ログ書きこみ処理]
# -> ログに記事を書き込む(wri_)
#
sub wri_ {
    if ($KLOG) {&er_('oldlogs');}
    &check_;
    if ($FORM{"PV"} && ($FLAG == 0)) {
        &get_uid();
        &hed_("Preview");
        $c_name=$name; $c_email=$email; $ti=$d_may; $c_txt=$txt; $c_sel=$sel;
        $c_ico=$CICO; $c_hr=$hr; $c_font=$font; $c_key=$delkey;
        $com=$comment; $com=~ s/<br>/\n/g;
        if (($com =~ /^<pre>/) && ($com =~ /<\/pre>$/)) {$Z = " checked"; }
        else {$T = " checked"; }
        $c_url = $url;
        $FORM_E = "";
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
            if ($FORM{"AgSg"}) {$HTML .= "記事ソ\ート:上げる(age)"; }
            else {$HTML .= "記事ソ\ート:下げる(sage)"; }
        }
        print<<"_PV_";
<h2>プレビュー</h2>
$HTML
<form action="$cgi_f" method="$met"$FORM_E>
<input type="submit" value="送信 O K"> / <strong>[<a href="#F">書き直す</a>]</strong>
<br><a name="F"></a>
<h2>▽ 書き直す ▽</h2>
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
    $comment.="<br>(携帯)";
}
if($UID){
    if ($Ag) { 
        $pUID = $Ag;
    } else {
        $pUID = Forum->cgi->cookie('UID');
        if ($pUID) {
            $pUID = 'n';
        }
    }
    if ($pUID eq "n") {
        &er_('cookieoff');
    }
}
&set_;
$epasswd = Forum->MigUtils->to_hash($FORM{'delkey'});
if ($pUID) {
    &set_("I", "$pUID");
}
if($tag){
    $comment=~ s/\&lt\;/</g;
    $comment=~ s/\&gt\;/>/g;
    $comment=~ s/\&quot\;/\"/g;
    $comment=~ s/<>/\&lt\;\&gt\;/g;
}
if($locks){&lock_($lockf);}
if($M_Rank){&rank;}
open(LOG,"$log") || &er_("Can't open $log");
@lines = <LOG>;
close(LOG);
$NOWTIME=time; &time_($NOWTIME);
($knum,$kd,$kname,$kem,$ksub,$kcom)=split(/<>/,$lines[0]);
$namber=$knum+1;
if($kd eq "" && $kcom eq ""){shift(@lines);}
if($mas_c){$E=0;}else{$E=1;}
$oya=0; @new=(); $SeMail=""; $WR=0; $R=~ s/:/：/g; $SIZE=0;
$txt=~ s/\:/：/g; $sel=~ s/\:/：/g; $txt=~ s/\|\|/｜｜/g; $sel=~ s/\|\|/｜｜/g; 
if($file){$SIZE+=-s "$i_dir/$file";}
if($o_mail){if($send && $FORM{'pub'}==0){$send=2;}elsif($send==0 && $FORM{'pub'}==0){$send=3;}}
if($smile){&smile_encode($comment);}
$new_="$namber<>$date<>$name<>$email<>$d_may<>$comment\t$userenv<>$url<>$space<>$end<>$type<>$epasswd<>";
$new_.="$Ip:$file:$E:$TL:$ICON\|$ICO\|$font\|$hr\|:$txt\|\|$sel\|\|$pUID\|\|:$R:<>$time_k<>$send<>\n";
#new_ = 投稿データ、$lines = ログ、@new=出力データ
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
            if($sml==2 || $sml==1){if($SeMail !~ /$mail/){$SeMail[$MAIL_TO]=$mail; $MAIL_TO++;}}
#			if($sml==2 || $sml==1){if($SeMail !~ /$mail/){if($q_mail){$SeMail.=" $mail";}else{$SeMail.=",$mail";}}}
            $new_line="$lines[$_]";
            if ($he_tp) {
                if (Forum->MigUtils->match_hash($de, $de, $FORM{'delkey'}) == 0) {
                    &er_('notcreator',"1");
                }
            }
            if(($nam eq "$kiji" && $oya==0) && $FORM{'N'} eq ""){push(@r_data,$new_); $oya=1;}
            $resres=1; $res_process=1;
            if($FORM{"AgSg"}==0){push(@new,@r_data); push(@new,$new_line);}
        }elsif($ty eq "$type"){
            if($sml==2 || $sml==1){if($SeMail !~ /$mail/){$SeMail[$MAIL_TO]=$mail; $MAIL_TO++;}}
#			if($sml==2 || $sml==1){if($SeMail !~ /$mail/){if($q_mail){$SeMail.=" $mail";}else{$SeMail.=",$mail";}}}
            if(($nam eq "$kiji" && $oya==0)||($ty eq "$kiji" && $oya==0 && $space > 15) && $FORM{'N'} eq ""){
                push(@r_data,$new_); $oya=1;
            }
            push(@r_data,$lines[$_]);
            if ($he_tp) {
                if (Forum->MigUtils->match_hash($de, $de, $FORM{'delkey'}) == 0) {
                    &er_('notcreator',"1");
                }
            }
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
            if($sml==2 || $sml==1){if($SeMail !~ /$mail/){$SeMail[$MAIL_TO]=$mail; $MAIL_TO++;}}
#			if($sml==2 || $sml==1){if($SeMail !~ /$mail/){if($q_mail){$SeMail.=" $mail";}else{$SeMail.=",$mail";}}}
            if(!$res_process){push(@new,$new_);$res_process=1;}
            $oya=1;
        }
        if($ON){
            if($i && -e "$i_dir/$i" && $LogDel){unlink("$i_dir/$i");}
            if($klog_s){unshift(@KLOG,$lines[$_]);}
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
if ($klog_s && @KLOG) {
    &log_;
}
if(-e $lockf){rmdir($lockf);}
if($t_mail || $o_mail){&mail_;}
if($H eq "F" && $tpend && $type){$FORM{"namber"}=$type; $space=0; &all2;}
    if ($conf{'rss'} eq 1) {&RSS; }
}
#--------------------------------------------------------------------------------------------------------------------
# [記事編集]
# -> 記事編集のフォームを出力(hen_)
#
sub hen_ {
    if ($KLOG) {&er_('oldlogs'); }
    if ($mo eq "") {
        &er_('edit_not_allowed');
    } elsif ($mo == 1) {
        if (Forum->user->group_check('admin') == 0) {
            &er_('invpass');
        }
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
                if (Forum->user->group_check('admin') != 0) {
                    $ok = 'm';
                } elsif (Forum->MigUtils->match_hash($de, $de, $FORM{'delkey'}) == 0) {
                    &er_('invpass');
                } else {
                    $ok = 'y';
                }
                $hen_l = "$cgi_f?$pp";
                $Lcom = "";
            } else {
                $hen_l = "$cgi_f?mode=del&amp;pass=$FORM{'pass'}&amp;$pp";
                $Lcom = "管理モードに";
            }
            if ($s && $end_f && (($end_c == 0) ||
                (Forum->user->group_check('admin') != 0)) &&
                $t) {
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
 *関連するレス記事をメールで受信しますか? <select name="send">
<option value="1"$Y>はい
<option value="0">いいえ
</select> 
 アドレス <select name="pub">
<option value="0">非表\示
<option value="1"$Pch>表\示
</select></td></tr>
_MAIL_
            }
            if ($tag) {
                $comment =~ s/</\&lt\;/g;
                $comment =~ s/>/\&gt\;/g;
            }
            ($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R) = split(/:/,$i);
            print <<"_HTML_";
<h2>記事No[$namber] の編集</h2>
$msg
<form action="$cgi_f" method="$met" name="post">$pf
<input type="hidden" name="pass" value="$FORM{'pass'}">
<input type="hidden" name="mode" value="h_w">
<input type="hidden" name="namber" value="$namber"><input type="hidden" name="mo" value="$mo">
<table class="Submittion" summary="form">
<tr><td><strong>お名前</strong></td><td>
<input type="text" name="name" value="$name" size="20" maxlength="100"></td></tr>
<tr><td><strong>E メール</strong></td><td>
<input type="text" name="email" value="$email" size="40" maxlength="100"></td></tr>
$Mbox
_HTML_
            if ($ua_select) {
                if (Forum->user->group_check('admin') != 0) {
                    if ($userenv) {
                        print "<input type=\"hidden\" value=\"$userenv\">";
                    }
                } else {
                    &UAsel;
                }
            }
            print "<tr><td><strong>タイトル</strong></td><td>";
            print "<input type=\"text\" name=\"d_may$actime\" size=\"40\" value=\"$d_may\" maxlength=\"100\"></td></tr>";
            print "<tr><td><strong>URL</strong></td><td><input type=\"text\" name=\"url\" value=\"http://$url\" size=\"60\" maxlength=\"100\"></td></tr>";
            print "<tr><td colspan=\"2\"><strong>コメント</strong>";
            print "通常モード/<input type=\"radio\" name=\"pre\" value=\"0\" $T>";
            print "図表\モード/<input type=\"radio\" name=\"pre\" value=\"1\" $Z>";
            $com=$comment;
            &smile_decode($com);

            print '(適当に改行を入れて下さい)<br>' . "\n" . '<textarea name="comment" rows="15" cols="80" ';
            if ($BBFACE) {
                print ' onselect="storeCaret(this);" onclick="storeCaret(this);" onkeyup="storeCaret(this);"';
            }
            print ">$com</textarea></td></tr>";
            if ($BBFACE) {print "$BBFACE"; }

            ($ICON,$ICO,$font,$hr)=split(/\|/,$TXT);
            ($txt,$sel,$yobi)=split(/\|\|/,$SEL);
            if($font){
                print "<tr><td>文字色</td><td>\n";
                foreach (0 .. $#fonts) {
                    if($font eq ""){$font="$fonts[0]";}
                    print"<input type=\"radio\" name=\"font\" value=\"";
                    if($font eq "$fonts[$_]"){print"$fonts[$_]\" checked><span class=\"col_$fonts[$_]\">■</span>\n";}
                    else{print"$fonts[$_]\"><span class=\"col_$fonts[$_]\">■</span>\n";}
                }
                print"</td></tr>";
            }
            if($hr){
                print"<tr><td>枠線色</td><td>\n";
                foreach (0 .. $#hr) {
                    if($hr eq ""){$cr="$hr[0]";}
                    print "<input type=\"radio\" name=\"hr\" value=\"";
                    if($hr eq "$hr[$_]"){print"$hr[$_]\" checked><font color=\"$hr[$_]\">■</font>\n";}
                    else{print"$hr[$_]\"><font color=\"$hr[$_]\">■</font>\n";}
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
                print"</select> <small>(画像を選択/";
                print"<a href=\"$cgi_f?mode=img&amp;$pp\"$TGT>サンプル一覧</a>)</small></td></tr>\n";
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
</td></tr><tr><td colspan="2" align="right"><input type="submit" value=" 編 集 " >
_HTML_
            print "<input type=\"reset\" value=\"リセット\"></td></tr></table></form></ul><hr width=\"95\%\">";
            last;
        }
    }
    close(DB);
    &foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [編集記事置換]
# -> 編集内容を置き換える(h_w_)
#
sub h_w_ {
    if ($KLOG) {
        # cannot write to old log files
        &er_('oldlogs');
    }
    if ((Forum->user->group_check('admin') == 0) && $mo) {
        &er_('invpass');
    }
    ($comment, $com_) = split('\t', $comment);
    if (($E_[0] eq "") && ($I_[0] eq "")) {
        $delkey = $FORM{'pass'};
        &check_;
        if ($tag) {
            $comment =~ s/\&lt\;/</g;
            $comment =~ s/\&gt\;/>/g;
            $comment =~ s/\&quot\;/\"/g;
            $comment =~ s/<>/\&lt\;\&gt\;/g;
        }
    }
    $comment =~ s/\t//g;
    if ($locks) {
        &lock_("$lockf");
    }
    if ($FORM{"pre"}) {
        $comment = '<pre>' . $comment . '</pre>';
    }
    @new = ();
    $flag = 0;
    $SIZE = 0;
    open(DB, "$log");
    while ($line = <DB>) {
        $line =~ s/\n//g;
        ($knam, $k, $kname, $kemail, $kd_may, $kcomment, $kurl,
            $ks, $ke, $kty, $kd, $ki, $kt, $sml) = split(/<>/, $line);
        if ($k eq "") {
            push(@new, "$line\n");
            next;
        }
        if ($namber eq "$knam") {
            if ($mo eq "") {
                $de = $kd;
                $FORM{'delkey'} = $FORM{'pass'};
                if (Forum->user->group_check('admin') != 0) {
                    $ok = 'm';
                } elsif (Forum->MigUtils->match_hash($epasswd, $de, $FORM{'delkey'}) == 0) {
                    &er_('invpass', "1");
                } else {
                    $ok = 'y';
                }
            }
            if ($EStmp) {
                &time_("");
                $EditCom = "$date 編集";
                if ($mo || ($ok eq "m")) {
                    $EditCom .= "(管理者)";
                } else {
                    $EditCom .= "(投稿者)";
                }
                if ($comment !~ /([0-9][0-9]):([0-9][0-9]):([0-9][0-9]) 編集/) {
                    $EditCom .= "<br><br>";
                } else {
                    $EditCom .= "<br>";
                }
                $comment = $EditCom . $comment . "\t" . $userenv;
            }
            ($KI, $Kico, $E, $Kfi, $KTX, $KS, $KR) = split(/:/, $ki);
            ($Ktxt, $Ksel, $Kyobi) = split(/\|\|/, $KS);
            if ($o_mail) {
                if ($send && ($FORM{'pub'} == 0)) {
                    $send = 2;
                } elsif (($send == 0) && ($FORM{'pub'} == 0)) {
                    $send = 3;
                }
            }
            $line = "$namber<>$k<>$name<>$email<>$d_may<>$comment<>$url<>$ks<>$end<>$kty<>$kd";
            $line .= "<>$KI:$Kico:$E:$Kfi:$ICON|$ICO|$font|$hr|:$txt\|\|$sel\|\|$Kyobi\|\|:$KR:<>$kt<>$send<>";
            $flag = 1;
        } elsif (@E_) {
            ($KI, $Kico, $E, $Kfi, $KTX, $KS, $KR) = split(/:/, $ki);
            $EF = 0;
            foreach $ENT (@E_) {
                if ($ENT eq $knam) {
                    $EF = 1;
                    if ($E) {
                        $EE = 0;
                    } else {
                        $EE = 1;
                    }
                    last;
                }
            }
            if ($EF) {
                if ($mo eq "") {
                    $de = $kd;
                    $FORM{'delkey'} = $FORM{'pass'};
                    if (Forum->MigUtils->match_hash($epasswd, $de, $FORM{'delkey'}) == 0) {
                        &er_('invpass',"1");
                    }
                }
                $line = "$knam<>$k<>$kname<>$kemail<>$kd_may<>$kcomment<>$kurl<>$ks<>$ke<>$kty<>$kd<>$KI:$Kico:$EE:$Kfi:$KTX:$KS:$KR:<>$kt<>$sml<>";
                $flag = 1;
            }
        } elsif (@I_) {
            ($KI, $Kico, $E, $Kfi, $KTX, $KS, $KR) = split(/:/, $ki);
            $EF = 0;
            foreach $ENT (@I_) {
                if ($ENT eq $knam) {
                    $EF = 1;
                    last;
                }
            }
            if ($EF) {
                if ($mo eq "") {
                    $de = $kd;
                    $FORM{'delkey'} = $FORM{'pass'};
                    if (Forum->MigUtils->match_hash($epasswd, $de, $FORM{'delkey'}) == 0) {
                        &er_('invpass',"1");
                    }
                }
                if ($Kico && (-e "$i_dir/$Kico")) {
                    unlink("$i_dir/$Kico");
                }
                $Kico = "";
                $E = 0;
                $Kfi = "";
 			    $line = "$knam<>$k<>$kname<>$kemail<>$kd_may<>$kcomment<>$kurl<>$ks<>$ke<>$kty<>$kd<>$KI:$Kico:$EE:$Kfi:$KTX:$KS:$KR:<>$kt<>$sml<>";
                $flag = 1;
            }
        } elsif ($FORM{'UP'}) {
            $UPt = $FORM{'UPt'};
            $UP = $FORM{'UP'};
            ($KI, $Kico, $E, $Kfi, $KTX, $KS, $KR) = split(/:/, $ki);
            if ($UPt) {
                if (($UPt eq $kty) && $Kico) {
                    $SIZE += (-s "$i_dir/$Kico");
                }
            } else {
                if (($UP eq $kty) && $Kico) {
                    $SIZE += (-s "$i_dir/$Kico");
                }
            }
            if ($UP eq $knam) {
                if ($mo eq "") {
                    $de = $kd;
                    $FORM{'delkey'} = $FORM{'pass'};
                    if (Forum->MigUtils->match_hash($epasswd, $de, $FORM{'delkey'}) == 0) {
                        &er_('invpass',"1");
                    }
                }
 			    if ($mas_c) {
                    $E = 0;
                } else {
                    $E = 1;
                }
                $SIZE += (-s "$i_dir/$file");
                $line = "$knam<>$k<>$kname<>$kemail<>$kd_may<>$kcomment<>$kurl<>$ks<>$ke<>$kty<>$kd<>$KI:$file:$E:$TL:$KTX:$KS:$KR:<>$kt<>$sml<>";
                $flag = 1;
            }
        }
        push(@new, "$line\n");
    }
    close(DB);
    if ($SIZE && ($max_or < int($SIZE/1024))) {
        &er_('uplimit', "1");
    }
    if ($flag == 0) {
        &er_('editinvid', "1");
    }
    if ($flag == 1) {
        open(DB, ">$log");
        print DB @new;
        close(DB);
    }
    if (-e $lockf) {
        rmdir($lockf);
    }
    if (@E_ || @I_ || $FORM{'UP'}) {
        if ($mo && (@E_ || @I_)) {
            &ent_;
        } else {
            if (@I_) {
                $msg = "<h3>ファイル削除</h3>";
                $FORM{"del"} = $I_[0];
            } elsif ($FORM{'UP'}) {
                $msg = "<h3>ファイルアップ完了</h3>$Henko";
                if ($mo) {
                    $kiji = $FORM{'UP'};
                } else {
                    $FORM{"del"} = $FORM{'UP'};
                }
            }
            $delkey = $FORM{"pass"};
            &hen_;
        }
    } elsif ($mo) {
        print Forum->cgi->header();
        Forum->template->set_vars('mode_id', 'admin');
        Forum->template->set_vars('mode_adm', 'editpost');
        Forum->template->process('htmlhead.tpl', \%tmplVars);
        print "<h3>編集完了</h3>";
        Forum->template->process('htmlfoot.tpl', \%tmplVars);
        exit;
    } else {
        $msg = "<h3>以下のように編集完了</h3>";
        $delkey = $FORM{"pass"};
        $FORM{"del"} = $namber;
        &hen_;
    }
    if ($conf{'rss'} eq 1) {
        &RSS;
    }
}
#--------------------------------------------------------------------------------------------------------------------
# [スレッド表示]
# -> スレッド形式で記事の一覧を表示する(alk_)
#
sub alk_ {
    $thread_oya = 0;
    if ($FORM{'page'} eq '') {
        $page = 0;
    } else {
        $page = $FORM{'page'};
    }
    @NEW = ();
    @RES = ();
    $List = "";
    $news = "";
    $On = 1;
    %N = ();
    %d = ();
    %n = ();
    $RS = 0;
    $K = 1;
    $TOya = 0;
    open(LOG, "$log") || &er_("Can't open $log");
    while (<LOG>) {
        ($namber, $date, $name, $email, $d_may, $comment, $url,
            $space, $end, $type, $del, $ip, $tim) = split(/<>/, $_);
        if ($type) {
            if ($On) {
                if (($time_k - $tim) > ($new_t * 3600)) {
                    $n{$type} = $hed_i;
                } else {
                    $n{$type} = $up_i_;
                    $On = 0;
                }
            }
            $tim = sprintf('%011d', $tim);
            if ($date) {
                $R{$type} .= "$tim<>$_";
            }
            $N{$type}++;
            $RS++;
        } else {
            if ($n{$namber} eq "") {
                if (($time_k - $tim) > ($new_t*3600)) {
                    $n{$namber} = $hed_i;
                } else {
                    $n{$namber} = $new_i;
                }
            }
            if ($tim eq "") {
                $tim = "$TIM";
            }
            $tim = sprintf("%011d", $tim);
            if ($Res_T == 2) {
                $tim = $N{$namber};
                $tim = sprintf("%05d", $tim);
            }
            push(@NEW, "$tim<>$_");
            ($Ip, $ico, $Ent, $fimg, $TXT, $SEL, $R) = split(/:/, $ip);
            ($ICON, $ICO, $font, $hr) = split(/\|/, $TXT);
            ($txt, $sel, $yobi) = split(/\|\|/, $SEL);
            if ($txt) {
                $Txt = "$TXT_T:[$txt]　";
            } else {
                $Txt = "";
            }
            if ($sel) {
                $Sel = "$SEL_T:[$sel]　";
            } else {
                $Sel="";
            }
            if ($d_may eq "") {
                $d{$namber} = $notitle;
            } else {
                $d{$namber} = $d_may;
            }
            if ($Txt || $Sel || ($Txt && $Sel)) {
                if ($TS_Pr == 0) {
                    $d{$namber} = "$Txt$Sel/" . "$d{$namber}";
                }
            }
            if ($N{$namber} eq "") {
                $N{$namber} = 0;
            }
            if ($Top_t && ($Res_T == 0) && ($Rno < $LiMax)) {
                $Rno++;
                $PAH = $alk_su * $K;
                if (($PAH) < $Rno) {
                    $PAL = "&amp;page=$PAH";
                    $K++;
                }
                $L_3 = $Rno-1;
                if ((($page + $alk_su) >= $Rno) && (($page) < $Rno)) {
                    $List .= "<a href=\"#$TOya\">$n{$namber}$d{$namber}($N{$namber})</a> |\n";
                    $TOya++;
                } else {
                    $List .= "<a href=\"$cgi_f?mode=res&amp;namber=$namber&amp;page=&amp;$pp\">$n{$namber}$d{$namber}($N{$namber})</a> |\n";
                }
            }
            $news = "";
            $On = 1;
        }
        $TIM = $tim;
    }
    close(LOG);

    if ($Res_T) {
        @NEW = sort(@NEW);
        @NEW = reverse(@NEW);
        if ($Top_t) {
            foreach (0..$#NEW) {
                if ($Rno > $LiMax) {last;}
                ($T, $namber, $date, $name, $email, $d_may, $comment, $url,
                    $space, $end, $type, $del, $ip, $tim) = split(/<>/, $NEW[$_]);
                $Rno++;
                $PAH = $alk_su * $K;
                if (($PAH) < $Rno) {
                    $PAL = "&amp;page=$PAH";
                    $K++;
                }
                $L_3 = $Rno-1;
                if ((($page + $alk_su) >= $Rno) && (($page) < $Rno)) {
                    $List .= "<a href=\"#$L_3\">$n{$namber}$d{$namber}($N{$namber})</a> |\n";
                } else {
                    $List .= "<a href=\"$cgi_f?mode=res&amp;namber=$namber&amp;page=&amp;$pp\">$n{$namber}$d{$namber}($N{$namber})</a> |\n";
                }
            }
        }
    }

    $total = @NEW;
    $NS = $RS + $total;
    $page_ = int(($total - 1) / $alk_su);
    $end_data = @NEW - 1;
    $page_end = $page + ($alk_su - 1);
    if ($page_end >= $end_data) {
        $page_end = $end_data;
    }
    $Pg = $page + 1;
    $Pg2 = $page_end + 1;
    $nl = $page_end + 1;
    $bl = $page - $alk_su;

    print Forum->cgi->header();
    Forum->template->set_vars('Top_t', $Top_t);
    Forum->template->set_vars('new_t', $new_t);
    Forum->template->set_vars('new_i', $new_i);
    Forum->template->set_vars('up_i_', $up_i_);
    Forum->template->set_vars('Henko', $Henko);
    Forum->template->set_vars('cou', $cou);
    Forum->template->set_vars('Pg', $Pg);
    Forum->template->set_vars('Pg2', $Pg2);
    Forum->template->set_vars('thread_total', $total);
    if ($cou) {
        Forum->template->set_vars('counter', &con_());
    }
    Forum->template->set_vars('Res_T', $Res_T);
    Forum->template->set_vars('cgi_f', $cgi_f);
    Forum->template->set_vars('pp', $pp);
    Forum->template->set_vars('alk_su', $alk_su);
    Forum->template->set_vars('page_', $page_);
    Forum->template->set_vars('Wf', $Wf);
    Forum->template->set_vars('af', $page / $alk_su);
    Forum->template->set_vars('List', $List);
    Forum->template->set_vars('PAGE', $page / $alk_su);
    $obj_template->process('alk_thread_disp.tpl', \%tmplVars);

    if ($bl >= 0) {
        $Bl = "<a href=\"$cgi_f?mode=alk&amp;page=$bl&amp;$pp$Wf\">";
        $Ble = "</a>";
    }
    if ($page_end ne $end_data) {
        $Nl = "<a href=\"$cgi_f?mode=alk&amp;page=$nl&amp;$pp$Wf\">";
        $Nle = "</a>";
    }

    $LinkNo = "";
    foreach ($page .. $page_end) {
        ($T, $nam, $date, $name, $email, $d_may, $comment, $url,
            $sp, $end, $ty, $del, $ip, $tim, $Se) = split(/<>/, $NEW[$_]);
        ($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
        ($ICON,$ICO,$font,$hr)=split(/\|/,$TXT);
        ($txt,$sel,$yobi)=split(/\|\|/,$SEL);
        &design($thread_oya,$date,$name,$email,$d_may,$comment,$url,$sp,$end,$ty,$del,$Ip,$tim,$ico,
            $Ent,$fimg,$ICON,$ICO,$font,$hr,$txt,$sel,$yobi,$Se,"","TR");
        print"<hr><br>\n";
        if (($thread_oya > 0) && (! $type)) {
            print"</div>\n</div>\n";
        }
        if ($type) {
            print"</div>\n";
        }
        print "$HTML";
        @RES = split(/\n/, $R{$nam});
        $PNO = 0;
        @RES = sort(@RES);
        if (@RES) {
            $Rn = $alk_rm;
            $RC = @RES;
            $Pg = $RC - $alk_rm + 1;
            if ($Pg <= 0) {
                $Pg = 1;
            }
            print "<hr><div class=\"Caption01l\">全返信 $RC 件中 $Pg ～ $RC 番目を表\示</div><br>\n";
            $RC_ = int($RC / $ResHy);
            $res = 0;
            $Dk = 0;
            $ResNo = $Pg - 1;
            $PgSt = $Pg - 1;
            $PgEd = $RC - 1;
            foreach ($PgSt..$PgEd) {
                ($T,$rnam,$rd,$rname,$rmail,$rdm,$rcom,$rurl,
                    $rsp,$re,$rtype,$del,$rip,$rtim,$Se)=split(/<>/,$RES[$_]);
                if ($nam eq "$rtype") {
                    $ResNo++;
                    ($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$rip);
                    ($ICON,$ICO,$font,$hr)=split(/\|/,$TXT);
                    ($txt,$sel,$yobi)=split(/\|\|/,$SEL);
                    $PNO = int($ResNo / $ResHy) * $ResHy;
                    &design($rnam,$rd,$rname,$rmail,$rdm,$rcom,$rurl,$rsp,$re,$rtype,$del,$Ip,$rtim,$ico,
                        $Ent,$fimg,$ICON,$ICO,$font,$hr,$txt,$sel,$yobi,$Se,$ResNo,"TR");
                    print "<hr class=\"Hidden\">\n$HTML";
                }
                if ($ResNo == $N{$nam}) {
                    last;
                }
            }
            if ($RC) {
                print "<hr><div class=\"Caption01r\">返信用スレッド表\示\n";
                $a = 0;
                for ($i = 0; $i <= $RC_; $i++) {
                    if ($i) {
                        $St = $i * $ResHy;
                        $En = $St + $ResHy - 1;
                        if (($RC + 1) <= $En) {
                            $En = $RC;
                        }
                    } else {
                        $En = $ResHy - 1;
                        if ($RC < $En) {
                            $En = $RC;
                        }
                        $St = "親";
                    }
                    print "[<a href=\"$cgi_f?mode=res&amp;namber=$nam&amp;rev=$r&amp;page=$a&amp;$pp\">$St ～ $En</a>]\n";
                    $a += $ResHy;
                }
                if ($Dk) {
                    print "<br>($Dk件は削除記事)\n";
                }
                print "</div>";
            }
        }
        $LinkNo = $nam;
        print "</div>\n";
        $thread_oya++;
    }
    print "<hr>\n";
    &allfooter("スレッド$alk_su");
    &foot_;
}

#--------------------------------------------------------------------------------------------------------------------
# [画像幅取得]
# -> ファイルが画像の場合、ファイルを読み込んで幅を取得します。それ以外のアイコン表示もおこないます(size)
# -> とほほのラウンジを参考にさせていただきました => http://tohoho.wakusei.ne.jp/
#
sub size {
    if (($Ent == 0) && $fimg) {
        $fimg = $no_ent;
        $A = 0;
    }
    if ($_[0]) {
        $FORM{"min"} = 2;
    } else {
        if ($CookOn eq "") {
            $FORM{'min'} = Forum->cgi->cookie('Cmin');
            if ($FORM{'min'}) {
                $FORM{'min'} = 0;
            }
            $CookOn=1;
        }
    }
    $A=0;
    $I=0;
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
        $Pr.="<small>$IW×$IH";
        if($Cg){$kW=$IW;$kH=$IH;}
        else{$Pr.=" =\&gt\; $kW×$kH";}
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
# [許可システム]
# -> アップファイル/記事の表示許可を与えます(ent_)
#
sub ent_ {
    if (Forum->user->group_check('admin') == 0) {
#    if (Forum->user->validate_password_admin($FORM{'pass'}) == 0) {
        &er_('invpass');
    }
#if($FORM{'pass'} ne "$pass"){&er_('invpass');}
&hed_("Permit");
print <<"_ENT_";
<table summary="allow"><tr><th>ファイル/記事表\示許可</th></tr></table><br>
<a href="$cgi_f?$pp"> 掲示板に戻る</a> / <a href="$cgi_f?mode=del&amp;pass=$FORM{"pass"}&amp;$pp">通常管理モード</a>
許可する/未許可にするファイルをチェックし、ボタンを押して下さい。
ファイル削除をチェックしてボタンを押すとファイルのみを削除できます。
記事のみの表\示許可は一度許可済みにすると、未許可に戻せません!

<form action="$cgi_f" method="$met">$pf
<input type="hidden" name="mode" value="ent"><input type="hidden" name="pass" value="$FORM{"pass"}">
<select name="check">
<option value="1">全未許可記事チェック
<option value="2">全許可済記事チェック
<option value="0">チェックをはずす
_ENT_
print <<"_ENT_";
<input type="submit" value="実行"></form><br>
<form action="$cgi_f" method="$met">$pf
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
            print"<th>許可チェック</th><th>投稿者情報</th><th>コメント</th><th>ファイル情報</th><th>ファイル削除</th></tr>\n";
        }
        $check="";	
        if($Ent){$eok="○"; if($FORM{"check"}==2){$check=" checked";}}
        else{$eok="<span class=\"red\">×</span>"; if($FORM{"check"}==1){$check=" checked";}}
        if($ty){$Re="($tyレス)";}else{$Re="";}
if((!$name)||($name eq ' ')||($name eq '　')){$name=$noname;}
        if($email){$name="<a href=\"mailto:$email\">$name</a>";}
        if($url){$url="/<a href=\"http://$url\"$TGT>HP</a>";}
        if(-s "$i_dir/$ico"){$Size = -s "$i_dir/$ico";}else{$Size = 0;}
        $comment =~ s/<br>/ /g; $TB=1;
        if($tag){ $comment =~ s/</&lt;/g; $comment =~ s/>/&gt;/g; }
        if(length($comment) > 100){
            $comment=substr($comment,0,98); $comment=$comment . '..';
            $comment.="<a href=\"$cgi_f?mode=one&amp;namber=$nam&amp;pass=$FORM{'pass'}&amp;$pp\"$TGT>全文</a>";
        }
        if($k){$BG=""; $k=0;}else{$BG=""; $k=1;}
        print <<"_ENT_";
<tr$BG><th><input type="checkbox" name="ENT" value="$nam$check">-$eok</th>
<td nowrap>#$nam $Re<br>├$name [$Ip]<br>
└<small>($date$url)</small></td>
<td>$comment<a href="$cgi_f?mode=one&amp;namber=$nam&amp;$pp"$TGT></a></td>
<td><a href="$i_Url/$ico"$TGT>$ico</a><br>($Size\Bytes)</td>
_ENT_
print "<th><input type=\"checkbox\" name=\"IMD\" value=\"$nam\"></th></tr>";
    $i++;
    if($i==30){print"</table>"; $i=0; $TB=0;}
    }else{next;}
}
close(LOG);
if($TB){print"</table>";}
print "<br><input type=\"submit\" value=\"許可/未許可 ファイル削除\"></form>\n";
&foot_;
}



################################################################################

##------------------------------------------------------------------------------
# con_ - manage counter (display time count)
#  vars : 
#  tmpl : 
sub con_ {
    my $cnt;
    if (($mode eq "") || ($mode eq "alk")) {
        if ($locks) {
            &lock_("$cloc");
        }
        open(NO, "$c_f") || &er_("Can't open $c_f", "1");
        $cnt = <NO>;
        close(NO);
        if (($FORM{'mode'} eq "") && ($FORM{'page'} eq "") &&
            ($ENV{'HTTP_REFERER'} !~ /$cgi_f/)) {
            $cnt++;
            open(NO, ">$c_f") || &er_("Can't write $c_f","1");
            print NO $cnt;
            close(NO);
        }
        if (-e $cloc) {
            rmdir($cloc);
        }
    }
    return $cnt;
}

##------------------------------------------------------------------------------
# er_ - display error notification
#  vars : 
#  tmpl : 
sub er_ {
    my ($errmsg, $unlock) = @_;
    if ((-e $lockf) && ($unlock == 1)) {rmdir($lockf); }
    if ((-e $cloc) && ($unlock == 1)) {rmdir($cloc); }
    if (-e "$i_dir/$file") {unlink("$i_dir/$file"); }
    if ($FORM{"URL"}) {
        ($KURL, $Ag) = split(/::/, $FORM{'URL'});
    }
    Forum->template->set_vars('BG', $BG);
    Forum->template->set_vars('errmsg', $errmsg);
    print Forum->cgi->header();
    $obj_template->process('error.tpl', \%tmplVars);
    exit;
}

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
    $tmplVars{'log'} = $log;
    $tmplVars{'word'} = $word;
    $tmplVars{'NS'} = $NS;
    $tmplVars{'total'} = $total;
    $tmplVars{'RS'} = $RS;
    $obj_template->process('allfooter.tpl', \%tmplVars);
}

##------------------------------------------------------------------------------
# man_ - display manual
#  vars : none
#  tmpl : man.tpl
#  rets : none
sub man_ {
    &hed_("Help");
    $tmplVars{'alk_su'} = $alk_su;
    $tmplVars{'alk_rm'} = $alk_rm;
    $tmplVars{'new_t'} = $new_t;
    $tmplVars{'end_f'} = $end_f;
    $tmplVars{'end_c'} = $end_c;
    $tmplVars{'UID'} = $UID;
    $tmplVars{'SPAM'} = $SPAM;
    $obj_template->process('man.tpl', \%tmplVars);
    exit;
}
##------------------------------------------------------------------------------
# new_ - show form for posting new
#  vars : 
#  tmpl : new.h2.tpl
#  rets : none
sub new_ {
    if (($topok == 0) &&
        (Forum->user->group_check('admin') == 0)) {
        &er_('newpasserr');
    }
    &get_uid();
    &hed_("Write New Message");
    $obj_template->process('new.h2.tpl', \%tmplVars);
    &forms_;
    &foot_;
}

##------------------------------------------------------------------------------
# get_uid - generate UID parameter
#  vars : 
#  tmpl : none
#  rets : uid ($pUID)
sub get_uid {
    if ($UID) {
        $pUID = Forum->cgi->cookie('UID');
        if ($pUID) {
            $pUID = "";
            @UID = ('a'..'z','A'..'Z','0'..'9');
            srand;
            $pUID .= "$UID[int(rand(62))]"; $pUID .= "$UID[int(rand(62))]";
            $pUID .= "$UID[int(rand(62))]"; $pUID .= "$UID[int(rand(62))]";
            $pUID .= "$UID[int(rand(62))]"; $pUID .= "$UID[int(rand(62))]";
            $pUID .= "$UID[int(rand(62))]"; $pUID .= "$UID[int(rand(62))]";
            &set_("I", "$pUID");
        }
        if ($pUID eq "n") {$pUID="未発行"; }
    }
    return $pUID;
}

##------------------------------------------------------------------------------
# hed_ - generate html header
#  vars : (title)
#  tmpl : htmlhead.tpl
#  rets : none
sub hed_ {
    print Forum->cgi->header();
    Forum->template->set_vars('htmltitle', $_[0]);
    Forum->template->set_vars('kiji_exist', $kiji_exist);
    $obj_template->process('htmlhead.tpl', \%tmplVars);
}

##------------------------------------------------------------------------------
# foot_ - generates html footer
#  vars : 
#  tmpl : htmlfoot.tpl
sub foot_ {
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
                        Forum->error->throw_error_user("「$curNW」は使用できません!");
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
        Forum->error->throw_error_user('longmail');
    }
    $email =~ s/\x0D\x0A|\x0D|\x0A//g;
    $url  = $FORM{'url'};
    if (length($url) > 1000) {
        Forum->error->throw_error_user('longurl');
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
    $obj_template->process('password.tpl', \%tmplVars);
    exit;
}

##------------------------------------------------------------------------------
# forms_ - show comment forms
#  vars : 
#  tmpl : 
sub forms_ {
    if ($KLOG) {&er_('cannot_write_oldlogs'); }

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
        $c_name  = Forum->cgi->cookie('name');
        $c_url   = Forum->cgi->cookie('url');
        $c_key   = Forum->cgi->cookie('delkey');
        $c_ico   = Forum->cgi->cookie('ico');
        if ($SEL_C) {$c_sel = Forum->cgi->cookie('sel'); }
        if ($TXT_C) {$c_txt = Forum->cgi->cookie('txt'); }

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
    $tmplVars{'multipart'} = 0;
    $tmplVars{'FORM_PV'} = $FORM{'PV'};
    $tmplVars{'tag'} = $tag;
    $tmplVars{'N_NUM'} = $N_NUM;
    $tmplVars{'nams'} = $nams;
    $tmplVars{'namber'} = $namber;
    $tmplVars{'sp'} = $sp;
    $tmplVars{'Hi'} = $Hi;
    $tmplVars{'c_name'} = $c_name;
    $tmplVars{'c_email'} = $c_email;
    $tmplVars{'c_url'} = $c_url;
    $tmplVars{'NMAX'} = $NMAX;
    $tmplVars{'TMAX'} = $TMAX;
    $tmplVars{'UID'} = $UID;
    $tmplVars{'pUID'} = $pUID;
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
        $tmplVars{'end_c'} = $end_c;
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
  $tmplVars{'icon_1'} = \@ico1;
  $obj_template->process('img_.tpl', \%tmplVars);
  exit;
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
    $obj_template->process('cookdel.tpl', \%tmplVars);
    exit;
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
    &hed_("No$namber の記事表\示");
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
    $tmplVars{'klog_h'} = $klog_h;

    $obj_template->process('read.tpl', \%tmplVars);
    exit;
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
                    &rep_title();
                    &comin_;
                }
            } else {
                if ($k == 1) {
                    $On = 1;
                    $O2 = 1;
                    &rep_title();
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
    &get_uid();
    &hed_("One Thread Res View / $TitleHed / Page: $PAGE");
    $page_ = int($total / $ResHy);
    $end_data = @TOP-1;
    $page_end = $page + ($ResHy - 1);
    if ($page_end >= $end_data) {$page_end = $end_data; }
    $tmplVars{'total'} = $total;
    $tmplVars{'page'} = $page;
    $tmplVars{'page_end'} = $page_end;
    $tmplVars{'cur_page'} = $page / $ResHy;
    $tmplVars{'ResHy'} = $ResHy;
    $tmplVars{'page_'} = $page_;
    $tmplVars{'form_namber'} = $FORM{'namber'};
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

    $bl = $page - $ResHy;
    $tmplVars{'bl'} = $bl;
    $tmplVars{'end_data'} = $end_data;

    if ($mo eq "") {$com = ""; }

    $tmplVars{'total'} = $total;
    $tmplVars{'En'} = $En;
    $tmplVars{'end_e'} = $end_e;
    $obj_template->process('res_.tpl', \%tmplVars);
    if (! ($r_max && ($total > $r_max))) {
        if (! ($En && $end_e)) {
            &forms_("N");
        }
    }
    &foot_;
}

##------------------------------------------------------------------------------
# rep_title - modify title on reply
sub rep_title {
    if ($d_may eq "") {
        $d_may = $notitle;
    } elsif ($d_may =~ /^Re\[\d+\]: ?(.*)$/i) {
        $d_may = $1;
    } elsif ($d_may =~ /^Re: ?(.*)$/i) {
        $d_may = $1;
    }
    $ti = "Re: $d_may";
    $space = $sp;
}

##------------------------------------------------------------------------------
# set_ - set cookie
#  vars : mode, parameter
#  tmpl : 
sub set_ {
    my ($mode) = (@_);
    if ($mode eq 'P') {
        Forum->cgi->add_cookie('-name', $s_pas, '-value', $s_pas, '-expires', '+30d');
    } elsif ($mode eq 'M') {
        Forum->cgi->add_cookie('-name', 'Cmin', '-value', $FORM{'min'}, '-expires', '+30d');
    } elsif ($mode eq 'I') {
        Forum->cgi->add_cookie('-name', 'UID', '-value', $_[1], '-expires', '+1826d');
    } else {
        Forum->cgi->add_cookie('-name', 'name', '-value', $name, '-expires', '+30d');
        Forum->cgi->add_cookie('-name', 'url', '-value', $url, '-expires', '+30d');
        Forum->cgi->add_cookie('-name', 'delkey', '-value', $delkey, '-expires', '+30d');
        Forum->cgi->add_cookie('-name', 'ico', '-value', $ico, '-expires', '+30d');
        if ($SEL_C) {
            Forum->cgi->add_cookie('-name', 'sel', '-value', $sel, '-expires', '+30d');
        }
        if ($TXT_C) {
            Forum->cgi->add_cookie('-name', 'txt', '-value', $txt, '-expires', '+30d');
        }
    }
}

##------------------------------------------------------------------------------
# l_m - create new file with a specified name
#  vars : 
#  tmpl : 
sub l_m {
    my ($fname) = @_;
    open(DB, ">$fname") || &er_("Can't make $fname");
    print DB "";
    close(DB);
    chmod(0666, $fname);
}

##------------------------------------------------------------------------------
# log_ - write data to "previous" logs
#  vars : 
#  tmpl : 
sub log_ {
    open(NO, "$klog_c") || &er_("Can't open $klog_c");
    my $n = <NO>;
    close(NO);

    my $klog_f = "$klog_d\/$n$klogext";
    unless (-e $klog_f) {
        &l_m($klog_f);
    } elsif ((-s $klog_f) > ($klog_l * 1024)) {
        $n++;
        open(NUM, ">$klog_c") || &er_("Can't write $klog_c");
        print NUM $n;
        close(NUM);
        $klog_f = "$klog_d\/$n$klogext";
        &l_m($klog_f);
    }

    open(LOG, ">>$klog_f") || &er_("Can't write $klog_f");
    print LOG @KLOG;
    close(LOG);
}

##------------------------------------------------------------------------------
# check_ - check and validate form input
#  vars : 
#  tmpl : 
sub check_ {
    my ($envkey, $envvalue);
    &check_proxy();

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

##------------------------------------------------------------------------------
# n_w_ - display new articles
#  vars : 
#  tmpl : 
sub n_w_ {
    my @NEW = ();
    # read new articles from DB, and stack to @NEW
    open(DB, $log);
    while (<DB>) {
        ($nam, $date, $name, $email, $d_may, $comment, $url,
            $sp, $end, $ty, $del, $ip, $tim, $Se) = split(/<>/, $_);
        if (($time_k - $tim) <= ($new_t * 3600)) {
            push(@NEW, "$tim<>$_<>");
        }
    }
    close(DB);

    $total = @NEW;
    $page_ = int($#NEW / $new_s);
    if ($FORM{'page'} eq '') {
        $page = 0;
    } else {
        $page = $FORM{'page'};
    }
    $end_data = @NEW - 1;
    $page_end = $page + ($new_s - 1);
    if ($page_end >= $end_data) {
        $page_end = $end_data;
    }
    $Pg = $page + 1;
    $Pg2 = $page_end + 1;
    $nl = $page_end + 1;
    $bl = $page - $new_s;
    if ($bl >= 0) {
        $Bl = "<a href=\"$cgi_f?page=$bl&amp;mode=n_w&amp;$pp\">";
        $Ble = "</a>";
    }
    if ($page_end ne $end_data) {
        $Nl = "<a href=\"$cgi_f?page=$nl&amp;mode=n_w&amp;$pp\">";
        $Nle = "</a>";
    }

    Forum->template->set_vars('new_t', $new_t);
    Forum->template->set_vars('total', $total);
    Forum->template->set_vars('Pg', $Pg);
    Forum->template->set_vars('Pg2', $Pg2);
    Forum->template->set_vars('Bl', $Bl);
    Forum->template->set_vars('Ble', $Ble);
    Forum->template->set_vars('af', $page / $new_s);
    Forum->template->set_vars('page_', $page_);
    Forum->template->set_vars('new_s', $new_s);
    Forum->template->set_vars('cgi_f', $cgi_f);
    Forum->template->set_vars('pp', $pp);
    Forum->template->set_vars('new_su', $FORM{"s"});
    Forum->template->set_vars('new_count', $#NEW);
    $new_su = $FORM{'s'};

    my @new_articles;
    if (@NEW) {
        @NEW = sort @NEW;
        # if not '0' (not from older), do reverse
        if ($new_su ne '0') {
            @NEW = reverse(@NEW);
        }
        foreach ($page .. $page_end) {
            my %article;
            ($Tim, $nam, $date, $name, $email, $d_may, $comment, $url,
                $sp, $end, $ty, $del, $ip, $tim, $Se) = split(/<>/, $NEW[$_]);
            ($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
            ($ICON,$ICO,$font,$hr)=split(/\|/,$TXT);
            ($txt,$sel,$yobi)=split(/\|\|/,$SEL);
            &design($nam,$date,$name,$email,$d_may,$comment,$url,$sp,$end,$ty,$del,$Ip,$tim,$ico,
                $Ent,$fimg,$ICON,$ICO,$font,$hr,$txt,$sel,$yobi,$Se,$ResNo,"N");
            push(@new_articles, $HTML);
        }
    }

    Forum->template->set_vars('new_articles', \@new_articles);
    print Forum->cgi->header();
    $obj_template->process('new_articles.tpl', \%tmplVars);
    exit;
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

