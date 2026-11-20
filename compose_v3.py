#!/usr/bin/env python3
"""news-image-20261120 — final entry v3 (sketsa 6 CALM + perbaikan Kevin
15:05 WIB "Perbaiki").

Perubahan dari v2 (semua dari Kevin / crosscheck ulang v2):
1. Swap 3 brief: 30 COP31 consult -> F1 Las Vegas FP2 (AMERICAS);
   32 NATO -> KCSE Kenya (AFRICA); 33 Children's Day -> Rand Afsel
   (AFRICA). Breadth: AFRICA 0->2, AMERICAS 2->3, total tetap 33.
2. Hero 3 COP31: ringkasan ditulis ulang tanpa "fossil fuels"
   (mengulang kata judul) -> "Draft omits phase-out wording; ...".
3. Hero 2 kriket: FOCUS 0.50 -> 0.0 supaya ujung tongkat pemukul
   utuh dengan margin langit krem di atasnya (dicek 3 nilai focus:
   0.0 memberi margin paling jelas; 0.35 masih memotong ujung
   tongkat karena ujungnya ada di y~7% aset).
4. LEGIBILITAS (keluhan Kevin: kartu 5-18 burem di HP): judul kartu
   10->11pt, ringkasan 8->9pt, CARD_H 140->150px; ringkasan yang tidak
   muat 2 baris di 9pt dipersingkat (fakta + angka tetap).
5. PETA: pin SATU warna selaras (emas isi + nomor navy, r 6.5) +
   dot brief emas; bintang hero tetap emas.
6. BORDER: tiap panel diberi border navy tipis; band MORE STORIES +
   peta diberi garis pembatas navy dengan baris kartu di atasnya.
7. DATE CHECK tetap 18 item; footer + sources UTUH (assert + crop 2x).

Frame: sketsa 6 "CALM" — 4 hero + 14 kartu (2 baris x 7 kolom) +
15 brief = 33 cerita. Isi cerita = pool 33 v1 yang SUDAH
terverifikasi + 3 brief pengganti terverifikasi (riset-afrika-
amerika-v3.md). Peta dunia dipertahankan (pelajaran ni19).
Footer: DATE CHECK 2 baris + sources 1 baris, assert
sources_bottom <= 1010 (v15 lesson: footer TIDAK BOLEH terpotong).

Deterministic: same inputs -> same bytes (PIL only, no randomness,
no network, no timestamps in the image). Run twice, compare sha256.
"""
import os
import sys

sys.path.insert(0, "/home/hatch/workspace/makefun/news-image-20261119")
sys.path.insert(0, "/home/hatch/workspace/makefun/news-image-20261120")

from PIL import Image, ImageDraw, ImageFont

import render_sketches as rs
import render_variants as rv

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
V1_ASSETS = "/home/hatch/workspace/makefun/news-image-20261120/repo-v1/assets"

# --- extra map places for ni20 (lon, lat) ---------------------------
rv.PLACES.update({
    "Jakarta": (106.8, -6.2), "Sydney": (151.2, -33.9),
    "Loyalty Islands": (171.2, -24.7), "Pukapuka": (-165.8, -10.9),
    "Madrid": (-3.7, 40.4), "Seoul": (127.0, 37.5),
    "Florida": (-81.5, 28.5), "Antalya": (30.7, 36.9),
    "Gopalpur": (85.0, 19.3), "Brisbane": (153.0, -27.5),
    "Taipei": (121.6, 25.0), "Wellington": (174.8, -41.3),
    "Hong Kong": (114.2, 22.3), "Paris": (2.35, 48.85),
    "New Delhi": (77.2, 28.6), "Shenzhen": (114.1, 22.5),
    "Kyiv": (30.5, 50.4), "Brussels": (4.4, 50.8),
    "Tokyo": (139.7, 35.7),
    # v3: kota brief baru (swap Afrika/Amerika)
    "Las Vegas": (-115.1, 36.2), "Nairobi": (36.8, -1.3),
    "Johannesburg": (28.0, -26.2),
})

PAPER = rv.PAPER
NAVY = rv.NAVY
INK = rv.INK
RED = rv.RED
GOLD = rv.GOLD
WHITE = rv.WHITE
CARD_BG = rv.CARD_BG
REGION_COLORS = rv.REGION_COLORS
BOLD, REG = rv.BOLD, rv.REG


