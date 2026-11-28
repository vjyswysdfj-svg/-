from PIL import Image, ImageDraw, ImageFont
F = "/usr/share/fonts/opentype/ipafont-gothic/ipagp.ttf"
NAVY, TEAL, LG, WHITE, INK, WARN = (30, 52, 96), (26, 154, 159), (236, 240, 245), (255, 255, 255), (40, 48, 60), (180, 84, 31)
def f(s): return ImageFont.truetype(F, s)
OUT = "/home/user/-/note-threads-ai-team/drafts/images/"

# 図1：6つのAIの比べ
rows = [("ChatGPT", "守った", "書かない", "順位を付けた"),
        ("Gemini", "1個こえた", "5個ずれ", "目的別"),
        ("Muse", "守った", "全部正確", "目的別"),
        ("Manus", "守った", "書かない", "なし"),
        ("Perplexity", "守った", "書かない", "目的別"),
        ("Claude", "守った", "全部正確", "弱点も指摘")]
W = 1280; H = 140 + 70 * 7 + 70
im = Image.new("RGB", (W, H), LG); d = ImageDraw.Draw(im)
d.text((W // 2, 60), "同じお願いで、6つのAIを比べた", font=f(44), fill=NAVY, anchor="mm")
xs = [60, 380, 640, 900, 1220]
y = 120
d.rounded_rectangle((60, y, 1220, y + 62), 10, fill=NAVY)
for i, h in enumerate(["AI", "30字以内", "字数の書き方", "おすすめ"]):
    d.text(((xs[i] + xs[i + 1]) // 2, y + 31), h, font=f(28), fill=WHITE, anchor="mm")
y += 70
for r in rows:
    d.rounded_rectangle((60, y, 1220, y + 62), 10, fill=WHITE)
    for i, c in enumerate(r):
        col = WARN if c in ("1個こえた", "5個ずれ") else (TEAL if c == "全部正確" else INK)
        d.text(((xs[i] + xs[i + 1]) // 2, y + 31), c, font=f(28 if i else 30), fill=col, anchor="mm")
    y += 70
d.text((W // 2, y + 30), "字数はPythonで数え直した。正確だった2つは、どちらもPythonで数えていた", font=f(26), fill=NAVY, anchor="mm")
im.save(OUT + "article13_fig1_titles.png")

# 図2：私が選んだ6つ
picks = [("ChatGPT", "読まれない記事のタイトルを変えてみた結果"),
         ("Gemini", "記事のタイトルを変えてみた結果と、そこから分かったこと"),
         ("Muse", "開かれない記事、タイトルを変えて試した結果"),
         ("Manus", "読まれない記事のタイトルを見直した記録"),
         ("Perplexity", "開かれない記事のタイトルを変えてみたら"),
         ("Claude", "note初心者の小さな実験：タイトルを変えてみた")]
H = 140 + 76 * 6 + 80
im = Image.new("RGB", (W, H), LG); d = ImageDraw.Draw(im)
d.text((W // 2, 60), "60個の中から、私が選んだ6つ", font=f(44), fill=NAVY, anchor="mm")
y = 120
for ai, t in picks:
    d.rounded_rectangle((60, y, 1220, y + 66), 12, fill=WHITE)
    d.rounded_rectangle((60, y, 290, y + 66), 12, fill=TEAL)
    d.rectangle((270, y, 290, y + 66), fill=TEAL)
    d.text((175, y + 33), ai, font=f(28), fill=WHITE, anchor="mm")
    d.text((320, y + 33), t, font=f(28), fill=INK, anchor="lm")
    y += 76
d.text((W // 2, y + 35), "6つとも「やってみた」「試した結果」「見直した記録」の形だった", font=f(30), fill=NAVY, anchor="mm")
im.save(OUT + "article13_fig2_choice.png")
print("ok")
