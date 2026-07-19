# PDF Extraction and Full-Text QC Workflow

Use this workflow before turning PDF-derived text, Zotero full text, OCR output, or downloaded publisher PDFs into thesis/paper evidence.

## Source Priority

1. Prefer original local PDF or publisher HTML when available.
2. Use Zotero `zotero_fulltext` as a discovery/preview layer unless it returns a clean Markdown/TXT source.
3. Treat Zotero indexed full text as lower confidence: it may contain OCR artifacts, translated text, broken formulas, missing tables, or lost figure context.
4. Do not use a translated PDF attachment as the primary evidence source unless the user explicitly asks for that translation.

## Windows / PowerShell Guardrails

- Do not use Bash heredoc syntax such as `python - <<'PY'` in PowerShell.
- Prefer helper scripts created with `apply_patch`, then run them with Python.
- Set UTF-8 for extraction/validation commands:

```powershell
$env:PYTHONIOENCODING='utf-8'
$env:PYTHONUTF8='1'
```

- Use `pathlib.Path(r"...")` or raw strings for Windows paths, especially paths containing Chinese characters.

## Extraction QC

- PyMuPDF warnings such as `No common ancestor in structure tree` are nonfatal if pages, text blocks, and figure assets are produced; record them in notes.
- Mark formulas, Greek letters, superscripts, primes, and table-heavy blocks as low-confidence when extracted text shows replacement characters or broken symbols.
- Validate JSON/source maps with Python `json.loads`, not only PowerShell `ConvertFrom-Json`.
- Verify every `assets/...` path before citing or inserting figures.
- For thesis writing, cite PDF-derived claims only after identifying page/block/table/figure evidence anchors.

## Writing Use Rule

Before inserting a citation or writing a literature-supported claim from extracted PDF text, confirm:

- `source`: original PDF, publisher HTML, Markdown/TXT OCR, Zotero index, or translated attachment;
- `evidence anchor`: page, section, figure/table, or block ID;
- `confidence`: high, medium, or low;
- `claim support`: what exact sentence or design/method point the source supports;
- `manual check needed`: formulas, equations, tables, or figure crops that require PDF-level verification.

If confidence is low, write the point as `待核全文` or place it under `需补充或确认` instead of treating it as citation support.

