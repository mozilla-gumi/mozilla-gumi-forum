#! /usr/bin/perl

require './common.pl';
require './set.cgi';
use strict;
use vars qw(%tmplVars);

my $pass = Forum->cgi->param('password');
if ($pass) {
    # processing mode
    if (Forum->user->validate_password_admin($pass) == 0) {
        Forum->error->throw_error_user('invpass');
    }
    print Forum->cgi->redirect(-location => './');
} elsif (Forum->cgi->param('logout')) {
    my $uid = Forum->user->revoke_cookie();
    if ($uid eq 0) {
        # logging out failed (not logged in, no cookie)
        Forum->error->throw_error_user('not_logged_in');
    } else {
        print Forum->cgi->redirect(-location => './');
    }
} else {
    # login form mode
    print Forum->cgi->header();
    Forum->template->set_vars('mode_id', 'login');
    Forum->template->process('login.tmpl', \%tmplVars);
}

exit;
