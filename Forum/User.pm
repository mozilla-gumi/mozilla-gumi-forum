# -*- Mode: perl; indent-tabs-mode: nil -*-
#
# Module for Mozilla-Gumi Forum - User authentication
#
# Copyright (C) 2008 - Mozilla-Gumi contributors
# Contributor(s):
#   Atsushi Shimono <shimono@mozilla.gr.jp>

package Forum::User;

use strict;

use Digest::MD5;

use base qw(Exporter);

use Forum::DB;
use Forum::Constants;

%Forum::Config::EXPORT = qw(
    new

    validate_password_admin
    get_uid
    restore_cookie
    parse_ua
);

our %conf = {
    'uid'      => 0,
    'ua_id'    => 0,
};

sub new {
    my ($self) = @_;

    $self->restore_cookie();
    $self->parse_ua();

    return $self;
}

sub validate_password_admin {
    my ($self, $pass) = @_;
    if ($conf{'uid'} != 0) {return $conf{'uid'}; }
    if (! defined($pass)) {return 0; }
    if ($pass eq Forum->config->GetParam('admin_pass')) {
        my $auth_user = 1;
        my $auth_key = $self->set_auth_key($auth_user);
        Forum->cgi->add_cookie('-name', 'auth_user', '-value', $auth_user);
        Forum->cgi->add_cookie('-name', 'auth_key', '-value', $auth_key);
        $conf{'uid'} = $auth_user;
        return $auth_user;
    }
    return 0;
}

sub get_uid {
    return $conf{'uid'};
}

sub restore_cookie {
    my $user = Forum->cgi->cookie('auth_user');
    my $key  = Forum->cgi->cookie('auth_key');
    if (defined($user) && defined($key)) {
        my $dbh = Forum->dbh;
        $conf{'uid'} = $dbh->db_auth_cookie($user, $key);
    }
}

sub parse_ua {
    my $ua = $ENV{'HTTP_USER_AGENT'};
    my $dbh = Forum->dbh;
    $conf{'ua_id'} = $dbh->db_ua_getid($ua);
    return $conf{'ua_id'};
}


# TEMPORARY HACK
sub group_check {
    my ($self, $group) = @_;
    if (($group eq 'admin') && ($conf{'uid'} == 1)) {
        return 1;
    }
    return 0;
}

################################################################## PRIVATE

sub set_auth_key {
    my ($self, $uid) = @_;
    my $ip = $ENV{'REMOTE_ADDR'};
    my $time = time();

    my $ctx = Digest::MD5->new;
    $ctx->add($ip . $time);
    my $hash = $ctx->b64digest;
    my $dbh = Forum->dbh;
    $dbh->db_auth_setcookie($uid, $hash);
    return $hash;
}

1;

__END__




