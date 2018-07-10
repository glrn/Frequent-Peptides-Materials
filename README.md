# Frequent Peptides Across the Tree of Life
Supplemental materials for TAU Thesis, including results, tables and graphs.

### Materials

- [_GOrilla_ results](materials/GOrilla results) of GO term enrichment for various target sets in Homo Sapiens, Drosophila Melanogaster, C. Elegans and Arabidopsis Thaliana.
- Visualization of [clusters of frequent short peptides](Frequent Short Peptides Clusters/Human) in human.
- [_WebGestalt_ results](materials/WebGestalt Results) for disease and pathway enrichment.
- [Lists of the most frequent short peptides across 28 species](materials/Most Frequent Short Peptides), before and after dilution of similar proteins, and the corresponding proteins.


### Thesis Abstract
In this work, we study Frequent Short Peptides (FSPs) in proteomes of species from across the Eukarya. Our definition of FSP captures peptides that are the most frequent among different proteins within the same species. Specifically, we are interested in short peptides of 10 amino acids. We show a considerable variance between the identities of FSPs of different species. For most species, the FSPs belong to a small set of homologous protein families, such as _zinc fingers_ and _olfactory receptors_ in humans.

We introduce a procedure for eliminating the over-representation of FSPs of homologous protein families, by using a sequence alignment algorithm to "dilute" similar proteins during the FSP counting process. This dilution procedure reveals a conspicuous presence of single amino-acid repeats (SAARs) and almost-SAARs among FSPs, especially in vertebrates.

An analysis of diluted groups of human proteins that contain FSPs reveals that many of them exhibit a significant Gene Ontology enrichment for terms related to regulation of RNA metabolism, regulation of DNA transcription, and nucleus components. A predominantly high enrichment level is observed for the 10-mers poly-alanine and poly-glutamine, which are among the most frequent peptides in human, and are also known to be correlated with neurodegenerative diseases and cancer.

Further analysis of diluted FSPs demonstrates that vertebrates, especially mammals, share many common frequent peptides, while invertebrates exhibit substantial dissimilarities between them. We use the diluted FSP sets to define a metric for distance between species, which provides a good quality clustering of vertebrates and other Eukaryotes, even when using only diluted FSPs that are not SAARs. Interestingly, a similar metric based on the non-diluted FSP sets does not correlate with phylogenetic proximity. The results hint an evolutionary mechanism through which the set of diluted FSPs was consolidated along the neurological complexity of species.


### Contact
Gal Ron, galr1@mail.tau.ac.il 
