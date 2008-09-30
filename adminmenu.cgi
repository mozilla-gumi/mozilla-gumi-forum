#! /usr/bin/perl

require './common.pl';
require './set.cgi';
use strict;
use vars qw(%tmplVars);

if (Forum->user->group_check('admin') == 0) {
    Forum->error->throw_error_user('not_logged_in');
}

print Forum->cgi->header();
Forum->template->set_vars('mode_id', 'admin');
Forum->template->process('admin/menu.tmpl', \%tmplVars);

exit;
