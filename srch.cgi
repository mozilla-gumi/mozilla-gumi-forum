#! /usr/bin/perl

require './common.pl';

&d_code_;

Forum->template->set_vars('mode_id', 'search');

$set[0] = "./set.cgi";
$SetUpFile = $set[0];
require $SetUpFile;

if ($logs) {
    unless (($logs eq "$log") ||
            ($logs =~ /^[\d]+$/) ||
            ($logs eq "all") ||
            ($logs eq "recent")) {
        Forum->error->throw_error_user('invalidfile');
    }
}
$SL = "$klog_d\/1$klogext";

if ($FORM{'mode'} eq "log") {
    &log_;
} elsif ($FORM{'mode'} eq "del") {
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
    $logs = $FORM{'logs'};
    $FORM{'N'} =~ s/([^0-9,])*?//g;
    my $neq = $FORM{'N'};
    $Neq = '';
    $Neq = "&amp;N=$neq" if ($neq);
    Forum->template->set_vars('Neq', $Neq);
    undef $neq;
}

##---
# srch_ - output search results
sub srch_ {
    print Forum->cgi->header();

    $KH = $klog_h[0];
    if ($FORM{"PAGE"} != 0) {
        $KH = $FORM{"PAGE"};
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

    if ($FORM{'word'} ne "") {
        @key_ws = split(/[ @\t]/, $FORM{'word'});
        if ($logs eq "all") {
            $Stert = 0;
            if ($FORM{'N'}) {
                ($N, $S) = split(/\,/, $FORM{'N'});
                $Stert = $N;
            }
            $End = $logcount - 1;
        } else {
            $Stert = 0;
            $End = 0;
        }
        @new = ();
        $Next = 0;
        foreach ($Stert .. $End) {
            if ($logs eq "all") {
                $I = $_ + 1;
                $IT = $I;
                $Log = "$klog_d\/$IT$klogext";
            } elsif ($logs eq 'recent') {
                $Log = $log;
            } else {
                $IT = $logs;
                $Log = "$klog_d\/$logs$klogext";
            }
            Forum->template->set_vars('file', $Log);
            open(DB, $Log) || Forum->error->throw_error_user('cannot_open_logfile');
            while ($Line = <DB>) {
                my $whole_hit = 0;
                my @lcnt = split(/<>/, $Line);
                my ($com, $env) = split(/\t/, $lcnt[5]);
                if ($FORM{'andor'} eq 'and') {$whole_hit = 1; }
                foreach $key_w (@key_ws) {
                    $key_w =~ s/^&$/&amp\;/g;
                    $key_w =~ s/^<$/\&lt\;/g;
                    $key_w =~ s/^>$/\&gt\;/g;
                    $key_w =~ s/^\"$/\&quot\;/g;
                    my $c_hit = 0;
                    if ($key_w =~ /[\x80-\xff]/) {      # not us-ascii
                        if (index($com, $key_w) >= 0) {$c_hit = 1; }
                    } else {
                        if ($BM) {
                            # regexps
                            $key_w =~ s/\[/\\[/g;
                            $key_w =~ s/\]/\\]/g;
                            $key_w =~ s/\\/\\\\/g;
                            if ($com =~ /$key_w/i) {$c_hit = 1; }
                        } else {
                            if (index($com, $key_w) >= 0) {$c_hit = 1; }
                        }
                    }
                    if ($c_hit) {
                        if ($FORM{'andor'} eq "or") {$whole_hit = 1; last; }
                    } else {
                        if ($FORM{'andor'} eq "and") {$whole_hit = 0; last; }
                    }
                }
                if ($whole_hit) {
                    push(@new, "$IT<>$Line");
                }
            }
            close(DB);
            if ((($#new + 1) >= 200) && ($logs eq "all")) {
                $Next = $I + 1;
                last;
            }
        }
    }
    $count = $#new + 1;
    if ($logs eq $log) {@new = reverse(@new); }
    my @articles;
    if ($count > 0) {
        $page_ = int($count / $KH);
        if ($FORM{'page'} == 0) {
            $page = 0;
        } else {
            $page = $FORM{'page'};
        }

        $page_end = $page + ($KH - 1);
        if ($page_end >= $#new - 1) {
            $page_end = $#new - 1;
        }

        foreach ($page .. $page_end) {
            my %article;
            ($IT, $nam, $date, $name, $email, $d_may, $comment_, $url,
                $sp, $e, $type, $del, $ip, $tim, $Se) = split(/<>/, $new[$_]);
            ($Ip, $ico, $Ent, $fimg, $TXT, $SEL, $R) = split(/:/, $ip);
            ($ICON, $ICO, $font, $hr) = split(/\|/, $TXT);
            ($txt, $sel, $yobi) = split(/\|\|/, $SEL);
            my ($comment, $userenv) = split(/\t/, $comment_);
            if ($date eq "") {next; }
            if ($ico) {
                if (($Ent == 0) && $fimg) {
                    $fimg = $no_ent;
                }
                if (-s "$i_dir/$ico") {
                    $Size = -s "$i_dir/$ico";
                } else {
                    $Size = 0;
                }
                $KB = int($Size / 1024);
                if ($KB == 0) {$KB = 1; }
                if ($Size) {
                    $Alt = '';
                    if ($fimg ne $no_ent) {
                        $Alt = " alt=\"$ico/$KB\KB\"";
                    }
                    if ($fimg eq $no_ent) {
                        $A = 0;
                    } elsif ($fimg eq "img") {
                        $Pr .= "<a href=\"$i_Url/$ico\"$TGT><img src='$i_Url/$i_ico' border=0$Alt>";
                        $A = 1;
                    } else {
                        $Pr .= "<a href=\"$i_Url/$ico\"$TGT>";
                        $A = 1;
                    }
                    if (($img_h eq "") && ($fimg ne img)) {
                        $Pr .= "<img src=\"$i_Url/$fimg\" border=0$Alt>";
                    } elsif (($img_h ne "") && ($fimg ne img)) {
                        $Pr .= "<img src=\"$i_Url/$fimg\" height=$img_h width=$img_w border=0$Alt>";
                    }
                    $AEND = "";
                    if ($A) {$AEND = "$ico</a>/"; }
                    $Pr .= "<br>$AEND $KB\KB\n";
                }
            }

            $article{'userenv'} = $userenv;
            $article{'ResNo'} = $ResNo;
            $article{'date'} = $date;
            $article{'end'} = $end;
            $article{'Pr'} = $Pr;
            $article{'d_may'} = $d_may;
            $article{'R'} = $R;
            $article{'name'} = $name;
            $article{'url'} = $url;
            $article{'comment'} = $comment;
            $article{'txt'} = $txt;
            $article{'sel'} = $sel;
            $article{'d_may'} = $d_may;
            $article{'type'} = $type;
            $article{'nam'} = $nam;
            $article{'IT'} = $IT;
            $article{'Se'} = $Se;
            $article{'e'} = $e;
            push(@articles, \%article);
        }
    }

    Forum->template->set_vars('o_mail', $o_mail);
    Forum->template->set_vars('TOPH', $TOPH);
    Forum->template->set_vars('notitle', $notitle);
    Forum->template->set_vars('TS_Pr', $TS_Pr);
    Forum->template->set_vars('TXT_T', $TXT_T);
    Forum->template->set_vars('SEL_T', $SEL_T);

    Forum->template->set_vars('BM', $BM);
    Forum->template->set_vars('logcount', $logcount);
    Forum->template->set_vars('count', $count);
    Forum->template->set_vars('page_count', $page_);
    Forum->template->set_vars('page', $page);
    Forum->template->set_vars('page_end', $page_end);
    Forum->template->set_vars('andor', $FORM{'andor'});
    Forum->template->set_vars('srch', $srch);
    Forum->template->set_vars('word', $FORM{'word'});
    Forum->template->set_vars('wordlist', join(' ', @key_ws));
    Forum->template->set_vars('klog_s', $klog_s);
    Forum->template->set_vars('log', $log);
    Forum->template->set_vars('logs', $logs);
    Forum->template->set_vars('FORM_KYO', $FORM{'KYO'});
    Forum->template->set_vars('klog_h', \@klog_h);
    Forum->template->set_vars('KH', $KH);
    Forum->template->set_vars('N', $N);
    Forum->template->set_vars('Next', $Next);
    Forum->template->set_vars('articles', \@articles);
    Forum->template->process('search_result.tmpl', \%tmplVars);
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
    my ($mens, $word);
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

