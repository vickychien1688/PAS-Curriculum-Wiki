# Extraction Notes

## Source Priority

- EOW official scope: Google Drive teacher manuals and exported PDFs.
- Reading Base: Canva master designs.
- Grammar Box: Canva master designs.
- Worksheet style: Dropbox preferred examples, supported by Canva layout examples.

Do not treat exported Reading Base or Grammar Box PDFs as final if Canva disagrees.

This folder is reserved for future helper scripts and extraction logs.

Current extraction was done with the bundled Codex runtime:

- Python: `/Users/chienhsiuting/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3`
- PDF metadata/rendering: `/Users/chienhsiuting/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/pdfinfo`, `pdftoppm`

Potential next helper:

```text
extract_pdf_outline.py
```

Purpose:

- extract text with `pypdf`
- normalize letter-spaced Canva PDF text
- render image-only PDFs for OCR/manual review
