#!/usr/local/bin/perl

require './common.pl';
require './set.cgi';
use strict;
use vars qw($locks $lockf $log $del_file $i_dir %conf %tmplVars);

Forum->template->set_vars('mode_id', 'admin');
Forum->template->set_vars('mode_adm', 'delpost');

if (Forum->user->group_check('admin') == 0) {
    Forum->error->throw_error_user('invpass');
}

if ($locks) {
    &lock_($lockf);
}

open(DB, "$log") || &er_("Can't open $log");
my @CAS = ();
my $dok = 0;
my $OYA = 0;

my $mens;
my @to_del = Forum->cgi->param('del');
my @deleted_id = ();
my $kiji = Forum->cgi->param('kiji');
while ($mens = <DB>) {
    $mens =~ s/\n//g;
    my ($nam, $d, $na, $mail, $d_, $com, $url, $sp, $e, $ty, $de, $ip, $ti)
        = split(/<>/, $mens);
    if ($d eq "") {
        push(@CAS, "$mens\n");
        $OYA = 1;
        next;
    }
    foreach my $namber (@to_del) {
        if ($namber eq $nam) {
            $del_file = '../data/dat/deleted.txt';
            open(OUT, ">>$del_file");
            print OUT "$mens\n";
            close (OUT);
            $mens = "";
            $dok += 1;
            push(@deleted_id, $namber);
            my ($I, $ico, $E, $fi, $TX, $S, $R) = split(/:/, $ip);
            if ($ico && (-e "$i_dir/$ico")) {unlink("$i_dir/$ico"); }
        }
    }
    if (($kiji ne "") && (($kiji eq "$nam") || ($kiji eq "$ty"))) {$mens = ""; }
    my $n = "\n";
    if (($mens eq "") && ($kiji eq "")) {
        my $Dm = "ŠÇ—Ò";
        $mens = "$nam<>$d<><><>iíœj<>‚±‚Ì‹L–‚Í$Dmíœ‚³‚ê‚Ü‚µ‚½<><>$sp<><>$ty<><><>$ti<><>";
    } elsif (($mens eq "") && ($kiji ne "")) {
        # if kiji = A, delete forever (and no log)
        $mens = "";
        $n = "";
        if ($OYA == 0) {
            $mens = "$nam<><><><><><><><><>$nam<><><><><>";
            $n = "\n";
        }
    }
    $OYA = 1;
    push(@CAS, "$mens$n");
}
close(DB);

open (DB,">$log");
print DB @CAS;
close(DB);
if (-e $lockf) {
    rmdir($lockf);
}

if ($conf{'rss'} eq 1) {
    &RSS();
}

Forum->template->set_vars('deleted', $dok);
Forum->template->set_vars('deleted_id', \@deleted_id);
print Forum->cgi->header();
Forum->template->process('admin/deleted.tmpl', \%tmplVars);

exit;

