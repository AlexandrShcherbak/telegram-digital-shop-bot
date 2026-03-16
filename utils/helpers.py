def send_message(chat_id, text, bot):
    bot.send_message(chat_id, text)

def log_activity(activity):
    with open('activity.log', 'a') as log_file:
        log_file.write(f"{activity}\n")

def format_price(price):
    return f"${price:.2f}"