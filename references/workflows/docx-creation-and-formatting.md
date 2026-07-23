# DOCX Creation and Chinese Academic Formatting

Use this workflow when the user asks to create a new Word manuscript, convert Markdown into `.docx`, or apply a Chinese academic formatting specification. For targeted changes to an existing Word file, also load [docx-ooxml-editing.md](docx-ooxml-editing.md).

This guide distills reusable workflow ideas from the external sources recorded in [external-skill-sources.md](../meta/external-skill-sources.md). It does not copy external scripts or establish a universal university format.

For the author-confirmed HFUT thesis Word project, load [hfut-thesis-word-objects.md](../style/hfut-thesis-word-objects.md) and use its observed figure, table, bilingual-caption, and numbered-equation structures. Do not replace those calibrated objects with generic academic defaults.

## Branch First: create / convert / revise

Classify the task before selecting tools:

| Branch | Typical input | Default action | Main risk |
|---|---|---|---|
| `create` | structured text, outline, data, figures, or template | generate a new `.docx` from a formatting contract | inferred formatting presented as official requirements |
| `convert` | Markdown plus figures, tables, citations, or LaTeX-like formulas | parse structure and map semantic objects into native Word objects | formulas, lists, captions, and fields degraded to plain text |
| `revise` | an existing `.docx` | preserve the original and edit a new copy using [docx-ooxml-editing.md](docx-ooxml-editing.md) | styles, fields, relationships, tracked changes, or rich objects damaged |

Do not rebuild an existing manuscript merely because generation is easier. Rebuilding is appropriate only when the user requests a clean regenerated version and accepts the formatting migration risk.

## Template precedence

Formatting authority is resolved in this order:

1. the user's supplied university, journal, competition, or institutional template;
2. explicit written formatting requirements supplied by the user;
3. styles already present in the source `.docx`;
4. a project-specific formatting specification confirmed for the task;
5. generic Chinese academic defaults used only as labeled fallback values.

Never describe a generic font, margin, caption, table, citation, or numbering rule as compliant with a specific institution unless that institution's current template has been checked.

## Formatting contract

Before generating or globally reformatting a document, establish the following contract. If a field is unknown and materially affects compliance, expose it as `待确认` rather than guessing.

| Object | Fields to lock |
|---|---|
| Page | paper size, orientation, margins, section breaks |
| Body text | Chinese and Latin fonts, size, alignment, first-line indent, line spacing, paragraph spacing |
| Headings | hierarchy, numbering, font, spacing, page-break behavior, TOC level |
| Lists | semantic numbering level, indentation, continuation/restart behavior |
| Figures | file, width, anchoring, caption position, numbering, source note |
| Tables | width, column proportions, alignment, border model, caption, continuation behavior |
| Equations | inline/block status, native Word equation requirement, numbering, punctuation |
| Citations | citation style, superscript/inline behavior, bibliography manager/field status |
| Front/back matter | title page, abstract, keywords, TOC, references, appendices, acknowledgements |
| Header/footer | content, section linkage, page-number style and starting page |

Keep this contract with the generated artifact or summarize it in the delivery report.

## Tool and representation choices

- For a new document, prefer a structured DOCX generator that creates paragraphs, styles, numbering, tables, relationships, and fields as Word objects.
- For Markdown conversion, parse headings, lists, tables, images, citations, and math semantically. Avoid regex-only conversion of the entire manuscript.
- For an existing document, prefer minimal OOXML changes or Word/LibreOffice-assisted edits under the existing safety workflow.
- Use Pandoc only when its mapping and reference document are controlled and the output is visually and structurally checked.
- Use Word or LibreOffice conversion as a validation or compatibility step, not as proof that academic formatting is correct.

Tool availability does not override the formatting contract. Record missing dependencies and any degraded representation in the final report.

## Academic object rules

### Headings and numbering

