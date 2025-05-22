import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Ganti dengan token dari @BotFather
BOT_TOKEN = '7922135318:AAHfv4iZMftMnBirqm4ZBsTqKVYu3IQ9hAk'

# Fungsi untuk mengambil harga APT dari CoinGecko
def get_aptos_price():
    try:
        url = 'https://api.coingecko.com/api/v3/simple/price?ids=aptos&vs_currencies=usd'
        response = requests.get(url)
        data = response.json()
        return data['aptos']['usd']
    except Exception as e:
        print("Error:", e)
        return None

# /start handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Ketik /aptos untuk melihat harga Aptos (APT) saat ini 💰")

# /aptos handler
async def aptos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    price = get_aptos_price()
    if price:
        await update.message.reply_text(f"Harga Aptos (APT) saat ini: ${price:.2f} USD 🔥")
    else:
        await update.message.reply_text("⚠️ Gagal mengambil data harga. Coba lagi nanti.")

# Main
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('aptos', aptos))

    print("Bot sedang berjalan...")
    app.run_polling()
