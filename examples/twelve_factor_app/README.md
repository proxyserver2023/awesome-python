### Codebase
> One codebase tracked in revision control, many deploys

![Distributed Codebase](https://www.12factor.net/images/codebase-deploys.png)


### Dependencies
> Explicitly declare and isolate dependencies.

Libraries installed through a packaging system can be installed system-wide (known as “site packages”) or scoped into the directory containing the app (known as “vendoring” or “bundling”).

Dependency declaration in a file `requirements.txt` and Dependency isolation in `virtualenv`.


### Config
> Store config in the environment

An app’s config is everything that is likely to vary between deploys (staging, production, developer environments, etc). This includes:

- Resource handles to the database, Memcached, and other backing services
- Credentials to external services such as Amazon S3 or Twitter
- Per-deploy values such as the canonical hostname for the deploy

Apps sometimes store config as constants in the code. This is a violation of twelve-factor, which requires strict separation of config from code. `Config varies substantially across deploys, code does not`.

### Backing Services
> Treat  backing services as attached resources.

![Attached Resources](https://www.12factor.net/images/attached-resources.png)





