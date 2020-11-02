#!/usr/bin/python3

import sys
from wikidata2df import wikidata2df
from mdutils.mdutils import MdUtils
import pandas as pd
import os.path
import rdflib
 

def main():
    wd_id = sys.argv[1]
    query = """
    SELECT ?item ?itemLabel
    WHERE
    {
    VALUES ?item {wd:""" + wd_id + """}  
    SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
    }
    """

    df = wikidata2df(query)

    title = df["itemLabel"][0]
    file_path = "notes/" + wd_id

    mdFile = MdUtils(file_name=file_path, title= title)
    
    mdFile.new_line("  [@wikidata:" + wd_id + "]")
    mdFile.new_line() 
    mdFile.new_header(1, "Highlights")
    mdFile.new_header(1, "Comments")
    mdFile.create_md_file()

    df_stored = pd.read_csv("read.csv")
    
    new_row = {"human_id": df["itemLabel"][0],
               "wikidata_id": df["item"][0]}
    df_stored = df_stored.append(new_row, ignore_index=True)
    df_stored = df_stored.drop_duplicates()

    print(df_stored)
    df_stored.to_csv("read.csv", index = False)



    g = rdflib.Graph()
    result = g.parse("read.ttl", format="ttl")
    wb=rdflib.Namespace("https://github.com/lubianat/wikidata_bib/tree/main/")
    wbc=rdflib.Namespace("https://github.com/lubianat/wikidata_bib/tree/main/collections/")
    wbn=rdflib.Namespace("https://github.com/lubianat/wikidata_bib/tree/main/notes/")
    wd=rdflib.Namespace("http://www.wikidata.org/entity/")


    s = rdflib.term.URIRef(wd+wd_id)
    p1 = rdflib.term.URIRef(wb+"has_notes")
    o1 = rdflib.term.URIRef(wbn+wd_id+".md")
    g.add((s, p1, o1))

    g.serialize(destination='read.ttl', format='turtle')

    if len(sys.argv) >2 :
        collections = sys.argv[2:]
        for collection in collections:
            if os.path.isfile("collections/" + collection):
                s = rdflib.term.URIRef(wd+wd_id)
                p2 = rdflib.term.URIRef(wb+"in_collection")
                o2 = rdflib.term.URIRef(wbc+collection)
                g.add((s, p2, o2))
    
    g.serialize(destination='read.ttl', format='turtle')

if __name__ == "__main__":
    wd_id = sys.argv[1]
    fname = "notes/" + wd_id + ".md"

    if os.path.isfile(fname):
        print("Article has already been read")
    else:
        main()
    

