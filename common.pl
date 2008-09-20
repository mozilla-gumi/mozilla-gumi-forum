#! /usr/bin/perl

use CGI;
use CGI::Carp;
use Encode;
use Encode::Guess qw/euc-jp shift-jis/;

use Forum;
use Forum::Template;
use Forum::Config;
use Forum::Error;

our $obj_cgi        = Forum->cgi;
our $obj_template   = Forum->template;
our $obj_config     = Forum->config;
our $obj_db         = Forum->dbh;
our $obj_user       = Forum->user;

our %tmplVars;

our $cfBrowser = Forum::Constants::LOCATIONS()->{'datacbbs'} . '/browser.dat';
our $cfMailer  = Forum::Constants::LOCATIONS()->{'datacbbs'} . '/mailer.dat';
our $cfOS      = Forum::Constants::LOCATIONS()->{'datacbbs'} . '/os.dat';

# default values : ip etc
$tmplVars{'COMipaddr'} = $ENV{'REMOTE_ADDR'};

sub UAsel{
    my @tmplist;
    my $tmpval;
    my $tmpcnd;

    my @listos = ();
    my $selos = '';
    if ( -f $cfOS ) {
        open(INDAT, $cfOS);
        foreach (<INDAT>) {
            chomp;
            @tmplist = split(/\t/, $_);
            $tmpval = shift(@tmplist);
            while ($tmpcnd = shift(@tmplist)) {
                if ($ENV{'HTTP_USER_AGENT'} !~ /${tmpcnd}/) {last; }
            }
            if ((!defined ($tmpcnd)) && ($selos eq '')) {
                $selos = $tmpval;
            } else {
                push(@listos, $tmpval);
            }
        }
        close(INDAT);
    } else {
        &er_('Can not open OS list data file.');
    }
    $tmplVars{'listos'} = \@listos;
    if($selos ne '') {
        $tmplVars{'os'} = $selos;
    }

    my @listbrowser = ();
    my $selbrowser = '';
    if ( -f $cfBrowser ) {
        open(INDAT, $cfBrowser);
        foreach (<INDAT>) {
            chomp;
            @tmplist = split(/\t/, $_);
            $tmpval = shift(@tmplist);
            while ($tmpcnd = shift(@tmplist)) {
                if ($ENV{'HTTP_USER_AGENT'} !~ /${tmpcnd}/) {last; }
            }
            if ((!defined ($tmpcnd)) && ($selbrowser eq '')) {
                $selbrowser = $tmpval;
            } else {
                push(@listbrowser, $tmpval);
            }
        }
        close(INDAT);
    } else {
        &er_('Can not open browser list data file.');
    }
    $tmplVars{'listbrowser'} = \@listbrowser;
    if ($selbrowser ne '') {
        $tmplVars{'browser'} = $selbrowser;
    }

    my @listmua;
    if ( -f $cfMailer ) {
        open(INDAT, $cfMailer);
        foreach (<INDAT>) {
            chomp;
            push(@listmua, $_);
        }
        close(INDAT);
    } else {
        &er_('Can not open mailer list data file.');
    }
    $tmplVars{'listmua'} = \@listmua;

    my $retVal = '';
    $obj_template->process('environment.tpl', \%tmplVars, \$retVal);
    return $retVal;
}


sub RSS{
    my %tmplRSS;
    my @rssItem;
    $RSS_I='';
    $RSS_R='';
    $desc_len = 2;
    $com = 0;
    $time = &RSStime(time());
    $rssfile = '../data/dat/news.rdf';

    $tmplRSS{'rsstarget'} = 'http://forum.mozilla.gr.jp/';

    @NEW=();
    open(DB, "$log");
    while (<DB>) {
        ($nam,$date,$name,$email,$d_may,$comment,$url,
        $sp,$end,$ty,$del,$ip,$time,$Se) = split(/<>/,$_);
        if (($time_k - $time) <= $new_t * 3600) {push(@NEW,"$time<>$_<>");}
    }
    close(DB);

    @NEW = reverse(sort(@NEW));
    if (($conf{'rss_num'} ne 0) && ($#NEW >= $conf{'rss_num'})) {
        $#NEW = $conf{'rss_num'} - 1;
    }

    if (@NEW) {
        if (! $conf{'rss_rev'}) {@NEW = reverse(@NEW); }
        foreach (@NEW) {
            my %rssOne;
            ($Tim,$nam,$date,$name,$email,$d_may,$comment,$url,
            $sp,$end,$ty,$del,$ip,$time,$Se) = split(/<>/,$_);
            $d_may   =~ s/\[(\d)+\]//g;
            $comment =~ s/<br>/\n/g;
            $comment =~ s/>>/>/g;
            $comment =~ s/> >/>/g;
            $comment =~ s/>/&gt;/g;
            $comment =~ s/</&lt;/g;
            $comment =~ s/200[34]*?•ÒW\((“Še|ŠÇ—)ŽÒ\)\n//g;
            $comment =~ s/^\n*//g;
            $comment =~ s/\n*$//g;
            $ty = $nam if (!$ty);

            $time = &RSStime($time);
            $desc = &RSS_cutstr($comment, $desc_len);
            $comment =~ s/\n/<br \/>/g;
            $rssOne{'content'} = $comment;
            $rssOne{'desc'} = $desc;
            $rssOne{'nam'} = $nam;
            $rssOne{'ty'} = $ty;
            $rssOne{'sp'} = $sp;
            $rssOne{'d_may'} = $d_may;
            $rssOne{'name'} = $name;
            $rssOne{'time'} = $time;
            $com++;
            push(@rssItem, \%rssOne);
        }
    }

    $tmplRSS{'items'} = \@rssItem;
    $obj_template->process('rss.tpl', \%tmplRSS, \$RSS_OUT);
    open(RSS, ">$rssfile") || &er_("Can't write $rssfile", "1");
    print RSS $RSS_OUT;
    close(RSS);

}

sub RSS_sanit ($) {
    my ($desc) = @_;
    $desc =~ s/&lt;(.*)&gt;?//g;
    $desc =~ s/\n&gt;(.*)\n?/\n/g;
    $desc =~ s/&gt;(.*)\n?/\n/g;
    $desc =~ s/&quot;//g;
    $desc =~ s/&amp;//g;
    $desc =~ s/(\n)+/\n/g;
    $desc =~ s/([\x00-\x09\x0b\x0c\x0e-\x1f])/'&#'.unpack('H2',$1).';'/ge;
    return $desc;
}

sub RSS_cutstr ($$) {
    my ($desc, $desc_len) = @_;
    my (@lines);
    @lines = split(/\n/, $desc);
    $#lines = $desc_len - 1;
    return join("\n", @lines);
}

sub RSStime ($) {
    my ($time) = @_;
    my ($sec, $min, $hour, $mday, $mon, $year) = (localtime($time))[0..5];
    my $format = "%04d-%02d-%02dT%02d:%02d:%02d%s";
    $year += 1900;
    $mon  += 1;
    $time = sprintf($format, $year, $mon, $mday, $hour, $min, $sec);
    $time .= '+09:00';
    return $time;
}

sub delcollect{
    $del_file = '../data/dat/deleted.txt';
    open(OUT, ">>$del_file");
    print OUT "$mens\n";
    close (OUT);
}


1;

