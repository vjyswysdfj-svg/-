from PIL import Image, ImageDraw, ImageFont
F = "/usr/share/fonts/opentype/ipafont-gothic/ipagp.ttf"
NAVY, TEAL, LG, WHITE, INK, GRAY = (30, 52, 96), (26, 154, 159), (236, 240, 245), (255, 255, 255), (40, 48, 60), (150, 160, 175)
def f(s): return ImageFont.truetype(F, s)
OUT = "/home/user/-/note-threads-ai-team/drafts/images/"

# 図1：変える前・変えた日・その後1週間
W, H = 1280, 700
im = Image.new("RGB", (W, H), LG); d = ImageDraw.Draw(im)
d.text((W // 2, 60), "タイトルを変える前と後で、開かれた回数", font=f(44), fill=NAVY, anchor="mm")
cols = [("変える前", "11/13〜11/17昼", 188, 4, NAVY),
        ("変えた日", "11/17昼〜11/18深夜", 12, 3, TEAL),
        ("その後の約1週間", "11/18深夜〜11/25朝", 75, 0, NAVY)]
bw, gap = 360, 40; x = (W - (bw * 3 + gap * 2)) // 2
for name, period, imp, pv, col in cols:
    d.rounded_rectangle((x, 130, x + bw, 560), 20, fill=WHITE, outline=col, width=4)
    d.text((x + bw // 2, 175), name, font=f(36), fill=col, anchor="mm")
    d.text((x + bw // 2, 222), period, font=f(24), fill=INK, anchor="mm")
    d.text((x + bw // 2, 300), f"表示 {imp}回", font=f(34), fill=INK, anchor="mm")
    d.text((x + bw // 2, 380), f"開かれた {pv}回", font=f(40), fill=col, anchor="mm")
    rate = f"{pv / imp * 100:.1f}%"
    d.text((x + bw // 2, 470), rate, font=f(64), fill=col, anchor="mm")
    x += bw + gap
d.text((W // 2, 610), "開かれた3回は、別の記事も公開した「変えた日」から翌日深夜までだけ。その後の1週間は0回", font=f(28), fill=NAVY, anchor="mm")
d.text((W // 2, 655), "数はnoteのアクセス状況から記録。とても少ないので、たまたまの可能性もある", font=f(22), fill=INK, anchor="mm")
im.save(OUT + "article11_fig1_before_after.png")

# 図2：記事ごとの開かれた割合（11/25朝）
rows = [("毎朝の予定をAIに", 11.6), ("働き方を変えたい", 11.1), ("担当ファイル（有料）", 10.9),
        ("見出し画像の指示文", 10.2), ("同じ指示文で5つのAI", 8.3), ("本屋さんのAIの本", 8.2),
        ("プロフィール", 8.0), ("5つのAIにネタ", 7.5), ("始めて1週間", 6.6),
        ("アクセス状況の見方", 6.4), ("禁止した言葉8つ", 2.5)]
H = 130 + len(rows) * 52 + 70
im = Image.new("RGB", (W, H), LG); d = ImageDraw.Draw(im)
d.text((W // 2, 60), "記事ごとの、開かれた割合（11/25朝）", font=f(44), fill=NAVY, anchor="mm")
y = 120; x0, scale = 470, 55
for name, v in rows:
    col = TEAL if name.startswith("禁止") else NAVY
    d.text((x0 - 20, y + 20), name, font=f(26), fill=col if col == TEAL else INK, anchor="rm")
    d.rounded_rectangle((x0, y + 4, x0 + int(v * scale), y + 38), 6, fill=col)
    d.text((x0 + int(v * scale) + 12, y + 21), f"{v}%", font=f(26), fill=col, anchor="lm")
    y += 52
d.text((W // 2, y + 30), "タイトルを変えた「禁止した言葉8つ」だけが、変えたあともいちばん低い", font=f(26), fill=TEAL, anchor="mm")
im.save(OUT + "article11_fig2_rates.png")
print("ok")
