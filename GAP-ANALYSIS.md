# Gap Analysis — news-image-20261120 v2 (sketsa 6 CALM)

**Tanggal:** 20 Nov 2026, ~14:00 WIB. **Dasar:** sketsa 6
(`sketches/sketch-ni20-v1r-6.png`, 4 hero 2x7 CALM, Kevin GAS 13:52 WIB)
dibandingkan rules-ledger.md + pelajaran ni19
(`analisis-kalah-di-mana-ni19.md`) + build v1 + checklist Kevin
(`design-revisions-kevin.md`, 28 butir). Isi cerita = pool 33 v1 yang
SUDAH terverifikasi; TIDAK ADA cerita baru, TIDAK ADA cerita 17–19 Nov
yang dihidupkan lagi.

## Ringkasan verdict

Dari 17 kekurangan yang dicari, **5 bisa diperbaiki di build ini**
(aset baru EU-UK + Brent, cek warna atas dengan aset AI asli, slice
kartu lebih tinggi, teks GTA diperjelas, ukuran file dioptimasi),
**8 sudah benar / tidak bisa diperbaiki tanpa merusak kriteria yang
lebih tinggi** (AMERICAS 2, AFRICA 0, Kyiv 2x, pin peta ter-skip,
contend, dsb. — dicatat jujur, bukan dipaksakan), dan **4 sudah
tertutup oleh desain sketsa 6** (peta dipertahankan, DATE CHECK tebal,
footer utuh, deck 5 cerita).

## Kekurangan + keputusan

