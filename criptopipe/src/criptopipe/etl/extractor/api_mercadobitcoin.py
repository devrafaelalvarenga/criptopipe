from criptopipe.src.criptopipe.etl.extractor.api_client import ApiClient
from criptopipe.src.criptopipe.config.settings import url_mb


class MercadoBitcoinFetcher(ApiClient):
    def __init__(self):
        super().__init__(url_mb)

    async def fetche_mercadobitcoin(self) -> dict:
        return await self.get_api()
