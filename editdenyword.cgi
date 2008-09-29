#!/usr/local/bin/perl

require './common.pl';
require './set.cgi';
use strict;
use vars qw($met %tmplVars);

if (Forum->user->group_check('admin') == 0) {
    Forum->error->throw_error_user('not_logged_in');
}

my $NWFile = "../data/cbbs/WordDeny.cgi";

print Forum->cgi->header();
Forum->template->set_vars('mode_id', 'admin');
Forum->template->set_vars('mode_adm', 'word');
Forum->template->set_vars('htmltitle', 'Deny Word Editor');
Forum->template->process('htmlhead.tpl', \%tmplVars);

my @d_ = Forum->cgi->param('del');

my $m = Forum->cgi->param('m');
my $Log = $NWFile;
my $msd = '';
my @deny;
my @NEW;

if($m eq "Add"){
    my $form_u = Forum->cgi->param('u');
    $form_u =~ s/\&lt\;/</g;
    $form_u =~ s/\&gt\;/>/g;
    open(OUT,">>$Log");
    print OUT "$form_u\n";
    close(OUT);
    $msd="<h3>$Logへ登録完了</h3>";
}elsif($m eq "Del"){
    open(DB,"$Log");
    @deny = <DB>;
    close(DB);
    @NEW = ();
    my $F=0;
    foreach $b (@deny) {
        $b =~ s/\n//g;
        foreach my $u (@d_) {if($u eq "$b"){$F=1; last;}}
        if($F){$F=0; next;}
        push(@NEW,"$b\n");
    }
    open (DB,">$Log");
    print DB @NEW;
    close(DB);
    $msd="<h3>$Log内削除完了</h3>";
}

print<<"_HTML_";
<table summary="deny" width="95\%">
<tr><th>排除IP/禁止文字列設定モード</th></tr></table>$msd
<ul>
<li>指定した物が含まれているとそれぞれ排除されます。</li>
<li><strong>[禁止文字列?]</strong> 使用されたくない文字列を指定します。大文字小文字は区別されます。<br>
例) 宣伝記事→URLを指定。タグ→開始タグの一部 &lt;img &lt;font 等。</li>
</ul>
_HTML_
my $Dcom="禁止文字列";
    if(-e $Log){
        open(DB,$Log) || Forum->error->throw_error_user("Can't open $Log");
        @deny = <DB>;
        close(DB);
# deleted $pass from html form : non needed : $pass => --pass--
        print<<"_EDIT_";
<hr><strong>■ $Dcomの追加</strong>
<form action="editdenyip.cgi" method="$met">
<input type="hidden" name="m" value="Add">
$Dcom /<input type="text" name="u" size="25" value=""> (例/cj-c.com)
_EDIT_
        print<<"_EDIT_";
<input type="submit" value="追 加">
</form><strong>■ $Log に登録済みの$Dcom</strong>
<form action="editdenyip.cgi" method="$met">
<input type="hidden" name="m" value="Del">
_EDIT_
        foreach(0..$#deny){
            $deny[$_]=~ s/\n//g; $deny[$_]=~ s/</\&lt\;/g; $deny[$_]=~ s/>/\&gt\;/g;
            print"<input type=\"checkbox\" name=\"del\" value=\"$deny[$_]\">- $deny[$_]<br>\n";
        }
        print '<br><input type="submit" value="削 除" ' . "\"><input type=\"reset\" value=\"リセット\"></form></ul>\n";
    }
    print"<hr width=\"95\%\">\n";
    Forum->template->process('htmlfoot.tpl', \%tmplVars);

exit;

