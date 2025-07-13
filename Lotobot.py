import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7349577271:AAEPXNPjaNeopIGefTQ9_yJfeoYkspMHg8k"  # Remplace par ton vrai token

# Fonction de base pour générer des numéros aléatoires
def generate_numbers(count: int) -> list:
    return sorted(random.sample(range(1, 91), count))

# Commande /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎰 Bienvenue sur le Bot Loto 🇨🇮!\n"
        "Voici les commandes disponibles :\n\n"
        "/standard - 🎯 1 numéro\n"
        "/doublechance - 🎯🎯 2 numéros\n"
        "/2n, /3n, /4n, /5n - Pour 2 à 5 numéros\n"
        "/turbo2, /turbo3, /turbo4, /turbo5 - Mode turbo 💨"
    )

# Générateurs standards
async def standard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nums = generate_numbers(1)
    await update.message.reply_text(f"🎯 Numéro : {nums[0]}")

async def double_chance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nums = generate_numbers(2)
    await update.message.reply_text(f"🎯 Double chance : {nums}")

async def num_handler(update: Update, context: ContextTypes.DEFAULT_TYPE, count: int):
    nums = generate_numbers(count)
    await update.message.reply_text(f"🎰 Voici {count} numéros : {nums}")

# Générateurs Turbo
async def turbo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE, count: int):
    nums = generate_numbers(count)
    message = "💨 TURBO MODE ACTIVÉ !\n🎰 Numéros générés :\n"
    message += " | ".join(str(n) for n in nums)
    await update.message.reply_text(message)

# Lancement du bot
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("standard", standard))
    app.add_handler(CommandHandler("doublechance", double_chance))
    app.add_handler(CommandHandler("2n", lambda u, c: num_handler(u, c, 2)))
    app.add_handler(CommandHandler("3n", lambda u, c: num_handler(u, c, 3)))
    app.add_handler(CommandHandler("4n", lambda u, c: num_handler(u, c, 4)))
    app.add_handler(CommandHandler("5n", lambda u, c: num_handler(u, c, 5)))
    app.add_handler(CommandHandler("turbo2", lambda u, c: turbo_handler(u, c, 2)))
    app.add_handler(CommandHandler("turbo3", lambda u, c: turbo_handler(u, c, 3)))
    app.add_handler(CommandHandler("turbo4", lambda u, c: turbo_handler(u, c, 4)))
    app.add_handler(CommandHandler("turbo5", lambda u, c: turbo_handler(u, c, 5)))

    print("✅ Bot lancé...")
    app.run_polling()
