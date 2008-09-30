# -*- Mode: perl; indent-tabs-mode: nil -*-
#
# Module for Mozilla-Gumi Forum - Config Loader
#
# Copyright (C) 2008 - Mozilla-Gumi contributors
# Contributor(s):
#   Atsushi Shimono <shimono@mozilla.gr.jp>

package Forum::Config;

use strict;

use base qw(Exporter);
use Data::Dumper;
use File::Temp;
use Safe;

use Forum::Constants;
use Forum::Error;

%Forum::Config::EXPORT = qw(
    new

    param_groups

    update_file
    GetParam
    SetParam
    GetHash

    check_param
);

our %params_def;
our $params;

sub new {
    my ($this) = @_;

    _load_param_list();
    $params = _read_param_file();
    _screen_params();

    return $this;
}

sub update_file {
    _write_param_file();
    $params = _read_param_file();
}

sub GetParam {
    my ($this, $name) = @_;
    if (! defined($name)) {
        return "";
    }
    return $params->{$name};
}

sub SetParam {
    my ($this, $name, $value) = @_;
    if (defined($name) && defined($value)) {
        $params->{$name} = $value;
    }
}

sub GetHash {
    return $params;
}

sub param_groups {
    my $param_groups = {};
    my $param_path = LOCATIONS()->{'install'};
    foreach my $item ((glob "$param_path/Forum/Config/*.pm")) {
        $item =~ m#/([^/]+)\.pm$#;
        my $group = $1;
        if ($group eq 'Common') {next; }
        $param_groups->{$group} = "Forum::Config::$group";
    }
    return $param_groups;
}

sub check_param {
    my ($self, $item, $value) = @_;
    my $cat = $item->{'type'};
    if ($cat eq 'number') {
    } elsif ($cat eq 'text') {
    } elsif ($cat eq 'select') {
    } else {
        $value = '';
    }
    if (exists $item->{'check'}) {
        my $err = $item->{'check'}->($value, $item);
        if ($err ne '') {
            Forum->error->throw_error_user('invalid_param',
                {name => $item->{'name'}, err => $err});
        }
    }
    return $value;
}

################################################################## PRIVATE

sub _load_param_list {
    my $panels = param_groups();
    foreach my $panel (keys %$panels) {
        my $mod_name = $panels->{$panel};
        eval("require $mod_name") || die "Require error $mod_name: $@";
        my @new_params = $mod_name->get_param_list();
        foreach my $item (@new_params) {
            $params_def{$item->{'name'}} = $item;
        }
    }
}

sub _screen_params {
    foreach my $item (keys %$params) {
        if (! defined($params_def{$item})) {
            delete $params->{$item};
        }
    }
    foreach my $item (keys %params_def) {
        if (! defined($params->{$item})) {
            $params->{$item} = $params_def{$item}->{'default'};
        }
    }
}

sub _write_param_file {
    my $param_dir  = LOCATIONS()->{'datadat'};
    my $param_file = $param_dir . '/params';
    _screen_params();

    # start dumping to file
    local $Data::Dumper::Sortkeys = 1;
    my ($fh, $tmpname) =
        File::Temp::tempfile('params.XXXXXX', DIR => $param_dir);
    print $fh (Data::Dumper->Dump([$params], ['*param']))
        || die "Can't write param file: $!";
    close $fh;

    # rename temporary file
    rename $tmpname, $param_file
        || die "Can't rename $tmpname to $param_file: $!";
}

sub _read_param_file {
    my %params;
    my $param_file = LOCATIONS()->{'datadat'} . '/params';
    if (-e $param_file) {
        # to read Dump-ed object file.
        my $obj_safe = new Safe;
        $obj_safe->rdo($param_file);
        die "Error reading $param_file: $!" if $!;
        die "Error evaluating $param_file: $@" if $@;
        %params = %{$obj_safe->varglob('param')};
    }
    # FATAL TRIAGE
    elsif ($ENV{'SERVER_SOFTWARE'}) {
        require CGI::Carp;
        CGI::Carp->import('fatalsToBrowser');
        die "ERROR READING PARAMETER DATA (params)",
    }
    return \%params;
}

1;

__END__




