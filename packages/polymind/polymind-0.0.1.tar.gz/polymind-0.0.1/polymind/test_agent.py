import asyncio

from metagpt.roles.product_manager import ProductManager
from metagpt.logs import logger

async def main():
    msg = "Write a PRD for building a multi-agent framework."
    role = ProductManager()
    result = await role.run(msg)
    logger.info(result.content[:100])

if __name__ == '__main__':
    asyncio.run(main())