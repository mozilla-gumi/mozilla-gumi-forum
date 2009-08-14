#! /usr/bin/perl

## WARNING!!!!
## もとの cbbs の設定ファイルとは大幅に違います。
## コメントを参考にして編集してください。
## $tmplVars{}になっている変数はそのうちテンプレートファイルへ移動します。
## 全ての変数は$conf{}に移行予定です。
## 全ての変数が$conf{}に移行後、設定ファイルはテキストベースになる予定です。

# オプションは基本的に以下のようにする
#  0 : しない、不可能
#  1 : する、可能
#  1 は not 0 を意味する

our %conf;
our %tmplVars;

our $ver = "Child Tree v8.92 (modified)";

#--- [基本設定] ----------------#
our $met   = "POST";        # 送信形式(POST or GET/ファイルアップを使う場合はPOST限定)
    $tmplVars{'met'} = $met;
$TOPH = 1;            # 初期表示(0=スレッド型 1=ツリー型 2=トピック型)
$max  = 100;            # 親記事最大保持件数
    $tmplVars{'max'} = $max;

#--- [記事投稿に関する設定] ----#
$topok= 1;            # 親記事投稿はだれでも可能?(1=YES 0=管理者のみ)
    $tmplVars{'topok'} = $topok;
$he_tp= 0;            # 返信を親記事投稿者のみの権利にする?(1=YES 0=NO)
    $tmplVars{'he_tp'} = $he_tp;
$r_max= 100;        # 返信の限度数(0 にすると無制限)
    $tmplVars{'r_max'} = $r_max;
$Res_i= 0;            # 記事引用を任意にする?(1=任意 0=自動)
$Res_T= 0;            # 親記事を投稿順に並べる?(1=YES 0=レス最新順)
$AgSg = 1;            # レスの際、記事移動を任意にする?(1=任意 0=自動)
$EStmp= 1;            # 編集されたらタイムスタンプを押す?(1=YES 0=NO)
$UID  = 0;            # ID機能を使う?(1=YES 0=NO / クッキー機能必須)
$tag  = 0;            # タグの使用(YES=1 NO=0)
    $tmplVars{'use_post_edit'} = 0;         # 投稿の編集・削除フォーム
    $tmplVars{'use_password'} = 0;          # 投稿時のパスワード登録フォーム

#--- [記事表示に関する設定] ----#
$t_max= 128;            # 記事タイトル表示限度(初期-半角40字/全角20字)
$AMark= '＠';            # メールアドレス置き換え文字列(画像の場合は<img>で)
$SPAM = ' ';            # アドレス収集ソフト対策(アドレスに追加され表示される文字列)
$TGT  = '';        # HOME以外の掲示板外へのリンクターゲット
    $tmplVars{'TGT'} = $TGT;

#--- [記事タイトルのヘッダを設定] -----------------------------------------------------------------
#       
# 画像=> <img>タグ / テキスト=> □など直接書く
# $hed_i は通常記事用 (テキスト例：○ / ●)
# $new_i は新着記事用 (テキスト例：Ｎ / NEW)
# $all_i は一括表示用 (テキスト例：□ / ALL) => ツリー表示用
# $up_i_ は更新記事用 (テキスト例：UP / ◇)  => トピック/スレッド表示用
#--------------------------------------------------------------------------------------------------
$hed_i= '<img src="file/hed.gif" height="15" width="15" border="0" alt="Message">';
$new_i= '<img src="file/new.gif" height="15" width="15" border="0" alt="New">';
$all_i= '<img src="file/all.gif" height="16" width="16" border="0" alt="All">';
$up_i_= '<img src="file/uph.gif" height="15" width="15" border="0" alt="Updated">';
    $tmplVars{'hed_i'} = $hed_i;
    $tmplVars{'new_i'} = $new_i;
    $tmplVars{'all_i'} = $all_i;
    $tmplVars{'up_i_'} = $up_i_;

#--- [チェックボックス設定] ----#
$end_f = 1;            # 解決チェックボックスを使う？(1=YES 0=NO)
$end_c = 0;            # 解決チェックは管理人のみ可能にする?(1=YES 0=NO)
$end_e = 0;            # 解決チェックが付いたら返信不可にする?(1=YES 0=NO)

