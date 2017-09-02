Overview
========

This is a presentation on using databases to perform the exploratory data analysis for a data science project.

This will cover:
 * Why use tools to choose which features to investigate
 * Why are databases good at this
 * How to use databases for this
 * Play along at home

Why Use Tools
-------------

Choosing the features to investigate involves using judgement.
As a programmer you are paid to use your judgement every day.
So you should be able to use your judgement to determine which features are valuable.

What if your judgement is wrong?
What if other features are more illuminating?
Cognitive bias is a consistent skew on judgement.

The Paul process of data science establishes a good environment for cognitive bias.
You establish what you want to determine and then investigate the data.
You are likely to choose features which you mentally associate with the goal.

Marketing has become more data driven.
Should feature selection be more data driven?

Why Use Databases
-----------------

Databases are data agnostic.
They can operate over anything you can put in a table.

There are strong theoretical foundations for databases.
A theoretical model doesn't always translate well to performance.

Databases need to be fast.
They are optimised for performing their job.
The best optimisation is to know the answer already, so database calculate answers in advance.

An index is such a calculation.
The existence of an index does not alter the result, it changes the speed.

Other such calculations can help with queries.
Joining data can be particularly slow.
The best algorithm to use for joining data depends on the amount of data.
To know how much data will be joined requires knowing how much data will be selected.
Knowing the distribution of values for a column permits good estimates.

The distribution of values can determine the quality of a feature.
A feature with a unique value per entry predicts nothing as every entry is different.
A feature with only a single value for all entries predicts nothing as every entry is the same.
The histogram of values will show the spread of values in a table.

How to get Statistics from Postgres
-----------------------------------

https://www.postgresql.org/docs/current/static/planner-stats.html
https://www.postgresql.org/docs/current/static/planner-stats-details.html
https://www.postgresql.org/docs/current/static/row-estimation-examples.html

➜ CREATE TABLE features
    (all_unique SERIAL, all_same INTEGER DEFAULT 1, five_values INTEGER, random_values INTEGER);
➜ INSERT INTO features
    (five_values, random_values)
    SELECT n, random() * 10000
        FROM generate_series(1, 5) n, generate_series(1, 200000);
➜ ANALYZE features;

➜ SELECT attname AS column, n_distinct, most_common_vals, most_common_freqs, histogram_bounds, correlation FROM pg_stats WHERE tablename = 'features';
─[ RECORD 1 ]─────┬───────────────────────────────────────────────────
column            │ all_unique
n_distinct        │ -1
most_common_vals  │ [null]
most_common_freqs │ [null]
histogram_bounds  │ {4,10093,19649,29321,39013,49415,60620,69880,...
correlation       │ 1
─[ RECORD 2 ]─────┼───────────────────────────────────────────────────
column            │ all_same
n_distinct        │ 1
most_common_vals  │ {1}
most_common_freqs │ {1}
histogram_bounds  │ [null]
correlation       │ 1
─[ RECORD 3 ]─────┼───────────────────────────────────────────────────
column            │ five_values
n_distinct        │ 5
most_common_vals  │ {1,2,4,5,3}
most_common_freqs │ {0.203767,0.2006,0.200333,0.197733,0.197567}
histogram_bounds  │ [null]
correlation       │ 1
─[ RECORD 4 ]─────┼───────────────────────────────────────────────────
column            │ random_values
n_distinct        │ 9995
most_common_vals  │ {5456,320,1726,2783,3178,4224,7841,8785,551,...
most_common_freqs │ {0.0004,0.000366667,0.000333333,0.000333333,...
histogram_bounds  │ {0,99,193,295,402,499,606,725,840,927,1035,...
correlation       │ 0.00250417


Elastic Search and TF-IDF
-------------------------

Elastic Search provides excellent text search.
It doesn't treat matching as a boolean question, instead it indicates how good the match is by scoring it.
One of the ways it scores it is to use TF-IDF.

When a word in the query is frequent in the match and rare in most documents then it increases the score more.
This is because the word is a strong indicator of the quality of the match.
Common words still contribute to the score, just much less.

To do all this elastic search must track term frequency in documents.

How to get Statistics from Elastic Search
-----------------------------------------

Pain in the butt tbh.
Go through the notebooks.
