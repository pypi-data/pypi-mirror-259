# AndromedaClient

AndromedaClient is a Python client for interacting with the Andromeda API of the Metropolitan Area Rhine Neckar.

## Installation

You can install AndromedaClient using pip:

```bash
pip install andromedaClient
```

## Usage

First, import the AndromedaClient class and create a new client:

from andromedaClient import AndromedaClient

client = AndromedaClient('http://localhost:8000', 'username', 'password')

You can then use the client to make requests to the Andromeda API:

response = client.get('/test')

