import nltk
import json

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from . import Phrases
from . import Classifier, classificador, palavrastreinamento, classifier

@api_view(['POST', ])
def sending_string(request):
    
    if request.method == 'POST':
        try:
            recieved_json_data = json.loads(request.body)
            testestemming = []
            stemmer = nltk.stem.RSLPStemmer()

            for (palavrastreinamento) in recieved_json_data['text'].split():
                comstem = [p for p in palavrastreinamento.split()]
                testestemming.append(str(stemmer.stem(comstem[0])))
            
            novo = classifier.extratorpalavras(testestemming)

            recieved_json_data['class'] = ((str(classificador.classify(novo))))
        
        except:
            recieved_json_data = ''
        
        if recieved_json_data != '':
            return Response(recieved_json_data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
