<p align="center">
  <img src="https://raw.githubusercontent.com/localstack/localstack/master/doc/localstack-readme-banner.svg" alt="LocalStack - A fully functional local cloud stack">
</p>

<p align="center">
  <a  href="https://pypi.org/project/localstack-extension-snowflake/"><img  alt="PyPI Version"  src="https://img.shields.io/pypi/v/localstack-extension-snowflake?color=blue"></a>
  <a href="https://hub.docker.com/r/localstack/snowflake"><img alt="Docker Pulls" src="https://img.shields.io/docker/pulls/localstack/snowflake"></a>
  <a href="https://pypi.org/project/localstack-extension-snowflake"><img alt="PyPi downloads" src="https://static.pepy.tech/badge/localstack-extension-snowflake"></a>
  <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
  <a href="https://twitter.com/localstack"><img alt="Twitter" src="https://img.shields.io/twitter/url/http/shields.io.svg?style=social"></a>
</p>

<p align="center">
  LocalStack is a cloud software development framework to develop and test your Snowflake data pipelines locally.
</p>

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#installing">Install</a> •
  <a href="#quickstart">Quickstart</a> •
  <a href="#base-image-tags">Base Image Tags</a> •
  <a href="#releases">Releases</a> •
  <a href="#support">Support</a> •
  <a href="#license">License</a>
  <br/>
  <a href="https://snowflake.localstack.cloud" target="_blank">📖 Docs</a> •
  <a href="https://snowflake.localstack.cloud/references/coverage/" target="_blank">☑️ Function coverage</a>
</p>

---

## Overview

LocalStack is a cloud service emulator that runs in a single container on your laptop or in your CI environment. LocalStack Snowflake emulator replicates the functionality of the real [Snowflake](https://snowflake.com) platform, allowing you to perform operations without an internet connection or a Snowflake account. This is valuable for developing and testing Snowflake data pipelines entirely on the local machine (and in CI pipelines), enabling quick feedback cycles, and not incurring costs of using the real system.

LocalStack Snowflake emulator supports the following features:

-   [**Basic operations**  on warehouses, databases, schemas, and tables](https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-example)
-   [**Storing files**  in user/data/named  **stages**](https://docs.snowflake.com/en/user-guide/data-load-local-file-system-create-stage)
-   [**Snowpark**  libraries](https://docs.snowflake.com/en/developer-guide/snowpark/python/index)
-   [**Snowpipe**  streaming with  **Kafka connector**](https://docs.snowflake.com/en/user-guide/data-load-snowpipe-streaming-kafka)
-   [**JavaScript and Python UDFs**](https://docs.snowflake.com/en/developer-guide/udf/javascript/udf-javascript-introduction)
-   … and more!

## Install

You can use the Snowflake Docker image to run the LocalStack Snowflake emulator. The Snowflake Docker image is available on the  [LocalStack Docker Hub](https://hub.docker.com/r/localstack/snowflake). To pull the Snowflake Docker image, execute the following command:

```bash
docker pull localstack/snowflake
```

You can start the Snowflake Docker container using the following methods:

1.  [`localstack`  CLI](https://docs.localstack.cloud/getting-started/installation/#localstack-cli)
2.  [`docker`  CLI](https://docs.docker.com/get-docker/)
3.  [Docker Compose](https://docs.docker.com/compose/install/)

> **Note**: Before starting, ensure you have a valid  `LOCALSTACK_AUTH_TOKEN`  to access the LocalStack Snowflake emulator. Refer to the [Auth Token guide](https://docs.localstack.cloud/getting-started/auth-token/) to obtain your Auth Token and specify it in the  `LOCALSTACK_AUTH_TOKEN`  environment variable.

### `localstack` CLI

To start the Snowflake Docker container using the  `localstack`  CLI, execute the following command:

```bash
export LOCALSTACK_AUTH_TOKEN=<your-auth-token>
IMAGE_NAME=localstack/snowflake localstack start
```

### `docker` CLI

To start the Snowflake Docker container using the  `docker`  CLI, execute the following command:

```bash
docker run \
    --rm -it \
    -p 4566:4566 \
    -e LOCALSTACK_AUTH_TOKEN=${LOCALSTACK_AUTH_TOKEN:?} \
    localstack/snowflake
```

### Docker Compose

Create a `docker-compose.yml`  file with the specified content:

```yaml
version: "3.8"

services:
  localstack:
    container_name: "localstack-main"
    image: localstack/snowflake
    ports:
      - "127.0.0.1:4566:4566"
    environment:
      - LOCALSTACK_AUTH_TOKEN=${LOCALSTACK_AUTH_TOKEN:?}
    volumes:
      - "./volume:/var/lib/localstack"
```

Start the Snowflake Docker container with the following command:

```bash
docker-compose up
```

## Quickstart

After starting the Snowflake Docker container, you can use the [Snowflake Python Connector](https://docs.snowflake.com/en/developer-guide/python-connector.html)  to interact with the LocalStack Snowflake emulator. The following example demonstrates how to create a Snowflake table using the Snowflake Python Connector:

```python
connection = snowflake.connector.connect(
    user="test",
    password="test",
    account="test",
    database="test",
    host="snowflake.localhost.localstack.cloud",
)
connection.cursor().execute("CREATE TABLE table1(col1 INT)")
```

Check out our [documentation](https://snowflake.localstack.cloud) for more examples and guides.

## Base Image Tags

We currently push the `latest` tag as our default tag. This tag is fully tested using our extensive integration test suite. This tag should be used if you want to stay up-to-date with the latest changes.

## Releases

Please refer to our [changelog page](https://snowflake.localstack.cloud/references/changelog/) to see the complete list of changes for each release.

## Support

Get in touch with the LocalStack Team to report issues & request new features, on the following channels:

-  [LocalStack Slack Community](https://localstack.cloud/contact/)
-  [LocalStack Discussion Page](https://discuss.localstack.cloud/)
-  [LocalStack Support email](mailto:support@localstack.cloud)

## License

(c) 2024 LocalStack
