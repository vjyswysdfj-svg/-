from PIL import Image, ImageDraw, ImageFont
F = "/usr/share/fonts/opentype/ipafont-gothic/ipagp.ttf"
NAVY, TEAL, LG, WHITE, INK = (30, 52, 96), (26, 154, 159), (236, 240, 245), (255, 255, 255), (40, 48, 60)
def f(s): return ImageFont.truetype(F, s)
OUT = "/home/user/-/note-threads-ai-team/drafts/images/"

# 図1：31項目の内訳
W, H = 1280, 770
im = Image.new("RGB", (W, H), LG); d = ImageDraw.Draw(im)
d.text((W // 2, 60), "31項目を、5つのまとまりに分けている", font=f(46), fill=NAVY, anchor="mm")
rows = [("内容", 5, "タイトル・仮置き・数字が記録と合うか"),
        ("表現", 5, "使わないと決めた言葉・絵文字の数"),
        ("権利・個人情報", 3, "出典・他人の情報が写っていないか"),
        ("noteの画面", 14, "見出し・画像・中央そろえ・リンク・スマホ表示"),
        ("公開したあと", 4, "マガジン追加・URLの記録・3,000字")]
y = 130; unit = 30
for name, n, desc in rows:
    d.rounded_rectangle((60, y, 1220, y + 104), 16, fill=WHITE)
    d.text((90, y + 34), name, font=f(34), fill=NAVY, anchor="lm")
    d.text((90, y + 76), desc, font=f(24), fill=INK, anchor="lm")
    x0 = 700
    for i in range(n):
        d.rounded_rectangle((x0 + i * unit, y + 30, x0 + i * unit + 24, y + 74), 5, fill=TEAL)
    d.text((1200, y + 52), f"{n}", font=f(40), fill=TEAL, anchor="rm")
    y += 116
d.text((W // 2, 735), "いちばん多いのは「noteの画面」の14項目。貼り付けと見た目の失敗が多かった", font=f(24), fill=INK, anchor="mm")
im.save(OUT + "article09_fig1_groups.png")

# 図2：失敗から項目が生まれる流れ
im = Image.new("RGB", (W, 670), LG); d = ImageDraw.Draw(im)
d.text((W // 2, 60), "1つの失敗から、1つの項目が生まれる", font=f(46), fill=NAVY, anchor="mm")
steps = [("失敗する", "本文が全部、\n大きく太い文字になった"),
         ("その場で足す", "「本文全体が見出しに\nなっていない」を追加"),
         ("次から確認", "公開の前に\n毎回チェックする")]
bw, gap = 340, 70; x = (W - (bw * 3 + gap * 2)) // 2
for i, (t, s) in enumerate(steps):
    col = NAVY if i != 1 else TEAL
    d.rounded_rectangle((x, 160, x + bw, 520), 20, fill=WHITE, outline=col, width=5)
    d.rounded_rectangle((x, 160, x + bw, 250), 20, fill=col)
    d.rectangle((x, 220, x + bw, 250), fill=col)
    d.text((x + bw // 2, 205), t, font=f(38), fill=WHITE, anchor="mm")
    d.multiline_text((x + bw // 2, 385), s, font=f(30), fill=INK, anchor="mm", align="center", spacing=14)
    if i < 2:
        ax = x + bw + 12
        d.polygon([(ax, 320), (ax + 46, 340), (ax, 360)], fill=TEAL)
    x += bw + gap
d.text((W // 2, 600), "これをくり返して、チェックリストは31項目になった", font=f(30), fill=NAVY, anchor="mm")
im.save(OUT + "article09_fig2_flow.png")
print("ok")
