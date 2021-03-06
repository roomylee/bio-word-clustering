import gensim
import os


class WordVector:
    def __init__(self, word, train_corpus=None, dim=100):
        # train_corpus is not None -> Train Again
        self.dim = dim
        self.word = word
        self.model = self.build_model(train_corpus)
        self.vector = self.model[self.word]

    def build_model(self, corpus):
        if corpus is None:
            try:
                print("Loading a pre-trained model...")
                model = gensim.models.Word2Vec.load(os.path.dirname(__file__)+"/model/bio_word2vec_%d_dim.model" % self.dim)
                print("Load success!")
            except Exception:
                raise
        else:
            print("Training a word2vec model Again...")
            model = self.train(corpus)
            print("Training success!")

        return model

    def train(self, corpus):
        print('Train Data Size :', len(corpus))
        model = gensim.models.Word2Vec(corpus, min_count=1, size=self.dim)
        model.save(os.path.dirname(__file__)+"/model/bio_word2vec_%d_dim.model" % self.dim)

        return model

    def reset_word(self, new_word):
        self.word = new_word
        self.vector = self.model[self.word]


if __name__ == '__main__':
    # word = ['happy']
    # corpus = [['I','am','happy']]
    # wv = WordVector(word, corpus)
    import data_helper
    _, _, relation = data_helper.get_triplet()
    corpus = data_helper.get_corpus()
    wv = WordVector(relation, corpus, dim=3)

    print(wv.word)
    print(wv.vector)