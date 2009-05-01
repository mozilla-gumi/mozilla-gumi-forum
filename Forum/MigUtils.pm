# -*- Mode: perl; indent-tabs-mode: nil -*-
#
# Module for Mozilla-Gumi Forum - Utilities only for migration
#
# Copyright (C) 2009 - Mozilla-Gumi contributors
# Contributor(s):
#   Atsushi Shimono <shimono@mozilla.gr.jp>

package Forum::MigUtils;

use strict;

use Forum::Constants;
use Forum::Error;

@Forum::MigUtils::EXPORT = qw(
    to_hash
    match_hash
);

sub to_hash {
    my ($key) = @_;
    my $time = time;
    my ($p1, $p2) = unpack("C2", $time);
    my $wk = $time / (60 * 60 * 24 * 7) + $p1 + $p2 - 8;
    my @saltset = ('a'..'z', 'A'..'Z', '0'..'9', '.', '/');
    my $nsalt = $saltset[$wk % 64] . $saltset[$time % 64];
    return crypt($key, $nsalt);
}

# return 1 on OK, return 0 on NG
sub match_hash {
    my ($match, $de, $key) = @_;
    my $crptkey = 0;
    if ($de =~ /^\$match\$/) {
        $crptkey = 3;
    }
    if (crypt($key, substr($de, $crptkey, 2)) eq $de) {
        return 1;
    }
    return 0;
}


################################################################## PRIVATE


1;

__END__

