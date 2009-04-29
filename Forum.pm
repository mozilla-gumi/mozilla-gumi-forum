# -*- Mode: perl; indent-tabs-mode: nil -*-
#
# Module for Mozilla-Gumi Forum - Master module
#
# Copyright (C) 2008 - Mozilla-Gumi contributors
# Contributor(s):
#   Atsushi Shimono <shimono@mozilla.gr.jp>

package Forum;

use strict;

use base qw(Exporter);

use Forum::Constants;
use Forum::Template;
use Forum::Config;
use Forum::Captcha;
use Forum::CGI;
use Forum::DB;
use Forum::User;
use Forum::MigUtils;

%Forum::EXPORT = qw(
    new

    request

    cgi
    config
    template
    dbh
    user
    error
);

our $_request = {};

sub new {
    my ($this) = @_;
    return $this;
}

sub request {
    return $_request;
}

sub cgi {
    my ($this) = @_;
    $this->request->{cgi} ||= new Forum::CGI;
    return $this->request->{cgi};
}

sub config {
    my ($this) = @_;
    $this->request->{config} ||= new Forum::Config;
    return $this->request->{config};
}

sub template {
    my ($this) = @_;
    $this->request->{template} ||= new Forum::Template;
    return $this->request->{template};
}

sub dbh {
    my $this = shift;
    $this->request->{dbh} ||= new Forum::DB::connect();
    return $this->request->{dbh};
}

sub user {
    my $this = shift;
    $this->request->{user} ||= new Forum::User;
    return $this->request->{user};
}

sub error {
    my $this = shift;
    $this->request->{error} ||= new Forum::Error;
    return $this->request->{error};
}

################################################################## PRIVATE

sub _cleanup {
    my $this = shift;
    my $dbh = request()->{dbh};
    $dbh->disconnect if $dbh;
    undef $_request;
}

sub END {
    _cleanup();
}

1;

__END__




