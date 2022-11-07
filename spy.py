from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

async def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open('bd.csv', 'a')
    file.write(f', {update.effective_user.id}, {update.effective_user.first_name}, {update.message.text}\n')
    file.close