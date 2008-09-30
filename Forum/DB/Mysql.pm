# -*- Mode: perl; indent-tabs-mode: nil -*-
#
# Module for Mozilla-Gumi Forum - DB Driver - MySQL
#
# Copyright (C) 2008 - Mozilla-Gumi contributors
# Contributor(s):
#   Atsushi Shimono <shimono@mozilla.gr.jp>

package Forum::DB::Mysql;

use strict;

use Forum::Constants;
use Forum::DB;

use base qw(Forum::DB);

sub new {
    my ($class, $user, $pass, $host, $dbname, $port, $sock) = @_;

    my $dsn = "DBI:mysql:host=$host;database=$dbname";
    $dsn .= ";port=$port" if $port;
    $dsn .= ";mysql_socket=$sock" if $sock;
    my $self = $class->db_new_conn($dsn, $user, $pass);

    $self->{private_table_locked} = "";
    bless($self, $class);

    return $self;
}

sub db_last_key {
    my ($self) = @_;
    my ($last_insert_id) = $self->selectrow_array('SELECT LAST_INSERT_ID()');
    return $last_insert_id;
}

sub db_lock_tables {
    my ($self, @tables) = @_;
    if ($self->{private_table_locked}) {
        Forum->error->throw_error_code("already_locked",
            {
                current => $self->{private_table_locked},
                new => join(', ', @tables),
            });
    } else {
        $self->do('LOCK TABLE ' . join(', ', @tables));
        $self->{private_table_locked} = join(', ', @tables);
    }
}

sub db_unlock_tables {
    my ($self, $abort) = @_;
    if (! $self->{private_table_locked}) {
        return if $abort;
        Forum->error->throw_error_code("not_locked");
    } else {
        $self->do('UNLOCK TABLES');
        $self->{private_table_locked} = '';
    }
}

################################################################## PRIVATE


1;

__END__




