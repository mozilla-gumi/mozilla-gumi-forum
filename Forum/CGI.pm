# -*- Mode: perl; indent-tabs-mode: nil -*-
#
# Module for Mozilla-Gumi Forum - CGI wrapper module
#
# Copyright (C) 2008 - Mozilla-Gumi contributors
# Contributor(s):
#   Atsushi Shimono <shimono@mozilla.gr.jp>

package Forum::CGI;

use strict;

use CGI qw(
    -no_xhtml
    :unique_headers
    :private_tempfiles
);
use base qw(CGI);

use Forum::Constants;
use Forum::Config;
use Forum::Error;

$| = 1; # disabling output buffering

sub DESTROY {};

sub new {
    my ($ic, @args) = @_;
    my $class = ref($ic) || $ic;
    my $self = $class->SUPER::new(@args);

    $self->{forum_cookie} = [];
    $self->charset('Shift_JIS');

    my $err = $self->cgi_error;
    if ($err) {
        print $self->header(-status => $err);
        die "CGI PARSER ERROR: $err";
    }

    return $self;
}

sub header {
    my $self = shift;
    if (scalar(@{$self->{forum_cookie}})) {
        if (scalar(@_) == 1) {
            unshift(@_, '-type' => shift(@_));
        }
        unshift(@_, '-cookie' => $self->{forum_cookie});
    }
    return $self->SUPER::header(@_) || "";
}

sub add_cookie {
    my $self = shift;

    my %param;
    my ($key, $value);
    while ($key = shift) {
        $value = shift;
        $param{$key} = $value;
    }

    if (! (defined($param{'-name'}) && defined($param{'-value'}))) {
        return;
    }
    $param{'-path'} = Forum->config->GetParam('cookie_path')
        if Forum->config->GetParam('cookie_path');
    $param{'-domain'} = Forum->config->GetParam('cookie_domain')
        if Forum->config->GetParam('cookie_domain');
    $param{'-expires'} = Forum->config->GetParam('cookie_expires')
        if Forum->config->GetParam('cookie_expires') &&
           (! defined($param{'-expires'}));

    my @parr;
    foreach (keys(%param)) {
        unshift(@parr, $_ => $param{$_});
    }

    push(@{$self->{forum_cookie}}, $self->cookie(@parr));
}

sub remove_cookie {
    my $self = shift;
    my ($name) = (@_);
    $self->add_cookie('-name'    => $name,
                      '-expires' => 'Tue, 01-Jan-1980 00:00:00 GMT',
                      '-value'   => 0);
}

################################################################## PRIVATE

1;

__END__




