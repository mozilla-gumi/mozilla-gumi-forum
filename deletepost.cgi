#! /usr/bin/perl

require './common.pl';
require './set.cgi';
use strict;
use vars qw($locks $lockf $log $i_dir %conf %tmplVars);

Forum->template->set_vars('mode_id', 'admin');
Forum->template->set_vars('mode_adm', 'delpost');

if (Forum->user->group_check('admin') == 0) {
    Forum->error->throw_error_user('invpass');
}

if ($locks) {
    &lock_($lockf);
}

my @CAS = ();
my @post_del;
my $del_file = '../data/dat/deleted.txt';

my $mens;
my @delid = Forum->cgi->param('delid');
my @deleted_id;
my @deleted_tree;
my $fulldel = Forum->cgi->param('fulldel');
my %del_ids_tree;
my %del_ids_post;

$fulldel ||= 'no';

foreach (@delid) {
    if (substr($_, 0, 1) eq 't') {
        $del_ids_tree{substr($_, 1)} = 1;
    } else {
        $del_ids_post{$_} = 1;
    }
}

open(DB, "$log") || Forum->error->throw_error_user("Can't open $log");
while ($mens = <DB>) {
    chomp($mens);
    my ($nam, $d, $na, $mail, $d_, $com, $url, $sp, $e, $ty, $de, $ip, $ti)
        = split(/<>/, $mens);
    if ($d eq '') {
        # Master line for current data
        push(@CAS, $mens);
        next;
    }
    if (defined($del_ids_post{$nam})) {
        # DELETE ONE
        push(@post_del, $mens);
        push(@deleted_id, $nam);
    } elsif (defined($del_ids_tree{$ty}) || defined($del_ids_tree{$nam})) {
        push(@post_del, $mens);
        push(@deleted_id, $nam);
        if ($ty eq 0) {push(@deleted_tree, $nam); }
    } else {
        push(@CAS, $mens);
        next;
    }
    my ($I, $ico, $E, $fi, $TX, $S, $R) = split(/:/, $ip);
    if ($ico && (-e "$i_dir/$ico")) {unlink("$i_dir/$ico"); }
    if ($fulldel ne "yes") {
        my $Dm = "ŠÇ—Ò";
        push(@CAS, "$nam<>$d<><><>iíœj<>‚±‚Ì‹L–‚Í$Dmíœ‚³‚ê‚Ü‚µ‚½<><>$sp<><>$ty<><><>$ti<><>");
    }
}
close(DB);

open (DB,">$log");
print DB join("\n", @CAS);
close(DB);

open(OUT, ">>$del_file");
print OUT join("\n", @post_del);
close (OUT);

if (-e $lockf) {
    rmdir($lockf);
}

if ($conf{'rss'} eq 1) {
    &RSS();
}

Forum->template->set_vars('deleted', $#post_del + 1);
Forum->template->set_vars('deleted_id', \@deleted_id);
Forum->template->set_vars('deleted_tree', \@deleted_tree);
Forum->template->set_vars('fulldel', $fulldel);
print Forum->cgi->header();
Forum->template->process('admin/deleted.tmpl', \%tmplVars);

exit;

