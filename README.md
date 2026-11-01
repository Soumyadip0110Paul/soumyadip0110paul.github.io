# Soumyadip Paul — personal website

## Folder layout

```
index.html                      the website
Soumyadip_Paul_CV_.pdf          CV (linked from the top bar)
.nojekyll                       tells GitHub Pages to serve files as-is
shrink_photos.py                optional: makes photos small before upload
update_photo_list.py            backup photo list (see below)
images/
  profile.jpg                   ← ADD your profile photo (profile.jpg / .jpeg / .png)
  photo-list.js                 backup list of photos, made by update_photo_list.py
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

Changes are live in 1–2 minutes. Press Ctrl+Shift+R (Cmd+Shift+R on Mac) to
reload without the browser's old copy.

The page works out which repository it's in from its own address, so the
repository can have any name. Only if you use a custom domain (not
*.github.io), fill in `GITHUB_OVERRIDE` near the top of the script.

## Backup photo list (recommended)

The page asks GitHub which photos are in each folder. GitHub allows each
visitor about 60 of these requests per hour, so as a backup, run this after
adding or removing photos and upload the result too:

    python update_photo_list.py

It updates `images/photo-list.js`. It's also needed if you preview the site by
double-clicking `index.html` on your computer, since the GitHub lookup only
works on the live site.

## Photos not showing? Check these

1. **Uploaded to the right place?** On github.com, open your repo and check you
   can click into `images` → `treks` → your trek folder → see the photos.
   `index.html` and the `images` folder must sit side by side.
2. **Names match exactly.** GitHub is case-sensitive: `images/Treks/` is not
   `images/treks/`. Keep folder names lowercase.
3. **Profile photo** must be inside `images/` and named `profile.jpg`,
   `profile.jpeg` or `profile.png`.
4. **Not .HEIC.** Browsers can't show iPhone HEIC files; run `shrink_photos.py`.
5. **Read the message on the page.** If the trek section can't load photos, it
   says why (e.g. which folder or repository it couldn't find).
6. **Previewing on your computer?** Run `python update_photo_list.py` first.
