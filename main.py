from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("5610197004:AAFnwUAMiNR2p82oQ7uPTa2YrFxqL3no0a4").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("calc", sum_command))
app.run_polling()