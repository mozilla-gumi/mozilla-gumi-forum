# -*- Mode: perl; indent-tabs-mode: nil -*-
#
# Module for Mozilla-Gumi Forum - Captcha module
#
# Copyright (C) 2008 - Mozilla-Gumi contributors
# Contributor(s):
#   Atsushi Shimono <shimono@mozilla.gr.jp>

package Forum::Captcha;

use strict;

use base qw(Exporter);
use Authen::Captcha;

use Forum::Constants;
use Forum::Config;

%Forum::Captcha::EXPORT = qw(
    new

    check
    generate

    get_md5
    get_code
);

our $obj_captcha;
our $obj_config;

our $cur_md5;
our $cur_code;

sub new {
    my ($this) = @_;

    $obj_captcha = Authen::Captcha->new();
    $obj_config = Forum->config;

    $obj_captcha->data_folder(Forum::Constants::LOCATIONS()->{'datacaptcha'});
    $obj_captcha->output_folder(Forum::Constants::LOCATIONS()->{'datacaptcha'});
    $obj_captcha->width($obj_config->GetParam('captcha_width'));
    $obj_captcha->height($obj_config->GetParam('captcha_height'));
    $obj_captcha->expire($obj_config->GetParam('captcha_expire'));
    $obj_captcha->keep_failures($obj_config->GetParam('captcha_fail'));

    return $this;
}

sub check {
    my ($this, $auth, $md5) = @_;
    return $obj_captcha->check_code($auth, $md5);
}

sub generate {
    my ($this, $length) = @_;
    ($cur_md5, $cur_code) = $obj_captcha->generate_code($length);
    return $cur_md5;
}

sub get_md5 {
    return $cur_md5;
}

sub get_code {
    return $cur_code;
}

################################################################## PRIVATE

1;

__END__