# ●チェック時、表示する物(タグ可 画像の時は<img>タグ)
$end_ok= '<strong class="red">済!</strong>';
    $tmplVars{'end_ok'} = $end_ok;


#--------------------------------------------------------------------------------------------------
# ●チェックを促すコメント(例: 解決したらチェック！)
$end_m =<<"_END_";

問題が解決したらチェックしてください

_END_
    $tmplVars{'end_m'} = $end_m;


#--- [ツリー表示設定] ----------*
    $tmplVars{'TrON'}  = 1;            # ツリー表示を使う?(1=YES 0=NO)
$a_max = 10;            # 1ページ表示ツリー数
$obg   = "#E0ECF6";        # 親記事のツリー背景色(〃)
$Keisen= 1;            # 罫線を表示する?(1=YES 0=NO)
$K_I   = '<img src="file/ol_ver.gif" height="14" width="15" alt="|">';            # 罫線(連結型/画像の場合は<img>)
$K_T   = '<img src="file/ol_con.gif" height="14" width="15" alt="|-">';            # 罫線(分岐型/ 〃 )
$K_L   = '<img src="file/ol_edg.gif" height="14" width="15" alt="L">';            # 罫線(終了型/ 〃 )
$K_SP  = '<img src="file/1pix.gif" height="1" width="15" alt="">';            # 罫線(スペース/ 〃)
    $tmplVars{'K_I'} = $K_I;
    $tmplVars{'K_T'} = $K_T;
    $tmplVars{'K_L'} = $K_L;
    $tmplVars{'K_SP'} = $K_SP;
$zure  = 6;            # ツリーのずれ調整(罫線OFFの場合有効)

#--- [トピック表示設定] --------*
    $tmplVars{'TpON'}  = 1;            # トピック表示を使う?(1=YES 0=NO)
$tab_m = 2;            # 1ページ表示テーブル数
$tpmax = 10;            # テーブル1つ当りの表示トピック数
$topic = 10;            # 1トピックの1ページ当りの表示数
$tp_hi = 0;            # トピック内容の初期配列(1=新着記事トップ 0=親トピックトップ)
$tpend = 0;            # レス後の表示内容(0=トップ 1=レスしたトピック)

#--- [スレッド表示設定] --------*
    $tmplVars{'ThON'}  = 1;            # スレッド表示を使う?(1=YES 0=NO)
$alk_su= 5;            # スレッド表示の際の親記事表示件数
$alk_rm= 5;            # 1スレッド内に表示するレス記事数
$Top_t = 1;            # 記事リストを表示する?(1=YES 0=NO)
$LiMax = 100;            # 記事リスト表示最大件数
$ResHy = 5;            # レス表示の区切り単位

#--- [メール設定] --------------*
$t_mail= 0;            # 全投稿を自分にメール通知する?(1=YES 0=NO)
$mymail= 0;            # 自分の投稿も通知?(1=YES 0=NO)
$mailto= 'user@host.ne.jp';    # 自分のメールアドレス
$o_mail= 1;            # 投稿者にレス記事通知機能を使う?(1=YES 0=NO)
$s_mail= '/var/qmail/bin/sendmail';    # sendmailパス
$q_mail= 1;            # qmailの場合1にする



#--- [カウンタ設定] ------------#
$cou  = 1;            # カウンタの設置 (1=YES 0=NO)
our $c_f  = "../data/dat/ccount.dat";        # カウンタファイル
our $cloc = "../data/dat/c.loc";        # カウンタロックファイル

#--- [ファイル名設定] ----------#
$cgi_f= "./cbbs.cgi";        # このファイル
    $tmplVars{'cgi_f'} = $cgi_f;
$srch = "./srch.cgi";        # 検索/過去ログ閲覧用CGI
    $tmplVars{'srch'} = $srch;
$log  = "../data/dat/cbbs_log.cgi";        # 記録ファイル
$lockf= "../data/dat/cbbs.loc";        # ロックファイル
$logid = "../data/dat/cbbs.ids";
##### DELETED FUNCTION
#$bup  =  0;            # バックアップをとる? (NO=0 YES=x(x は更新頻度日数を入れる))
#$bup_f= "../data/dat/cbbs.bak";        # バックアップファイル
$locks = 1;            # ファイルをロックする?(1=YES 0=NO)

