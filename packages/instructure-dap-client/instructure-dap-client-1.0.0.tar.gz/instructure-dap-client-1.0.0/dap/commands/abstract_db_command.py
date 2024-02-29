import logging

from ..integration.database import DatabaseConnection
from .base import Arguments, CommandRegistrar

logger = logging.getLogger("dap")


class AbstractDbCommandRegistrar(CommandRegistrar):
    async def _before_execute(self, args: Arguments) -> None:
        if not args.connection_string:
            raise ValueError("missing database connection string")

        logger.debug(f"Checking connection to {args.connection_string}")
        connection = DatabaseConnection(args.connection_string)
        async with connection.connection as conn:
            # simply open and close connection to check validity
            pass
