import pandas as pd
from rest_framework.views import APIView
# Create your views here.
import numpy as np
import ssl
from rest_framework.response import Response


class JokesView(APIView):
    global jokelist
    ssl._create_default_https_context = ssl._create_unverified_context
    try:
        data = pd.read_csv(
            'https://gist.githubusercontent.com/chimpastic/e7917903f3b9fe385600d1968fa6161a/raw/773665e2b6ee09b3afca7c9d3273f8b08ba2e9e3/jokes.csv')
        jokelist = []
        for j in np.random.randint(38268, size=100):
            jokelist.append(
                [data.iloc[j][0], data.iloc[j][1], data.iloc[j][2]])
    except:
        jokelist["Sorry unable to connect"]

    def get(self, request):

        return Response({'jokes': jokelist})
