# -*- coding:utf-8 -*-
import os

from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
from jieba.analyse import ChineseAnalyzer

analyzer = ChineseAnalyzer()  # replace the origin anlayzer
schema = Schema(title = TEXT(stored = True), path = ID(stored=True), content=TEXT(analyzer=analyzer))
ix = create_in("./WHOOSH_BASE",  schema=schema);

writer = ix.writer()

cDir = "/Users/cocotang/code/holyFinish/old_sphinx_flask/sourceDir"

for dirpath, dirnames, filenames in os.walk(cDir):
    for searchFile in filenames:
        with open(cDir + "/" + searchFile) as f:
            # writer.add_document(title=searchFile, path=dirpath + "/" + searchFile, content=f.read())
            writer.add_document(title=searchFile.decode("utf-8"), path=str(dirpath + "/" + searchFile).decode('utf-8'), content=f.read().decode("utf-8"))

writer.commit()


results = []
with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema).parse(u"我")   # unicode error
    # query = QueryParser("content", ix.schema).parse("Chinese")
    results = searcher.search(query)
    print results[0]

print len(results)


