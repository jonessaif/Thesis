# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:27:47 2020

@author: Ratnesh
"""

# import gensim.downloader as api
# from sklearn.decomposition import PCA
# from matplotlib import pyplot

from gensim.models.word2vec import Word2Vec
import codecs
import numpy
model = Word2Vec.load('word2vec.model')

def load_word_vectors(file_destination, primary_language="hindi"):
    """
    This method loads the word vectors from the supplied file destination.
    It loads the dictionary of word vectors and prints its size and the vector dimensionality.
    """
    #print "XAVIER - returning null dictionary"
    #return {}

    print("Loading pretrained word vectors from", file_destination, "- treating", primary_language, "as the primary language.")
    word_dictionary = {}

    lp = {}
    lp["english"] = u"en_"
    lp["german"] = u"de_"
    lp["italian"] = u"it_"
    lp["russian"] = u"ru_"
    lp["sh"] = u"sh_"
    lp["bulgarian"] = u"bg_"
    lp["polish"] = u"pl_"
    lp["spanish"] = u"es_"
    lp["french"] = u"fr_"
    lp["portuguese"] = u"pt_"
    lp["swedish"] = u"sv_"
    lp["dutch"] = u"nl_"
    lp["hindi"] = u"hi_"

    language_key = lp[primary_language]

    f = codecs.open(file_destination, 'r', 'utf-8')

    for line in f:
        line = line.split(" ", 1)
        transformed_key = line[0].lower()



        word_dictionary[transformed_key] = numpy.fromstring(line[1], dtype="float32", sep=" ")

        if word_dictionary[transformed_key].shape[0] != 300:
            print(transformed_key, word_dictionary[transformed_key].shape)

    print(len(word_dictionary), "vectors loaded from", file_destination)

    # return normalise_word_vectors(word_dictionary)

fp = "vectors_w2v.txt"
load_word_vectors(fp,"hindi")