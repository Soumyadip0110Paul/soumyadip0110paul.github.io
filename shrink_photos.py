"""
Shrink photos before uploading so the website loads fast.

Phone/camera photos are usually 4-10 MB each. This resizes every image in a
folder (and its subfolders) to max 1800 px on the long side and saves it as
an optimized JPEG of ~300-600 KB. Originals are moved to a backup folder.

Setup (once):   pip install pillow
Usage:          python shrink_photos.py images/treks
                python shrink_photos.py images/papers
"""
import sys, shutil
from pathlib import Path
from PIL import Image, ImageOps

MAX_SIDE = 1800
QUALITY = 82
EXTS = {".jpg", ".jpeg", ".png", ".webp", ".heic"}

def main(folder):
    root = Path(folder)
    backup = root.parent / (root.name + "_originals")
    count = 0
    for path in sorted(root.rglob("*")):
        if path.suffix.lower() not in EXTS or not path.is_file():
            continue
        try:
            img = ImageOps.exif_transpose(Image.open(path))  # fix phone rotation
        except Exception as e:
            print(f"skip {path}: {e}")
            continue
        rel = path.relative_to(root)
        (backup / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, backup / rel)

        img.thumbnail((MAX_SIDE, MAX_SIDE))
        is_figure = "papers" in path.parts and path.suffix.lower() == ".png"
        if is_figure:
            img.save(path, optimize=True)          # keep PNG for sharp plots/diagrams
            out = path
        else:
            out = path.with_suffix(".jpg")
            img.convert("RGB").save(out, "JPEG", quality=QUALITY, optimize=True, progressive=True)
            if out != path:
                path.unlink()
        print(f"ok  {rel}  ->  {out.stat().st_size // 1024} KB")
        count += 1
    print(f"\nDone: {count} images. Originals backed up in {backup} (don't upload that folder).")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__); sys.exit(1)
    main(sys.argv[1])
