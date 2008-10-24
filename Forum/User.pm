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
    revoke_cookie
    parse_ua
    user_data
);

our %conf;

sub new {
    my ($self) = @_;

    $conf{'uid'} = $self->restore_cookie();
    $conf{'gid'} = $self->group_check();
    $conf{'ua_id'} = $self->parse_ua();
    $conf{'name'} = '';
    $self->fetch_userdata();

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
        $conf{'name'} = 'admin';
        return $auth_user;
    }
    return 0;
}

sub get_uid {
    return $conf{'uid'};
}

sub get_name {
    return $conf{'name'};
}

sub get_ua_id {
    return $conf{'ua_id'};
}

sub user_data {
    return \%conf;
}

sub fetch_userdata {
    my ($self);
    if ($conf{'uid'} eq 0) {
    }
##### TEMPORARY HACK - SHOULD MOVE 'name' TO DB.
    if ($conf{'uid'} eq 1) {
        $conf{'name'} = 'admin';
    }
}

sub restore_cookie {
    my $user = Forum->cgi->cookie('auth_user');
    my $key  = Forum->cgi->cookie('auth_key');
    if (defined($user) && defined($key)) {
        my $dbh = Forum->dbh;
        $conf{'uid'} = $dbh->db_auth_cookie($user, $key);
        return $conf{'uid'};
    }
    return 0;
}

sub revoke_cookie {
    my $user = Forum->cgi->cookie('auth_user');
    my $key  = Forum->cgi->cookie('auth_key');
    if (defined($user) && defined($key)) {
        my $dbh = Forum->dbh;
        my $ret = $dbh->db_revoke_cookie($user, $key);
        if ($ret != 0) {
            $conf{'uid'} = 0;
            $conf{'gid'} = 0;
            $conf{'name'} = '';
        }
        return $ret;
    }
    return 0;
}

sub parse_ua {
    my $ua = $ENV{'HTTP_USER_AGENT'};
    my $dbh = Forum->dbh;
    $conf{'ua_id'} = $dbh->db_ua_getid($ua);
    return $conf{'ua_id'};
}

# TEMPORARY HACK - FIX : restore_cookie
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




