# -*- Mode: perl; indent-tabs-mode: nil -*-
#
# Module for Mozilla-Gumi Forum - Config Definition - DB
#
# Copyright (C) 2008 - Mozilla-Gumi contributors
# Contributor(s):
#   Atsushi Shimono <shimono@mozilla.gr.jp>

package Forum::Config::DB;

use strict;

use Forum::Config::Common;

$Forum::Config::DB::sortkey = "01";

sub get_param_list {
    my $class = shift;
    my @param_list = (
        {
            name     => 'db_driver',
            type     => 'select',
            choices  => [ 'mysql' ],
            default  => 'mysql',
        },
        {
            name     => 'db_host',
            type     => 'text',
            default  => 'localhost',
        },
        {
            name     => 'db_name',
            type     => 'text',
            default  => 'forum',
        },
        {
            name     => 'db_port',
            type     => 'number',
            default  => 0,
        },
        {
            name     => 'db_sock',
            type     => 'text',
            default  => '',
        },
        {
            name     => 'db_user',
            type     => 'text',
            default  => 'forum',
        },
        {
            name     => 'db_pass',
            type     => 'text',
            default  => '',
        },
        {
            name     => 'db_err_maxlen',
            type     => 'number',
            default  => 4000,
        },
    );
    return @param_list;
}

1;

__END__




