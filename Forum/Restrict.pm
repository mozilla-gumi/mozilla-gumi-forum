# -*- Mode: perl; indent-tabs-mode: nil -*-
#
# Module for Mozilla-Gumi Forum - Access/Modification restrict
#
# Copyright (C) 2009 - Mozilla-Gumi contributors
# Contributor(s):
#   Atsushi Shimono <shimono@mozilla.gr.jp>

package Forum::Restrict;

use strict;

use Forum::Constants;
use Forum::Error;
use Forum::DB;

@Forum::Restrict::EXPORT = qw(
    check_ip
);

# CREATE TABLE ip_blacklist (
#   ipstart       int                  NOT NULL                            ,
#   ipend         int                  NOT NULL                            ,
#   datereg       DATETIME             NOT NULL                            ,
#   dateend       DATETIME             NOT NULL                            ,
#   isread        ENUM("no", "yes")    NOT NULL                            ,
#   reason        tinytext             NOT NULL                            
# );
sub check_ip {
    my $sth = Forum->DB->prepare(
        "SELECT * FROM ip_blacklist " _
        "WHERE ipstart <= ? AND ipend >= ? AND dateend >= NOW()");
}

sub get_list {
}

sub add {
    my ($ipstart, $ipend, $dateend, $isread, $reason) = @_;
}


################################################################## PRIVATE


1;

__END__

