# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['metaphor',
 'metaphor.alation',
 'metaphor.azure_data_factory',
 'metaphor.bigquery',
 'metaphor.bigquery.lineage',
 'metaphor.bigquery.profile',
 'metaphor.common',
 'metaphor.custom',
 'metaphor.custom.data_quality',
 'metaphor.custom.governance',
 'metaphor.custom.lineage',
 'metaphor.custom.metadata',
 'metaphor.custom.query_attributions',
 'metaphor.datahub',
 'metaphor.dbt',
 'metaphor.dbt.cloud',
 'metaphor.dbt.generated',
 'metaphor.fivetran',
 'metaphor.glue',
 'metaphor.hive',
 'metaphor.kafka',
 'metaphor.kafka.schema_parsers',
 'metaphor.looker',
 'metaphor.metabase',
 'metaphor.monte_carlo',
 'metaphor.mssql',
 'metaphor.mysql',
 'metaphor.notion',
 'metaphor.postgresql',
 'metaphor.postgresql.profile',
 'metaphor.postgresql.usage',
 'metaphor.power_bi',
 'metaphor.redshift',
 'metaphor.redshift.lineage',
 'metaphor.redshift.profile',
 'metaphor.s3',
 'metaphor.snowflake',
 'metaphor.snowflake.lineage',
 'metaphor.snowflake.profile',
 'metaphor.static_web',
 'metaphor.synapse',
 'metaphor.tableau',
 'metaphor.thought_spot',
 'metaphor.trino',
 'metaphor.unity_catalog',
 'metaphor.unity_catalog.profile']