- Use Word styles and multilevel numbering rather than typing heading numbers into every paragraph.
- Confirm whether numbering restarts by chapter and whether front matter is numbered.
- Keep heading text separate from numbering definitions so the TOC and cross-references remain maintainable.
- Check mixed Chinese/Latin font behavior in numbered headings; do not assume one run font controls all generated numbering text.

### Lists

- Use Word numbering definitions for semantic lists; do not use literal Unicode bullets as a substitute for list structure.
- Preserve list level, indentation, restart/continue state, and spacing.
- Do not convert ordinary prose lines into lists solely because they begin with a number or symbol.

### Three-line tables

- Use a three-line table only when required by the applicable template or selected manuscript style.
- The usual structure is a top rule, a rule below the header, and a bottom rule, with other borders suppressed.
- Put the caption above or below the table according to the controlling template, not a generic convention.
- Validate column widths, units, decimal alignment, header hierarchy, row splitting, and page continuation separately from border appearance.
- Avoid simulated borders made from text characters or paragraph underlines.

### Figures and captions

- Insert images through document relationships and preserve aspect ratio.
- Use caption paragraphs or `SEQ` fields when automatic numbering and cross-references are required.
- Keep caption numbering, figure references, and the actual image set synchronized.
- Verify image resolution and legibility after rendering, especially for formulas, axis labels, and Chinese text.

### Equations

- If native Word equations are required, represent equations as OMML. A MathML-to-OMML route may be used when verified.
- Do not leave raw LaTeX in ordinary text runs and call it a Word equation.
- For numbered block equations, use a stable layout that centers the equation and right-aligns the number without visible table borders when a table-based layout is used.
- Detect inline math conservatively. Plain identifiers, years, units, or isolated numbers are not automatically equations.
- Preserve equation punctuation, symbol definitions, and cross-references.

### Citations and references

- Apply the citation and bibliography style required by the target institution or journal. GB/T 7714 is one possible requirement, not a universal default.
- Preserve bibliography fields or reference-manager links when present unless the user explicitly accepts conversion to static text.
- Superscript citation formatting must be confirmed against the template and must not change the citation content or range.

### TOC, fields, headers, and page numbers

- A generated TOC, caption number, cross-reference, or bibliography field may require a field refresh in Word before values appear correctly.
- Respect section breaks and header/footer linkage when page numbering changes between front matter and body text.
- Report fields that were created but not refreshed.

## Tracked changes and comments

- Detect tracked changes and comments before conversion or revision.
- Do not silently accept or reject revisions. Follow the user's explicit instruction.
- If a clean copy is requested, retain the original and record whether revisions were accepted through Word, LibreOffice, or another controlled process.
- Comments, footnotes, endnotes, bookmarks, and hyperlinks are rich objects; preserve them unless the scope explicitly includes them.

## Validation ladder

Apply the lowest sufficient level and escalate for formal submission files:

1. **Package integrity**: confirm the output is a readable ZIP-based `.docx` and required package parts/relationships exist.
2. **XML integrity**: parse modified XML; run schema or office-specific validation when available.
3. **Content integrity**: compare paragraph, table, figure, equation, caption, citation, and heading counts against the source or generation plan.
4. **Semantic spot checks**: extract representative headings, tables, equations, citations, and page-number settings.
5. **Rendering check**: render to PDF/images and inspect representative pages for overflow, border errors, blank objects, formula degradation, and pagination problems.
6. **Office round trip**: open/save with Microsoft Word or LibreOffice when compatibility matters, while noting that a successful open does not prove formatting compliance.
7. **Template compliance review**: compare the rendered artifact against the current institutional or journal specification.

For a thesis or submission manuscript, package/XML checks alone are insufficient. At least one rendering check and one visual spot check are expected.

## Delivery report

Report:

- output path and whether the source/original was preserved;
- selected branch: `create`, `convert`, or `revise`;
- formatting authority and unresolved contract fields;
- representation used for equations, captions, numbering, citations, and tables;
- validation levels completed and any tool unavailable;
- unrefreshed fields, tracked-change status, and remaining compatibility or compliance risks.
