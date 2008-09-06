#! /usr/bin/perl

## WARNING!!!!
## もとの cbbs の設定ファイルとは大幅に違います。
## コメントを参考にして編集してください。
## $tmplVars{}になっている変数はそのうちテンプレートファイルへ移動します。
## 全ての変数は$conf{}に移行予定です。
## 全ての変数が$conf{}に移行後、設定ファイルはテキストベースになる予定です。

#######################################################################
## MODIFICATION LOG
##
## Date       Author       Description
## ----       ------       -----------
## xx/01/2002 Ryuzi Kambe  Initial Release
##                         Customized Child Tree 5.1 for mozilla.gr.jp.
##                          1. Set color scheme
##                          2. Set/disabled some variables
##
## 03/02/2002 Gashu        Additional customization
##                          1. Set outliner images
##                          2. Changed styles to refer external CSS
##                              VARIABLE: ($STYLE)
##                          3. Changed description for fixed box
##                          4. Changed max length of title
##                              VARIABLE: ($t_max)
##                          5. Added related links(optional)
##                              VARIABLE: ($linkrel)
##                          6. Added additional help comments(optional)
##                              VARIABLE: ($helpadd)
##                          7. Added caption to main logo
##                              VARIABLE: ($talt)
##
## 22/02/2002 Gashu        Additional customization
##                          1. Enabled alternate style sheets
##                          2. Enabled some meta names
##                          3. Added a description about fixed font to Note.
##
## 08/03/2002 Gashu        Set titles for link item.
##
## 21/04/2005 Tooyama      Set titles for link item 2nd and more.
##
## 25/03/2006 Makoto       Additional customization
##                          1. Added custom header mode
##                              VARIABLE: ($custom_header_mode)
##                                        ($custom_header)
##
## 29/06/2006 Makoto       Delete "kanrimode = 2" description.
##                         (Bug-jp 5233)
##
#######################################################################

# オプションは基本的に以下のようにする
#  0 : しない、不可能
#  1 : する、可能
#  1 は not 0 を意味する

our %conf;

#--- [基本設定] ----------------#
$met   = "POST";		# 送信形式(POST or GET/ファイルアップを使う場合はPOST限定)
    $tmplVars{'backurl'} = 'http://www.mozilla.gr.jp/';
#$backurl="http://www.mozilla.gr.jp";	# 戻るURL(http://～でOK)
$TOPH = 1;			# 初期表示(0=スレッド型 1=ツリー型 2=トピック型)
$max  = 100;			# 親記事最大保持件数

#--- [タイトル設定] ------------#
##$title = "";		# タイトル => tmpl/head.tmpl
##$tface = "Times New Roman";	# タイトルのフォント
##$tsize = 6;			# タイトルのサイズ
##$tcolor= "#ffffff";		# タイトルの色(16進数)
    $tmplVars{'t_img'} = 'file/logo.gif';
    $tmplVars{'twid'} = '186';
    $tmplVars{'thei'} = '67';
    $tmplVars{'talt'} = 'もじら組纏';
#$t_img= "file/logo.gif";			# タイトル画像をURLで指定
#$twid = "186";			#  〃 の横幅(ピクセル指定)
#$thei = "67";			#  〃 の縦幅(　〃　)
#$talt = "もじら組纏";			#  〃 キャプション(　〃　)

#--- [色デザイン設定] ----------#
$text = "#003366";		# 標準文字色指定(16進数)
$bg   = "#C7D0D9";		# 背景色の指定  (〃)
$link = "blue";		# 未リンク色の指定(〃)
$vlink= "purple";		# 既リンク色の指定(〃)
##$ttb  = "#C7D0D9";		# 汎用的な表上部色(〃)
##$k_back="#FFFFFF";		# 記事の中の背景色(〃)
##$t_back="#E0ECF6";		# 記事題名の背景色(〃)
##$t_font="#008080";		# 記事題名の文字色(〃)
##$res_f ="#666666";		# 引用記事の色    (〃)
##$kijino="#008080";		# 記事NOの色      (〃)
##$back = "";			# 背景画像をURLで指定(無いの場合は記入しない)