package_data = \
{'': ['*'], 'metaphor.common': ['docs/*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'aws-assume-role-lib>=2.10.0,<3.0.0',
 'boto3>=1.28.57,<2.0.0',
 'botocore>=1.31.58,<2.0.0',
 'canonicaljson>=2.0.0,<3.0.0',
 'jsonschema>=4.18.6,<5.0.0',
 'metaphor-models==0.30.17',
 'pathvalidate>=3.2.0,<4.0.0',
 'pyarrow[pandas]>=14.0.1,<15.0.0',
 'pydantic[email]==2.5.1',
 'python-dateutil>=2.8.1,<3.0.0',
 'requests>=2.28.1,<3.0.0',
 'setuptools>=68.0.0,<69.0.0',
 'smart-open>=6.3.0,<7.0.0']

extras_require = \
{':extra == "all" or extra == "looker"': ['GitPython>=3.1.37,<4.0.0'],
 'all': ['asyncpg>=0.29.0,<0.30.0',
         'avro>=1.11.3,<2.0.0',
         'azure-identity>=1.14.0,<2.0.0',
         'azure-mgmt-datafactory>=3.1.0,<4.0.0',
         'beautifulsoup4>=4.12.3,<5.0.0',
         'confluent-kafka>=2.3.0,<3.0.0',
         'databricks-sdk>=0.14.0,<0.15.0',
         'databricks-sql-connector>=3.0.0,<4.0.0',
         'fastavro>=1.9.2,<2.0.0',
         'google-cloud-bigquery>=3.1.0,<4.0.0',
         'google-cloud-logging>=3.5.0,<4.0.0',
         'gql[requests]>=3.4.1,<4.0.0',
         'grpcio-tools>=1.59.3,<2.0.0',
         'lkml>=1.3.1,<2.0.0',
         'llama-hub==0.0.67',
         'llama-index==0.9.48',
         'looker-sdk>=23.6.0,<24.0.0',
         'lxml>=5.0.0,<5.1.0',
         'more-itertools>=10.1.0,<11.0.0',
         'msal>=1.20.0,<2.0.0',
         'msgraph-beta-sdk==1.0.0',
         'parse>=1.20.0,<2.0.0',
         'pycarlo>=0.8.1,<0.9.0',
         'pyhive>=0.7.0,<0.8.0',
         'pymssql>=2.2.9,<3.0.0',
         'pymysql>=1.0.2,<2.0.0',
         'sasl>=0.3.1,<0.4.0',
         'snowflake-connector-python>=3.7.1,<4.0.0',
         'SQLAlchemy>=1.4.46,<2.0.0',
         'sql-metadata>=2.8.0,<3.0.0',
         'sqllineage>=1.3.8,<1.4.0',
         'tableauserverclient>=0.25,<0.26',
         'thoughtspot_rest_api_v1==1.5.3',
         'thrift>=0.16.0,<0.17.0',
         'thrift-sasl>=0.4.3,<0.5.0',
         'trino>=0.327.0,<0.328.0'],
 'bigquery': ['google-cloud-bigquery>=3.1.0,<4.0.0',
              'google-cloud-logging>=3.5.0,<4.0.0',
              'sql-metadata>=2.8.0,<3.0.0'],
 'datafactory': ['azure-identity>=1.14.0,<2.0.0',
                 'azure-mgmt-datafactory>=3.1.0,<4.0.0'],
 'datahub': ['gql[requests]>=3.4.1,<4.0.0'],
 'hive': ['pyhive>=0.7.0,<0.8.0',
          'sasl>=0.3.1,<0.4.0',
          'thrift>=0.16.0,<0.17.0',
          'thrift-sasl>=0.4.3,<0.5.0'],
 'kafka': ['avro>=1.11.3,<2.0.0',
           'confluent-kafka>=2.3.0,<3.0.0',
           'grpcio-tools>=1.59.3,<2.0.0'],
 'looker': ['lkml>=1.3.1,<2.0.0',
            'looker-sdk>=23.6.0,<24.0.0',
            'sql-metadata>=2.8.0,<3.0.0'],
 'metabase': ['sql-metadata>=2.8.0,<3.0.0'],
 'monte-carlo': ['pycarlo>=0.8.1,<0.9.0'],
 'mssql': ['pymssql>=2.2.9,<3.0.0'],
 'mysql': ['pymysql>=1.0.2,<2.0.0', 'SQLAlchemy>=1.4.46,<2.0.0'],
 'notion': ['llama-hub==0.0.67', 'llama-index==0.9.48'],
 'postgresql': ['asyncpg>=0.29.0,<0.30.0'],
 'power-bi': ['msal>=1.20.0,<2.0.0',
              'msgraph-beta-sdk==1.0.0',
              'sql-metadata>=2.8.0,<3.0.0'],
 'redshift': ['asyncpg>=0.29.0,<0.30.0', 'sqllineage>=1.3.8,<1.4.0'],
 's3': ['fastavro>=1.9.2,<2.0.0',
        'more-itertools>=10.1.0,<11.0.0',
        'parse>=1.20.0,<2.0.0'],
 'snowflake': ['snowflake-connector-python>=3.7.1,<4.0.0',
               'sql-metadata>=2.8.0,<3.0.0'],
 'static-web': ['beautifulsoup4>=4.12.3,<5.0.0',
                'llama-hub==0.0.67',
                'llama-index==0.9.48',
                'lxml>=5.0.0,<5.1.0'],
 'synapse': ['pymssql>=2.2.9,<3.0.0'],
 'tableau': ['sqllineage>=1.3.8,<1.4.0', 'tableauserverclient>=0.25,<0.26'],
 'throughtspot': ['thoughtspot_rest_api_v1==1.5.3'],
 'trino': ['trino>=0.327.0,<0.328.0'],
 'unity-catalog': ['databricks-sdk>=0.14.0,<0.15.0',
                   'databricks-sql-connector>=3.0.0,<4.0.0']}

entry_points = \
{'console_scripts': ['metaphor = metaphor.__main__:main']}

setup_kwargs = {
    'name': 'metaphor-connectors',
    'version': '0.13.131',
    'description': "A collection of Python-based 'connectors' that extract metadata from various sources to ingest into the Metaphor app.",
    'long_description': '<a href="https://metaphor.io"><img src="https://github.com/MetaphorData/connectors/raw/main/logo.png" width="300" /></a>\n\n# Metaphor Connectors\n\n[![Codecov](https://img.shields.io/codecov/c/github/MetaphorData/connectors)](https://app.codecov.io/gh/MetaphorData/connectors/tree/main)\n[![CodeQL](https://github.com/MetaphorData/connectors/workflows/CodeQL/badge.svg)](https://github.com/MetaphorData/connectors/actions/workflows/codeql-analysis.yml)\n[![PyPI Version](https://img.shields.io/pypi/v/metaphor-connectors)](https://pypi.org/project/metaphor-connectors/)\n![Python version 3.8+](https://img.shields.io/badge/python-3.8%2B-blue)\n![PyPI Downloads](https://img.shields.io/pypi/dm/metaphor-connectors)\n[![Docker Pulls](https://img.shields.io/docker/pulls/metaphordata/connectors)](https://hub.docker.com/r/metaphordata/connectors)\n[![License](https://img.shields.io/github/license/MetaphorData/connectors)](https://github.com/MetaphorData/connectors/blob/master/LICENSE)\n\nThis repository contains a collection of Python-based "connectors" that extract metadata from various sources to ingest into the [Metaphor](https://metaphor.io) platform.\n\n## Installation\n\nThis package requires Python 3.8+ installed. You can verify the version on your system by running the following command,\n\n```shell\npython -V  # or python3 on some systems\n```\n\nOnce verified, you can install the package using [pip](https://docs.python.org/3/installing/index.html),\n\n```shell\npip install "metaphor-connectors[all]"  # or pip3 on some systems\n```\n\nThis will install all the connectors and required dependencies. You can also choose to install only a subset of the dependencies by installing the specific [extra](https://packaging.python.org/tutorials/installing-packages/#installing-setuptools-extras), e.g.\n\n```shell\npip install "metaphor-connectors[snowflake]"\n```\n\nSimilarly, you can also install the package using `requirements.txt` or `pyproject.toml`.\n\n## Docker\n\nWe automatically push a [docker image](https://hub.docker.com/r/metaphordata/connectors) to Docker Hub as part of the CI/CD. See [this page](./docs/docker.md) for more details.\n\n## GitHub Action\n\nYou can also run the connectors in your CI/CD pipeline using the [Metaphor Connectors](https://github.com/marketplace/actions/metaphor-connectors-github-action) GitHub Action.\n\n## Connectors\n\nEach connector is placed under its own directory under [metaphor](./metaphor) and extends the `metaphor.common.BaseExtractor` class.\n\n| Connector Name                                                    | Metadata                                 |\n|-------------------------------------------------------------------|------------------------------------------|  \n| [azure_data_factory](metaphor/azure_data_factory/)                | Lineage, Pipeline                        |\n| [bigquery](metaphor/bigquery/)                                    | Schema, description, statistics, queries |\n| [bigquery.lineage](metaphor/bigquery/lineage/)                    | Lineage                                  |\n| [bigquery.profile](metaphor/bigquery/profile/)                    | Data profile                             |\n| [custom.data_quality](metaphor/custom/data_quality/)              | Data quality                             |\n| [custom.governance](metaphor/custom/governance/)                  | Ownership, tags, description             |\n| [custom.lineage](metaphor/custom/lineage/)                        | Lineage                                  |\n| [custom.metadata](metaphor/custom/metadata/)                      | Custom metadata                          |\n| [custom.query_attributions](metaphor/custom/query_attributions/)  | Query attritutions                       |\n| [datahub](metaphor/datahub/)                                      | Description, tag, ownership              |\n| [dbt](metaphor/dbt/)                                              | dbt model, test, lineage                 |\n| [dbt.cloud](metaphor/dbt/cloud/)                                  | dbt model, test, lineage                 |\n| [fivetran](metaphor/fivetran/)                                    | Lineage, Pipeline                        |\n| [glue](metaphor/glue/)                                            | Schema, description                      |\n| [looker](metaphor/looker/)                                        | Looker view, explore, dashboard, lineage |\n| [kafka](metaphor/kafka/)                                          | Schema, description                      |\n| [metabase](metaphor/metabase/)                                    | Dashboard, lineage                       |\n| [monte_carlo](metaphor/monte_carlo/)                              | Data monitor                             |\n| [mssql](metaphor/mssql/)                                          | Schema                                   |\n| [mysql](metaphor/mysql/)                                          | Schema, description                      |\n| [notion](metaphor/notion/)                                        | Document embeddings                      |\n| [postgresql](metaphor/postgresql/)                                | Schema, description, statistics          |\n| [postgresql.profile](metaphor/postgresql/profile/)                | Data profile                             |\n| [postgresql.usage](metaphor/postgresql/usage/)                    | Usage                                    |\n| [power_bi](metaphor/power_bi/)                                    | Dashboard, lineage                       |\n| [redshift](metaphor/redshift/)                                    | Schema, description, statistics, queries |\n| [redshift.lineage](metaphor/redshift/lineage/)                    | Lineage                                  |\n| [redshift.profile](metaphor/redshift/profile/)                    | Data profile                             |\n| [snowflake](metaphor/snowflake/)                                  | Schema, description, statistics, queries |\n| [snowflake.lineage](metaphor/snowflake/lineage/)                  | Lineage                                  |\n| [snowflake.profile](metaphor/snowflake/profile/)                  | Data profile                             |\n| [synapse](metaphor/synapse/)                                      | Schema, queries                          |\n| [tableau](metaphor/tableau/)                                      | Dashboard, lineage                       |\n| [thought_spot](metaphor/thought_spot/)                            | Dashboard, lineage                       |\n| [trino](metaphor/trino/)                                          | Schema, description, queries             |                       \n| [unity_catalog](metaphor/unity_catalog/)                          | Schema, description                      |\n| [unity_catalog.profile](metaphor/unity_catalog/profile/)          | Statistics                               |\n\n## Development\n\nSee [Development Environment](docs/develop.md) for more instructions on how to set up your local development environment.\n\n## Custom Connectors\n\nSee [Adding a Custom Connector](docs/custom.md) for instructions and a full example of creating your custom connectors.\n',
    'author': 'Metaphor',
    'author_email': 'dev@metaphor.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://metaphor.io',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8.1,<3.12',
}


setup(**setup_kwargs)
