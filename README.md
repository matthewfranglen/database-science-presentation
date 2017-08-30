# Database Data Science Presentation

See it [here](https://matthewfranglen.github.io/database-science-presentation/).

This was built using [reveal.js](https://github.com/hakimel/reveal.js)

## Docker

You can use docker to run postgres:

```
docker run --rm --name pg -P postgres
```

You can then connect to it from a locally installed postgres client:

```
psql -p $(docker port pg 5432 | sed -e 's/.*://') -h localhost -U postgres postgres
```

This will allow you to easily run the sample SQL statements.