#--- [記事投稿に関する設定] ----#
$topok= 1;			# 親記事投稿はだれでも可能?(1=YES 0=管理者のみ)
$he_tp= 0;			# 返信を親記事投稿者のみの権利にする?(1=YES 0=NO)
$r_max= 100;		# 返信の限度数(0 にすると無制限)
$Res_i= 0;			# 記事引用を任意にする?(1=任意 0=自動)
$Res_T= 0;			# 親記事を投稿順に並べる?(1=YES 0=レス最新順)
$AgSg = 1;			# レスの際、記事移動を任意にする?(1=任意 0=自動)
$EStmp= 1;			# 編集されたらタイムスタンプを押す?(1=YES 0=NO)
$UID  = 0;			# ID機能を使う?(1=YES 0=NO / クッキー機能必須)
$IDCol= "#FA8605";		# ID機能を使う場合の表示文字色
$wrap = "soft";			# コメントフォームの改行形式(soft=手動 or hard=強制)
$tag  = 0;			# タグの使用(YES=1 NO=0)
    $tmplVars{'use_post_edit'} = 0;         # 投稿の編集・削除フォーム
    $tmplVars{'use_password'} = 0;          # 投稿時のパスワード登録フォーム

#--- [記事表示に関する設定] ----#
$t_max= 128;			# 記事タイトル表示限度(初期-半角40字/全角20字)
$AMark= '＠';			# メールアドレス置き換え文字列(画像の場合は<img>で)
$SPAM = ' ';			# アドレス収集ソフト対策(アドレスに追加され表示される文字列)
$URLIM= "";			# URLに画像を使う場合はhttp://～で指定
$UI_Wi= "";			# ↑利用の場合画像横幅
$UI_He= "";			#      〃     画像縦幅(横縦両方記述)
$TGT  = "_blank";		# HOME以外の掲示板外へのリンクターゲット

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

#--- [チェックボックス設定] ----#
$end_f = 1;			# 解決チェックボックスを使う？(1=YES 0=NO)
$end_c = 0;			# 解決チェックは管理人のみ可能にする?(1=YES 0=NO)
$end_e = 0;			# 解決チェックが付いたら返信不可にする?(1=YES 0=NO)

# ●チェック時、表示する物(タグ可 画像の時は<img>タグ)
$end_ok= '<strong class="red">済!</strong>';

#--------------------------------------------------------------------------------------------------
# ●チェックを促すコメント(例: 解決したらチェック！)
$end_m =<<"_END_";

問題が解決したらチェックしてください

_END_


#--- [ツリー表示設定] ----------*
$TrON  = 1;			# ツリー表示を使う?(1=YES 0=NO)
$a_max = 10;			# 1ページ表示ツリー数
$obg   = "#E0ECF6";		# 親記事のツリー背景色(〃)
$Keisen= 1;			# 罫線を表示する?(1=YES 0=NO)
$K_I   = '<img src="file/ol_ver.gif" height="14" width="15" alt="|">';			# 罫線(連結型/画像の場合は<img>)
$K_T   = '<img src="file/ol_con.gif" height="14" width="15" alt="|-">';			# 罫線(分岐型/ 〃 )
$K_L   = '<img src="file/ol_edg.gif" height="14" width="15" alt="L">';			# 罫線(終了型/ 〃 )
$K_SP  = '<img src="file/1pix.gif" height="1" width="15" alt="">';			# 罫線(スペース/ 〃)
$zure  = 6;			# ツリーのずれ調整(罫線OFFの場合有効)

#--- [トピック表示設定] --------*
$TpON  = 1;			# トピック表示を使う?(1=YES 0=NO)
$tab_m = 2;			# 1ページ表示テーブル数
$tpmax = 10;			# テーブル1つ当りの表示トピック数
$topic = 10;			# 1トピックの1ページ当りの表示数
$tp_hi = 0;			# トピック内容の初期配列(1=新着記事トップ 0=親トピックトップ)
$tpend = 0;			# レス後の表示内容(0=トップ 1=レスしたトピック)

#--- [スレッド表示設定] --------*
$ThON  = 1;			# スレッド表示を使う?(1=YES 0=NO)
$alk_su= 5;			# スレッド表示の際の親記事表示件数
$alk_rm= 5;			# 1スレッド内に表示するレス記事数
$Top_t = 1;			# 記事リストを表示する?(1=YES 0=NO)
$LiMax = 100;			# 記事リスト表示最大件数
$ResHy = 5;			# レス表示の区切り単位

#--- [メール設定] --------------*
$t_mail= 0;			# 全投稿を自分にメール通知する?(1=YES 0=NO)
$mymail= 0;			# 自分の投稿も通知?(1=YES 0=NO)
$mailto= 'user@host.ne.jp';	# 自分のメールアドレス
$o_mail= 1;			# 投稿者にレス記事通知機能を使う?(1=YES 0=NO)
$s_mail= '/var/qmail/bin/sendmail';	# sendmailパス
$q_mail= 1;			# qmailの場合1にする

