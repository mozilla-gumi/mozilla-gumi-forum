# -*- Mode: perl; indent-tabs-mode: nil -*-
#
# Module for Mozilla-Gumi Forum - Constants Definitions
#
# Copyright (C) 2008 - Mozilla-Gumi contributors
# Contributor(s):
#   Atsushi Shimono <shimono@mozilla.gr.jp>

package Forum::Constants;

use strict;

use base qw(Exporter);
use File::Basename;
use Cwd;

@Forum::Constants::EXPORT = qw(
  FORUM_VERSION

  LOCATIONS

  contenttypes
  SAFE_PROTOCOLS
  DB_MODULE

  DB_UNLOCK_ABORT
);


use constant FORUM_VERSION => "0.1.1";

use constant contenttypes =>
  {
    "html" => "text/html" ,
    "rdf"  => "application/rdf+xml" ,
    "atom" => "application/atom+xml" ,
    "xml"  => "application/xml" ,
    "js"   => "application/x-javascript" ,
    "csv"  => "text/csv" ,
    "jpg"  => "image/jpeg" ,
    "gif"  => "image/gif" ,
    "png"  => "image/png" ,
    "ics"  => "text/calendar" ,
  };

use constant SAFE_PROTOCOLS => (
  'ftp', 'http', 'https', 'irc', 'view-source',
);

use constant DB_MODULE => {
    'mysql'   => {
        db   => 'Forum::DB::Mysql',
        dbd  => 'DBD::mysql',
        name => 'MySQL',
    },
};

# DB
use constant DB_UNLOCK_ABORT => 1;

# installation locations
# parent
#  => <installation>/ : script installation (like public_html)
#  => data/ : data storage
#    => cache/ : Perl TT cache
#    => captcha/ : Captcha module temporary storage
#    => cbbs/ : Settings (will be deleted?)
#    => dat/ : Data storage (will be deleted?)
sub LOCATIONS {
    # absolute path for installation ("installation")
    my $inspath = dirname(dirname($INC{'Forum/Constants.pm'}));
    # detaint
    $inspath =~ /(.*)/;
    $inspath = $1;
    if ($inspath eq '.') {
       $inspath = getcwd();
    }
    my $parpath = dirname($inspath);
    my $instname = substr($inspath, length($parpath) + 1);
    my $datapath = "$parpath/data";

    return {
        'install'     => $inspath,
        'cgi_path'    => $inspath,
        'rel_tmpl'    => './tmpl/',
        'templates'   => "$inspath/tmpl",
        'datadir'     => $datapath,
        'datacache'   => "$datapath/cache",
        'datacaptcha' => "$datapath/captcha",
        'datacbbs'    => "$datapath/cbbs",
        'datadat'     => "$datapath/dat",
        'instname'    => $instname,
    };
}


1;

__END__

