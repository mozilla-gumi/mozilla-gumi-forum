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
    $msd="<h3>$Log�֓o�^����</h3>";
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
    $msd="<h3>$Log���폜����</h3>";
}

print<<"_HTML_";
<table summary="deny" width="95\%">
<tr><th>�r��IP/�֎~������ݒ胂�[�h</th></tr></table>$msd
<ul>
<li>�w�肵�������܂܂�Ă���Ƃ��ꂼ��r������܂��B</li>
<li><strong>[�֎~������?]</strong> �g�p���ꂽ���Ȃ���������w�肵�܂��B�啶���������͋�ʂ���܂��B<br>
��) ��`�L����URL���w��B�^�O���J�n�^�O�̈ꕔ &lt;img &lt;font ���B</li>
</ul>
_HTML_
my $Dcom="�֎~������";
    if(-e $Log){
        open(DB,$Log) || Forum->error->throw_error_user("Can't open $Log");
        @deny = <DB>;
        close(DB);
# deleted $pass from html form : non needed : $pass => --pass--
        print<<"_EDIT_";
<hr><strong>�� $Dcom�̒ǉ�</strong>
<form action="editdenyip.cgi" method="$met">
<input type="hidden" name="m" value="Add">
$Dcom /<input type="text" name="u" size="25" value=""> (��/cj-c.com)
_EDIT_
        print<<"_EDIT_";
<input type="submit" value="�� ��">
</form><strong>�� $Log �ɓo�^�ς݂�$Dcom</strong>
<form action="editdenyip.cgi" method="$met">
<input type="hidden" name="m" value="Del">
_EDIT_
        foreach(0..$#deny){
            $deny[$_]=~ s/\n//g; $deny[$_]=~ s/</\&lt\;/g; $deny[$_]=~ s/>/\&gt\;/g;
            print"<input type=\"checkbox\" name=\"del\" value=\"$deny[$_]\">- $deny[$_]<br>\n";
        }
        print '<br><input type="submit" value="�� ��" ' . "\"><input type=\"reset\" value=\"���Z�b�g\"></form></ul>\n";
    }
    print"<hr width=\"95\%\">\n";
    Forum->template->process('htmlfoot.tpl', \%tmplVars);

exit;

