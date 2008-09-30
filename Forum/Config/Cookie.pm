# -*- Mode: perl; indent-tabs-mode: nil -*-
#
# Module for Mozilla-Gumi Forum - Config Definition - cookie
#
# Copyright (C) 2008 - Mozilla-Gumi contributors
# Contributor(s):
#   Atsushi Shimono <shimono@mozilla.gr.jp>

package Forum::Config::Cookie;

use strict;

use Forum::Config::Common;

$Forum::Config::Cookie::sortkey = "01";

sub get_param_list {
    my $class = shift;
    my @param_list = (
        {
            name     => 'cookie_path',
            type     => 'text',
            default  => '',
        },
        {
            name     => 'cookie_domain',
            type     => 'text',
            default  => '',
        },
        {
            name     => 'cookie_expires',
            type     => 'text',
            default  => '+1m',
        },
    );
    return @param_list;
}

1;

__END__


