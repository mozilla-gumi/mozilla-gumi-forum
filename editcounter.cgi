#! /usr/bin/perl

require './common.pl';
require './set.cgi';
use strict;
use vars qw($cou $c_f %tmplVars);

if (Forum->user->group_check('admin') == 0) {
    Forum->error->throw_error_user('not_logged_in');
}
if (! $cou) {
    Forum->error->throw_error_user('counter_not_used');
}

Forum->template->set_vars('mode_id', 'admin');
Forum->template->set_vars('mode_adm', 'count');

my $ncnt = Forum->cgi->param('newcount');
if (defined($ncnt)) {
    if($ncnt =~ /^\d+$/){
        open(NO,">$c_f") || Forum->error->throw_error_user("Can't write $c_f");
        print NO $ncnt;
        close(NO);
        Forum->template->set_vars('edited', 1);
    } else {
        Forum->template->set_vars('error_param', $ncnt);
        Forum->error->throw_error_user('invalid_param');
    }
}


open(NO,"$c_f") || Forum->error->throw_error_user("Can't open $c_f");
my $cnt = <NO>;
close(NO);
Forum->template->set_vars('cnt', $cnt);

print Forum->cgi->header();
Forum->template->process('admin/editcounter.tmpl', \%tmplVars);

exit;


