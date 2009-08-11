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
                } elsif (Forum::MigUtils::match_hash($de, $de, $FORM{'delkey'}) == 0) {
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
                } elsif (Forum::MigUtils::match_hash($epasswd, $de, $FORM{'delkey'}) == 0) {
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
                    if (Forum::MigUtils::match_hash($epasswd, $de, $FORM{'delkey'}) == 0) {
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
                    if (Forum::MigUtils::match_hash($epasswd, $de, $FORM{'delkey'}) == 0) {
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
                    if (Forum::MigUtils::match_hash($epasswd, $de, $FORM{'delkey'}) == 0) {
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