### 1. AMERICAS 2/33 — TIDAK BISA diperbaiki di build ini
Kriteria 2 (breadth) menghukum wilayah tipis; ni19: "AFRICA 0" disebut
di 18/20 duel. Tapi riset pengganti + ATM 20 Nov tidak menemukan cerita
Amerika/Afrika Jumat yang kuat dan terverifikasi ("No strong verified
Americas story Friday"). Memaksakan cerita lemah/17–19 Nov akan
melanggar kriteria 1 (tanggal) dan 4 (faithful) — yang LEBIH TINGGI
secara leksikografis daripada breadth. Bukti penyeimbang: rank 2 ni19
(Afrika 2) tetap #2; rank 30 ni19 (Oceania 1) tetap top-30 — wilayah
tipis saja tidak menjatuhkan entri. **Mitigasi yang sudah ada:**
2 cerita Americas ditempatkan menonjol (kartu 7 Florida + brief 31
flood-watch); legenda peta tetap jujur menulis "AMERICAS 2".

### 2. AFRICA 0/33 — TIDAK BISA diperbaiki di build ini
Sama seperti #1. Tidak ada cerita Afrika Jumat yang terverifikasi
(Migrant/Dakar dan Kenya flood adalah 17–19 Nov — sudah dibuang di
ATM). **Tidak dipaksakan.** Legenda menulis "AFRICA 0" secara jujur
(seperti v1); menyembunyikan angka 0 justru berisiko dibaca juri
sebagai menyembunyikan kelemahan. Catatan ni19: rank 2 punya Afrika 2
dan tetap #2 — jadi 0 bukan vonis mati, tapi tetap kelemahan yang
dicatat.

### 3. Kyiv 2x (hero 4 + kartu 5) — TIDAK BISA dihapus, SUDAH dibedakan
Satu peristiwa (serangan rudal dini hari 01:25) muncul dua kali.
Menghapus salah satunya berarti membuang cerita Jumat terverifikasi
dan menurunkan total ke 32. **Mitigasi yang sudah ada:** hero = sudut
serangan ("Missiles hit Kyiv in the early hours", aset rudal malam);
kartu = sudut dampak/semalam ("Kyiv hit again overnight", aset
kebakaran kota). Judul dan ringkasan berbeda; peta hanya mem-pin Kyiv
sekali (duplikat di-skip). Risiko skor kecil, dicatat.

### 4. EU-UK + Brent naik jadi kartu — BUTUH ASET BARU (DIPERBAIKI)
Sketsa 6 mempromosikan 2 brief v1 (EU-UK #31, Brent #25) menjadi
kartu 17 dan 18. Aset AI keduanya BELUM ADA (v1 hanya punya 16 aset:
4 hero + 12 kartu). **Perbaikan:** generate 2 aset baru gaya rumah
ni19 v13 (STYLE_GUIDE_v13.md) — EU-UK: aula summit Brussels, meja
panjang + lingkaran bintang emas; Brent: kapal tanker merah di laut
teal, matahari kuning. Dicek satu per satu di ukuran tampil sebelum
compose (maks 2x ulang per panel, aturan v13).

### 5. Urutan kartu dituning untuk warna motif Pillow, bukan aset AI
(DIPERBAIKI)
Urutan kartu sketsa 6 dipilih supaya warna ATAS tetangga beda ≥25
(diukur dari motif Pillow). Aset AI punya warna atas yang BERBEDA —
urutan itu belum tentu lolos dengan aset asli. **Perbaikan:**
hitung `check_top_colors` dari aset AI asli saat compose; bila ada
tabrakan (<25), pertama ubah `focus_y` panel itu (cara v3 — geser
slice vertikal), baru bila masih tabrakan tukar posisi dua kartu
bertetangga dan catat perubahannya di build-note-v2.md.

### 6. Slice gambar kartu tipis, subjek bisa terpotong di tepi bawah
(DIPERBAIKI SEBAGIAN)
Risiko v1 #3: truk pemadam Kyiv-fire dan jabat tangan APEC terpotong
sebagian di tepi bawah slice (kartu v1 cuma 110px, slice ~50px).
**Perbaikan:** geometri sketsa 6 memakai kartu 140px (bukan 110px) —
slice gambar jadi ~69px, memberi ruang lebih untuk subjek. Tetap
wajib cek visual per kartu: bila subjek masih terpotong, geser
`focus_y` (JANGAN zoom out — aturan Kevin #19).

### 7. "Metascore 99/150" di kartu GTA bisa dibaca 99 dari 150
(DIPERBAIKI)
Ringkasan calm sketsa 6: "Reviews open 12:00 PT. Metascore 99/150."
— juri bisa membaca "99/150" sebagai skor 99 dari 150, padahal
faktanya Metascore 99 dari 150 kritikus. **Perbaikan:** pakai
"Reviews open 12:00 PT. Metascore 99 (150 critics)." bila muat
2 baris di 8pt/lebar 139px (tes wrap saat compose); bila tidak muat,
"Metascore 99, 150 critics." — angka dan makna tidak berubah.

### 8. Ringkasan Google calm kehilangan sudut "Jakarta wants answers"
(DITERIMA, dicatat)
Calm: "19,000 channels removed. (Reuters)" — v1: "19,000 YouTube
channels removed; Indonesia wants answers." Teks v1 pecah 3 baris di
kartu 139px/8pt (tes wrap sketsa), jadi pemangkasan ini DIPAKSA oleh
ruang. Sudut Jakarta tetap ada di judul kartu ("Jakarta asks Google
to explain") dan angka 19,000 tetap. **Diterima.**

### 9. Ukuran file kalah tie-break (pelajaran ni19 v15) — DIPERBAIKI
v15 (448.016 byte) kalah tie-break dari entri seri 409.834 byte —
rank 199 vs 201. v1 ni20 515.586 byte (lebih besar lagi). Tie-break
hanya berlaku bila skor seri di playoff, tapi gratis untuk diperbaiki.
**Perbaikan:** simpan entry.png dengan `optimize=True` (PIL, tetap
deterministik — byte sama tiap run) dan cek ukuran akhir; bila masih
>450KB, catat sebagai sisa risiko, jangan korbankan keterbacaan.

### 10. Footer terpotong (cacat v15 ni19) — SUDAH TERTUTUP
Sketsa 6 sudah diverifikasi: tinta terbawah y=1006, margin 17px
(crop 60px terbawah 2x). Geometri final SAMA PERSIS dengan sketsa
(masthead 62, deck 40, timeline 44, strip 58, hero 175, kartu 140×2,
band 247, DATE CHECK 9pt 2 baris + sources 1 baris). **Tetap
diwajibkan:** assert `sources_bottom ≤ 1010` + crop 60px terbawah 2x
setelah compose — jangan percaya geometri saja.

### 11. Peta dunia — SUDAH TERTUTUP (dipertahankan)
Pelajaran ni19: 8/8 sampel top-50 punya peta; v15 tanpa peta.
Sketsa 6 PUNYA peta 400px kiri bawah + legenda region. **Tidak
diubah.** Pin yang ter-skip karena tumpang tindih (Kyiv, Taipei,
Shenzhen, Hong Kong, Brussels/Paris — sama seperti v1) diterima:
peta tetap terbaca, bintang emas Gopalpur tetap.

### 12. DATE CHECK — SUDAH TERTUTUP (tebal, spesifik)
10 item? Bukan — ni20 DATE CHECK menyebut 18 cerita 17–19 Nov yang
sengaja dibuang + klaim penutup. Teori "DATE CHECK tipis" sudah MATI
di ni19 (v15 10 item > rank 1 yang 9 item), tapi DATE CHECK tebal
tetap benar sebagai bukti kriteria 1+3+4. **Tidak diubah.**

### 13. Deck 5 berita terbesar — SUDAH TERTUTUP
Checklist Kevin #4 (deck 5 berita, bukan 3): deck v1/sketsa 6 sudah
memuat 5 cerita dalam 2 baris (Akvan, COP31, Nicholls, Asia markets,
Prabowo–Xi). **Tidak diubah.**

### 14. Bar "STORIES BY REGION" — SUDAH TERTUTUP (dihapus)
Checklist Kevin #3: bar hitungan region SUDAH tidak ada di v1/sketsa 6
— hitungan hanya di legenda kecil di bawah peta. **Tidak diubah.**

### 15. Kepadatan kata — BUKAN TUAS (teori mati di ni19)
v15 ~590 kata di tengah band top-5 ni19 (330–700). Sketsa 6 ~33
cerita, kata seorde v1. Jangan kejar lebih padat/jarang sebagai tuas
skor — fokus ke keterbacaan (judul/ringkasan ≤2 baris, assert di
compose). **Tidak diubah.**

### 16. Skor `contend` — TIDAK BISA diperbaiki dari build
v15 tidak punya contend (median +2,4 untuk yang punya); aturan
pemberiannya TIDAK TAHU; hipotesis terkuat = snapshot waktu (v15
dinilai paling akhir 06:14Z). **Satu-satunya tuas: submit LEBIH AWAL**
— urusan parent setelah Kevin Gas, bukan build. Dicatat di
build-note-v2.md sebagai pengingat submit.

### 17. Duel proxy masih blokir OpenRouter 402 — DI LUAR BUILD
v2 belum di-duel (sama seperti v1). Parent yang urus setelah build
+ keputusan Kevin soal kunci akun kedua vs top-up. **Bukan blocker
build.**

## Checklist Kevin 28 butir — status untuk v2

| # | Butir | Status v2 |
|---|---|---|
| 1–2 | 3 sketsa, kirim dulu baru build | SUDAH (6 sketsa, Kevin pilih #6) |
| 3 | Hapus bar STORIES BY REGION | SUDAH (hanya legenda peta) |
| 4 | Deck 5 berita | SUDAH |
| 5 | Deck tanpa awalan "N stories" | SUDAH |
| 6 | MORE STORIES rata atas-bawah, sejajar peta | SUDAH (geometri sketsa 6; cek visual) |
| 7 | Peta 400px rasio asli, tanpa gap laut | SUDAH (rs.draw_map seperti v1) |
| 8 | Tanpa divider strip–hero | SUDAH |
| 9 | Tanpa legenda pins di kotak peta | SUDAH |
| 10 | Peta full setinggi kotak | SUDAH (map_h = band_h − 18) |
| 11 | SATU gaya selaras | SUDAH (gaya rumah v13 + 2 aset baru sama) |
| 12 | Subjek BESAR, utuh, tengah | CEK PER KARTU (crosscheck 2x) |
| 13 | Gambar ikut komposisi sketsa; cek tiap kartu | CEK PER KARTU (crosscheck 2x) |
| 14 | Presiden tidak seram (kepala polos) | SUDAH (aset v1; aset baru: figur polos) |
| 15 | Bendera ~3:2, tidak gepeng | CEK (aset EU-UK baru) |
| 16–17 | GTA kota / Anthropic | TIDAK RELEVAN ni20 |
| 18 | Gambar jangan hambar, konteks kelihatan | CEK PER KARTU |
| 19 | Kepotong tepi → turunin elemen, jangan zoom out | ATURAN (focus_y) |
| 20 | Komposisi seimbang kiri-kanan | CEK VISUAL |
| 21 | Warna atas tetangga beda | CEK PROGRAMATIK (lihat #5) |
| 22 | Footer tanpa catatan produksi | SUDAH (DATE CHECK + sources saja) |
| 23 | Van Gogh dibuang | SUDAH |
| 24 | Beda dari build teman Kevin | SUDAH (frame R3-rev2 sendiri) |
| 25–26 | Reply = acuan gambar itu; hero = flat Pillow (koreksi lama) | — (sketsa 6 yang dipilih = acuan) |
| 27 | AI vs flat — Kevin pilih AI 13:05 WIB | SUDAH (build pakai aset AI) |
| 28 | Fokus 20 November saja | SUDAH (33 cerita murni 20 Nov) |

## Yang diperbaiki di build v2 (ringkas)

1. Generate aset AI EU-UK + Brent gaya rumah v13.
2. `check_top_colors` dari aset AI asli; perbaiki via `focus_y` dulu.
3. Kartu 140px → slice ~69px (lebih lega dari v1).
4. GTA: "Metascore 99 (150 critics)." bila muat, kalau tidak
   "Metascore 99, 150 critics."
5. Simpan PNG `optimize=True`; laporkan ukuran akhir.
6. Assert footer + crop 60px terbawah 2x (wajib, bukan opsional).
7. Submit lebih awal (pengingat untuk parent — bukan langkah build).
