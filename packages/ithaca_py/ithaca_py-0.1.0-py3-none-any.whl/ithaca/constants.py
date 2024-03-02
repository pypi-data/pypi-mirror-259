"""Environment Constants."""


ENVS = {
    "PRODUCTION": {
        "base_url": "https://app.ithacaprotocol.io/api/v1",
        "ws_url": "wss://app.ithacaprotocol.io",
        "rpc_url": "https://arbitrum.llamarpc.com",
        "subgraph": "https://api.studio.thegraph.com/query/43740/ithaca-arbitrum/v1.1.0",  # type: ignore  # noqa: E501
    },
    "UAT": {
        "base_url": "https://testnet.ithacaprotocol.io/api/v1",
        "ws_url": "wss://testnet.ithacaprotocol.io/wss",
        "rpc_url": "https://arbitrum-goerli-rpc.publicnode.com",
        "subgraph": "https://api.studio.thegraph.com/query/43740/ithaca-subgraph/v1.1.2",  # type: ignore  # noqa: E501
    },
    "CANARY": {
        "base_url": "https://app.canary.ithacanoemon.tech/api/v1",
        "ws_url": "wss://app.canary.ithacanoemon.tech/wss",
        "rpc_url": "https://arbitrum-goerli-rpc.publicnode.com",
        "subgraph": None,
    },
    "LOCAL": {
        "base_url": "https://localhost:8078/api/v1",
        "ws_url": "wss://localhost:8079",
        "rpc_url": "http://localhost:8545",
        "subgraph": None,
    },
}
