# ETL orchestration logic
from criptopipe.src.criptopipe.etl.extractor.api_coinbase import CoinbaseFetcher
from criptopipe.src.criptopipe.etl.extractor.api_mercadobitcoin import MercadoBitcoinFetcher
from criptopipe.src.criptopipe.etl.extractor.api_binance import BinanceFetcher
import asyncio


async def main() -> dict:
    coinbase = CoinbaseFetcher()
    mercadobitcoin = MercadoBitcoinFetcher()
    binance = BinanceFetcher()
    results = await asyncio.gather(
        coinbase.fetche_coinbase(),
        mercadobitcoin.fetche_mercadobitcoin(),
        binance.fetche_binance()
    )
    return results


# if __name__ == "__main__":
    # asyncio.run(main())
