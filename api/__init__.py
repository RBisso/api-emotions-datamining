import nltk
import os
from . import words_db

#nltk.donwload('stopwords')
nltk.data.path.append(os.path.join(os.getcwd(),'nltk_data/'))

class Phrases():

    def __init__(self, **kwargs):
        for field in ('text', 'category'):
            setattr(self, field, kwargs.get(field, None))

class Classifier():

    basetreinamento = words_db.basetreinamento
    baseteste = words_db.baseteste

    stopwordsnltk = nltk.corpus.stopwords.words('portuguese')

    def aplicastemmer(self, texto):
        stemmer = nltk.stem.RSLPStemmer()
        frasessstemming = []
        for (palavras, emocao) in texto:
            comstemming = [str(stemmer.stem(p)) for p in palavras.split() if p not in self.stopwordsnltk]
            frasessstemming.append((comstemming, emocao))
        return frasessstemming

    def buscapalavras(self, frases):
        todaspalavras = []
        for (palavras, emocao) in frases:
            todaspalavras.extend(palavras)
        return todaspalavras

    def buscafrequencia(self, palavras):
        palavras = nltk.FreqDist(palavras)
        return palavras

    def buscapalavrasunicas(self, frequencia):
        freq = frequencia.keys()
        return freq

    def extratorpalavras(self, documento):
        doc = set(documento)
        caracteristicas = {}
        for palavras in palavrasunicastreinamento:
            caracteristicas['%s' % palavras] = (palavras in doc)
        return caracteristicas


classifier = Classifier()

frasescomstemmingtreinamento = classifier.aplicastemmer(classifier.basetreinamento)
frasescomstemmingteste = classifier.aplicastemmer(classifier.baseteste)

palavrastreinamento = classifier.buscapalavras(frasescomstemmingtreinamento)
palavrasteste = classifier.buscapalavras(frasescomstemmingteste)

frequenciatreinamento = classifier.buscafrequencia(palavrastreinamento)
frequenciateste = classifier.buscafrequencia(palavrasteste)

palavrasunicastreinamento = classifier.buscapalavrasunicas(frequenciatreinamento)
palavrasunicasteste = classifier.buscapalavrasunicas(frequenciateste)

basecompletatreinamento = nltk.classify.apply_features(classifier.extratorpalavras, frasescomstemmingtreinamento)
basecompletateste = nltk.classify.apply_features(classifier.extratorpalavras, frasescomstemmingteste)

classificador = nltk.NaiveBayesClassifier.train(basecompletatreinamento)