# news-image-20261120 — build note v2 (sketsa 6 CALM)

Build: 20 Nov 2026 ~14:00–14:15 WIB. Kevin GAS sketsa 6 13:52 WIB
("Gas sketsa 6 — Analisis yang kurang, crosscheck, proxy").
**JANGAN submit — build saja, kirim hasil ke parent untuk dicek Kevin
dulu. Proxy duel oleh parent setelah build (OpenRouter 402 masih
blokir — keputusan kunci akun kedua vs top-up masih menunggu Kevin).**

## Hasil

- Repo: `~/workspace/makefun/news-image-20261120/repo-v2/` (BELUM commit,
  BELUM ada repo GitHub — dibuat saat submit, seperti v15/v1)
- `entry.png`: **491.710 byte, sha256
  `59567b28fd669d958f830d13066a744b68da96c96146986baf3a118a3961a6bd`**,
  1024×1024 RGB, ≤1 MiB ✓ (lebih kecil dari v1 515.586 byte —
  `optimize=True`)
- `compose_v2.py`: kode baru ditulis di sesi ini (frame sketsa 6 CALM,
  4 hero + 14 kartu + 15 brief = **33 cerita**)
- `main.py`: Python 3.13 stdlib only, copy entry.png ke output
- README.md (3 badge make.fun) + STORIES.md (33 cerita + sumber) +
  LICENSE (MIT) + entry-manifest.json + GAP-ANALYSIS.md
- Determinisme: compose 2× byte-identik, main.py 2× byte-identik
  (sha256 sama `59567b28…`)
- Pre-submit check kit (`makefun check --worktree`, kit ni20):
  **4 pass** (competition_open, snapshot, license_osi, entrypoint),
  **1 fail** (`transcripts_present` — transkrip di-bundle PARENT saat
  submit, bukan oleh build agent; sama seperti v13/v14r1/v15/v1 sebelum
  submit), 14 skip (transcript checks, tanpa sesi), 5 "at submission"
  (repo_public, repo_owner, repo_created_after_open, commit_in_repo,
  duplicate_snapshot — beres saat repo GitHub dibuat + push + submit)

## Yang berubah dari v1 (lihat GAP-ANALYSIS.md)

1. **Layout sketsa 6:** 4 hero + 14 kartu (2 baris × 7 kolom) + 15 brief.
   EU-UK + Brent NAIK dari brief jadi kartu 17–18.
2. **Aset AI baru (2):** EU-UK (aula summit Brussels, 7 pemimpin kepala
   polos, lingkaran bintang emas, bendera EU + Prancis) dan Brent
   (kapal tanker merah + kontainer + laut teal). Keduanya gaya rumah
   v13, dicek satu per satu sebelum compose — LOLOS, tanpa regenerasi.
   Brent dipotong 50% atas (langit krem) → file
   `media-generation-card-brent-oil-crop.webp`: tanpa crop, warna atas
   Brent (krem) tabrakan dengan EU-UK (krem) 18,9 < 25; setelah crop
   jarak 82,0.
3. **CALM (4 perbaikan Kevin):** strip panel NAVY semua; bilah bawah
   kartu angka EMAS; titik timeline EMAS isi + outline navy; nomor brief
   polos tanpa batang warna; sumber dilipat inline "(Reuters)" di akhir
   ringkasan (tanpa baris sumber terpisah).
4. **Kartu 140px (v1: 110px):** slice gambar ~69px (v1: ~50px) —
   subjek lebih lega; hero 175px, slice ~92px (COP31 108px karena
   judulnya 1 baris).
5. **GTA:** ringkasan jadi "Reviews open 12:00 PT. Metascore 99.
   (GeekRadar)" — "Metascore 99 (150 critics)" tidak muat 2 baris di
   8pt (tes wrap: 3 baris), dan "99/150" di sketsa bisa dibaca 99 dari
   150. Angka 99 tetap; "150 critics" hilang dari ringkasan (tetap
   tercatat di STORIES.md).
6. **PNG `optimize=True`:** 491.710 byte (v1: 515.586) — tie-break
   ukuran file (pelajaran v15: kalah tie-break dari entri seri yang
   lebih kecil).

## Crosscheck 2x (aturan Kevin 20 Nov 11:08 WIB)

**Crosscheck 1 — saat proses:**
- 2 ilustrasi AI baru dilihat SATU PER SATU sebelum compose. LOLOS
  (gaya rumah ni19 v13: kertas krem, outline navy tipis, blok warna
  datar, tanpa teks di gambar; subjek besar + utuh; pemimpin wajah
  polos). Tidak ada regenerasi.
