# Soumyadip Paul — personal website

## Folder layout

```
index.html                      the website
Soumyadip_Paul_CV_.pdf          CV (linked from the top bar)
.nojekyll                       tells GitHub Pages to serve files as-is
shrink_photos.py                optional: makes photos small before upload
images/
  profile.jpg                   ← ADD your profile photo with this exact name
  treks/
    sandakphu-2024/             ← one folder per trek, any number of photos
    kedarkantha-2023/
    <any-new-trek>/
  papers/
    ris-phase-opt/              ← figures for each paper
    wslr-qaoa-mimo/
    ciacon-nlp/
    hqaoa-blockchain/
    vlsi-thermal/
    qhf-blockchain/
    rcs-blockchain/
```

The two trek folders are examples. Rename them to your real treks or delete them.
Empty folders are ignored on the site, so it's fine to leave them.

## Adding trek photos

1. Make a folder for the trek inside `images/treks/`, e.g. `images/treks/sandakphu-2024/`.
   The folder name becomes the filter button: `sandakphu-2024` → "Sandakphu 2024".
2. Drop in as many photos as you like.
3. (Recommended) shrink them: `python shrink_photos.py images/treks`
4. Upload / push to GitHub. The photos appear automatically — no code changes.

Each trek gets its own filter button, and photos load 12 at a time with a
"Show more photos" button, so 200+ photos is fine.

**Captions** come from file names: `summit-at-sunrise.jpg` → "Summit at sunrise".
Add numbers to control order: `01-base-camp.jpg`, `02-summit.jpg` (numbers are hidden).
Phone names like `IMG_2041.jpg` work too; they'll just have plain captions.

## Adding paper figures

Put images into the paper's folder, e.g. `images/papers/wslr-qaoa-mimo/01-system-model.png`.
They show as clickable thumbnails in that paper's card.
Tip: export figures as PNG for sharp plots.

To add a new paper, add an entry to the `publications` list in `index.html`
and create `images/papers/<its id>/`.

## File name rules

- Use lowercase letters, numbers and hyphens: `rupin-pass-2025.jpg` ✓
- Avoid spaces and brackets: `WhatsApp Image (2).jpeg` ✗
- Allowed types: .jpg .jpeg .png .webp .gif .avif .svg
  (iPhone .HEIC isn't shown by browsers — `shrink_photos.py` converts it to .jpg)

## Uploading to GitHub Pages

Repo: `soumyadip0110paul.github.io`, branch `main`.

- Website: open the repo → Add file → Upload files → drag the whole folder
  contents (keep the `images/` structure) → Commit.
- Command line: `git add . && git commit -m "Update site" && git push`

Changes are live in 1–2 minutes. Images are listed using GitHub's API; if
your repo or branch name differs, edit the `GITHUB` block at the top of the
script in `index.html`.

Don't upload `*_originals/` folders created by the shrink script.
Keep the repo under ~1 GB (GitHub Pages limit) — shrinking photos helps a lot.
