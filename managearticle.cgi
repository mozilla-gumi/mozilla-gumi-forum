#!/usr/local/bin/perl

require './common.pl';
require './set.cgi';

$res_r=1;
&d_code_;

$ag=$ENV{'HTTP_USER_AGENT'};

$pf="";
$pp="";

if ($FORM{'KLOG'}) {
    $KLOG=$FORM{'KLOG'};
    $tmplVars{'TrON'}=0;
    $tmplVars{'TpON'}=1;
    $tmplVars{'ThON'}=0;
    $TOPH=2;
    unless($KLOG=~ /^[\d]+/) {
        Forum->error->throw_error_user('invalidfile');
    }
    $log="$klog_d\/$KLOG$klogext";
    $pp = "&KLOG=$KLOG";
    $pf = "<input type=\"hidden\" name=\"KLOG\" value=\"$KLOG\">\n";
    $tmplVars{'KLOG'} = $KLOG;
}
$tmplVars{'pp'} = $pp;
$tmplVars{'pf'} = $pf;

Forum->template->set_vars('mode_id', 'admin');
Forum->template->set_vars('mode_adm', 'admin');

if (Forum->user->group_check('admin') == 0) {
    Forum->error->throw_error_user('invpass');
}

print Forum->cgi->header();
Forum->template->set_vars('htmlhead', 'Editor');
Forum->template->process('htmlhead.tpl', \%tmplVars);

