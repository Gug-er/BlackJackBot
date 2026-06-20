from aiogram import Router

from aiogram.filters import Command, CommandStart
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer("Hello there! Choose from the options below😁")
    
@router.message(Command('help'))
async def help_command(message: Message):
    await message.answer('Here are the available commands:'
                         '\n/start - Start the bot'
                         '\n/help - Show this help message'
                         '\n/rules - Show the rules')
    
@router.message(Command('rules'))
async def rules_command(message: Message):
    await message.answer("There will be rules")
     

    