import asyncio
import aiohttp
import logging
from datetime import datetime
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


class ApiClient:
    def __init__(self, url: str = ''):
        self.url = url

    async def get_api(self) -> dict:
        base_url: str = self.url
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(base_url, ssl=ssl_context) as response:
                    if response.status == 200:
                        data = await response.json()
                        if 'metadata' not in data:
                            data['metadata'] = {}
                            data['metadata']['timestamp'] = datetime.now().isoformat()
                            logger.info(
                                f'Dados da API da {base_url} coletados com sucesso')
                        print(data)
                    else:
                        logger.error(
                            f'Erro ao acessar a API {base_url}: {response.status}')
                        return None
        except asyncio.exceptions.CancelledError as e:
            print(e)
        except asyncio.exceptions.TimeoutError as e:
            print(e)
