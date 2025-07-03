# ETL orchestration logic
from criptopipe.src.criptopipe.etl.extractor.api_extractor import Fetcher
import asyncio

if __name__ == "__main__":
    fetcher = Fetcher()
    asyncio.run(fetcher.main())
