# HFUT Thesis Word Figure, Table, and Equation Objects

Use this guide when the controlling project is a Hefei University of Technology master's thesis Word document and the user has selected the author-confirmed local reference structure. It records the observed Word object structure for figures, tables, and equations; it is not a universal claim about every historical or future university template.

## Formatting-authority boundary

Apply this guide only after the formatting authority has been resolved. A current official template or explicit university requirement overrides this project-calibrated guide. If neither is available, describe these rules as the author-confirmed project convention rather than an institution-wide requirement. Use the local reference only for structure and style; do not copy its author, title, data, captions, or conclusions.

## Bilingual caption contract

- Use point-separated chapter numbering: `图 3.1`, `Fig 3.1`, `表 3.1`, `Tab 3.1`, and `(3.1)`. Do not silently convert these labels to hyphenated numbering, `Fig.`, `Figure`, `Table`, or another convention.
- Give the Chinese and English titles two separate Word paragraphs. A soft return inside one paragraph is not equivalent.
- Keep the same number in both language versions and keep in-text callouts synchronized with the visible number.
- When Chinese and English image versions are temporarily retained for later selection, keep them as two figure objects rather than a merged two-panel figure. Give each retained object a complete bilingual caption pair; a temporary version note does not replace either caption.

## Figure container contract

The observed figure object is one centered **2-row × 1-column** Word table:

1. The first row is the figure content row and contains the drawing or image.
2. The second row is the caption row and contains two separate centered paragraphs in the same cell: Chinese first, English second.

The wrapper may retain the Word table style `Table Grid`, but all borders explicitly set to `none`. Do not create a third row for the English caption. The observed captions follow forms such as `图 1.3  中文图题` and `Fig 1.3  English caption`, without a period after `Fig`.

For the calibrated reference, the Chinese caption paragraph uses style `图目录`, the English caption paragraph uses style `图表`, and both are centered, 10.5 pt, and single-spaced. The effective Chinese/Latin font pairing is 宋体/Times New Roman. Preserve the controlling template's existing style definitions instead of recreating styles from names alone.

Keep the two table rows together as one figure block. Preserve image aspect ratio and the existing anchoring behavior unless the task explicitly changes it.

## Table container contract

The observed table object is **not** enclosed with its captions in an outer wrapper table. Its document order is:

1. Chinese caption paragraph, for example `表 3.1  中文表题`, style `表目录`;
2. English caption paragraph, for example `Tab 3.1  English table title`, style `图表`;
3. the native Word data table, style `三线表`.

The data table is centered and occupies the available width (`w:tblW` percentage value `5000` in the calibrated reference). Cells are vertically centered. Caption and table text are effectively 10.5 pt with 宋体 for Chinese and Times New Roman for Latin text.

For the three-line border model, top and bottom borders use `w:sz="12"` (1.5 pt), and the header bottom border uses `w:sz="4"` (0.5 pt). Suppress vertical borders and other internal horizontal borders. Apply the header rule to the last header row when a multi-row header is used. Do not place captions in a merged first row, and do not add an outer container merely to bind captions to the table.

## Equation contract

Use a native OMML equation in one paragraph with Word style `公式`. The calibrated paragraph is centered with 1.15 line spacing; mathematical runs use Cambria Math.

Use one OMML **Equation Array** so the equation is centered and its number appears at the far right on the same line. The calibrated XML uses an equation-array alignment marker `#` followed by the parenthesized number object, producing a visible number such as `(2.1)`. Do not put a numbered equation in a one-row, three-column wrapper table, and do not position the number with repeated spaces or manual tab characters. Do not leave raw LaTeX in ordinary `w:t` runs.

In Chinese body text, cite the equation as `式（2.1）`. The prose callout uses Chinese full-width parentheses even though the displayed equation number is `(2.1)`.

## Structure validation

For every created or revised object, validate OOXML structure before relying on rendered appearance:

- **Figure:** confirm one 2-row × 1-column wrapper table, no visible borders, one figure-content row, and two caption paragraphs in the single caption cell.
- **Table:** confirm two preceding caption paragraphs, no outer wrapper, native style `三线表`, top/bottom `w:sz="12"`, header bottom `w:sz="4"`, and no vertical/internal body rules.
- **Equation:** confirm native OMML, paragraph style `公式`, an Equation Array with a right-side number, and no layout table or plain-text LaTeX substitute.
- **Captions/callouts:** confirm `图/Fig`, `表/Tab`, point-separated numbers, bilingual paragraph order, and body references such as `式（2.1）`.
- **Rendered result:** verify that images, titles, borders, equation alignment, and pagination match the controlling reference. For a single-section edit, inspect only the pages occupied by that section; use the broader DOCX audit workflow for global changes.

If the generator cannot reproduce a native object reliably, clone the corresponding object from the controlling template/reference and replace only the image, text, or OMML payload while preserving styles and container structure.