def F(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, fnt, max_w):
    return rv.wrap(d, text, fnt, max_w)


def cover_crop(img, tw, th, focus_y=0.5):
    """Cover-crop to (tw, th); focus_y 0..1 picks the vertical band."""
    iw, ih = img.size
    scale = max(tw / iw, th / ih)
    nw, nh = int(iw * scale + 0.5), int(ih * scale + 0.5)
    img = img.resize((nw, nh), Image.LANCZOS)
    x = (nw - tw) // 2
    y = int((nh - th) * focus_y + 0.5)
    return img.crop((x, y, x + tw, y + th))


def asset_path(name):
    """Aset dicari di repo-v2/assets dulu, lalu repo-v1/assets."""
    p = os.path.join(ASSETS, name)
    if os.path.exists(p):
        return p
    return os.path.join(V1_ASSETS, name)


# ------------------------------------------------------------------ content
# (num, city, topic, region, title, summary, asset, map_city)
# summary = SATU string (sudah termasuk sumber inline "(Sumber)").
HEROES = [
    (1, "Gopalpur", "CYCLONE", "ASIA",
     "Cyclone Akvan hits India's east coast",
     "Landfall 07:30 IST, gusts to 90 km/h. 300,000 evacuated "
     "to shelters. (IMD)",
     "media-generation-hero-akvan-0-57cc4497-f8ab-4ea0-b839-20b217a7edff.webp",
     "Gopalpur"),
    (2, "Wellington", "CRICKET", "OCEANIA",
     "Nicholls 175* lifts New Zealand to 368",
     "Nicholls 175*; Phillips adds 118. NZ 368; India 85/0 "
     "at stumps. (ESPNcricinfo)",
     "media-generation-hero-cricket-0-671710f6-d8d0-445d-a073-e8bdb63940ee.webp",
     "Wellington"),
    (3, "Antalya", "CLIMATE", "MIDEAST",
     "COP31 draft drops fossil fuels",
     "Draft omits phase-out wording; final text due midnight. (Reuters)",
     "media-generation-hero-cop31-0-c8e0597b-6e2f-4f06-83c4-058822566b89.webp",
     "Antalya"),
    (4, "Kyiv", "MISSILES", "EUROPE",
     "Missiles hit Kyiv in the early hours",
     "Missiles strike the capital from 01:25. Blasts heard "
     "across the city. (Reuters)",
     "media-generation-hero-kyiv-0-3d735a58-045a-492e-8624-4f5c75015b47.webp",
     "Kyiv"),
]

