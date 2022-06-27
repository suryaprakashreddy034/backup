import pandas as pd
from pandas.io import gbq

project_id='gcptraining-321605'


query="""SELECT * FROM `gcptraining-321605.gcp_bigquerytraining.personal`"""

set1=gbq.read_gbq(query,project_id)

print(set1)