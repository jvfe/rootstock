# Wikidata Bib - Literature Manager and dashboard

This repo is a propotype for bibliography management using Wikidata. 

The overarching goal is to leverage linked open data to navigate your studies and personal notes. 

You can check an example of a query dashboard for readings at [lubianat.github.io/wikidata_bib](https://lubianat.github.io/wikidata_bib).

Check [SETUP.md](./SETUP.md) for instructions on how to get started. 
# Basic usage

Clone the repository on your machine. 

Setup the execution permissions for the Wikidata Bib scripts:

```bash

gh repo clone lubianat/wikidata_bib
cd wikidata_bib
chmod +x wread
chmod +x pop
chmod +x wadd
chmod +x wlog
```

The scripts are written in Python3. To install the requirements, run:

```bash
pip3 install -r requirements.txt
```

Each script has a different function: 
    - `wread`  reads an article, provided in the form of a Wikidata QID (opens a markdown for notes and, if possible, a pdf of the article)
    - `pop` reads the first article from the `toread.md` list
    - `wadd` adds a bunch of new articles based on a user-provided Wikidata query
    - `wlog` logs the current progress to GitHub

For reading an independent paper, get its Q-ID on [Wikidata][https://wikidata.org] and run it like this:


```bash
./wread Q108766311
```

This will open the notes file for the paper [Representing COVID-19 information in collaborative knowledge graphs: The case of Wikidata (Q108766311)
](https://www.wikidata.org/wiki/Q108766311). Most biomedical articles are currently represented on Wikidata, and should be easy to find via Wikidata's search box. 

If your article of interest is not on Wikidata, you can add the info there directly on [Wikidata's interface](https://www.wikidata.org/wiki/Special:NewItem) or, if you are an experienced user, by searching the DOI/arXiv ID at the [Scholia][https://scholia.toolforge.org] and following the instructions. 


# Repository structure
- docs
- src
- notes
    - Q1123.md
    - Q2234.md
- toread.md
- read.ttl
- read.csv
- config.yaml
- pop
- wadd
- wlog
- wread

### Scaffolding files

- toread.md

A markdown stack/list of titles of papers.

The papers can be organized by sections, with section headers corresponding to the names in the `config.yaml` file.
Articles are stored as Wikidata identifiers, to automatically pull the information when actually reading. 

You can, of course, store just the name of the article or other information and later locate and update the file with the Wikidata QID. 


- config.yaml

A configuration file mapping shortcuts to use in the command line to categories in the `toread.md`. These shortcuts are used when invoking the scripts from the command line.


- read.ttl

An RDF file linking the wikidata URIs for the articles you are reading to your notes. 
Each note file will have an URI. For now I`ll use the property wb:has_notes, where wb is this repository URL

- read.csv 

A csv file linking article titles/human readable info to Wikidata ids.

- notes
A folder containing markdown notes for each article. Each article get its on file, named by Wikidata ID. 
If the material does not fit on Wikidata, just add it as a new header to other.md.

- docs
  
The html content for GitHub Pages, providing analytics on what has been read. 

### Scripts for use

- wadd

Adds a set of new articles to one of the lists in toread.md. Example for single-cell transcriptomics articles in either Nature or Science: https://w.wiki/3LhF
`$ ./wadd https://w.wiki/3MDs -p --new`

- wlog
Adds a commit to git for the articler read and pushes it to GitHub.
`$ ./wlog`

- wread
Read an article that is not on the list in toread.md. 

`$ ./wread Q107542983`

- pop

Pops the first QID in one of the lists in the toread.md file. The command is followed by a shortcut, specifying which list to look for (this is set up in the config.yaml file). 

For example, `$ ./pop ct` will remove the first QID from the "Cell Types" list and open the article for note-taking.

## Notes structure

# The title of the work
    The citation in [Manubot](https://manubot.org/) syntax

## A header saying "Highlights"

Copy-and-pasted highlights from the text. No copy-right claim can be made on this session, and all copy-paste content must fall under fair use guidelines for proprietary content. Basically, that means you should not use the copy-pasted content for anything else other than personal notes.

--> Any comments made by you should be preceeded by an arrow. And
    if they take another line, it is enough that they are indented.

And then you can continue highlighting.

## A header saying "Comments"

Any general comments that did not fit inlinely. 
