"""Run inside the final notebook environment if you want table export logic as a script reference.

The authoritative export code is also present as the final table-export cell
in FinalProject.ipynb.
"""

from pathlib import Path


def export_tables(namespace):
    table_dir = Path("tables")
    table_dir.mkdir(exist_ok=True)

    tables_to_export = {
        "LIB": "LIB.csv",
        "CORPUS": "CORPUS.csv",
        "VOCAB": "VOCAB.csv",
        "BOW": "BOW.csv",
        "BOW_DOC": "BOW_DOC.csv",
        "BOW_UNIT": "BOW_UNIT.csv",
        "BOW_PARA": "BOW_PARA.csv",
        "BOW_SENT": "BOW_SENT.csv",
        "DTCM": "DTCM.csv",
        "DTM": "DTM.csv",
        "TFIDF": "TFIDF.csv",
        "TFIDF_REDUCED": "TFIDF_REDUCED.csv",
        "TFIDF_L2": "TFIDF_L2.csv",
        "SIGS": "SIGS.csv",
        "PCA_COMPONENTS": "PCA_COMPONENTS.csv",
        "DCM": "DCM.csv",
        "LOADINGS": "LOADINGS.csv",
        "TOPICS": "TOPICS.csv",
        "THETA": "THETA.csv",
        "PHI": "PHI.csv",
        "TCM": "TCM.csv",
        "VOCAB_SENT": "VOCAB_SENT.csv",
        "BOW_SENT": "BOW_SENT_WEIGHTED.csv",
        "DOC_SENT": "DOC_SENT.csv",
        "DOC_SENT_DOC": "DOC_SENT_DOC.csv",
        "VOCAB_W2V": "VOCAB_W2V.csv",
        "TSNE": "TSNE.csv",
        "TSNE_CLUSTERS": "TSNE_CLUSTERS.csv",
        "TOPIC_YEAR": "TOPIC_YEAR.csv",
        "MAP_DF": "MAP_DF.csv",
        "COUNTRY_SENT_NORM": "COUNTRY_SENT_NORM.csv",
    }

    exported = []
    for table_name, file_name in tables_to_export.items():
        if table_name in namespace:
            obj = namespace[table_name]
            if hasattr(obj, "to_csv"):
                obj.to_csv(table_dir / file_name)
                exported.append(file_name)
    return exported

