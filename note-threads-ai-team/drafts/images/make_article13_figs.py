from PIL import Image, ImageDraw, ImageFont
F = "/usr/share/fonts/opentype/ipafont-gothic/ipagp.ttf"
NAVY, TEAL, LG, WHITE, INK = (30, 52, 96), (26, 154, 159), (236, 240, 245), (255, 255, 255), (40, 48, 60)
def f(s): return ImageFont.truetype(F, s)
OUT = "/home/user/-/note-threads-ai-team/drafts/images/"
T = ["noteのタイトルを変えても、読まれなかった話", "記事が開かれない理由は、タイトルだけじゃなかった",
     "noteを2週間続けて気づいた、タイトルより大事なこと", "読まれない記事のタイトルを変えてみた結果",
     "タイトルを工夫すれば読まれると思っていた", "note初心者がタイトルを変えて分かったこと",
     "記事が読まれない原因を、タイトルのせいにしていた", "タイトルを変えても反応が変わらなかった理由",
     "noteを始めて2週間、タイトルについて考えたこと", "読まれる記事は、タイトルの言い方だけでは決まらない"]
W = 1280; H = 130 + 10 * 58 + 80
im = Image.new("RGB", (W, H), LG); d = ImageDraw.Draw(im)
d.text((W // 2, 60), "AIが出したタイトル案10個（ChatGPT）", font=f(44), fill=NAVY, anchor="mm")
y = 120
for i, t in enumerate(T, 1):
    mine = i == 4; ai = i == 2
    d.rounded_rectangle((60, y, 1220, y + 48), 10, fill=TEAL if mine else WHITE)
    col = WHITE if mine else INK
    d.text((90, y + 24), f"{i}.", font=f(26), fill=col, anchor="lm")
    d.text((140, y + 24), t, font=f(26), fill=col, anchor="lm")
    tag = "私が選んだ" if mine else ("AIの1位" if ai else "")
    if tag:
        d.text((1195, y + 24), tag, font=f(24), fill=WHITE if mine else NAVY, anchor="rm")
    y += 58
d.text((W // 2, y + 35), "10個とも30字以内・強い言葉なし。ただし切り口はほぼ同じ", font=f(28), fill=NAVY, anchor="mm")
im.save(OUT + "article13_fig1_titles.png")

H = 600
im = Image.new("RGB", (W, H), LG); d = ImageDraw.Draw(im)
d.text((W // 2, 60), "AIのおすすめと、私が選んだもの", font=f(44), fill=NAVY, anchor="mm")
cards = [("AIのおすすめ1位", "記事が開かれない理由は、\nタイトルだけじゃなかった", "理由：続きが気になる", NAVY),
         ("私が選んだもの", "読まれない記事の\nタイトルを変えてみた結果", "理由：実体験が伝わる", TEAL)]
x = 80
for head, body, why, col in cards:
    d.rounded_rectangle((x, 130, x + 540, 500), 20, fill=WHITE, outline=col, width=5)
    d.rounded_rectangle((x, 130, x + 540, 210), 20, fill=col)
    d.rectangle((x, 180, x + 540, 210), fill=col)
    d.text((x + 270, 170), head, font=f(34), fill=WHITE, anchor="mm")
    d.multiline_text((x + 270, 320), body, font=f(34), fill=INK, anchor="mm", align="center", spacing=16)
    d.text((x + 270, 450), why, font=f(30), fill=col, anchor="mm")
    x += 580
d.text((W // 2, 550), "どれを選ぶかは、そのnoteが何を大事にしているかで決まる", font=f(28), fill=NAVY, anchor="mm")
im.save(OUT + "article13_fig2_choice.png")
print("ok")
