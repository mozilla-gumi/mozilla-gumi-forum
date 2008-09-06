#! /usr/bin/perl

use strict;

if ($ENV{'REQUEST_METHOD'} ne 'GET') {
    print "Content-Type: text/plain\n\nerror\n";
    exit;
}

my $md5sum = $ENV{'QUERY_STRING'};
if ($md5sum =~ /\//) {
    print "Content-Type: text/plain\n\nerror1\n";
    exit;
}
if ( -r "../data/captcha/$md5sum.png" ) {
    open (INDAT, "../data/captcha/$md5sum.png");
    print "Content-Type: image/png\n\n";
    binmode INDAT;
    print <INDAT>;
    close (INDAT);
} else {
    print "Content-Type: text/plain\n\nerror2\n";
    exit;
}

exit;

