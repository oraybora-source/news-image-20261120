# news-image-20261120 — build note v3 (perintah Kevin "Perbaiki" 15:05 WIB)

Build: 20 Nov 2026 ~15:07–15:15 WIB. Kevin "Perbaiki" setelah crosscheck
ulang v2 kartu per kartu (parent cek 18 panel 1–18 di 2x + band bawah +
footer 60px). **JANGAN submit — build saja, kirim hasil ke parent untuk
dicek Kevin dulu, submit hanya setelah Kevin Gas.**

## Hasil

- Repo: `~/workspace/makefun/news-image-20261120/repo-v3/` (BELUM commit,
  BELUM ada repo GitHub — dibuat saat submit, seperti v2)
- `entry.png`: **497.129 byte, sha256
  `f1f267fdc16e466e8f8be3f376d77dddc3786f84aa095dd37729d9f443d768f4`**,
  1024×1024 RGB, ≤1 MiB ✓ (v2: 491.710 byte — naik 5.419 byte karena
  kartu 150px + teks lebih besar; masih jauh di bawah 1 MiB)
- `compose_v3.py`: port compose_v2.py + 7 perbaikan (di bawah)
- `main.py`: Python 3.13 stdlib only, copy entry.png ke output
- README.md + LICENSE (MIT, disalin v2) + STORIES.md (v3) +
  entry-manifest.json + GAP-ANALYSIS.md (v2, referensi)
- Determinisme: compose 2× byte-identik (`f1f267fd…`), main.py 2×
  byte-identik (sha256 sama)
- Pre-submit check kit (`makefun check --worktree`, kit ni20):
  **4 pass** (competition_open, snapshot, license_osi, entrypoint),
  **1 fail** (`transcripts_present` — transkrip di-bundle PARENT saat
  submit, bukan oleh build agent; sama seperti v2), 14 skip, 5 "at
  submission" (repo_public, repo_owner, repo_created_after_open,
  commit_in_repo, duplicate_snapshot — beres saat repo GitHub dibuat +
  push + submit)

## Yang berubah dari v2 (7 perbaikan, semua wajib dari tugas)

1. **Swap 3 brief** (riset-afrika-amerika-v3.md, semua TERVERIFIKASI):
   30 COP31 consult → F1 Las Vegas FP2 (Russell 1:47.272, Gasly +0.071,
   Formula1.com 05:17Z); 32 NATO → KCSE Kenya (1.048.355 peserta,
   rekor >1 juta, People Daily 07:00, KNEC); 33 Children's Day → Rand
   Afsel (17,56/USD 05:40 GMT, terendah 12 bulan, Reuters 06:29 UTC).
   Breadth: AFRICA 0→2, AMERICAS 2→3, total tetap 33. Kartu tidak
   disentuh isinya (kecuali #2–3 di bawah). Legenda peta otomatis
   terbarui: EUROPE 5 · AMERICAS 3 · ASIA-PAC 12 · MIDEAST 2 ·
   AFRICA 2 · OCEANIA 5 · WORLD 4.
2. **COP31 (hero 3):** ringkasan "Draft cuts fossil fuels; final text
   due midnight." → "Draft omits phase-out wording; final text due
   midnight. (Reuters)" — tidak lagi mengulang kata judul. Fakta
   tetap (draft 144→80 paragraf, tanpa kata "fossil").
3. **Hero 2 kriket:** focus_y 0.50 → **0.0**. Dicek 3 nilai focus
   (0.0 / 0.10 / 0.15) lewat render slice langsung: ujung tongkat ada
   di y~7% aset (1920×1280), jadi focus 0.35 (percobaan pertama) MASIH
   memotong ujungnya; focus 0.0 memberi margin langit krem yang jelas
   di atas ujung tongkat. Trade-off dicatat jujur: slice 92px tidak
   bisa memuat tongkat + kaki sekaligus — di focus 0.0 pemukul
   terpotong sekitar pinggang (tetap terbaca jelas sebagai pemukul
   kriket merayakan + penonton + pegunungan). Top-color tetap lolos
   (top_bad kosong).
4. **Legibilitas kartu (keluhan utama Kevin):** judul kartu 10→11pt,
   ringkasan 8→9pt, CARD_H 140→150px (band bawah 247→227px, footer
   tetap di y 952, margin 17px). Ringkasan yang tidak muat 2 baris di
   9pt dipersingkat (tes wrap sebelum compose, fakta + angka tetap):
   #6 "First SCO forum opens in Delhi. Runs 20–22 Nov." → "SCO forum
   opens in Delhi. 20–22 Nov."; #13 tanpa "MSCI"; #14 tanpa
   "Indonesia-China"; #16 tanpa "warning issued"; #17 digabung 1
   kalimat. Judul #8 "Xi meets Albanese, Prabowo in Shenzhen" (3 baris
   di 11pt) → "Xi meets Albanese, Prabowo" (kota tetap di strip +
   ringkasan). Brief kolom 1 dipersingkat (#20 "terrorism"→"terror",
   #23 tanpa "Won-Joon", #26 tanpa "-led", #29 tanpa "in Tokyo", #32
   baru "KCSE ends; record 1.05m candidates.") supaya muat di band
   yang 20px lebih pendek (kolom 1: 15 baris → 10 baris, 150px ≤ 207px).
   Cek 360px (di bawah): judul kartu 5–18 TERBACA jelas di lebar HP,
   ringkasan lebih terbaca dari v2 (masih kecil di 360px — batas format,
   sama seperti yang dihadapi juri di ~300px).
