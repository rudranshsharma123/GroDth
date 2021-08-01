  
import os

model = "sentence-transformers/msmarco-distilbert-base-v3"
top_k = 1

port = 12345
workspace_dir = os.path.join(os.path.abspath('workspace'))
datafile = os.path.abspath(os.path.dirname(__file__) + "/./data/smol.csv")
encoder = 'jinahub://TransformerTorchEncoder'

max_docs = 656