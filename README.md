# Biomedical Retractions


## Identifying biomedical articles at risk for retraction

* Tagline: (i.e: Analyze political botnet activity on Twitter and develop effective counter-measures)
* Date: October 2016
* Category: Applied Research
* Author(s): [Graham Mueller](https://github.com/wgmueller1)

## Project Status:

* Brainstorming Phase: Currently collecting data for baseline models.


## Community Links:

* [Mailing list](https://groups.google.com/forum/#!forum/aion-identifying-biomedical-articles-at-risk-for-retraction)
* [![Gitter chat](https://badges.gitter.im/gitterHQ/services.png)](https://gitter.im/ai-open-network/biomedical-retractions)

## Problem description:

Develop a model capable of reliably flagging biomedical articles (appearing on bioRxiv or in biomedical scientific publications) that may be at risk of retraction. Such articles would then be carefully reviewed by peers in the community.

## Why this problem matters:

Although the retraction of a scientific article in the biomedical literature is still a rare event, it is getting increasingly frequent [here](#ref-one) and [here](#ref-two).

1. Retractions reflect error, misconduct, and fraud, which can significantly affect the scientific community and [undermine the trust](https://www.washingtonpost.com/news/morning-mix/wp/2015/03/27/fabricated-peer-reviews-prompt-scientific-journal-to-retract-43-papers-systematic-scheme-may-affect-other-journals/) that the public puts in science.
2. Detecting articles at risk of retraction could help focus the attention of efforts like [Retraction Watch](http://retractionwatch.com/) and other post-publication peer review groups.
3. In turn, if the detection of problematic articles becomes more effective, the incentive for fraud is greatly diminished and the penalty for errors is increased, which should improve the overall quality and reliability of the biomedical literature.

## Datasets:

>PubMed Central® (PMC) is a free full-text archive of biomedical and life sciences journal literature at the U.S. National Institutes of Health's National Library of Medicine (NIH/NLM).
>
>The Open Access Subset (OA Subset) is the largest collection of articles available for text mining via PMC. Articles in the OA Subset are still protected by copyright in most cases, but are made available for download under a Creative Commons or similar license that generally allows more liberal redistribution and reuse than a traditional copyrighted work.
>
>To download a collection in PMC for text mining, you must use the designated services (usually the PMC FTP service).

https://www.ncbi.nlm.nih.gov/pmc/tools/ftp/


## Extracting Data - Preprocessing details:


Once you have downloaded the data, extract the directories and place them in the data folder.  Please do not commit the ~45GB worth of xml files to this repo!

From the root directory, you can create the text file which lists the path of each journal article using the following:

>find .  -iname '*.nxml' > files-all.txt

The spark script uses the path of each article as input, loads the xml and parse out the article-type, which identifies whether an article was retracted or not.  To run this script use:

> spark-submit scripts/spark_retractions.py


## Requirements

Python 2.7+
lxml

Apache Spark is used for parsing the xml documents.
http://spark.apache.org

## Relevant Work:



## Contribute:


* Provide a starting point readme file and status of the current project for new researchers. These projects can take months if not longer sometimes to complete, such information will help onboarding faster.
* Guideline on how to edit-add new resources to this project, if there is a specific requirement, mention them. i.e:
  - Please create a branch and do a pull-request when adding to this example project.
  - Open Issues if something is not clear in the readme, or found linguistic/ grammar mistakes.


### References:
-----
1. <a href="ref-one"></a>[A Comprehensive Analysis of Articles Retracted Between 2004 and 2013 from Biomedical Literature – A Call for Reforms](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4142449/)
2. <a href="ref-two"></a>[Why Has the Number of Scientific Retractions Increased?](https://www.ncbi.nlm.nih.gov/pubmed/21486985)
3. [Why and how do journals retract articles? An analysis of Medline retractions 1988-2008](https://www.ncbi.nlm.nih.gov/pubmed/21486985)


----
**PS: Last few notes:**
* Be Nice & Be Respectful.
* Value other people's work, please reference them. Don't just copy & paste what you find elsewhere when it comes to sharing information.
* Give constructive criticism, as in if you see something not working, or wrong, suggest an attempt to tackle resolving the issue.
* Please Ask Questions: This is one big attempt to open up opportunity for everyone being able to contribute, if they can add value towards these research topics.
* Also, keep in mind that most of the researchers that are opening these projects might have full-time work/research. If there is a specific question, try opening an issue, use the given open communication channels rather than direct contact.