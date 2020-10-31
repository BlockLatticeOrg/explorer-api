[![explorer-api](https://circleci.com/gh/BlockLatticeOrg/explorer-api.svg?style=shield)](https://circleci.com/gh/BlockLatticeOrg/explorer-api)

# Explorer API
The Explorer API is one of the parts of the [BlockLattice.org](https://blocklattice.org/) ecosystem. It's an API to extract basic information from [Nano](https://nano.org/) blocks and accounts.

If you want to contribute to this project, this document will show you how to setup this application locally so you can test on your machine and improve upon it.


## Installation

In order to run this API, you must have [Python 3.8+](https://www.python.org/downloads/) and [Poetry](https://python-poetry.org/) installed.

### Install dependencies

Enter project's Poetry shell:
```bash
$ poetry shell
```

Install project dependencies:
```bash
$ poetry install
```

### Run local tests

Copy `local.env` to `.env`:
```bash
$ cp local.env .env
```

Run tests with Pytest:
```bash
$ pytest .
```

All tests should pass.

## Running

### Running the API locally

Run the app with `uvicorn`
```bash
$ uvicorn explorer_api.main:app --reload
```

Now the project is running on [http://127.0.0.1:8000](http://127.0.0.1:8000), and the docs can be accessed at [http://127.0.0.1:8000/v1/docs](http://127.0.0.1:8000/v1/docs).

### Using docs

Within the docs, you can test the API with real data as long as you setup a node url. In order to do that, you must configure an IP on your `.env` file:

```bash
NANO_NODE_IP=<real-node-ip>
```

If you don't have a remote or local node, you can learn how to setup your own Nano node [here](https://docs.nano.org/running-a-node/overview/).
_Note: instead of running with IPv6 `[::1]`, you should use IPv4 `0.0.0.0` when running locally._

After setting up a node, you now can test directly from the browser at [http://127.0.0.1:8000/v1/docs](http://127.0.0.1:8000/v1/docs), where you can use the endpoints and request real data from the network. It's important to note that if your node is still not fully synced, you may not be able to extract updated data.


### Contributing

When adding a new feature or refactoring some code, you must create a new branch to upload it.

```bash
$ git checkout -b <new-feature>
```

Before every commit, run the automatic tester and linter:

```bash
$ make tester
$ make linter
```

If you want to check if the commit will pass:

```bash
$ pre-commit
```
