# -*- Mode: perl; indent-tabs-mode: nil -*-
#
# Module for Mozilla-Gumi Forum - Config Definition - Administration
#
# Copyright (C) 2008 - Mozilla-Gumi contributors
# Contributor(s):
#   Atsushi Shimono <shimono@mozilla.gr.jp>

package Forum::Config::Admin;

use strict;

use Forum::Config::Common;

$Forum::Config::Admin::sortkey = "01";

sub get_param_list {
    my $class = shift;
    my @param_list = (
        {
            name     => 'admin_pass',
            type     => 'text',
            default  => '',
        },
        {
            name     => 'admin_authexpr',
            type     => 'number',
            default  => 7,
        },
    );
    return @param_list;
}

1;

__END__




