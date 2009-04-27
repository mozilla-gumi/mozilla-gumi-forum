# -*- Mode: perl; indent-tabs-mode: nil -*-
#
# Module for Mozilla-Gumi Forum - Template
#
# Copyright (C) 2008 - Mozilla-Gumi contributors
# Contributor(s):
#   Atsushi Shimono <shimono@mozilla.gr.jp>

package Forum::Template;

use strict;

use base qw(Exporter);
use Template;

use Forum::Constants;
use Forum::Config;
use Forum::Util;
use Forum::User;

%Forum::Template::EXPORT = qw(
    new

    process

    set_vars
    vars
);

our $obj_config;
our $conf_template;
our %hash_vars = {};

sub new {
    my ($this) = @_;

    $obj_config = Forum->config;
    $conf_template = {
        INCLUDE_PATH => Forum::Constants::LOCATIONS()->{'rel_tmpl'},
        INTERPOLATE  => 1,
        POST_CHOMP   => 0,
        EVAL_PERL    => 1,
        COMPILE_DIR  => Forum::Constants::LOCATIONS()->{'datacache'},
#        DEBUG => 'parser, undef',
        PRE_PROCESS  => 'initialize.none.tmpl',
        FILTERS      => {
            none       => \&Forum::Util::filter_none,
            js         => \&Forum::Util::filter_js,
            html_lb    => \&Forum::Util::filter_html_lb,
            html_nb    => \&Forum::Util::filter_html_nb,
            html       => \&Forum::Util::filter_html,
            text       => \&Forum::Util::filter_text,
            url_quote  => \&Forum::Util::filter_url_quote,
            auto       => \&Forum::Util::filter_orig_auto,
            color_text => \&Forum::Util::filter_color_text,
            color_text => [
                sub {
                    my ($text, $words, $mode) = @_;
                    return sub {
                        my ($vars) = shift;
                        Forum::Util::filter_color_text($vars, $words, $mode);
                    };
                }, 1 ],
        },
        CONSTANTS => _load_constants(),
        VARIABLES => {
            'Param'    => sub { return $obj_config->GetHash(); },
            'in_group' => sub { return Forum->user->group_check($_[0]); },
            'user'     => sub { return Forum->user->user_data; },
        },
    };

    return $this;
}

sub process {
    my ($this, $template, $cur_vars, $out) = @_;
    my $obj_template = Template->new($conf_template);
    if (defined($cur_vars)) {
        foreach (keys(%$cur_vars)) {
            Forum->template->set_vars($_, $cur_vars->{$_});
        }
    }
    $obj_template->process($template, Forum->template->vars(), $out);
}

sub set_vars {
    my ($self, $name, $value) = @_;
    $hash_vars{$name} = $value;
}

sub vars {
    my ($self) = @_;
    return \%hash_vars;
}

################################################################## PRIVATE

sub _load_constants() {
    my %consts;
    foreach my $item (@Forum::Constants::EXPORT) {
        if (ref Forum::Constants->$item) {
            $consts{$item} = Forum::Constants->$item;
        } else {
            my @list = (Forum::Constants->$item);
            $consts{$item} = (scalar(@list) == 1) ? $list[0] : \@list;
        }
    }
    return \%consts;
}


1;

__END__


