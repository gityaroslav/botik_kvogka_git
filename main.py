from pyrogram import Client, filters
import tgcrypto

app = Client(
    "my_account",
    api_id=15335811,
    api_hash="d5432a68519e4ef1c1948b4bd1cf2d8c"
)

@app.on_message(filters.me)
def echo(client, message):
    message.reply_text(message.text)

app.run()