#--- [新着記事設定] ------------#
$new_t = 24;            # NEW/UPアイコンがつく新着記事は何時間以内の記事?
$new_s = 10;            # 新着記事を表示する記事数
$new_su= 1;            # 新着記事のソート順(1=新しいほど上 0=1の逆)

#--- [発言ランク設定] ----------#
$M_Rank= 0;            # ランキングを取得?(1=YES 0=NO)
    $tmplVars{'M_Rank'} = $M_Rank;
$RLOG  = "../data/dat/rank.dat";        # ランキングログ
$RDEL  = 30;            # ランキングから削除される日数
$RBEST = 30;            # ランキング表示数
$RLOCK = "../data/dat/rank.loc";        # ランキングロックファイル(使用は56行目に依存)

# ●レベル設定 右に行くほど高い(設定しない場合は空行 @RLv=(); にする)
@RLv   = ("一般人","付き人","軍団","ファミリー","ベテラン","大御所");
$RSPL  = 50;            # レベルの区切り単位(初期値だと50回ごとにレベルアップ)
$RGimg = "";            # グラフに画像を使う場合その画像のURLを入れる
$RGhei = 7;            # グラフ画像の縦幅
# ●ランク外にする人の名前(ない場合は空行 @NoRank=(); にする)
@NoRank= ("管理人の名前","りゅういち");

#--- [検索設定] ----------------#
$Kyo_f = "#F9FF06";        # 検索語強調表示の背景色
$Met   = "GET";            # 検索の際のデータ受け渡し形式(POST or GET)
@klog_h= (20,30,40,50);        # 検索表示件数(左端は過去ログ表示件数としても利用)
$klog_a= 1;            # 全過去ログ検索を許可する?(1=YES 0=NO)

#--- [過去ログ関係] ------------#
$klog_s= 1;            # 過去ログ機能を使う?(1=YES 0=NO)
    $tmplVars{'klog_s'} = $klog_s;
$klog_c= "../data/dat/klog.log";        # 過去ログ数のカウントファイル
$klog_d= "../data/dat/";            # 過去ログ生成ディレクトリ
$klog_l= 100;            # 過去ログ記録 KB 数

#--- [RSS] ---#
    $conf{'rss'}     = 1;   # RSS出力するか (1 : する)
    $conf{'rss_num'} = 20;  # RSS表示アイテム数 (0 : 無制限)
    $conf{'rss_rev'} = 1;   # 新着記事ソート順 (1 : 新着が先頭、0 : 古い順)


### オリジナルファイルアップ機能は(一時)削除済み : これらの設定は利用されません
$i_dir = "../data/dat/file";
$i_Url = "http://moz.rsz.jp/forums/file";
@exn= (".gif",".jpg",".jpeg",".png",".txt",".lzh",".zip",".mid",".mov",".tbz");
@exi= ("img","img","img","img","txt.gif","arc.gif","arc.gif","oto.gif","oto.gif","arc.gif");
$H2    = 250;            # 縮小モード時imgの最高縦幅
$W2    = 250;            # 〃 横幅
$img_h = 15;            # @exi(img以外) $no_ent $no_img の縦幅
$img_w = 15;            # 〃 横幅 (限定しない場合は両方記入しない)
$ResUp = 1;            # レスもファイルアップ可能にする?(1=YES 0=NO)
$max_or= 5000;            # 親/レス記事の合計ファイルサイズ限度(↑が1の場合重要)
$max_fs= 1000;            # ひとつの記事あたりのファイルサイズの限度
                # (キロバイト(1KByte=1024Bytes)指定)
    $tmplVars{'max_or'} = $max_or;
    $tmplVars{'max_fs'} = $max_fs;
$mas_c = 0;            # ファイル表示は管理者チェックがいる?(1=File 2=File/記事 0=NO)
    $tmplVars{'mas_C'} = $mas_c;
$no_ent= "no.gif";        # ↑が1の場合許可されるまで表示される画像($i_dirにいれる)
$i_ico = "i.gif";        # アイコンモードの画像代替画像(〃)
$LogDel= 1;            # 過去ログ移行時ファイルを削除する?(1=YES 0=NO)



