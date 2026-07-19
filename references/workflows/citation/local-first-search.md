# Local-First Search

Use this guide to find candidate literature for citation support. The search order is designed to protect thesis/paper claims from weak web-only references.

## Search Order

### 1. User-Provided Sources

Check first:

- references pasted by the user;
- the current draft's existing citation markers;
- provided reference lists, DOI lists, EndNote/RIS/BibTeX/Zotero exports, or thesis bibliographies;
- source files, notes, Word comments, analysis reports, and existing citation maps in the project.

Reuse existing numbering when it is already stable and clearly matched. Otherwise assign temporary `[R#]` markers.

### 2. Local Literature And Zotero-Like Library

Search likely local sources with `rg` before web search. Typical locations include:

- `doc_text.txt`;
- local RDF exports;
- `analysis/*参考文献*.md`;
- `analysis/*引文*.md`;
- `analysis/*证据*.md`;
- `analysis/library_abstract_summaries.json`;
- `files/`;
- `research_rag/data/files/`;
- Zotero storage full-text `.txt` files when available.

Use targeted Chinese and English keywords. For technical topics, search object, method, variable, output indicator, and synonym clusters rather than only the broad topic.

If Zotero MCP/API is available, query title, author, DOI, abstract, attachment path, tags, and full-text snippets. If unavailable, inspect local RDF, extracted full text, file names, and local notes directly.

For corpus-level learning before major writing, use:

- [../zotero-library-learning.md](../zotero-library-learning.md);
- [../zotero-fulltext-corpus-workflow.md](../zotero-fulltext-corpus-workflow.md).

### 3. InstSci Or Publisher Access

Use [../instsci-paper-retrieval-workflow.md](../instsci-paper-retrieval-workflow.md) when:

- a high-value DOI/title is known but full text is missing;
- publisher access needs visible-browser verification;
- target-journal exemplars must be acquired;
- closed-access status must be documented.

Keep access evidence separate from citation support. A successful retrieval only means the source can be inspected; it does not prove the sentence.

### 4. Web Search Fallback

Use web search only when:

- fewer than two strong local sources support an important background or research-status paragraph;
- local sources are too old, too weak, or outside the needed parameter range;
- DOI, journal, year, official metadata, or standard/code status must be verified;
- the user asks for newer or broader references.

For technical academic claims, prefer:

1. standards/codes or official specification pages for normative statements;
2. publisher pages, DOI metadata, CrossRef, OpenAlex, Semantic Scholar, or official repositories for bibliographic verification;
3. high-relevance review papers for field background;
4. original experimental, FE, analytical, or ML papers for specific technical claims.

Do not use ordinary web pages as scholarly support unless they are official standards, official datasets, official software documentation, or publisher pages.

## Search Record

When web, API, InstSci, or database search is used, record:

- source/tool;
- query terms and filters;
- date if recency matters;
- number of records reviewed when practical;
- selected DOI/URL/path;
- access status;
- evidence status: full-text checked, abstract-only, metadata-only, snippet-only, or official-document based.

This record can be compact in the final answer, but it must exist in the working notes or candidate table when citations are inserted.

## Stop Conditions

Stop searching when:

- each citable claim has at least one strong or clearly sufficient source;
- additional sources only duplicate the same support;
- the claim is actually unsupported and should be downgraded;
- the missing source requires user-provided access, a standard/code, or full-text confirmation beyond the current task.

Do not continue web searching merely to increase citation count.
