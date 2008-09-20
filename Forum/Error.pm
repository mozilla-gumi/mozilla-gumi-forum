# -*- Mode: perl; indent-tabs-mode: nil -*-
#
# Module for Mozilla-Gumi Forum - Error handlers (to output)
#
# Copyright (C) 2008 - Mozilla-Gumi contributors
# Contributor(s):
#   Atsushi Shimono <shimono@mozilla.gr.jp>

package Forum::Error;

use strict;

use base qw(Exporter);

use Forum::Constants;

%Forum::Config::EXPORT = qw(
    new

    throw_error_user
    throw_error_code
);

our %params_def;
our $params;

sub new {
    my ($this) = @_;
    return $this;
}

sub throw_error_code {
    my ($self, $err_id) = @_;
    $self->_throw_error('error/code.tmpl', $err_id);
}

sub throw_error_user {
    my ($self, $err_id) = @_;
    $self->_throw_error('error/user.tmpl', $err_id);
}

################################################################## PRIVATE

sub _throw_error {
    my ($self, $fname, $err_id) = @_;
    Forum->dbh->db_unlock_tables(Forum::Constants::DB_UNLOCK_ABORT);

    Forum->template->set_vars('error', $err_id);
    print Forum->cgi->header();
    Forum->template->process($fname, Forum->template->vars);

    exit;
}


1;

__END__




