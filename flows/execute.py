from jina import Executor, Document, DocumentArray, requests
import os
# from utils.helper import clean_string
# import numpy as np
# from typing import Tuple

top_k = 2

path = os.path.join(os.path.abspath('workspace/DiskIndexer/0/apps.json'))
class MyIndexer(Executor):
    """Simple indexer class"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._docs = DocumentArray()
        self.top_k = top_k
        if os.path.exists(self.save_path):
            self._docs = DocumentArray.load(self.save_path)
        else:
            self._docs = DocumentArray()

    @property
    def save_path(self):
        if not os.path.exists(self.workspace):
            os.makedirs(self.workspace)
        return os.path.join(self.workspace, "tags.json")

    def close(self):
        self._docs.save(self.save_path)

    @requests(on="/index")
    def index(self, docs: "DocumentArray", **kwargs):
        self._docs.extend(docs)
        return docs

    @requests(on="/search")
    def search(self, docs, **kwargs):
        # print(
        #     f"\tSearching index of {len(self._docs)} Documents for \"{docs[0].text}\"")
        darr = self._docs
        res = darr.get_attributes('text')
        tags = [res[i].split('-') for i in range(len(res))]
        rq_doc = DocumentArray()
        for i, tag in enumerate(tags):
            if docs[0].text == tag[0] or docs[0].text in tag[0]:
                rq_doc.append(darr[i])
        return rq_doc
        





       

        # return DocumentArray([required_doc])