5. **Peta:** pin SATU warna — fungsi `draw_map_v3` lokal di
   compose_v3.py (rs.draw_map tidak diubah): pin panel emas isi +
   nomor navy (r 5.5→6.5, font 7→8pt), dot brief emas + outline navy
   (r 3→3.5). Bintang hero (Gopalpur) tetap emas + outline navy.
   Pin yang ter-skip SAMA seperti v2 (Kyiv #5, Taipei #9, Shenzhen #14,
   Paris #24, Hong Kong #28 — tumpang tindih); 3 pin/dot baru
   (Las Vegas, Nairobi, Johannesburg) semuanya terpasang.
6. **Border (arahan Kevin 15:02–15:03 WIB):** tiap panel kartu/hero
   diberi border navy tipis (rectangle outline di draw_panel_ai);
   band MORE STORIES + peta diberi garis pembatas navy (width 2) di
   atasnya, di celah 4px dengan baris kartu di atasnya.
7. **DATE CHECK tetap 18 item 17–19 Nov;** strip angka region
   diperbarui otomatis; footer + baris Sources UTUH (crop 60px
   terbawah 2x — pelajaran v15).

## Crosscheck 2x (aturan Kevin 20 Nov 11:08 WIB)

**Crosscheck 1 — saat proses:**
- Tes wrap SEMUA judul + ringkasan kartu di ukuran baru (11pt/9pt,
  lebar 129px) SEBELUM compose: 6 gagal di percobaan pertama (#6, #8,
  #13, #14, #16, #17) → dipersingkat, tes ulang sampai SEMUA 2 baris.
  Ringkasan hero 3 baru dites 2 baris di 11pt/lebar 237px.
- Tes baris brief per kolom di band baru (207px): kolom 1 gagal
  (15 baris = 225px) → 5 brief dipersingkat → 10 baris = 150px.
- Render slice kriket di 3 nilai focus sebelum memilih 0.0.
- Geometri dihitung dulu: band_y 721, band_h 227, map_h 209,
  DATE CHECK y 952, sources_bottom 1007, margin 17px.

**Crosscheck 2 — setelah selesai:** entry.png dilihat penuh + 18 panel
satu per satu di 2x + band bawah 2x + footer 60px 2x + downscale 360px
(v3 vs v2 berdampingan, 2 baris kartu):
- 18/18 panel LOLOS: judul ≤2 baris, ringkasan ≤2 baris, teks utuh,
  angka/tanggal cocok dengan STORIES.md v3; subjek utuh. Catatan kecil
  (bukan cacat): pemukul kriket terpotong di pinggang (trade-off
  focus 0.0, lihat #3); meja krem kartu EU-UK masih menyatu dengan
  kertas di ukuran kecil (pemimpin + bintang + bendera tetap terbaca);
  papan "VI" kartu GTA tidak kentara di slice tipis (sama seperti v1/v2).
- Peta: semua pin emas + nomor navy, dot baru Las Vegas/Nairobi/
  Johannesburg terpasang; legenda region baru utuh.
- Brief 19–33: semua terbaca, nomor polos tanpa batang warna.
- Garis pembatas navy di atas band terlihat jelas; border tiap panel
  terlihat jelas.
- **Cek bawah 60px di 2x (pelajaran v15):** DATE CHECK 2 baris UTUH +
  baris "Sources: … Disputed claims are attributed, not stated as
  fact." UTUH sepenuhnya, margin kertas bersih 17px di bawahnya
  (sources_bottom 1007). Cacat v15 TIDAK terulang.
- **Cek 360px (kriteria lolos/gagal v3):** judul kartu 5–18 TERBACA
  jelas di lebar 360px (lebih jelas dari v2 — bandingkan
  ni20v3-360-row1/row2 vs ni20v2-360-row1/row2); ringkasan terbaca
  dengan usaha, lebih baik dari v2. LOLOS dengan catatan jujur:
  ringkasan masih kecil di 360px karena batas format (139px/kartu),
  bukan karena masih ada yang salah render.

## Yang TIDAK berubah dari v2 (sengaja)

- Isi 30 cerita lain + angka + tanggal: SAMA (pool v1 terverifikasi).
- Peta dunia dipertahankan (pelajaran ni19: 8/8 top-50 punya peta).
- DATE CHECK 18 item + klaim penutup; deck 5 cerita; strip 6 angka.
- Kyiv 2x (hero 4 + kartu 5) — tetap, sudah dibedakan sudutnya.
- Pantauan sore (koalisi Johannesburg, presser Trump 12:00 ET) TIDAK
  dimasukkan — belum matang saat build. **Pengumuman koalisi
  Johannesburg TIDAK dicek ulang saat build ini** (bukan klaim tidak
  ada pengumuman — hanya tidak dicari); bila parent/Kevin menemukan
  pengumuman terverifikasi Jumat sore, itu kandidat v4. Presser Trump
  12:00 ET = 00:00 WIB Sabtu — di luar jendela build; bila ada berita
  besar, itu kandidat v4 (parent yang putuskan).

## Label klaim

- **TERVERIFIKASI:** semua angka/fakta di STORIES.md v3 (sumber di
  sana); determinisme 2x (compose + main.py); kit lint 4 pass / 1 fail
  (transcripts_present); top_bad kosong; footer utuh (crop 2x);
  18/18 panel lolos crosscheck 2x; cek 360px.
- **ESTIMASI:** target dev rank ≤150 (rules-ledger); v3 butuh +4,465
  poin dari dev v2 (982,336) untuk bar rank-50 — perbaikan breadth
  menargetkan penentu duel yang tercatat, tapi bukti ni19 bilang
  perbaikan tidak keluar dari noise dev (±4 poin).
- **TIDAK TAHU:** isi presser Trump 12:00 ET; hasil akhir COP31;
  aturan siapa dapat skor `contend`.

## Yang tersisa untuk submit (oleh parent, SETELAH Kevin cek + Gas)

1. Kirim entry final v3 ke Kevin dulu (aturan: hasil dikirim sebelum
   minta Gas submit).
2. Buat repo GitHub BARU `news-image-20261120` — PERHATIAN: repo v2
   sudah ada di oraybora-source (commit a919aab2). v3 = submit ulang
   (Force_Last) ke repo yang SAMA atau repo baru? Aturan: repo dibuat
   setelah 20 Nov 00:00 UTC (repo v2 memenuhi); entry v3 adalah
   snapshot baru di repo yang sama — parent yang putuskan (cek
   `makefun status` + aturan Force_Last: submit terakhir = final).
   Bila repo baru: publik, dibuat setelah 20 Nov 00:00 UTC, About:
   website make.fun + topik makefun.
3. Commit + push repo-v3 (tambah `.makefun/owner.json` wallet payout).
4. Bundle transkrip (`makefun bundle`, dari parent setelah semua
   subagent selesai) + `makefun check --transcripts`.
5. **Submit LEBIH AWAL** (pelajaran ni19) — begitu Kevin Gas, jangan
   tunda. Deadline Min 22 Nov 2026 07:00 WIB. Kuota sesudah submit v2:
   entries_made 1, day left 2, can_submit true.
6. Update cron score-watch ni20 (saat ini menonton v2) ke submission
   v3 bila v3 di-submit; jangan buat cron baru.
7. Proxy duel v3 vs top-5 ni20 (oleh parent, setelah keputusan
   OpenRouter Kevin — 402 masih blokir).

## Estimasi token build

~90.000 token [ESTIMASI] (port compose + tes wrap + 2x compose ulang
+ crosscheck visual 18 panel + band + footer + 360px; belum termasuk
token parent).
