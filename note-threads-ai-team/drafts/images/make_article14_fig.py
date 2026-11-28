from PIL import Image, ImageDraw, ImageFont
F = "/usr/share/fonts/opentype/ipafont-gothic/ipagp.ttf"
NAVY, TEAL, LG, WHITE, INK = (30, 52, 96), (26, 154, 159), (236, 240, 245), (255, 255, 255), (40, 48, 60)
def f(s): return ImageFont.truetype(F, s)
W, H = 1280, 760
im = Image.new("RGB", (W, H), LG); d = ImageDraw.Draw(im)
d.text((W // 2, 60), "講座の「3つのナレッジ」と、私がもう持っていたファイル", font=f(40), fill=NAVY, anchor="mm")
rows = [("ドメイン知識", "何について書くか", "中古車を見るところと見方／自分の経歴とテーマ"),
        ("ライティングルール", "どう書くか", "文章のルール／使わない言葉8つ／事実の確かめ方"),
        ("伸びる投稿の構成", "どんな形が読まれるか", "記事の型／公開前チェックリスト31項目／投稿の分析メモ")]
y = 130
for name, sub, mine in rows:
    d.rounded_rectangle((60, y, 470, y + 160), 18, fill=NAVY)
    d.text((265, y + 60), name, font=f(34), fill=WHITE, anchor="mm")
    d.text((265, y + 110), sub, font=f(24), fill=WHITE, anchor="mm")
    d.polygon([(495, y + 60), (545, y + 80), (495, y + 100)], fill=TEAL)
    d.rounded_rectangle((570, y, 1220, y + 160), 18, fill=WHITE, outline=TEAL, width=4)
    parts = mine.split("／")
    for j, p in enumerate(parts):
        d.text((600, y + 40 + j * 42), "・" + p, font=f(26), fill=INK, anchor="lm")
    y += 185
d.text((W // 2, 715), "失敗するたびに足してきたファイルが、そのまま3つに当てはまっていた", font=f(28), fill=NAVY, anchor="mm")
im.save("/home/user/-/note-threads-ai-team/drafts/images/article14_fig1_knowledge.png")
print("ok")
