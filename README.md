# user2code2vec

Embeddings for Profiling Students Based on Distributional Representations of Source Code. 

Full research paper presented at Learning Analytics & Knowledge 2019 Conference in AZ, USA ([LAK 2019](https://lak19.solaresearch.org/))

Please consider [citing](data/citations/azcona2019user2code2vec.md) this paper if you use any of the work.

## Representations

* [Program Vectors][vectors]

## code2vec

* [BOW (bag-of-words) Part I][bow_first], [BOW Part II][bow_second]
* [Embeddings Part I][emb_f], [Embeddings Part II][emb_s]

## user2code2vec

* [user2code2vec][user2code2vec]

## Utils

* [Viz an AST][viz]: An abstract syntax tree (AST) is a tree representation of the abstract syntactic structure of source code written in a programming language. In Python, we leverage the ast module to process trees of the Python abstract syntax grammar. Visualizations are made using a great [notebook](https://github.com/hchasestevens/show_ast) developed by H. Chase Stevens.

* [BOW][emb_example]
* [Word Embeddings][emb_example]

[vectors]: notebooks/Program%20Vectors.ipynb
[bow_first]: notebooks/code2vec%20BOW.ipynb
[bow_second]: notebooks/code2vec%20BOW%20(Train%20%26%20Score).ipynb
[emb_f]: notebooks/code2vec%20Embeddings.ipynb
[emb_s]: notebooks/code2vec%20Embeddings%20II.ipynb
[user2code2vec]: notebooks/user2code2vec.ipynb
[viz]: notebooks/Visualize%20an%20AST.ipynb
[emb_example]: notebooks/Word%20Embeddings%20Example.ipynb
[bow_example]: notebooks/BOW%20Example.ipynb