CARDS = [
    (5, "Kyiv", "KYIV HIT", "EUROPE",
     "Kyiv hit again overnight",
     "Missiles strike the capital; blasts heard. (Reuters)",
     "media-generation-card-kyiv-fire-0-b0721218-0300-4922-bbd8-d44ae4355d8c.webp",
     "Kyiv"),
    (6, "New Delhi", "SCO", "ASIA",
     "Modi opens SCO civilisations forum",
     "SCO forum opens in Delhi. 20–22 Nov. (Nation Press)",
     "media-generation-card-sco-0-b60ce69d-a5ad-4c24-bc9e-4f8f5c15037d.webp",
     "New Delhi"),
    (7, "Florida", "FLOODS", "AMERICAS",
     "Florida river still rising",
     "Crest 18.6 ft Fri; schools shut. (Florida Today)",
     "media-generation-card-florida-0-77f1aa21-04d5-4f2d-997e-00e60a4a9fc0.webp",
     "Florida"),
    (8, "Shenzhen", "APEC", "ASIA",
     "Xi meets Albanese, Prabowo",
     "Bilaterals in Shenzhen after APEC week. (Reuters)",
     "media-generation-card-apec-0-12b23d50-5daa-402d-a203-5363db48fa25.webp",
     "Shenzhen"),
    (9, "Taipei", "STOCKS", "ASIA",
     "Taiex slides again Friday",
     "Taiwan stocks fall 6.4%; chips lead losses. (Reuters)",
     "media-generation-card-taipei-0-c76fd1fa-a6fb-43de-9a31-aa5bbdf2bb6c.webp",
     "Taipei"),
    (10, "Markets", "GOLD", "WORLD",
     "Gold plunges on Friday",
     "Gold falls 2.8% intraday to $3,520. (KuCoin News)",
     "media-generation-card-gold-0-c9ad5856-901f-4387-8bf5-f693b1573a67.webp",
     "Global"),
    (11, "Brisbane", "CONCERT", "OCEANIA",
     "Robbie Williams plays Brisbane",
     "BRITPOP at Suncorp tonight; Auckland next. (Suncorp)",
     "media-generation-card-brisbane-0-56a51c4f-8b50-46be-a5c0-c74a916d52d2.webp",
     "Brisbane"),
    (12, "Global", "GAMES", "WORLD",
     "GTA VI user scores open at noon",
     "Reviews open 12:00 PT. Metascore 99. (GeekRadar)",
     "media-generation-card-gta-0-990fab60-003c-46b1-bb58-2c1ff0c3a703.webp",
     "Global"),
    (13, "Tokyo", "MARKETS", "ASIA",
     "Asia markets plunge",
     "Asia \u22122.5%; Nikkei \u22124.1%, Kospi \u22124.7%. (Reuters)",
     "media-generation-card-asia-markets-0-3200f7db-87dd-4c60-8b5d-891f8eeaae04.webp",
     "Tokyo"),
    (14, "Shenzhen", "DEALS", "ASIA",
     "Prabowo, Xi sign $86.8bn deals",
     "Pacts worth about Rp1,600 trillion. (Xinhua)",
     "media-generation-card-prabowo-xi-0-9c1490cd-b0a8-4b70-9689-832f138701ae.webp",
     "Shenzhen"),
    (15, "Jakarta", "YOUTUBE", "ASIA",
     "Jakarta asks Google to explain",
     "19,000 channels removed. (Reuters)",
     "media-generation-card-indonesia-google-0-8d8ce221-2a6c-4277-97e9-ad7e20eb11ff.webp",
     "Jakarta"),
    (16, "Loyalty Is.", "QUAKE", "OCEANIA",
     "M5.6 quake off Loyalty Islands",
     "00:49 UTC, 10 km deep; no tsunami. (USGS)",
     "media-generation-card-quake-0-7a34fb0a-42b2-49f9-9b00-dbbfae3cd6c8.webp",
     "Loyalty Islands"),
    (17, "Brussels", "SUMMIT", "EUROPE",
     "EU-UK summit opens in Brussels",
     "Second EU-UK summit in Brussels. (Consilium)",
     "media-generation-card-euuk-brussels-0-da84f179-b5fd-441a-89b0-5d93c85e3e71.webp",
     "Brussels"),
    (18, "Global", "OIL", "WORLD",
     "Brent rises to $92.77",
     "Brent $92.77; WTI $83.40. Oil up on Friday. (Reuters)",
     "media-generation-card-brent-oil-crop.webp",
     "Global"),
]

# (num, city, region, text) — 15 briefs: 17 brief v1 minus EU-UK + Brent
# (keduanya naik jadi kartu 17-18), nomor ulang 19-33.
BRIEFS = [
    (19, "Tokyo", "ASIA", "Japan core CPI rises 2.2% in October."),
    (20, "Sydney", "OCEANIA", "Sydney terror raids: several arrested."),
    (21, "Global", "WORLD", "Pakistan beat Sri Lanka by 8 wickets."),
    (22, "Madrid", "EUROPE", "Spain students strike over education cuts."),
    (23, "Seoul", "ASIA", "Samsung names Choi to head Mobile."),
    (24, "Paris", "EUROPE", "Harris meets Macron in Paris."),
    (25, "Taipei", "ASIA", "Taiwan reports 2,700 accounts to Meta."),
    (26, "Riyadh", "MIDEAST", "Saudi coalition intercepts Houthi missile."),
    (27, "Pukapuka", "OCEANIA", "Cyclone Xavier: Pukapuka on storm alert."),
    (28, "Hong Kong", "ASIA", "Hong Kong Open quarter-finals decided."),
    (29, "Tokyo", "ASIA", "Anti-Takaichi protest draws 10,000."),
    (30, "Las Vegas", "AMERICAS",
     "Russell tops wet Las Vegas FP2: 1:47.272; Gasly +0.071."),
    (31, "Florida", "AMERICAS", "Flood watch holds through Saturday."),
    (32, "Nairobi", "AFRICA", "KCSE ends; record 1.05m candidates."),
    (33, "Johannesburg", "AFRICA",
     "Rand hits one-year low at 17.56 per dollar."),
]

