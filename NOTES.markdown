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

➜ CREATE TABLE boring_features (all_same INTEGER, all_unique INTEGER, two_values INTEGER, five_values INTEGER);
CREATE TABLE

➜ INSERT INTO boring_features (all_same, all_unique, five_values, two_values) SELECT 1, n + (5 * m), n, m FROM generate_series(1, 5) n, generate_series(0, 1) m;
INSERT 0 10

➜ ANALYZE boring_features ;
ANALYZE

➜ SELECT relname AS table, reltuples AS rows FROM pg_class WHERE relname = 'boring_features';
      table      │ rows
─────────────────┼──────
 boring_features │   10

➜ SELECT attname AS column, n_distinct, most_common_vals, most_common_freqs, histogram_bounds, correlation FROM pg_stats WHERE tablename = 'boring_features';
   column    │ n_distinct │ most_common_vals │   most_common_freqs   │    histogram_bounds    │ correlation
─────────────┼────────────┼──────────────────┼───────────────────────┼────────────────────────┼─────────────
 all_same    │          1 │ {1}              │ {1}                   │ [null]                 │           1
 all_unique  │         -1 │ [null]           │ [null]                │ {1,2,3,4,5,6,7,8,9,10} │    0.636364
 two_values  │       -0.2 │ {0,1}            │ {0.5,0.5}             │ [null]                 │    0.636364
 five_values │       -0.5 │ {1,2,3,4,5}      │ {0.2,0.2,0.2,0.2,0.2} │ [null]                 │           1
