# biomedical-retractions


## Data Sources

>PubMed Central® (PMC) is a free full-text archive of biomedical and life sciences journal literature at the U.S. National Institutes of Health's National Library of Medicine (NIH/NLM). 
>
>The Open Access Subset (OA Subset) is the largest collection of articles available for text mining via PMC. Articles in the OA Subset are still protected by copyright in most cases, but are made available for download under a Creative Commons or similar license that generally allows more liberal redistribution and reuse than a traditional copyrighted work. 
>
>To download a collection in PMC for text mining, you must use the designated services (usually the PMC FTP service).

https://www.ncbi.nlm.nih.gov/pmc/tools/ftp/

## Instructions

Once you have downloaded the data, extract the directories and place them in the data folder.  Please do not commit the ~45GB worth of xml files to this repo!  

From the root directory, you can create the text file which lists the path of each journal article using the following:

>find .  -iname '*.nxml' > files-all.txt

The spark script uses the path of each article as input, loads the xml and parse out the article-type, which identifies whether an article was retracted or not.  To run this script use:

> spark-submit scripts/spark_retractions.py


## Requirements




## Notes