DECK_LINES = [
    "Akvan lands in India \u00b7 COP31's last day \u00b7 Nicholls lifts New Zealand",
    "Asia markets plunge \u00b7 Prabowo and Xi sign $86.8bn in Shenzhen",
]

TIMELINE = [
    ("01:25", "Kyiv missiles", "EUROPE"),
    ("07:30", "Akvan landfall", "ASIA"),
    ("12:00 PT", "GTA reviews open", "WORLD"),
    ("12:00 ET", "Trump presser due", "AMERICAS"),
    ("21:00", "COP31 text due", "MIDEAST"),
]

NUMBERS = [
    ("300,000", "evacuated for Akvan", "ASIA"),
    ("$92.77", "Brent crude per barrel", "WORLD"),
    ("\u22122.5%", "MSCI Asia, Friday", "ASIA"),
    ("175*", "Nicholls' runs, day two", "OCEANIA"),
    ("423", "rescue teams deployed", "ASIA"),
    ("19,000", "YouTube channels removed", "ASIA"),
]

DATECHECK_REST = (
    "Not Friday's news, so not on this page: Senate vote \u00b7 IAEA report \u00b7 "
    "Sensex \u00b7 Fiji \u00b7 Europe talks \u00b7 Dakar boat \u00b7 Dhaka fire \u00b7 Takaichi \u00b7 "
    "Australia sanctions \u00b7 hockey \u00b7 Quad \u00b7 Romania \u00b7 Zelenskyy \u00b7 rupee \u00b7 "
    "Kenya flood \u00b7 Thai pact \u00b7 Husky \u00b7 Dow \u2014 all 17\u201319 Nov. Every story "
    "here happened, or was first reported, on Friday 20 November 2026.")

SOURCES_LINE = (
    "Sources: Reuters \u00b7 AP \u00b7 IMD \u00b7 USGS \u00b7 RSMC Nadi \u00b7 AFP \u00b7 Le Monde \u00b7 "
    "IANS \u00b7 Xinhua \u00b7 ESPNcricinfo \u00b7 Metacritic. "
    "Disputed claims are attributed, not stated as fact.")

# focus_y per panel num: which vertical band of the AI asset the thin
# card/hero slice shows (0 = top, 1 = bottom). v1 values kept; untuk
# kartu focus_y tidak berpengaruh (slice menampilkan seluruh tinggi
# aset karena th/ih > tw/iw) — warna atas kartu ditentukan tepi atas
# aset (dicek di /tmp/topcheck.py: hanya tabrakan 17-18, diperbaiki
# dengan crop Brent).
FOCUS = {
    1: 0.50, 2: 0.0, 3: 0.50, 4: 0.50,
    5: 0.55, 6: 0.50, 7: 0.62, 8: 0.50,
    9: 0.50, 10: 0.50, 11: 0.50, 12: 0.55,
    13: 0.50, 14: 0.40, 15: 0.50, 16: 0.50,
    17: 0.50, 18: 0.50,
}

HERO_H = 175
CARD_H = 150  # v3: 140 -> 150 (legibilitas: judul kartu 11pt, ringkasan 9pt)
BOTTOM_MARGIN = 24  # v15 lesson: explicit paper below the last line

