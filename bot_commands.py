from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}')
    
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/time\n/help\n/calc')
    
async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')
    
async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    items = update.message.text.split()
    await update.message.reply_text(f'{items[1]} = {eval(items[1])}')