#--- [パスワード制限設定] ------#
$s_ret= 0;			# 記事を見る際の制限(0=しない 1=書くとき 2=書く&読むとき)
$s_pas= "7777";			# 上記が1or2の場合のパスワード(半角英数2文字以上)

#--- [カウンタ設定] ------------#
$cou  = 1;			# カウンタの設置 (1=YES 0=NO)
$fig  = 7;			# カウンタの桁数
#$c_co = "#38B52F";		# テキスト=> テキストの色
$m_wid= 8;			# 画像=> 画像の横サイズ
$m_hei= 12;			#  〃 => 画像の縦サイズ
$m_pas= "";			#  〃 => ディレクトリのパス(使用しない場合そのまま)
$c_f  = "../data/dat/ccount.dat";		# カウンタファイル
$cloc = "../data/dat/c.loc";		# カウンタロックファイル

#--- [ファイル名設定] ----------#
$cgi_f= "./cbbs.cgi";		# このファイル
if($ENV{HTTP_HOST} =~ /mozilla.gr.jp/){$cgi_f="./";}
$srch = "./srch.cgi";		# 検索/過去ログ閲覧用CGI
$log  = "../data/dat/cbbs_log.cgi";		# 記録ファイル
$lockf= "../data/dat/cbbs.loc";		# ロックファイル
$bup  =  0;			# バックアップをとる? (NO=0 YES=x(x は更新頻度日数を入れる))
$bup_f= "../data/dat/cbbs.bak";		# バックアップファイル
$locks = 1;			# ファイルをロックする?(1=YES 0=NO)

#--- [新着記事設定] ------------#
$new_t = 24;			# NEW/UPアイコンがつく新着記事は何時間以内の記事?
$new_s = 10;			# 新着記事を表示する記事数
$new_su= 1;			# 新着記事のソート順(1=新しいほど上 0=1の逆)

#--- [発言ランク設定] ----------#
$M_Rank= 0;			# ランキングを取得?(1=YES 0=NO)
$RLOG  = "../data/dat/rank.dat";		# ランキングログ
$RDEL  = 30;			# ランキングから削除される日数
$RBEST = 30;			# ランキング表示数
$RLOCK = "../data/dat/rank.loc";		# ランキングロックファイル(使用は56行目に依存)

# ●レベル設定 右に行くほど高い(設定しない場合は空行 @RLv=(); にする)
@RLv   = ("一般人","付き人","軍団","ファミリー","ベテラン","大御所");
$RSPL  = 50;			# レベルの区切り単位(初期値だと50回ごとにレベルアップ)
$RGimg = "";			# グラフに画像を使う場合その画像のURLを入れる
$RGhei = 7;			# グラフ画像の縦幅
# ●ランク外にする人の名前(ない場合は空行 @NoRank=(); にする)
@NoRank= ("管理人の名前","りゅういち");

#--- [検索設定] ----------------#
$Kyo_f = "#F9FF06";		# 検索語強調表示の背景色
$Met   = "GET";			# 検索の際のデータ受け渡し形式(POST or GET)
@klog_h= (20,30,40,50);		# 検索表示件数(左端は過去ログ表示件数としても利用)
$klog_a= 1;			# 全過去ログ検索を許可する?(1=YES 0=NO)

#--- [過去ログ関係] ------------#
$klog_s= 1;			# 過去ログ機能を使う?(1=YES 0=NO)
$klog_c= "../data/dat/klog.log";		# 過去ログ数のカウントファイル
$klog_d= "../data/dat/";			# 過去ログ生成ディレクトリ
$klog_l= 100;			# 過去ログ記録 KB 数

#--- [RSS] ---#
    $conf{'rss'}     = 1;   # RSS出力するか (1 : する)
    $conf{'rss_num'} = 20;  # RSS表示アイテム数 (0 : 無制限)
    $conf{'rss_rev'} = 1;   # 新着記事ソート順 (1 : 新着が先頭、0 : 古い順)

#--------------------------------------------------------------------------------------------------
#                     [ ファイルアップの設定 ]
# 不適切な画像のアップの監視など、適切な管理が必要!!
# 1)@exn はアップ可能ファイル拡張子(ドット(.)から記入/必ず小文字で)
#     例) .gif .txt .lzh .mid .mpeg .mp3 等
# 2)@exi は@exnを表示するアイコン画像
#     ・ファイルアップするディレクトリ($i_dir)に入れる
#     ・画像の場合は img といれると画像が表示される
# 3)ファイルをアップするディレクトリのパーミッションは777 or 755
# 4)画像縦横幅自動取得可能拡張子は以下の通り
#     (.gif/.GIF/.png/.PNG/.jpg/.jpeg/.JPG/.JPEG/.bmp/.BMP)
#--------------------------------------------------------------------------------------------------
$i_mode= 0;			# ファイルアップモードを使う?(1=YES 0=NO)