- Top-color dihitung dari aset AI ASLI (bukan motif sketsa):
  satu-satunya tabrakan 17–18 (18,9) diperbaiki dengan crop Brent
  (lihat atas). Setelah compose: `top_bad` KOSONG (jarak minimum
  37,6 — hero 2–3; 40,5 — kartu 8–9).
- Semua judul ≤2 baris, semua ringkasan ≤2 baris, semua brief ≤3 baris
  (assert di compose_v2.py). Total 33 cerita (assert).

**Crosscheck 2 — setelah selesai:** entry.png dilihat penuh + crop
per-bagian (heroes, 2 baris kartu, band bawah) + crop 60px terbawah 2x:
- 18 panel: subjek utuh + terbaca. Catatan kecil (bukan cacat):
  ujung tongkat pemukul kriket hero 2 menyentuh tepi atas slice;
  meja krem kartu EU-UK menyatu dengan kertas di ukuran kecil
  (pemimpin + bintang + bendera tetap terbaca); papan "VI" kartu GTA
  tidak kentara di slice tipis (sama seperti v1 — aset + focus sama).
- Peta: 5 pin di-skip (log): Kyiv #5, Taipei #9, Shenzhen #14,
  Paris #24, Hong Kong #28 (tumpang tindih area padat — sama seperti
  v1). Bintang emas = Gopalpur. Legenda region utuh.
- Brief 19–33: semua terbaca, nomor polos tanpa batang warna,
  kolom rata dengan bawah peta.
- **Cek bawah 60px di 2x (pelajaran v15):** DATE CHECK 2 baris UTUH +
  baris "Sources: … Disputed claims are attributed, not stated as
  fact." UTUH sepenuhnya, margin kertas bersih 17px di bawahnya
  (sources_bottom 1007, assert ≤1010). Cacat v15 TIDAK terulang.

## Yang TIDAK berubah dari v1 (sengaja)

- Isi 33 cerita + angka + tanggal: SAMA (pool v1 terverifikasi).
  Tidak ada cerita baru, tidak ada cerita 17–19 Nov yang dihidupkan.
- Peta dunia dipertahankan (pelajaran ni19).
- DATE CHECK 18 item + klaim penutup; deck 5 cerita; strip 6 angka.
- AMERICAS 2/33, AFRICA 0/33, Kyiv 2x — tidak bisa diperbaiki tanpa
  merusak kriteria yang lebih tinggi (lihat GAP-ANALYSIS.md #1–3).

## Label klaim

- **TERVERIFIKASI:** semua angka/fakta di STORIES.md (sumber di sana);
  determinisme 2x; kit lint 4 pass / 1 fail (transcripts_present);
  top_bad kosong; footer utuh (crop 2x).
- **ESTIMASI:** target dev rank ≤150 (rules-ledger); tidak ada duel
  proxy (OpenRouter 402 masih blokir).
- **TIDAK TAHU:** isi presser Trump 12:00 ET; penutupan emas Jumat
  (dipakai intraday ~$3.520); hasil akhir COP31; aturan siapa dapat
  skor `contend` (hipotesis: snapshot waktu — v15 dinilai paling
  akhir 06:14Z).

## Yang tersisa untuk submit (oleh parent, SETELAH Kevin cek + Gas)

1. Kirim entry final v2 ke Kevin dulu (aturan: hasil dikirim sebelum
   minta Gas submit).
2. Buat repo GitHub BARU `news-image-20261120` di oraybora-source
   (publik, dibuat setelah 20 Nov 00:00 UTC), About: website make.fun
   + topik makefun.
3. Commit + push repo-v2 (tambah `.makefun/owner.json` wallet payout).
4. Bundle transkrip (`makefun bundle`, dari parent setelah semua
   subagent selesai) + `makefun check --transcripts`.
5. **Submit LEBIH AWAL** (pelajaran ni19: v15 dinilai paling akhir dan
   tidak dapat contend) — begitu Kevin Gas, jangan tunda. Deadline
   Min 22 Nov 2026 07:00 WIB.
6. Proxy duel v2 vs top-10 ni20 (oleh parent, setelah keputusan
   OpenRouter Kevin) + score-watch cron untuk ni20.

## Estimasi token build

~150.000 token [ESTIMASI] (2 generasi gambar + compose + audit +
crosscheck visual; belum termasuk token parent).
