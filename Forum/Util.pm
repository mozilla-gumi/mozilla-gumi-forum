# -*- Mode: perl; indent-tabs-mode: nil -*-
#
# Module for Mozilla-Gumi Forum - Utility functions
#
# Copyright (C) 2008 - Mozilla-Gumi contributors
# Contributor(s):
#   Atsushi Shimono <shimono@mozilla.gr.jp>

package Forum::Util;

use strict;

use Template;

@Forum::Util::EXPORT = qw(
    filter_none
    filter_js
    filter_html_lb
    filter_html_nb
    filter_html
    filter_text
    filter_url_quote
    filter_orig_auto
);

sub filter_none {
    return $_[0];
}

sub filter_js {
    my ($var) = @_;
    $var =~ s/([\\\'\"\/])/\\$1/g;
    $var =~ s/\n/\\n/g;
    $var =~ s/\r/\\r/g;
    $var =~ s/\@/\\x40/g; # anti-spam for email addresses
    return $var;
}

sub filter_html_lb {
    my ($var) = @_;
    $var =~ s/\r\n/\&#013;/g;
    $var =~ s/\n\r/\&#013;/g;
    $var =~ s/\r/\&#013;/g;
    $var =~ s/\n/\&#013;/g;
    return $var;
}

sub filter_html_nb {
    my ($var) = @_;
    $var =~ s/ /\&nbsp;/g;
    $var =~ s/-/\&#8209;/g;
    return $var ;
}

sub filter_html {
    my ($var) = Template::Filters::html_filter(@_);
    $var =~ s/\@/\&#64;/g;
    return $var;
}

sub filter_text {
    my ($var) = @_;
    $var =~ s/<[^>]*>//g;
    $var =~ s/\&#64;/@/g;
    $var =~ s/\&lt;/</g;
    $var =~ s/\&gt;/>/g;
    $var =~ s/\&quot;/\"/g;
    $var =~ s/\&amp;/\&/g;
    return $var;
}

sub filter_url_quote {
    my ($var) = @_;
    # IF utf8 mode, must utf8::encode 'var'
    $var =~ s/([^a-zA-Z0-9_\-.])/uc sprintf("%%%02x",ord($1))/eg;
    return $var;
}

sub filter_orig_auto {
    my ($var) = @_;
    my $preremoved = 0;
    if ($var =~ /<\/?pre>/i) {
        $var =~ s/<pre>//i;
        $var =~ s/<\/pre>//i;
        $preremoved = 1;
    }
    # tweak (for text data file)
    $var =~ s/<br[^\>]*>/\r\n/g;
    # maint
    $var = "\r\n" . $var . "\r\n";

    # article number linkify
    $var =~ s/\r\n((?:\>|&gt;)(?:\>|&gt;| |\t)*)([0-9\,\-]+)([^\r\n]*)/\r\n<a href=\"?mode=one&amp;namber=$2\">$1$2<\/a>$3/g;
    $var =~ s/(no)\s*([0-9\,\-]+)/<a href=\"?mode=one&amp;namber=$2\">$1$2<\/a>/ig;

    # URI linkify
    $var =~ s/([^=^\"]|^)((h?)(ttp|ttps)(\:[\w\.\~\-\/\?\&\+\=\:\@\%\;\#\,\|]+))/$1<a href="h$4$5">$3$4$5<\/a>/g;
    $var =~ s/([^=^\"]|^)((ftp)\:[\w\.\~\-\/\?\&\+\=\:\@\%\;\#\,\|]+)/$1<a href="$2">$2<\/a>/g;
    # mark ">xxxx" lines as quoted
    $var =~ s/\r\n((?:&gt;|>)[^\r\n]*)/\r\n<span class="Quoted">$1<\/span>/g;

    # bug-jp 6389
    $var =~ s!mozillazine-jp +([0-9]+)!<a href="http://forums.mozillazine.jp/viewtopic.php?t=$1">mozillazine-jp $1</a>!g;
    $var =~ s!bug-jp +([0-9]+)!<a href="http://bugzilla.mozilla.gr.jp/show_bug.cgi?id=$1">bug-jp $1</a>!g;
    $var =~ s!bug-org +([0-9]+)!<a href="https://bugzilla.mozilla.org/show_bug.cgi?id=$1">bug-org $1</a>!g;

    if ($preremoved eq 1) {
        $var = '<pre>' . $var . '</pre>';
        $var =~ s/<br[\/ ]*/\n/g;
    } else {
        $var =~ s/\r\n/<br \/>\r\n/g;
    }
    return $var;
}


1;

__END__


