# Taking notes and using Wikidata Bib

WikidataBib gathers a number of different purposes:

    - Make it easy to read a long list of articles
    - Provide searchable notes/highlights
    - Capture the timeline of academic readings
    - Provide personal visualization of reading statistics
    - Insert a reading routine in the context of Wikidata
    - Record notes in a device-independent fashion

This usage tutorial explains bit by bit  different parts of the project. 

## Reading articles on-demand

The basic usage of Wikidata Bib starts by reading articles on demand. 

Explaining by example, let's consider you want to read  an article titled "Wikidata as a knowledge graph for the life sciences" ([https://elifesciences.org/articles/52614](https://elifesciences.org/articles/52614)). 
After searching for the title, or doi, on [wikidata.org](https://wikidata.org) you will get a Q-identifier for the article.
In this case it is  [Q87830400](https://www.wikidata.org/wiki/Q87830400).

On your WikidataBib directory, in the command line, run: 

```bash
./wread Q87830400
```

The system will open a markdown notes file and (if possible) download a pdf for the document.
The notes file will contain some general info for the paper and sessions for:
    
    - copying "highlights" from the paper
    - adding comments 
    - adding "tags" to facilitate search later
    - links to Scholia, Wikidata and Author Disambiguator 

By going to Wikidata or Author Disambiguator you can improve the metadata on the articles you are interested, improving the dashboards you will use later. 

After reading the article, you can commit your changes to GitHub, so as to update the repository. 
While you can do your update manually, the short script `./wlog` logs your reading to GitHub in a quick way. 

## Reading articles from a list

To really benefit from Wikidata Bib, you will want to do more than just read articles on demand.

You will want to have an ordered stack of articles to read. 

The list of article QIDs stay in the `toread.md` file, and there are two basic usage modes:

- One single list of articles to read
- Multiple lists divided by topics 

Let's started with the single list to get familiar with the system. 

### Single list

The idea is a list that you can "pop" articles out whenever you sit down to read. 

To populate the list, just add the Wikidata Q-ID of your articles of interest

The code `./pop` will look for the first Q-ID in the `toread.md` and process it as in the on-demand reading step. 

It will also remove the Q-ID from the file, so you can advance in your reading articles.





# Sections to add

- Reading a paper with Wikidata Bib
- Adding an article to Wikidata
- Tagging and retrieving content. 
- Adding a new list via ./wadd and SPARQL queries