# ●相対パス/絶対パス でファイルアップする場所(ファイルアップ用)
$i_dir = "../data/dat/file";

# ●http:// のURL でファイルアップする場所(ファイル表示用)
$i_Url = "http://moz.rsz.jp/forums/file";

# ●@exn と @exi は必ずペアで
@exn= (".gif",".jpg",".jpeg",".png",".txt",".lzh",".zip",".mid",".mov",".tbz");
@exi= ("img","img","img","img","txt.gif","arc.gif","arc.gif","oto.gif","oto.gif","arc.gif");

$H2    = 250;			# 縮小モード時imgの最高縦幅
$W2    = 250;			# 〃 横幅
$img_h = 15;			# @exi(img以外) $no_ent $no_img の縦幅
$img_w = 15;			# 〃 横幅 (限定しない場合は両方記入しない)
$ResUp = 1;			# レスもファイルアップ可能にする?(1=YES 0=NO)
$max_or= 5000;			# 親/レス記事の合計ファイルサイズ限度(↑が1の場合重要)
$max_fs= 1000;			# ひとつの記事あたりのファイルサイズの限度
				# (キロバイト(1KByte=1024Bytes)指定)
$mas_c = 0;			# ファイル表示は管理者チェックがいる?(1=File 2=File/記事 0=NO)
$no_ent= "no.gif";		# ↑が1の場合許可されるまで表示される画像($i_dirにいれる)
$i_ico = "i.gif";		# アイコンモードの画像代替画像(〃)
$LogDel= 1;			# 過去ログ移行時ファイルを削除する?(1=YES 0=NO)


#--- [フォームスタイル設定]-----#
$fss  = 0;			# フォームのスタイルシート利用(1=YES 0=NO)

# 上の項目が 1 の場合設定
# わからない場合は初期設定のまま
# $fst=StyleSheet $on/$off=JavaScrip
#--------------------------------------------------------------------------------------------------
$fst=<<"SS_";
<STYLE TYPE="text/css">
<!--
-->
</STYLE>
SS_
# ↑は削除不可-------------------------------------------------------------------------------------
# ● マウスが乗ったときや、フォーカスをえた時の動作
#$on= "backgroundColor='#FDE8B5'\;";

# ● マウスがどいたときや、フォーカスを失った時の動作
#$off="backgroundColor='#FFFFFF'\;";

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
$Icon   = 0;			# アイコン機能を使う?(1=YES 0=NO)
# アイコン機能は一時削除済み
$IconDir= "./icon";		# 画像のあるディレクトリ(URLでもOK/最後のスラッシュは省く)

@ico1 = ('rob6.gif','rob2.gif','panda.gif','neko2.gif','mouse.gif','coara.gif','qes.gif','randam','master');
@ico2 = ('ホイールロボ','くるりロボ','ぱんだ','ふとめネコ','ねずみ','こあら','疑問ねこ','ランダム','管理者用');
@ico3 = ('rob6_m.gif','rob2_m.gif','panda_m.gif','neko2_m.gif','mouse_m.gif','coara_m.gif','qes_m.gif','randam','master');


$IconHei= "32";			# 画像の縦幅(ピクセル指定)
$IconWid= "32";			# 画像の横幅(〃) サイズを限定しない場合 両方記入しない
$I_Hei_m= "15";			# @ico3の縦幅(ピクセル指定)
$I_Wid_m= "15";			# @ico3の横幅(〃) サイズを限定しない場合 両方記入しない
$Ico_h  = 4;			# アイコン一覧で改行をする数
$Ico_w  = 100;			# アイコン一覧の表示幅(ピクセル指定)
$Ico_kp = 10;			# アイコン一覧/ファイルアップ一覧の改ページ個数
$Ico_k  = "ktai.gif";		# 携帯端末からのアイコン(使わない場合は記入しない)
$Ico_km = "ktai_m.gif";		# 携帯端末からのミニアイコン(〃)

#--- [管理者用アイコン] --------#
# -> 他のアイコンと同じディレクトリに入れる(画像幅は上の設定に依存)
# -> @mas_i = 管理用アイコンファイル名
# -> @mas_m = ヘッダ用ミニアイコンファイル名
# -> @mas_p = パスワード 投稿時削除キーに入れる 使い分けで複数の管理者アイコンが使用可
@mas_i= ('master.gif','rob6.gif');
@mas_m= ('masmin.gif','rob6_m.gif');
@mas_p= ('7777','8888');

