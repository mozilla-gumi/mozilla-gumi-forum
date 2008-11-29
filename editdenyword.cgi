#! /usr/bin/perl

require './common.pl';
require './set.cgi';
use strict;
use vars qw($met %tmplVars);

if (Forum->user->group_check('admin') == 0) {
    Forum->error->throw_error_user('not_logged_in');
}

my $NWFile = Forum::Constants::LOCATIONS()->{'worddeny'};

Forum->template->set_vars('mode_id', 'admin');
Forum->template->set_vars('mode_adm', 'word');

my @d_ = Forum->cgi->param('del');

my $m = Forum->cgi->param('m');
my $Log = $NWFile;
my $msd = '';
my @deny;
my @NEW;

if ($m eq "Add") {
    my $form_u = Forum->cgi->param('u');
    $form_u =~ s/\&lt\;/</g;
    $form_u =~ s/\&gt\;/>/g;
    open(OUT,">>$Log");
    print OUT "$form_u\n";
    close(OUT);
    Forum->template->set_vars('action', 'add');
} elsif($m eq "Del") {
    open(DB,"$Log");
    @deny = <DB>;
    close(DB);
    @NEW = ();
    my $F=0;
    foreach $b (@deny) {
        $b =~ s/\n//g;
        foreach my $u (@d_) {if($u eq "$b"){$F=1; last;}}
        if($F){$F=0; next;}
        push(@NEW,"$b\n");
    }
    open (DB,">$Log");
    print DB @NEW;
    close(DB);
    Forum->template->set_vars('action', 'del');
}

# So, let's load contents for display.
open(DB, $NWFile) || Forum->error->throw_error_user("Can't open $NWFile");
@deny = ();
foreach (<DB>) {
    chomp($_);
    if ($_ eq '') {next; }
    push(@deny, $_);
}
Forum->template->set_vars('word_list', \@deny);
close(DB);

print Forum->cgi->header();
Forum->template->process('admin/editdenyword.tpl', \%tmplVars);

exit;

