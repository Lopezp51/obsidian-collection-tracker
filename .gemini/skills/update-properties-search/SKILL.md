---
name: update-properties-search
description: Updates Markdown file properties to match 'Templates/PROPOSTA_PROPRIEDADES.md', preserving existing values and researching missing creative team info (Roteiro, Arte, Cores). Use this when a comic or manga note needs its properties standardized and filled with metadata.
---

# Update Properties Search

## Overview
This skill standardizes the YAML frontmatter of comic and manga notes in the Obsidian vault. it ensures that all notes follow the property order and list defined in `Templates/PROPOSTA_PROPRIEDADES.md`, while automatically searching for and filling in missing creative team information (Writer, Artist, Colorist).

## Workflow

1.  **Read Target File:** Load the content of the Markdown file to be updated.
2.  **Load Template:** Read `Templates/PROPOSTA_PROPRIEDADES.md` to get the master list of properties and their intended order.
3.  **Map Properties:**
    - Preserve existing values from the target file if the property names match.
    - If a property is in the template but missing from the target, add it (initially empty or with default).
    - If a property is in the target but NOT in the template, move it to the end or keep it if it's common (like `tags`).
4.  **Research Creative Team:**
    - Identify if `Roteiro`, `Arte`, or `Cores` are empty.
    - If any are empty, perform a `google_web_search` using the title of the work (and "equipe criativa" or "creative team") to find the names of the writer, artist, and colorist.
    - Fill these values in the target note's frontmatter.
5.  **Reorder & Update:** Reconstruct the frontmatter using the exact order from `Templates/PROPOSTA_PROPRIEDADES.md`.
6.  **Verify:** Ensure the resulting YAML is valid and the content remains intact.

## Guidelines
- **Property Order:** Strictly follow the order in `Templates/PROPOSTA_PROPRIEDADES.md`.
- **Formatting Lists:** Properties like `Coleção`, `Editora`, `Roteiro`, `Arte`, and `Cores` MUST be formatted as YAML lists (using bullet points `-`) instead of comma-separated strings.
  - **Individual Items:** NEVER group multiple people in a single list item. If a source mentions "John Doe and Jane Doe" or "John Doe, Jane Doe", they must be split into separate bullet points.
  - Example:
    ```yaml
    Cores:
      - Richard Horie
      - Tanya Horie
    ```
- **Search Strategy:** Use specific queries like `[Title] [Volume] [Editora] creative team comic` or `[Title] [Volume] equipe criativa quadrinho`.
- **Value Preservation:** Never overwrite a value that is already present unless specifically asked or if the value is clearly a placeholder (like `0` for evaluation if the user says otherwise).
- **Encoding and Character Integrity:** ALWAYS use UTF-8 encoding when reading and writing files. DO NOT modify or "correct" property names that contain accents or special characters (e.g., `Situação`, `Avaliação`, `Coleção`). These names must be preserved exactly as they appear in the template or original file to maintain compatibility with Obsidian and local scripts.
- **Default Values:** Use the defaults provided in the template (e.g., `Favorito: false`, `Avaliação: 0`).

## Example Search Query
If updating "Absolute Batman 04.md":
- `Absolute Batman 04 comic creative team`
- `Absolute Batman 04 roteiro arte cores`
