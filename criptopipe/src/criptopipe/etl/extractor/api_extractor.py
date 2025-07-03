# Base HTTP client using aiohttp
# Funções assíncronas para requisição
import asyncio
import aiohttp
import logging
from datetime import datetime
from criptopipe.src.criptopipe.config.settings import url_binance, url_coinbase, url_mb
from criptopipe.src.criptopipe.config.logger import CollectorLogger
import certifi
import ssl

ssl_context = ssl.create_default_context(cafile=certifi.where())

collector_logger = CollectorLogger()
# Configura o logger
collector_logger.configure_logging()
# Define o nome do logger
logger_name: str = 'collector_logs.criptopipe.api_base'
# Define o logger para o módulo atual
logger: str = logging.getLogger(logger_name)


class Fetcher():
    """
    Fetcher is an asynchronous class responsible for collecting cryptocurrency data from multiple APIs.

    Methods:
        fetch_coinbase() -> str:
            Asynchronously fetches data from the Coinbase API endpoint defined in the config.
            Prints the response data if successful, otherwise prints an error message.

        fetch_binance() -> str:
            Asynchronously fetches data from the Binance API endpoint defined in the config.
            Prints the response data if successful, otherwise prints an error message.

        fetch_mb() -> str:
            Asynchronously fetches data from the Mercado Bitcoin API endpoint defined in the config.
            Prints the response data if successful, otherwise prints an error message.

        main():
            Runs all fetch methods concurrently using asyncio.gather.

    Usage:
        Instantiate the Fetcher class and run the main method to fetch data from all APIs concurrently.
    """

    async def fetch_coinbase(self) -> dict:
        try:
            logger.info(
                "Iniciando a coleta de dados da API da Coinbase")
            # url_coinbase: str = url_coinbase
            async with aiohttp.ClientSession() as session:
                async with session.get(url=url_coinbase, ssl=ssl_context) as response:
                    if response.status == 200:
                        data_coinbase = await response.json()
                        if 'metadata' not in data_coinbase:
                            data_coinbase['metadata'] = {}
                        data_coinbase['metadata']['timestamp'] = datetime.now(
                        ).isoformat()
                        data_coinbase['metadata']['source'] = 'Coinbase'
                        logger.info(
                            "Dados da API da Coinbase coletados com sucesso")
                        print(data_coinbase)
                    else:
                        logger.error(
                            f"Erro ao acessar a API Coinbase: {response.status}")
                        return None
        except asyncio.exceptions.CancelledError as e:
            print(e)
        except asyncio.exceptions.TimeoutError as e:
            print(e)

    async def fetch_binance(self) -> dict:
        try:
            # url_binance: str = url_binance
            logger.info(
                "Iniciando a coleta de dados da API da Binance")
            async with aiohttp.ClientSession() as session:
                async with session.get(url=url_binance, ssl=ssl_context) as response:
                    if response.status == 200:
                        data_binance = await response.json()
                        if 'metadata' not in data_binance:
                            data_binance['metadata'] = {}
                        data_binance['metadata']['timestamp'] = datetime.now(
                        ).isoformat()
                        data_binance['metadata']['source'] = 'Binance'
                        logger.info(
                            "Dados da API da Binance coletados com sucesso")
                        print(data_binance)
                    else:
                        logger.error(
                            f"Erro ao acessar a API Binance: {response.status}")
                        return None
        except asyncio.exceptions.CancelledError as e:
            print(e)
        except asyncio.exceptions.TimeoutError as e:
            print(e)

    async def fetch_mb(self) -> dict:
        # url_mb: str = url_mb
        logger.info(
            "Iniciando a coleta de dados da API da MB")
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url_mb, ssl=ssl_context) as response:
                if response.status == 200:
                    data_mb = await response.json()
                    if 'metadata' not in data_mb:
                        data_mb['metadata'] = {}
                    data_mb['metadata']['timestamp'] = datetime.now().isoformat()
                    data_mb['metadata']['source'] = 'MB'
                    logger.info(
                        "Dados da API da MB coletados com sucesso")
                    print(data_mb)
                else:
                    logger.error(
                        f"Erro ao acessar a API Mercado Bitcoin: {response.status}")
                    return None

    async def main(self) -> dict:
        results = await asyncio.gather(
            self.fetch_coinbase(),
            self.fetch_binance(),
            self.fetch_mb()
        )
        return results
