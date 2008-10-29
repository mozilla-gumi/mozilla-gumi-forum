#! /usr/bin/perl

require './common.pl';
require './set.cgi';
use strict;
use vars qw(%tmplVars);

if (Forum->user->group_check('admin') == 0) {
    Forum->error->throw_error_user('not_logged_in');
}

my $IpFile = Forum::Constants::LOCATIONS()->{'ipdeny'};
if (! -e $IpFile) {
    Forum->error->throw_error_user("Can't find $IpFile");
}

Forum->template->set_vars('mode_id', 'admin');
Forum->template->set_vars('mode_adm', 'ip');

my @d_ = Forum->cgi->param('del');
my $m = Forum->cgi->param('m');
my @deny;
my @NEW;

if ($m eq "Add") {
    my $form_u = Forum->cgi->param('u');
    if ($form_u !~ /^[\d\.\:]+$/) {
        Forum->template->set_vars('error_param', $form_u);
        Forum->error->throw_error_user('invalid_param');
    }
    open(OUT,">> $IpFile") || Forum->error->throw_error_user("Can't open $IpFile");
    print OUT "$form_u\n";
    close(OUT);
    Forum->template->set_vars('action', 'add');
} elsif ($m eq "Del") {
    open(DB, $IpFile) || Forum->error->throw_error_user("Can't open $IpFile");
    @NEW = ();
    my $ip;
    foreach $ip (<DB>) {
        chomp($ip);
        if ($ip eq '') {next; }
        foreach (@d_) {
            if ($ip eq $_) {
                $ip = '';
                last;
            }
        }
        push(@NEW, $ip) if ($ip ne '');
    }
    close(DB);

    open (DB,"> $IpFile") || Forum->error->throw_error_user("Can't open $IpFile");
    print DB join("\n", @NEW);
    print DB "\n";
    close(DB);
    Forum->template->set_vars('action', 'del');
}


# for easy use on adding.
my $mo = Forum->cgi->param('mo');
if ($mo =~ /^([\d\.\:]+)$/) {
    Forum->template->set_vars('opt_ip', $1);
}


# So, let's load contents for display.
open(DB, $IpFile) || Forum->error->throw_error_user("Can't open $IpFile");
@deny = ();
foreach (<DB>) {
    chomp($_);
    if ($_ eq '') {next; }
    push(@deny, $_);
}
Forum->template->set_vars('ip_list', \@deny);
close(DB);

# execute template.
print Forum->cgi->header();
Forum->template->process('admin/editdenyip.tmpl', \%tmplVars);

exit;

