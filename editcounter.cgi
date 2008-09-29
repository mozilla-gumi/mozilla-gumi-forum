#! /usr/bin/perl

require './common.pl';
require './set.cgi';
use strict;
use vars qw($cou $met $c_f %tmplVars);

if (Forum->user->group_check('admin') == 0) {
    Forum->error->throw_error_user('not_logged_in');
}
if (! $cou) {
    Forum->error->throw_error_user('counter_not_used');
}

Forum->template->set_vars('mode_id', 'admin');
Forum->template->set_vars('mode_adm', 'count');
Forum->template->set_vars('htmltitle', 'Editor');

my $msg;
my $ncnt = Forum->cgi->param('newcount');
if (defined($ncnt)) {
    if($ncnt =~ /^\d+$/){
        open(NO,">$c_f") || Forum->error->throw_error_user("Can't write $c_f");
        print NO $ncnt;
        close(NO);
        $msg="<h3>カウンタ値編集完了</h3>";
    } else {
        Forum->template->set_vars('error_param', $ncnt);
        Forum->error->throw_error_user('invalid_param');
    }
}

print Forum->cgi->header();
Forum->template->process('htmlhead.tpl', \%tmplVars);

open(NO,"$c_f") || Forum->error->throw_error_user("Can't open $c_f");
my $cnt = <NO>;
close(NO);

print <<_BUP_;
<form action="editcounter.cgi" method="$met">
<input type="hidden" name="mode" value="del">
<strong>[カウンタ値編集]</strong><br>
カウント数/
<input type="text" name="newcount" value="$cnt" size="7">
<input type="submit" value="編集">
</form>

$msg

_BUP_

Forum->template->process('htmlfoot.tpl', \%tmplVars);

exit;


