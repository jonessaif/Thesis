from gensim.models import Word2Vec
model = Word2Vec.load("word2vec.model")
model.wv.save_word2vec_format('test_w2v.txt', binary=False)
