#! /usr/bin/perl

require './common.pl';
require "./set.cgi";

if ($obj_cgi->param('password') ne '') {
    # processing mode
    if (Forum->user->validate_password_admin($obj_cgi->param('pass')) == 0) {
        Forum->error->throw_error_user('invpass');
    }
    print $cgi->redirect(-location => './');
} else {
    # login form mode
    print Forum->cgi->header();
    $obj_template->process('login.tmpl', \%tmplVars);
}

exit;
