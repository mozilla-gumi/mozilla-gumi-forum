# -*- Mode: perl; indent-tabs-mode: nil -*-
#
# Module for Mozilla-Gumi Forum - DB interface part
#
# Copyright (C) 2008 - Mozilla-Gumi contributors
# Contributor(s):
#   Atsushi Shimono <shimono@mozilla.gr.jp>

package Forum::DB;

use strict;

use DBI;
use base qw(DBI::db);

use Forum::Constants;
use Forum::Config;
use Forum::Util;

BEGIN {
    if ($ENV{SERVER_SOFTWARE}) {
        require CGI::Carp;
        CGI::Carp->import('fatalsToBrowser');
    }
}

sub connect {
    my $config = Forum->config->GetHash();
    return _connect(
        $config->{'db_driver'},
        $config->{'db_host'},
        $config->{'db_name'},
        $config->{'db_port'},
        $config->{'db_sock'},
        $config->{'db_user'},
        $config->{'db_pass'},
    )
}

sub _connect {
    my ($driver, $host, $dbname, $port, $sock, $user, $pass) = @_;
    my $pkg_module = DB_MODULE->{lc($driver)}->{db};

    eval ("require $pkg_module")
        || die ("'$driver' is not a valid DB module. " . $@);
    my $dbh = $pkg_module->new($user, $pass, $host, $dbname, $port, $sock);
    return $dbh;
}

sub db_server_version {
    my ($self) = @_;
    return $self->get_info(18);
}

sub db_last_key {
    my ($self, $table, $column) = @_;
    return $self->last_insert_id(
        Forum->config->GetParam('db_name'), undef, $table, $column);
}

sub db_transaction_start {
    my ($self) = @_;
    if ($self->{private_db_in_transaction}) {
        Forum->error->throw_error_code("nested_transaction");
    } else {
        $self->begin_work();
        $self->{private_db_in_transaction} = 1;
    }
}

sub db_transaction_commit {
    my ($self) = @_;
    if (! $self->{private_db_in_transaction}) {
        Forum->error->throw_error_code("not_in_transaction");
    } else {
        $self->commit();
        $self->{private_db_in_transaction} = 0;
    }
}

sub db_transaction_rollback {
    my ($self) = @_;
    if (! $self->{private_db_in_transaction}) {
        Forum->error->throw_error_code("not_in_transaction");
    } else {
        $self->rollback();
        $self->{private_db_in_transaction} = 0;
    }
}

sub db_new_conn {
    my ($class, $dsn, $user, $pass, $attr) = @_;
    $attr = {
        RaiseError => 0,
        AutoCommit => 1,
        PrintError => 0,
        ShowErrorStatement => 1,
        HandleError => \&_handle_error,
        TaintIn => 1,
        FetchHashKeyName => 'NAME',
    } if (! defined($attr));
    my $self = DBI->connect($dsn, $user, $pass, $attr)
        or die "\nCan't connect to the DB.\n$DBI::errstr\n";
    $self->{RaiseError} = 1;
    $self->{private_db_in_transaction} = 0;
    bless($self, $class);
    return $self;
}

sub db_ua_getid {
    my ($self, $ua) = @_;
    my $sth = $self->prepare('SELECT id, count FROM ua_list WHERE ua = ?');
    $sth->execute($ua);
    if (defined(my $ref = $sth->fetchrow_hashref())) {
        $sth = $self->prepare('UPDATE ua_list SET count = ? WHERE id = ?');
        $sth->execute($ref->{'count'} + 1, $ref->{'id'});
        return $ref->{'id'};
    }
    $sth = $self->prepare('INSERT INTO ua_list (ua, count) VALUES (?, 1)');
    $sth->execute($ua);
    return $self->db_last_key('ua_list', 'id');
}

sub db_auth_cookie {
    my ($self, $user, $key) = @_;
    my $expr = Forum->config->GetParam('admin_authexpr');
    my $sth = $self->prepare('SELECT uid FROM auth WHERE cookie = ? AND ' .
        'uid = ? AND ' .
        'DATE_SUB(NOW(), INTERVAL ? DAY) < lastdate');
    $sth->execute($key, $user, $expr);
    if (defined(my $ref = $sth->fetchrow_hashref())) {
        $sth = $self->prepare('UPDATE auth SET lastdate = NOW() ' .
            'WHERE uid = ? AND cookie = ?');
        $sth->execute($user, $key);
        $self->_db_auth_cookie_squash();
        return $ref->{'uid'};
    }
    $self->_db_auth_cookie_squash();
    return 0;
}

sub db_revoke_cookie {
    my ($self, $user, $key) = @_;
    my $sth = $self->prepare('SELECT uid FROM auth WHERE cookie = ? AND ' .
        'uid = ?');
    $sth->execute($key, $user);
    if (defined(my $ref = $sth->fetchrow_hashref())) {
        $sth = $self->prepare('DELETE FROM auth WHERE uid = ? AND cookie = ?');
        $sth->execute($user, $key);
        return $ref->{'uid'};
    }
    return 0;
}

sub db_auth_setcookie {
    my ($self, $uid, $hash) = @_;
    my $sth = $self->prepare('INSERT INTO auth (uid, cookie, lastdate) VALUES (?, ?, NOW())');
    $sth->execute($uid, $hash);
}

################################################################## PRIVATE

sub _db_auth_cookie_squash {
    my ($self) = @_;
    my $expr = Forum->config->GetParam('admin_authexpr');
    my $sth = $self->prepare('DELETE FROM auth WHERE ' .
        'lastdate < DATE_SUB(NOW(), INTERVAL ? DAY)');
    $sth->execute($expr)
}

sub _handle_error {
    require Carp;
    my $db_err_maxlen = Forum->config->GetParam('db_err_maxlen');
    if (($db_err_maxlen > 0) && ($db_err_maxlen < length($_[0]))) {
        $_[0] = substr($_[0], 0, $db_err_maxlen / 2) . ' ... ' .
                substr($_[0], - $db_err_maxlen / 2);
        $_[0] = Carp::longmess($_[0]);
    }
    return 0;
}

1;

__END__



