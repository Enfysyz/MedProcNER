# MEDPROCNER TRAIN SET README

## What is MEDPROCNER

MedProcNER stands for MEDical PROCedure Named Entity Recognition. It is a shared task and set of resources focused on the detection, normalization and indexing of clinical procedures in medical documents in Spanish. MedProcNER is complementary to the DisTEMIST corpus (https://temu.bsc.es/distemist) as they both use the same document collection, which is why it's also called ProcTEMIST.

This repository includes the Train Set of the task's Subtask 1, which includes a total of 750 documents. Training data for subtask 2 and 3 will be released later on.

MedProcNER was developed by the Barcelona Supercomputing Center's NLP for Biomedical Information Analysis and used as part of BioASQ @ CLEF 2023. For more information on the corpus, annotation scheme and task in general, please visit: https://temu.bsc.es/medprocner.

## Folder Structure

The MedProcNER corpus is offered in two different formats, each separated in a different folder. The text files are also offered individually. All in all, the folder structure is:

- `brat/`

Includes the brat .ann files together with the .txt files (`brat/medprocner_brat_train_subtask1`).

For more information on brat's format please visit: https://brat.nlplab.org/standoff.html

- `tsv/`

This folder includes tab-separated files (tsv) where each line represents an annotation. The file `medprocner_tsv_train_subtask1.tsv` includes the data for Subtask 1 with the following columns: "filename", "ann_id", "label", "start_span", "end_span" and "text".

- `txt/`

These are the standalone text files.

## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

## Contact

If you have any questions or suggestions, please contact us at:

- Salvador Lima-López (<salvador [dot] limalopez [at] gmail [dot] com>)
- Martin Krallinger (<krallinger [dot] martin [at] gmail [dot] com>)
