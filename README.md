Database Data Science Presentation
==================================

See it [here](https://matthewfranglen.github.io/database-science-presentation/).

This was built using [reveal.js](https://github.com/hakimel/reveal.js)

Python
------

This requires a [pyenv](https://github.com/pyenv/pyenv) at python 3.6.2.
You need to install the requirements with:

```
pip install -r requirements.txt
```

Docker
------

You can use docker to run postgres and elastic search to allow easy testing.

### Postgres

```
docker run --rm --name pg -p 5432:5432 postgres
```

You can then connect to it from a locally installed postgres client:

```
psql -p 5432 -h localhost -U postgres postgres
```

This will allow you to easily run the sample SQL statements.

### Elastic Search

```
docker run --rm --name es -p 9200:9200 -e "http.host=0.0.0.0" -e "transport.host=127.0.0.1" -e "xpack.security.enabled=false" docker.elastic.co/elasticsearch/elasticsearch:5.5.2
```

You can query elastic search using curl:

```
curl localhost:9200
```

The notebooks also cover connecting to elastic search using python.

Postgres
--------

An example of using this is available in the `Using Postgres to Select Features.ipynb` notebook.
The presentation also features some sample SQL that you can run, reproduced below:

```sql
CREATE TABLE features (
    all_unique SERIAL,
    all_same INTEGER DEFAULT 1,
    five_values INTEGER,
    random_values INTEGER
);

INSERT INTO features
    (five_values, random_values)
    SELECT n, random() * 10000
        FROM generate_series(1, 5) n,
             generate_series(1, 200000);

ANALYZE features;

SELECT
    attname AS column,
    n_distinct,
    most_common_vals,
    most_common_freqs,
    histogram_bounds,
    correlation
FROM pg_stats
WHERE tablename = 'features';
```

Elastic Search
--------------

You can load the pickled data using the `Elastic Search Population.ipynb` notebook.
An example of term frequency extraction is available in `Elastic Search Term Extraction.ipynb`.