#--- [アイコン設定] -------------------------------------------------------------------------------
# @ico1 => ファイル名 (xxx.gif/yyy.jpg 等)
# @ico2 => アイコン名 (ねこ/いぬ 等)
# @ico1 @ico2 は必ずペアで 長い場合は、カンマ(,)の前後で改行OK
# @ico3 => 記事ヘッダファイル名 (xxx.gif/yyy.jpg 等)
#          記事ヘッダにアイコンを反映させる
#          @ico1 と同じ数用意する。randam/masterも同じ位置に入れる
#          記事ヘッダ画像ぐらいの小さめの画像を用意
#          使わない場合は空行列 @ico3=(); に
# [管理者アイコン] 初期/最後に設定済み @ico1 に master を設定する(@ico2 も応じて設定)
# [ランダム機能]   初期/最後から2番目に設定済み @ico1 に randam を設定する(〃)
#--------------------------------------------------------------------------------------------------
$Icon   = 0;            # アイコン機能を使う?(1=YES 0=NO)
# アイコン機能は一時削除済み
$IconDir= "./icon";        # 画像のあるディレクトリ(URLでもOK/最後のスラッシュは省く)

@ico1 = ('rob6.gif','rob2.gif','panda.gif','neko2.gif','mouse.gif','coara.gif','qes.gif','randam','master');
@ico2 = ('ホイールロボ','くるりロボ','ぱんだ','ふとめネコ','ねずみ','こあら','疑問ねこ','ランダム','管理者用');
@ico3 = ('rob6_m.gif','rob2_m.gif','panda_m.gif','neko2_m.gif','mouse_m.gif','coara_m.gif','qes_m.gif','randam','master');


$I_Hei_m= "15";            # @ico3の縦幅(ピクセル指定)
$I_Wid_m= "15";            # @ico3の横幅(〃) サイズを限定しない場合 両方記入しない
$Ico_h  = 4;            # アイコン一覧で改行をする数
$Ico_w  = 100;            # アイコン一覧の表示幅(ピクセル指定)
$Ico_kp = 10;            # アイコン一覧/ファイルアップ一覧の改ページ個数
$Ico_k  = "ktai.gif";        # 携帯端末からのアイコン(使わない場合は記入しない)
$Ico_km = "ktai_m.gif";        # 携帯端末からのミニアイコン(〃)

#--- [管理者用アイコン] --------#
# -> 他のアイコンと同じディレクトリに入れる(画像幅は上の設定に依存)
# -> @mas_i = 管理用アイコンファイル名
# -> @mas_m = ヘッダ用ミニアイコンファイル名
# -> @mas_p = パスワード 投稿時削除キーに入れる 使い分けで複数の管理者アイコンが使用可
@mas_i= ('master.gif','rob6.gif');
@mas_m= ('masmin.gif','rob6_m.gif');
@mas_p= ('7777','8888');


#--- [選択枠線色を設定] --------#
# -> 枠線色選択を使用する場合設定
# -> 設定方法は @hr = ('#xxxxxx','#yyyyyy','#zzzzzz') という風に
@hr   = ();

# 閲覧を許可しないIPアドレス(数字/最初の3区切りを指定) 同じようにいくつでも指定可能
@ips=("xxx.xxx.xxx","yyy.yyy.yyy","zzz.zzz.zzz");

$Proxy= 0;            # proxyサーバ経由だと書き込みさせない場合1

$NMAX = 50;            # 名前の入力限度(制限しない場合は0/半角文字数)
$TMAX = 100;            # タイトル入力限度( 〃 )
$CMAX = 10000;            # コメント限度( 〃 )

#--- [セレクト/テキスト設定] ---#
# それぞれひとつずつ設定できます。
#-------------------------------#
$SEL_F = 1;            # セレクトフォームを使う? (0=NO 1=YES)
$SEL_T = "記事内容";        # フォームの用途説明
$SEL_C = 0;            # クッキーに保存する?(0=NO 1=YES)
$SEL_R = 0;            # 使用は親記事のみ?(0=NO 1=YES)
# 選択候補の設定
@SEL   = ("(選択してください)","質問","答え","バグ報告","お礼(問題解決)",,"お礼(問題未解決)","提案","補足","オフトピ");