# ------------------------------------------------------------------ chrome
def draw_masthead_band(d, W, y):
    """PITA NAVY: masthead jadi pita navy full-width, 62 px."""
    f_small = F(BOLD, 11)
    f_date = F(BOLD, 30)
    d.rectangle([12, y, W - 12, y + 62], fill=NAVY)
    d.text((W // 2, y + 4), "THE WORLD IN ONE IMAGE",
           font=f_small, fill=WHITE, anchor="ma")
    parts = [("FRIDAY ", WHITE), ("20", GOLD), (" NOVEMBER 2026", WHITE)]
    total = sum(d.textlength(t, font=f_date) for t, _ in parts)
    x = (W - total) // 2
    yy = y + 22
    for t, col in parts:
        d.text((x, yy), t, font=f_date, fill=col)
        x += d.textlength(t, font=f_date)
    d.line([(12, y + 60), (W - 12, y + 60)], fill=GOLD, width=2)
    return y + 62


def draw_deck5(d, W, y):
    """Deck dalam kotak berbingkai navy, 2 baris merah 13pt."""
    f = F(BOLD, 13)
    d.rectangle([12, y, W - 12, y + 40], fill=CARD_BG, outline=NAVY,
                width=2)
    yy = y + 3
    for ln in DECK_LINES:
        lines = wrap(d, ln, f, W - 24 - 16)
        assert len(lines) == 1, f"deck pecah: {ln} -> {lines}"
        d.text((W // 2, yy), lines[0], font=f, fill=RED, anchor="ma")
        yy += 18
    return y + 40


def draw_timeline_bar(d, W, y):
    """Timeline horizontal CALM: 5 jam 20 Nov, titik EMAS semua
    (perbaikan Kevin #4 — selaras, bukan warna-warni per titik)."""
    f_tl = F(BOLD, 10)
    f_tm = F(BOLD, 11)
    line_y = y + 18
    d.line([(24, line_y), (W - 24, line_y)], fill=NAVY, width=2)
    seg = (W - 48) // 5
    for i, (tm, label, region) in enumerate(TIMELINE):
        cx = 24 + seg * i + seg // 2
        d.ellipse([cx - 6, line_y - 6, cx + 6, line_y + 6], fill=GOLD,
                  outline=NAVY, width=1)
        d.text((cx, y), tm, font=f_tm, fill=RED, anchor="ma")
        d.text((cx, line_y + 9), label, font=f_tl, fill=INK, anchor="ma")
    return line_y + 26


def draw_numbers_strip(d, W, y, h=58):
    """Strip angka CALM: 6 kartu kecil berbingkai, angka 21pt navy,
    bilah bawah EMAS semua (perbaikan Kevin #1)."""
    f_n = F(BOLD, 21)
    f_c = F(BOLD, 9)
    widths = [162, 162, 161, 162, 161, 162]
    assert sum(widths) + 5 * 6 == W - 24
    x = 12
    for i, (num, cap, region) in enumerate(NUMBERS):
        cw = widths[i]
        x0, x1 = x, x + cw
        d.rectangle([x0, y, x1, y + h], fill=WHITE, outline=NAVY, width=1)
        d.rectangle([x0, y + h - 3, x1, y + h], fill=GOLD)
        d.text(((x0 + x1) // 2, y + 3), num, font=f_n, fill=NAVY,
               anchor="ma")
        lines = wrap(d, cap, f_c, cw - 12)
        assert len(lines) <= 2, f"caption kartu angka pecah: {cap} -> {lines}"
        yy = y + 31
        for ln in lines:
            d.text(((x0 + x1) // 2, yy), ln, font=f_c, fill=INK,
                   anchor="ma")
            yy += 12
        x = x1 + 6
    return y + h


def draw_datecheck(d, W, y):
    """DATE CHECK: pita navy full-width (cermin masthead), teks putih 9pt
    bold; awalan '✓ DATE CHECK —' emas. Di bawahnya SATU baris sources
    9pt abu-abu (termasuk disclaimer) — v15 lesson: baris terakhir
    harus UTUH dengan margin kertas di bawahnya (BOTTOM_MARGIN)."""
    prefix = "\u2713 DATE CHECK \u2014 "
    f = F(BOLD, 9)
    pref_w = d.textlength(prefix, font=f)
    lines = wrap(d, DATECHECK_REST, f, W - 48 - pref_w)
    assert len(lines) <= 3, f"datecheck pecah >3: {lines}"
    box_h = 8 + len(lines) * 13 + 6
    d.rectangle([12, y, W - 12, y + box_h], fill=NAVY)
    d.line([(12, y + box_h - 2), (W - 12, y + box_h - 2)], fill=GOLD,
           width=2)
    yy = y + 7
    for j, ln in enumerate(lines):
        if j == 0:
            total_w = pref_w + d.textlength(ln, font=f)
            x0 = (W - total_w) // 2
            d.text((x0, yy), prefix, font=f, fill=GOLD)
            d.text((x0 + pref_w, yy), ln, font=f, fill=WHITE)
        else:
            d.text((W // 2, yy), ln, font=f, fill=WHITE, anchor="ma")
        yy += 13
    f2 = F(REG, 9)
    src_y = y + box_h + 4
    sw = d.textlength(SOURCES_LINE, font=f2)
    assert sw <= W - 24, f"sources line terlalu panjang: {sw}"
    d.text((W // 2, src_y), SOURCES_LINE, font=f2, fill=(90, 90, 90),
           anchor="ma")
    src_bottom = src_y + 11  # 9pt REG: ascender ~9px + 2px safety
    assert src_bottom <= 1024 - 14, \
        f"sources line terlalu rendah: bottom {src_bottom}"
    return {"datecheck_lines": len(lines), "sources_bottom": src_bottom,
            "bottom_margin": 1024 - src_bottom}


# ------------------------------------------------------------------ panels
def draw_panel_ai(im, x, y, w, h, story, title_pt, sum_pt, strip_h=15):
    """Satu panel CALM: strip NAVY + slice ilustrasi AI + judul +
    ringkasan (sumber sudah inline di ringkasan — TIDAK ADA baris
    sumber terpisah). Mengembalikan warna atas gambar (rata-rata
    baris 2-8 piksel di tengah) untuk cek warna tetangga."""
    d = ImageDraw.Draw(im)
    f_title = F(BOLD, title_pt)
    f_sum = F(REG, sum_pt)
    d.rectangle([x, y, x + w, y + strip_h], fill=NAVY)
    strip = f"{story['num']} \u00b7 {story['city'].upper()} \u00b7 {story['topic']}"
    f_strip = F(BOLD, 10 if strip_h >= 15 else 9)
    while (d.textlength(strip, font=f_strip) > w - 10
           and f_strip.size > 8):
        f_strip = F(BOLD, f_strip.size - 1)
    d.text((x + 6, y + strip_h // 2), strip, font=f_strip, fill=WHITE,
           anchor="lm")
    tw = wrap(d, story["title"], f_title, w - 10)
    assert len(tw) <= 2, f"judul pecah >2: {story['title']} -> {tw}"
    s_lines = wrap(d, story["summary"], f_sum, w - 10)
    assert len(s_lines) <= 2, \
        f"ringkasan pecah >2: {story['num']} -> {s_lines}"
    text_h = len(tw) * (title_pt + 3) + len(s_lines) * (sum_pt + 3) + 4
    img_h = h - strip_h - text_h - 4
    assert img_h >= 48, f"gambar {story['num']} terlalu pendek: {img_h}"
    src = Image.open(asset_path(story["asset"])).convert("RGB")
    pic = cover_crop(src, w, img_h, FOCUS.get(story["num"], 0.5))
    im.paste(pic, (x, y + strip_h))
    yy = y + strip_h + img_h + 2
    for ln in tw:
        d.text((x + 5, yy), ln, font=f_title, fill=INK)
        yy += title_pt + 3
    for ln in s_lines:
        d.text((x + 5, yy), ln, font=f_sum, fill=INK)
        yy += sum_pt + 3
    # v3 (arahan Kevin): tiap panel = kartu ber-border navy tipis.
    d.rectangle([x, y, x + w, y + h], outline=NAVY, width=1)
    px = pic.crop((w // 2 - 10, 2, w // 2 + 10, 8))
    cols = list(px.getdata())
    avg = tuple(sum(c[i] for c in cols) // len(cols) for i in range(3))
    return avg, img_h


def draw_briefs_nobar(im, x, y, w, h, briefs, first_num, font_pt=12):
    """MORE STORIES CALM: nomor brief polos TANPA batang warna di
    samping nomor (perbaikan Kevin #3). 3 kolom, rata atas-bawah."""
    d = ImageDraw.Draw(im)
    f_n = F(BOLD, font_pt)
    f_c = F(BOLD, font_pt)
    f_t = F(REG, font_pt)
    cols = [[], [], []]
    for i, b in enumerate(briefs):
        cols[i % 3].append(b)
    col_w = (w - 16) // 3
    lh = font_pt + 3
    col_items = []
    for col in cols:
        items = []
        for (n, city, region, text) in col:
            head = f"{n}. {city}: "
            hw = d.textlength(head, font=f_n)
            lines = []
            words = text.split()
            cur = ""
            first_w = col_w - hw - 6
            for wd in words:
                trial = (cur + " " + wd).strip()
                lim = first_w if not lines else col_w - 6
                if d.textlength(trial, font=f_t) <= lim:
                    cur = trial
                else:
                    lines.append(cur)
                    cur = wd
            if cur:
                lines.append(cur)
            assert len(lines) <= 3, f"brief {n} pecah >3: {lines}"
            items.append((n, city, region, lines, head))
        col_items.append(items)
    for ci, items in enumerate(col_items):
        cx = x + ci * col_w + (8 if ci else 0)
        total_lines = sum(len(it[3]) for it in items)
        gaps = h - total_lines * lh
        gap_each = max(0, gaps // (len(items) + 1))
        yy = y + gap_each
        for (n, city, region, lines, head) in items:
            d.text((cx, yy), f"{n}. ", font=f_n, fill=RED)
            nx = cx + d.textlength(f"{n}. ", font=f_n)
            d.text((nx, yy), f"{city}: ", font=f_c, fill=NAVY)
            tx = nx + d.textlength(f"{city}: ", font=f_c)
            d.text((tx, yy), lines[0], font=f_t, fill=INK)
            yy += lh
            for ln in lines[1:]:
                d.text((cx, yy), ln, font=f_t, fill=INK)
                yy += lh
            yy += gap_each
    return y + h


def draw_map_v3(im, x, y, mw, mh, panels, briefs, hero_city):
    """Peta dunia v3: SAMA seperti rs.draw_map, kecuali pin SATU warna
    selaras palet calm (emas isi + nomor navy, r 6.5) dan dot brief
    emas (r 3.5) — pin multi-warna region di v2 tidak selaras tema.
    Bintang hero (Gopalpur) tetap emas + outline navy."""
    d = ImageDraw.Draw(im)
    d.rectangle([x, y, x + mw, y + mh], fill=CARD_BG, outline=NAVY, width=1)
    mtmp = Image.new("RGB", (mw - 2, mh - 2), rv.SEA)
    md = ImageDraw.Draw(mtmp)
    for poly in rv.CONTINENTS:
        pts = [rv.project(lon, lat, 0, 0, mw - 2, mh - 2) for lon, lat in poly]
        md.polygon(pts, fill=rv.LAND, outline=(180, 160, 115))
    im.paste(mtmp, (x + 1, y + 1))
    md = ImageDraw.Draw(im)
    fp = F(BOLD, 8)
    placed = []
    skipped = []

    def place(px, py, r):
        for (qx, qy, qr) in placed:
            if ((px - qx) ** 2 + (py - qy) ** 2) ** 0.5 < 10:
                return False
        placed.append((px, py, r))
        return True

    for p in panels:
        city = p["map_city"]
        if city not in rv.PLACES:
            continue
        lon, lat = rv.PLACES[city]
        px, py = rv.project(lon, lat, x + 1, y + 1, mw - 2, mh - 2)
        if p["city"] == hero_city:
            if place(px, py, 8):
                md.polygon(rv.star_points(px, py, 8, 3.5), fill=GOLD,
                           outline=NAVY)
            continue
        if not place(px, py, 6.5):
            skipped.append((city, p["num"]))
            continue
        md.ellipse([px - 6.5, py - 6.5, px + 6.5, py + 6.5], fill=GOLD,
                   outline=NAVY, width=1)
        mark = str(p["num"])
        tw = md.textlength(mark, font=fp)
        md.text((px - tw / 2, py - 4.5), mark, font=fp, fill=NAVY)
    seen = {rv.PLACES[p["map_city"]] for p in panels
            if p["map_city"] in rv.PLACES}
    for (n, city, region, _t) in briefs:
        if city in ("Global",) or city not in rv.PLACES:
            continue
        if rv.PLACES[city] in seen:
            continue
        seen.add(rv.PLACES[city])
        lon, lat = rv.PLACES[city]
        px, py = rv.project(lon, lat, x + 1, y + 1, mw - 2, mh - 2)
        if not place(px, py, 3.5):
            skipped.append((city, n))
            continue
        md.ellipse([px - 3.5, py - 3.5, px + 3.5, py + 3.5],
                   fill=GOLD, outline=NAVY, width=1)
    return skipped


def to_panel(t):
    num, city, topic, region, title, summary, asset, map_city = t
    return {"num": num, "city": city, "topic": topic, "region": region,
            "title": title, "summary": summary, "asset": asset,
            "map_city": map_city}


def region_legend(counts):
    disp = {"ASIA": "ASIA-PAC"}
    parts = []
    for r in rs.REGION_ORDER:
        parts.append(f"{disp.get(r, r)} {counts[r]}")
    return " \u00b7 ".join(parts)


def build(path):
    W = 1024
    im = Image.new("RGB", (W, 1024), PAPER)
    d = ImageDraw.Draw(im)
    heroes = [to_panel(t) for t in HEROES]
    cards = [to_panel(t) for t in CARDS]
    panels = heroes + cards
    briefs = [(n, city, region, text) for n, city, region, text in BRIEFS]
    counts = rs.region_counts(panels, briefs)
    total = sum(counts.values())
    assert total == 33, f"total cerita {total} != 33"

    y = 12
    y = draw_masthead_band(d, W, y)
    y = draw_deck5(d, W, y + 4)
    y = draw_timeline_bar(d, W, y + 4)
    y = draw_numbers_strip(d, W, y + 4)
    y += 6
    tops = {}
    img_hs = {}
    n_hero = len(heroes)
    hero_w = (W - 24 - 4 * (n_hero - 1)) // n_hero
    for i, st in enumerate(panels[:n_hero]):
        xx = 12 + i * (hero_w + 4)
        tops[(0, i)], img_hs[st["num"]] = draw_panel_ai(
            im, xx, y, hero_w, HERO_H, st, 13, 11)
    y += HERO_H + 4
    n_col = 7
    card_w = (W - 24 - 4 * (n_col - 1)) // n_col
    for r in range(2):
        for c in range(n_col):
            st = panels[n_hero + r * n_col + c]
            xx = 12 + c * (card_w + 4)
            tops[(1 + r, c)], img_hs[st["num"]] = draw_panel_ai(
                im, xx, y, card_w, CARD_H, st, 11, 9)
        y += CARD_H + 4
    band_y = y
    # v3 (arahan Kevin): band MORE STORIES + peta diberi batas atas yang
    # jelas (garis navy) dengan baris kartu di atasnya.
    d.line([(12, band_y - 2), (W - 12, band_y - 2)], fill=NAVY, width=2)
    # Cadangan 10px di bawah band untuk footer (pelajaran v15 ni19):
    # DATE CHECK 2 baris 9pt + baris sources berakhir di y~1007,
    # margin kertas 17px.
    band_h = 1024 - 72 - band_y - 4
    map_w = 400
    map_h = band_h - 18
    skipped = draw_map_v3(im, 12, band_y, map_w, map_h, panels, briefs,
                          "Gopalpur")
    f_lg = F(BOLD, 8)
    d.text((12 + map_w // 2, band_y + map_h + 3), region_legend(counts),
           font=f_lg, fill=NAVY, anchor="ma")
    bx = 12 + map_w + 12
    bw = W - 12 - bx
    f_bh = F(BOLD, 12)
    d.text((bx, band_y), "MORE STORIES FROM 20 NOVEMBER", font=f_bh,
           fill=NAVY)
    draw_briefs_nobar(im, bx, band_y + 20, bw, band_h - 20, briefs,
                      len(panels) + 1, font_pt=12)
    y = band_y + band_h + 4
    dc = draw_datecheck(d, W, y)
    im.save(path, optimize=True)
    return {"total": total, "counts": counts,
            "top_bad": rs.check_top_colors(tops),
            "tops": {f"{r},{c}": v for (r, c), v in tops.items()},
            "img_hs": img_hs,
            "map_skipped": skipped, "band_y": band_y,
            "band_h": band_h, "map_h": map_h, "datecheck": dc}


if __name__ == "__main__":
    import json
    out = os.path.join(HERE, "entry.png")
    res = build(out)
    print(json.dumps(res, default=str, indent=1))
    print("OK", out)