my @NEW=();
my $RES=();
my $FSize=0;
my $RS=0;
my @lines=();
my %R=();

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
if($FORM{"mode2"} eq "LockOff"){
    $msg="<h3>ロック解除完了</h3>";
    if(-e $lockf){rmdir($lockf); $msg.="($lockf解除)";}else{$msg.="($lockf無し)";}
    if(-e $cloc){rmdir($cloc);   $msg.="($cloc解除)"; }else{$msg.="($cloc無し)";}
}
$total=@NEW; $NS=$RS+$total;
$page_=int(($total-1)/$a_max);
if(-s $log){$l_size=int((-s $log)/1024);}else{$l_size=0;}
if($topok==0){$NewMsg="<li><a href=\"$cgi_f?mode=new&amp;&amp;pass=$FORM{'pass'}$pp\">管理用新規作成</a>\n";}
if($i_mode || $mas_c){
    if($FSize){$FSize=int($FSize/1024); $FileSize="<br>アップファイル合計サイズ：$FSize\KB";}else{$FSize=0;}
    $FP ="<form action=\"$cgi_f\" method=\"$met\"$TGT>\n";
    $FP.="<strong>[画像/記事表\示許可]</strong><br><input type=\"hidden\" name=\"mode\" value=\"ent\">$pf\n";
    $FP.="<input type=\"hidden\" name=\"pass\" value=\"$FORM{'pass'}\"><input type=\"submit\" value=\"表\示許可システム\"></form>\n";
}
print <<"_HTML_";
<h2>管理モード</h2>
<ul>
<li>現在のログのサイズ：$l_size\KB　記事数：$NS(親/$total 返信/$RS)$FileSize</li>
<li>記事を編集したい場合、その記事のタイトルをクリック。</li>
<li>削除したい記事にチェックを入れ「削除」ボタンを押して下さい。</li>
<li>記事Noの横のIPアドレスをクリックすると排除IPモードへ情報を送ります。</li>
<li>ツリー削除をするとツリーが跡形も無く消えます。</li>
<li>記事削除は、その記事に対する返信がない場合は完全削除になります。<br>
その記事に対する返信がある場合は完全に削除されず削除記事になります。</li>
<li>削除記事は「記事完全削除」をチェックすると完全に消せます。</li>
<li><a href="#FMT">ロック解除/ログ初期化/フリーフォーム修復/ログコンバート$BUL</a>
$NewMsg</li>
</ul>
_HTML_
print "$FP";
if($cou){
    open(NO,"$c_f") || Forum->error->throw_error_user("Can't open $c_f");
    $cnt = <NO>;
    close(NO);
    print 'カウント数/' . $cnt . '<br>';
}
print <<"_HTML_";
$msg
<form action=\"deletepost.cgi\" method="$met">
<input type="hidden" name="page" value="$FORM{"page"}">
<hr>
_HTML_
if($FORM{'page'} eq ''){$page=0;}else{$page=$FORM{'page'};}
$end_data=@NEW - 1;
$page_end=$page + ($a_max - 1);
if($page_end >= $end_data){$page_end=$end_data;}
$nl=$page_end + 1;
$bl=$page - $a_max;
if($bl >= 0){$Bl="<a href=\"$cgi_f?mode=del&amp;page=$bl&amp;pass=$FORM{'pass'}&amp;$pp\">"; $Ble="</a>";}
if($page_end ne $end_data){$Nl="<a href=\"$cgi_f?mode=del&amp;page=$nl&amp;pass=$FORM{'pass'}&amp;$pp\">"; $Nle="</a>";}
$Plink="<div class=\"Caption01c\"><strong>全ページ</strong> $Bl$Ble /\n\n";
$a=0;
for($i=0;$i<=$page_;$i++){
    $af=$page/$a_max;
    if($i != 0){$Plink.=" ";}
    if($i eq $af){$Plink.="[<strong>$i</strong>]\n";}else{$Plink.="[<a href=\"$cgi_f?page=$a&amp;mode=del&amp;pass=$FORM{'pass'}&amp;$pp\">$i</a>]\n";}
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
if((!$name)||($name eq ' ')||($name eq '　')){$name=$noname;}
    if($email ne ""){$name = "<a href=\"mailto:$email\">$name</a>";}
    if($d_may eq ""){$d_may= "$notitle";}
    if($yobi){$yobi=" [ID:$yobi]";}
    if(length($d_may)>$t_max){$d_may=substr($d_may,0,($t_max-2));$d_may="$d_may..";}
    $date=substr($date,2,19);
print '<table class="Tree" summary="Tree" cellspacing="0" cellpadding="0" border="0">';
print '<tr><td><input type="radio" name="kiji" value="';
print $namber;
print '>ツリー削除</td><td class="Highlight">' . "\n" . '<input type="checkbox" name="del" value="' . "$namber\">\n";
    print <<"_HTML_";
<a href="$cgi_f?mode=nam&amp;pass=$FORM{'pass'}&amp;kiji=$namber&amp;mo=1&amp;$pp">$d_may</a>
/ $name :$date <span class="ArtId">(#$namber)</span>
[<a href="editdenyip.cgi?mo=$ip" $TGT>$ip</a>]$ico
</td></tr>
_HTML_

##H=T
#foreach ($page .. $page_end) {
#	($T,$namber,$date,$name,$email,$d_may,$comment,$url,
#		$space,$end,$type,$del,$ip,$tim,$Se)=split(/<>/,$NEW[$_]);
#	if(($time_k - $tim) > $new_t*3600){$news="$hed_i";}else{$news="$new_i";}
#if((!$name)||($name eq ' ')||($name eq '　')){$name=$noname;}
#	if($email && $Se < 2){$name="$name <a href=\"mailto:$SPAM$email\">$AMark</a>";}
#	($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
#	($ICON,$ICO,$font,$hr)=split(/\|/,$TXT);
#	($txt,$sel,$yobi)=split(/\|\|/,$SEL);
#	if(@ico3 && $Icon && ($ICON ne "" || $comment=~/<br>\(携帯\)$/)){
#		if($I_Hei_m){$WHm=" width=\"$I_Wid_m\" height=\"$I_Hei_m\"";}
#		if($ICON ne ""){if($ICON=~ /m/){$ICON=~ s/m//; $mICO=$mas_m[$ICON];}else{$mICO=$ico3[$ICON];}}
#		elsif($Icon && $comment=~/<br>\(携帯\)$/){$mICO="$Ico_km";}
#		$news.="<img src=\"$IconDir\/$mICO\" border=\"0\"$WHm>";
#	}
#	if($ico && $i_mode){$Pr=""; &size(1); $Pr=" "."$Pr";}else{$Pr="";}
#	if($d_may eq ""){$d_may="$notitle";}
#	if($yobi){$yobi="[ID:$yobi]";}
#	if($txt){$Txt="$TXT_T:[$txt]　";}else{$Txt="";}
#	if($sel){$Sel="$SEL_T:[$sel]　";}else{$Sel="";}
#	if($Txt || $Sel ||($Txt && $Sel)){if($TS_Pr==0){$d_may="$Txt$Sel/"."$d_may";}}
#	if(length($d_may)>$t_max){$d_may=substr($d_may,0,($t_max-2));$d_may="$d_may.."; }
#	$date=substr($date,2,19);
#if((!$name)||($name eq ' ')||($name eq '　')){$name=$noname;}
#	print <<"_HTML_";
#<br>
#<table class="Tree" summary="Tree" cellspacing="0" cellpadding="0" border="0">
#<tr><td class="Highlight" width="1\%">
#<a href="$cgi_f?mode=all&amp;namber=$namber&amp;type=$type&amp;space=$space&amp;$pp">$all_i</a></td>
#<td class="Highlight" width="99\%"><a href="$cgi_f?mode=one&amp;namber=$namber&amp;type=$type&amp;space=$space&amp;$pp">$news $d_may</a>
#/ $name :$date $yobi<span class="ArtId">(#$namber)</span> $Pr
#_HTML_

#---kanri
#foreach ($page .. $page_end) {
#	($namber,$date,$name,$email,$d_may,$comment,$url,
#		$space,$end,$type,$delkey,$Ip) = split(/<>/,$NEW[$_]);
#	($ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$Ip);
#	($txt,$sel,$yobi)=split(/\|\|/,$SEL);
#	if($ico){$ico=" [File:<a href=\"$i_Url\/$ico\"$TGT>$ico</a>]";}
#if((!$name)||($name eq ' ')||($name eq '　')){$name=$noname;}
#	if($email ne ""){$name = "<a href=\"mailto:$email\">$name</a>";}
#	if($d_may eq ""){$d_may= "$notitle";}
#	if($yobi){$yobi=" [ID:$yobi]";}
#	if(length($d_may)>$t_max){$d_may=substr($d_may,0,($t_max-2));$d_may="$d_may..";}
#	$date=substr($date,2,19);
#print '<input type="radio" name="kiji" value="' . $namber . '" ';
#print '>ツリー削除<br><input type="checkbox" name="del" value="' . "$namber\">\n";
#	print <<"_HTML_";
#<a href="$cgi_f?mode=nam&amp;pass=$FORM{'pass'}&amp;kiji=$namber&amp;mo=1&amp;$pp">$d_may</a>
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
#			print"<a href=\"$cgi_f?mode=one&amp;namber=$rnam&amp;type=$rtype&amp;space=$rsp&amp;$pp\">$news $rdm</a>\n";
if((!$rname)||($rname eq ' ')||($rname eq '　')){$rname=$noname;}
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
#			if(@ico3 && $Icon &&($rICON ne "" || $rcom=~/<br>\(携帯\)$/)){
#				if($I_Hei_m){$WHm=" width=\"$I_Wid_m\" height=\"$I_Hei_m\"";}
#				if($rICON ne ""){if($rICON=~ /m/){$rICON=~ s/m//; $mrICO=$mas_m[$rICON];}else{$mrICO=$ico3[$rICON];}}
#				elsif($Icon && $rcom=~/<br>\(携帯\)$/){$mrICO="$Ico_km";}
#				$news.="<img src=\"$IconDir\/$mrICO\" border=\"0\"$WHm>";
#			}
#			if($ico && $i_mode){$Pr=""; &size(1); $Pr=" "."$Pr";}else{$Pr="";}
#			if($rdm eq ""){$rdm="$notitle"; }
#			if($yobi){$yobi="[ID:$yobi]";}
#			if($txt){$Txt="$TXT_T:[$txt]　";}else{$Txt="";}
#			if($sel){$Sel="$SEL_T:[$sel]　";}else{$Sel="";}
#			if($Txt || $Sel ||($Txt && $Sel)){if($TS_Pr==0){$rdm="$Txt$Sel/"."$rdm";}}
#			if(length($rdm)>$t_max){$rdm=substr($rdm,0,($t_max-2)); $rdm="$rdm..";}
#			print "</td></tr><tr><td></td><td nowrap>\n";
#			if($Keisen){print"$Sen";}
#			else{
#				$rspz=$rsp/15*$zure;
#				print "." x $rspz;
#			}
#			print"<a href=\"$cgi_f?mode=one&amp;namber=$rnam&amp;type=$rtype&amp;space=$rsp&amp;$pp\">$news $rdm</a>\n";
#if((!$rname)||($rname eq ' ')||($rname eq '　')){$rname=$noname;}
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
#if((!$rname)||($rname eq ' ')||($rname eq '　')){$rname=$noname;}
#}
            print <<"_HTML_";
<input type="checkbox" name="del" value="$rnam">
<a href="$cgi_f?mode=nam&amp;pass=$FORM{'pass'}&amp;kiji=$rnam&amp;mo=1&amp;$pp">$rdm</a>
/ $rname :$rd $ryobi <span class="ArtId">(#$rnam)</span>
[<a href="editdenyip.cgi?mo=$rip"$TGT>$rip</a>]$ico $re</td></tr>
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
    $tmplVars{'FORM'} = \%FORM;
    if ( -e $lockf ) {$tmplVars{'lockf'} = $lockf; }
    if ( -e $cloc ) {$tmplVars{'cloc'} = $cloc; }
    $tmplVars{'log'} = $log;

    print '</ul><input type="checkbox" name="kiji" value="A" ' . "\">記事完全削除<br>\n";
    print '<input type="submit" value=" 削 除 " ' . "\">\n";
    print '<input type="reset" value="リセット" ' . "\"></form>\n";
    print "<strong>";
    if($Bl){print"<div class=\"Caption01r\">[ $Bl前の返信$a_max件$Ble ]\n";}
    if($Nl){if($Bl){print"| ";}else{print "<div class=\"Caption01r\">";} print"[ $Nl次の返信$a_max件$Nle ]\n</div>\n";}else{print "</div>";}
    print <<"_HTML_";
</strong><br>$Plink
<SCRIPT language="JavaScript">
<!--
function Link(url) {
    if(confirm("本当に実行してもOKですか?\\n(実行すると内容は元に戻せません!)")){location.href=url;}
    else{location.href="#FMT";}
}
//-->
</SCRIPT>
<a name="FMT"><hr width="95\%"></a>
*JavaScript を ONにしてください*
<table summary="lock" border="1" bordercolor="$ttb" width="90\%">
<tr><td colspan="2"><form action="$cgi_f" method="$met"><strong>[ロックファイルの解除(削除)]</strong><ul>
<input type="button" value="ロック解除" onClick="Link('$cgi_f?mode=del&amp;pass=$FORM{"pass"}&amp;mode2=LockOff&amp;$pp')">
<li>ロックファイルがどうしても削除されない場合に試してください。問題が無い場合はあまり使わないで下さい<ul>
_HTML_
    if(-e $lockf){print"<li>メインログ($lockf):ロック中\n";}
    if(-e $cloc){print"<li>カウンタログ($cloc):ロック中\n";}
    print<<"_HTML_";
</ul><li>ロック中のログがあっても、ユーザが操作中の場合があります。しばらく様子を見て実行してください。
</ul></form></td></tr>
_HTML_
    print"</td></tr></table>\n";

Forum->template->process('htmlfoot.tpl', \%tmplVars);

exit;

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

