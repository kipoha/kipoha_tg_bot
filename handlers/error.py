import asyncio
from aiogram import types, Dispatcher
from aiogram.utils import exceptions


async def exception_retry_handler(update: types.Update, exception: exceptions.RetryAfter):
    await asyncio.sleep(exception.timeout)
    return True


def reg_error_handlers(dp: Dispatcher):
    dp.register_errors_handler(
        exception_retry_handler,
        exception=exceptions.RetryAfter
    )