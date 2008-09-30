# -*- Mode: perl; indent-tabs-mode: nil -*-
#
# Module for Mozilla-Gumi Forum - Config Definition - Captcha
#
# Copyright (C) 2008 - Mozilla-Gumi contributors
# Contributor(s):
#   Atsushi Shimono <shimono@mozilla.gr.jp>

package Forum::Config::Captcha;

use strict;

use Forum::Config::Common;

$Forum::Config::Captcha::sortkey = "01";

sub get_param_list {
    my $class = shift;
    my @param_list = (
        {
            name     => 'captcha_width',
            type     => 'number',
            default  => 25,
        },
        {
            name     => 'captcha_height',
            type     => 'number',
            default  => 35,
        },
        {
            name     => 'captcha_expire',
            type     => 'number',
            default  => 3600,
        },
        {
            name     => 'captcha_fail',
            type     => 'number',
            default  => 1,
        },
        {
            name     => 'captcha_length',
            type     => 'number',
            default  => 6,
        },
    );
    return @param_list;
}

1;

__END__




