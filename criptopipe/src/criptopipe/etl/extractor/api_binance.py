from criptopipe.src.criptopipe.etl.extractor.api_client import ApiClient
from criptopipe.src.criptopipe.config.settings import url_binance


class BinanceFetcher(ApiClient):
    def __init__(self):
        super().__init__(url_binance)

    async def fetche_binance(self) -> dict:
        return await self.get_api()
