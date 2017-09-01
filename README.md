Database Data Science Presentation
==================================

See it [here](https://matthewfranglen.github.io/database-science-presentation/).

This was built using [reveal.js](https://github.com/hakimel/reveal.js)

Docker
------

You can use docker to run postgres and elastic search to allow easy testing.

### Postgres

```
docker run --rm --name pg -P postgres
```

You can list the published port and hostname with:

```
docker port pg 5432
```

You can then connect to it from a locally installed postgres client:

```
psql -p $(docker port pg 5432 | sed -e 's/.*://') -h localhost -U postgres postgres
```

This will allow you to easily run the sample SQL statements.

### Elastic Search

```
docker run --rm --name es -P -e "http.host=0.0.0.0" -e "transport.host=127.0.0.1" -e "xpack.security.enabled=false" docker.elastic.co/elasticsearch/elasticsearch:5.5.2
```

You can get the port that it runs on in a similar manner:

```
docker port es 9200
```

You can then use this in curl requests or for use in python.

Postgres
--------

...

Elastic Search
--------------

You can load the pickled data using the `populate_es.py` script.

This requires a [pyenv](https://github.com/pyenv/pyenv) at python 3.6.2.
You need to install the requirements with `pip install -r requirements.txt`.