$TXT_F = 0;            # テキストフォームを使う? (0=NO 1=YES)
$TXT_T = "CGI名";        # フォームの用途説明
$TXT_C = 1;            # クッキーに保存する?(0=NO 1=YES)
$TXT_H = 0;            # 入力必須項目にする?(0=NO 1=YES)
$TXT_Mx= 30;            # 入力限度(初期状態/半角30文字)
$TXT_R = 0;            # 使用は親記事のみ?(0=NO 1=YES)

$TS_Pr = 1;            # 記事内表示位置(0=タイトル前 1=コメント前 2=コメント後)
                # (上記セレクト/テキストとも同じ位置に置かれます)


###added by victory , 2nd Tooyama
$notitle = '題名未設定';    #タイトル無しの場合に付けられるタイトル
$noname = '名前未設定';        #名前無しの場合に付けられる名前
$kanrimode = 1;        #管理モード表示/非表示 0:非表示 1:表示
$tdsep=' / ';
$klogext='.klog.cgi';
$atchange='-nosp@m.';

@bbsmile=qw[
    :D            icon_biggrin.gif    Very_Happy            :D
    :\)            icon_smile.gif        Smile                :)
    :\(            icon_sad.gif        Sad                    :(
    :oops:        icon_redface.gif    Embarassed            :oops:
    :o            icon_surprised.gif    Surprised            :o
    :shock:        icon_eek.gif        Shocked                :shock:
    :\?            icon_confused.gif    Confused            :?
    8\)            icon_cool.gif        Cool                8)
    :lol:        icon_lol.gif        Laughing            :lol:
    :x            icon_mad.gif        Mad                    :x
    :P            icon_razz.gif        Razz                :P
    :cry:        icon_cry.gif        Crying_or_Very_sad    :cry:
    :evil:        icon_evil.gif        Evil_or_Very_Mad    :evil:
    :twisted:    icon_twisted.gif    Twisted_Evil        :twisted:
    :roll:        icon_rolleyes.gif    Rolling_Eyes        :roll:
    :wink:        icon_wink.gif        Wink                :wink:
    :!:            icon_exclaim.gif    Exclamation            :!:
    :ques:        icon_question.gif    Question            :ques:
    :idea:        icon_idea.gif        Idea                :idea:
    :arrow:        icon_arrow.gif        Arrow                :arrow:
    :\|            icon_neutral.gif    Neutral                :|
    :mrgreen:     icon_mrgreen.gif    Mr.Green            :mrgreen:
];

$BBFACE=1;
$smiledir='smiles/';
$useragent = $ENV{HTTP_USER_AGENT};
$useragent =~ s/</&lt;/;
$useragent =~ s/>/&gt;/;
if($BBFACE){
    $BBFACE = '<tr><td title="ONにすると投稿後画像に変換します">';
    $BBFACE .= 'スマイリー<input id="smile" name="smile" type="hidden" value="ON"></td><td>';
    for ($_ = 0; $_ < scalar(@bbsmile); $_ +=4) {
        $BBFACE .= "\n";
        $BBFACE .= '<img onclick="emoticon(' . "'$bbsmile[$_]'" . ')" src="' . "$smiledir$bbsmile[$_+1]" . '" border="0" alt="' . $bbsmile[$_+2] . '" title="' . $bbsmile[$_+2] . '" class="bbsmile" />';
    }
    $BBFACE .= "<br>\n <span onclick=\"emoticon('UA')\" title=\"クリックでテキストエリアに貼\り付けられます\">$useragent</span></td>\n</tr>";
}

sub smile_encode{
    $smile_pre = '<img src="' . $smiledir;

    for ($_ = 0; $_ < scalar(@bbsmile); $_ +=4) {
        $smile_aft = '" alt="' . $bbsmile[$_+2] . '">';
        $comment =~ s/ $bbsmile[$_] / $smile_pre$bbsmile[$_+1]$smile_aft /g;
    }
}

sub smile_decode{
    $smile_pre = '<img src="' . $smiledir;

    for ($_ = 0; $_ < scalar(@bbsmile); $_ +=4) {
        $smile_aft = '" alt="' . $bbsmile[$_+2] . '">';
        $com =~ s/$smile_pre$bbsmile[$_+1]$smile_aft/$bbsmile[$_+3]/g;
    }
}

$ua_select=1;


1;
