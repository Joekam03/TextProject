# DS 5001 Final Project

This repository contains a digital analytical edition of a corpus of national constitutions.

## Main Files

- `FinalProject.ipynb` is the complete final notebook.
- `docs/FinalProject_no_code.ipynb` is a PDF-export copy with code cells hidden in metadata.
- `sections/` contains runnable section notebooks split by project part.
- `tables/` is the output folder for generated CSV tables.
- `Plot images/` contains generated plot images and interactive map HTML files.
- `lexicons/` contains the sentiment lexicon files used by the sentiment analysis.

## Run Order

Run `FinalProject.ipynb` from top to bottom. The final export cell writes generated tables to `tables/`.

To refresh section notebooks, rerun the corresponding notebook in `sections/`. Later section notebooks include earlier setup code so they can run independently.

## PDF Export

Use `docs/FinalProject_no_code.ipynb` for PDF export if you want a version with code hidden and markdown/images/tables visible.

If exporting manually from JupyterLab:

1. Open `docs/FinalProject_no_code.ipynb`.
2. Run all cells if needed.
3. Export to PDF or HTML/PDF with code input hidden.

## Dependencies

Install dependencies with:

```bash
pip install -r requirements.txt
```
