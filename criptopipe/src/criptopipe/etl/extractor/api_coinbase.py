from criptopipe.src.criptopipe.etl.extractor.api_client import ApiClient
from criptopipe.src.criptopipe.config.settings import url_coinbase


class CoinbaseFetcher(ApiClient):
    def __init__(self):
        super().__init__(url_coinbase)

    async def fetche_coinbase(self) -> dict:
        return await self.get_api()
