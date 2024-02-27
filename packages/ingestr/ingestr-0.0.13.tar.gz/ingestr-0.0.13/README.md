<div align="center">
    <img src="https://github.com/bruin-data/ingestr/blob/main/resources/ingestr.svg?raw=true" width="500" />
    <p>Ingest & copy data from any source to any destination without any code</p>
    <img src="https://github.com/bruin-data/ingestr/blob/main/resources/demo.gif?raw=true" width="750" />
</div>


-----

Ingestr is a command-line application that allows you to ingest data from any source into any destination using simple command-line flags, no code necessary.

- ✨ copy data from your database into any destination
- ➕ incremental loading: `append`, `merge` or `delete+insert`
- 🐍 single-command installation

ingestr takes away the complexity of managing any backend or writing any code for ingesting data, simply run the command and watch the data land on its destination.


## Installation
```
pip install ingestr
```

## Quickstart

```bash
ingestr \
    --source-uri 'postgresql://admin:admin@localhost:8837/web?sslmode=disable' \
    --source-table 'public.some_data' \
    --dest-uri 'bigquery://<your-project-name>?credentials_path=/path/to/service/account.json' \
    --dest-table 'ingestr.some_data'
```

That's it.

This command will:
- get the table `public.some_data` from the Postgres instance.
- upload this data to your BigQuery warehouse under the schema `ingestr` and table `some_data`.

## Documentation
You can see the full documentation [here](https://bruin-data.github.io/ingestr/getting-started/quickstart.html).


## Supported Sources & Destinations

| Database             | Source | Destination |
|----------------------|--------|-------------|
| Postgres             | ✅      | ✅         |
| BigQuery             | ✅      | ✅         |
| Snowflake            | ✅      | ✅         |
| Redshift             | ✅      | ✅         |
| Databricks           | ✅      | ✅         |
| DuckDB               | ✅      | ✅         |
| Microsoft SQL Server | ✅      | ✅         |
| SQLite               | ✅      | ❌         |
| MySQL                | ✅      | ❌         |

More to come soon!

## Acknowledgements
This project would not have been possible without the amazing work done by the [SQLAlchemy](https://www.sqlalchemy.org/) and [dlt](https://dlthub.com/) teams. We relied on their work to connect to various sources and destinations, and built `ingestr` as a simple, opinionated wrapper around their work.