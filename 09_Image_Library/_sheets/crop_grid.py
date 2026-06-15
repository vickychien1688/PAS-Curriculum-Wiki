#!/usr/bin/env python3
"""Crop a generated grid image into individual square icons.

Method: split into R row-bands (y-projection of content), then within each band
split into C column-bands (x-projection). For each cell, tight-crop to content,
pad to a centered square with a small margin, resize, and save color + bw.

Usage:
  crop_grid.py <input.png> <rows> <cols> <out_dir> <name1,name2,...>
Names are row-major. Use "skip" for an intentionally blank cell.
"""
import sys, os
from PIL import Image
import numpy as np

WHITE_THR = 244      # pixel considered "white/background" if all channels >= this
MIN_CONTENT = 0.002  # min fraction of dark pixels for a band/cell to count as content
OUT_SIZE = 300
MARGIN = 0.08        # white margin around content when squaring

def content_mask(arr):
    # arr: HxWx3 ; True where non-white (ink/color present)
    return (arr[:, :, :3].min(axis=2) < WHITE_THR)

def bands(profile, n, min_run_frac=0.04):
    """Given a 1-D boolean content profile, return n (start,end) content bands
    by splitting at the n-1 widest gaps. Robust to uneven icon sizes."""
    L = len(profile)
    # find indices that have content
    idx = np.where(profile)[0]
    if len(idx) == 0:
        # fall back to even split
        step = L / n
        return [(int(i*step), int((i+1)*step)) for i in range(n)]
    # build runs of content
    runs = []
    s = idx[0]; prev = idx[0]
    for i in idx[1:]:
        if i == prev + 1:
            prev = i
        else:
            runs.append((s, prev)); s = i; prev = i
    runs.append((s, prev))
    # merge tiny runs into neighbours by gap size: we want exactly n bands.
    # Strategy: compute gaps between consecutive runs; keep splitting only at the
    # largest gaps so we end with n groups.
    if len(runs) <= n:
        groups = [[r] for r in runs]
    else:
        gaps = []
        for i in range(len(runs)-1):
            gaps.append((runs[i+1][0] - runs[i][1], i))  # (gap_size, after_run_i)
        gaps.sort(reverse=True)
        split_after = sorted(g[1] for g in gaps[:n-1])
        groups = []
        cur = [runs[0]]
        si = 0
        for i in range(len(runs)-1):
            if si < len(split_after) and i == split_after[si]:
                groups.append(cur); cur = [runs[i+1]]; si += 1
            else:
                cur.append(runs[i+1])
        groups.append(cur)
    out = []
    for g in groups:
        out.append((g[0][0], g[-1][1]))
    # pad to n if needed
    while len(out) < n:
        out.append(out[-1])
    return out[:n]

def tight_square(cell_arr):
    """Return PIL square image (color) tightly cropped + padded, or None if empty."""
    m = content_mask(cell_arr)
    if m.mean() < MIN_CONTENT:
        return None
    ys, xs = np.where(m)
    y0, y1, x0, x1 = ys.min(), ys.max()+1, xs.min(), xs.max()+1
    crop = cell_arr[y0:y1, x0:x1, :3]
    h, w = crop.shape[:2]
    side = int(max(h, w) * (1 + 2*MARGIN))
    sq = np.full((side, side, 3), 255, np.uint8)
    oy = (side - h)//2; ox = (side - w)//2
    sq[oy:oy+h, ox:ox+w] = crop
    img = Image.fromarray(sq, "RGB").resize((OUT_SIZE, OUT_SIZE), Image.LANCZOS)
    return img

def main():
    inp, rows, cols, out_dir, names = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], sys.argv[5]
    names = names.split(",")
    os.makedirs(out_dir, exist_ok=True)
    im = Image.open(inp).convert("RGB")
    arr = np.asarray(im)
    H, W = arr.shape[:2]
    m = content_mask(arr)
    row_prof = m.sum(axis=1) > (W * 0.004)
    rbands = bands(row_prof, rows)
    cells = []
    for (ry0, ry1) in rbands:
        sub = m[ry0:ry1, :]
        col_prof = sub.sum(axis=0) > (sub.shape[0] * 0.004)
        cbands = bands(col_prof, cols)
        for (cx0, cx1) in cbands:
            cells.append((ry0, ry1, cx0, cx1))
    saved = []
    for i, (ry0, ry1, cx0, cx1) in enumerate(cells):
        if i >= len(names): break
        name = names[i].strip()
        if name == "skip" or name == "":
            continue
        # add a little context padding around the detected band before tight crop
        pad = 6
        yy0, yy1 = max(0, ry0-pad), min(H, ry1+pad)
        xx0, xx1 = max(0, cx0-pad), min(W, cx1+pad)
        cell = arr[yy0:yy1, xx0:xx1]
        sq = tight_square(cell)
        if sq is None:
            print(f"  [skip-empty] cell {i} ({name})")
            continue
        cpath = os.path.join(out_dir, f"{name}-v1-color.png")
        bpath = os.path.join(out_dir, f"{name}-v1-bw.png")
        sq.save(cpath)
        sq.convert("L").save(bpath)
        saved.append(name)
    print("SAVED:", saved)

if __name__ == "__main__":
    main()
