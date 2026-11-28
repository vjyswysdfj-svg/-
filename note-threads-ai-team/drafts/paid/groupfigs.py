from PIL import Image, ImageDraw, ImageFont
import json
F='/usr/share/fonts/opentype/ipafont-gothic/ipagp.ttf'
f=lambda s: ImageFont.truetype(F,s)
NAVY=(30,52,96); TEAL=(26,154,159); W=(255,255,255); LG=(236,240,245); TXT=(40,44,52); GR=(90,98,110)
S={1:('自分のジャンル・日付','手数料・需要の表'),2:('他の発信者の画面','違いの一覧表'),3:('参考記事の画面','型のカード'),4:('今週の日付・ジャンル','試せる話題の表'),5:('コメント・数字','読者像のカード'),
6:('調べた結果・今週やったこと','記事の候補4〜6案'),7:('候補・数字','今週書く記事'),8:('選んだテーマ','構成表'),9:('構成表','見出しの一覧'),
10:('構成表・見出し','タイトル3〜5案'),11:('タイトル・構成','書き出しの文'),12:('構成・本人のメモ','貼り付け用の初稿'),13:('記事の狙い','最後の呼びかけ'),
14:('初稿','分かりやすさの指摘'),15:('初稿・本人のメモ','事実確認表'),16:('初稿・画像の一覧','権利の確認表'),17:('初稿・タイトル','言葉のチェック表'),
18:('使う数字の一覧','素材リスト'),19:('タイトル','画像アプリへの指示文'),20:('数字・仕組み','図と表'),
21:('テーマ・読者','ハッシュタグ5つ'),22:('原稿・画像・チェック表','公開した記事と記録'),
23:('コメントの画面','分類と返信の案'),24:('アクセス状況の画面','数字のレポート'),25:('数字のレポート','次の打ち手3つ'),26:('進み具合・作業時間','毎朝の予定')}
R=json.load(open('roles.json'))
for i,r in enumerate(R,1): r[0]=i
groups=['調べる','企画する','書く','確かめる','素材をつくる','公開する','分析・改善']
for gi,g in enumerate(groups,1):
    rs=[r for r in R if r[1]==g]
    H=230+len(rs)*130+60
    im=Image.new('RGB',(1280,H),W); d=ImageDraw.Draw(im)
    def c(t,y,s,col,x=640):
        w=d.textlength(t,font=f(s)); d.text((x-w/2,y),t,font=f(s),fill=col)
    c(f'工程{gi}「{g}」の{len(rs)}つの担当',30,42,NAVY); d.line([560,92,720,92],fill=TEAL,width=4)
    d.text((80,130),'担当',font=f(26),fill=GR); d.text((420,130),'AIに渡すもの',font=f(26),fill=GR); d.text((860,130),'返ってくるもの',font=f(26),fill=GR)
    y=180
    for k,r in enumerate(rs):
        a,b=S[r[0]]
        d.rounded_rectangle([60,y,380,y+100],radius=14,fill=NAVY)
        d.text((85,y+32),f'{r[0]} {r[2]}'+('（人）' if r[0]==22 else ''),font=f(30 if len(r[2])<8 else 26),fill=W)
        d.rounded_rectangle([400,y,800,y+100],radius=14,fill=LG); d.text((425,y+34),a,font=f(26 if len(a)<14 else 22),fill=TXT)
        d.polygon([(812,y+35),(812,y+65),(840,y+50)],fill=TEAL)
        d.rounded_rectangle([850,y,1220,y+100],radius=14,fill=(220,240,241),outline=TEAL,width=2); d.text((875,y+34),b,font=f(26 if len(b)<12 else 22),fill=NAVY)
        y+=130
    nxt={1:'→ 結果は「企画する」へ',2:'→ 選んだ記事は「書く」へ',3:'→ 初稿は「確かめる」へ',4:'→ 直した原稿は「素材をつくる」へ',5:'→ 画像と図は「公開する」へ',6:'→ 公開した記事は「分析・改善」へ',7:'→ 打ち手は次の記事の「調べる」「企画する」へ'}[gi]
    c(nxt,y+5,28,TEAL)
    im.save(f'../images/paid_group{gi}.png')
print('ok')
