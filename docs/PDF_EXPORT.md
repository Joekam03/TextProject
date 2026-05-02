# PDF Export Notes

Use `docs/FinalProject_no_code.ipynb` for the final PDF export.

The notebook has code-cell metadata tags for hidden inputs:

- `hide-input`
- `remove-input`
- `jupyter.source_hidden = true`

Recommended workflow:

1. Run `FinalProject.ipynb` from top to bottom.
2. Confirm the images in `Plot images/` and CSVs in `tables/` have been generated.
3. Open `docs/FinalProject_no_code.ipynb`.
4. Export to PDF from JupyterLab / VS Code with code inputs hidden.

If `nbconvert` is installed, try:

```bash
jupyter nbconvert docs/FinalProject_no_code.ipynb --to pdf --no-input --output FinalProject
```

If PDF export fails because LaTeX is missing, export to HTML first and print/save the HTML as PDF:

```bash
jupyter nbconvert docs/FinalProject_no_code.ipynb --to html --no-input --output FinalProject
```