#--- [選択文字色を設定] --------#
# -> 文字色選択を使用する場合設定
# -> 設定方法は @fonts = ('#xxxxxx','#yyyyyy','#zzzzzz') という風に
@fonts= ('black','blue','green','aqua','red','pink','yellow');

#--- [選択枠線色を設定] --------#
# -> 枠線色選択を使用する場合設定
# -> 設定方法は @hr = ('#xxxxxx','#yyyyyy','#zzzzzz') という風に
@hr   = ();

# 閲覧を許可しないIPアドレス(数字/最初の3区切りを指定) 同じようにいくつでも指定可能
@ips=("xxx.xxx.xxx","yyy.yyy.yyy","zzz.zzz.zzz");

$Proxy= 0;			# proxyサーバ経由だと書き込みさせない場合1

$NMAX = 50;			# 名前の入力限度(制限しない場合は0/半角文字数)
$TMAX = 100;			# タイトル入力限度( 〃 )
$CMAX = 10000;			# コメント限度( 〃 )

#--- [セレクト/テキスト設定] ---#
# それぞれひとつずつ設定できます。
#-------------------------------#
$SEL_F = 1;			# セレクトフォームを使う? (0=NO 1=YES)
$SEL_T = "記事内容";		# フォームの用途説明
$SEL_C = 0;			# クッキーに保存する?(0=NO 1=YES)
$SEL_R = 0;			# 使用は親記事のみ?(0=NO 1=YES)
# 選択候補の設定
@SEL   = ("(選択してください)","質問","答え","バグ報告","お礼(問題解決)",,"お礼(問題未解決)","提案","補足","オフトピ");

$TXT_F = 0;			# テキストフォームを使う? (0=NO 1=YES)
$TXT_T = "CGI名";		# フォームの用途説明
$TXT_C = 1;			# クッキーに保存する?(0=NO 1=YES)
$TXT_H = 0;			# 入力必須項目にする?(0=NO 1=YES)
$TXT_Mx= 30;			# 入力限度(初期状態/半角30文字)
$TXT_R = 0;			# 使用は親記事のみ?(0=NO 1=YES)

$TS_Pr = 1;			# 記事内表示位置(0=タイトル前 1=コメント前 2=コメント後)
				# (上記セレクト/テキストとも同じ位置に置かれます)


###added by victory , 2nd Tooyama
$notitle = '題名未設定';	#タイトル無しの場合に付けられるタイトル
$noname = '名前未設定';		#名前無しの場合に付けられる名前
$kanrimode = 1;		#管理モード表示/非表示 0:非表示 1:表示
$tdsep=' / ';
$klogext='.klog.cgi';
$atchange='-nosp@m.';

@bbsmile=qw[
	:D			icon_biggrin.gif	Very_Happy			:D
	:\)			icon_smile.gif		Smile				:)
	:\(			icon_sad.gif		Sad					:(
	:oops:		icon_redface.gif	Embarassed			:oops:
	:o			icon_surprised.gif	Surprised			:o
	:shock:		icon_eek.gif		Shocked				:shock:
	:\?			icon_confused.gif	Confused			:?
	8\)			icon_cool.gif		Cool				8)
	:lol:		icon_lol.gif		Laughing			:lol:
	:x			icon_mad.gif		Mad					:x
	:P			icon_razz.gif		Razz				:P
	:cry:		icon_cry.gif		Crying_or_Very_sad	:cry:
	:evil:		icon_evil.gif		Evil_or_Very_Mad	:evil:
	:twisted:	icon_twisted.gif	Twisted_Evil		:twisted:
	:roll:		icon_rolleyes.gif	Rolling_Eyes		:roll:
	:wink:		icon_wink.gif		Wink				:wink:
	:!:			icon_exclaim.gif	Exclamation			:!:
	:ques:		icon_question.gif	Question			:ques:
	:idea:		icon_idea.gif		Idea				:idea:
	:arrow:		icon_arrow.gif		Arrow				:arrow:
	:\|			icon_neutral.gif	Neutral				:|
	:mrgreen: 	icon_mrgreen.gif	Mr.Green			:mrgreen:
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

$use_col=0;		#記事の文字色指定とその表示への適用 0:
if(!$use_col){@fonts=();}
$ua_select=1;

$target_blank =0;		#新しい窓を開かせるかどうか。0:off しない場合は次の3行で抹殺します。
if($target_blank){
$TGT  = ' target="_blank"';		# HOME以外の掲示板外へのリンクターゲット
}else{$TGT="";}




1;#削除不可
