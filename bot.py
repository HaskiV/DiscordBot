import discord
import responses


# Отправляем сообщения
async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTA0OTcyMTAzNDkwOTE3MTcyMg.GgyT_t.B_KLT4pJChjEtj4mNRMtn9GoCiBCgwGwcotxhA'
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} запущен!')

    @client.event
    async def on_message(message):
        # Проверяем не застревает ли бот в цикле
        if message.author == client.user:
            return

        # Получаем данные о пользователе
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # Дебажим
        print(f"{username} сообщает: '{user_message}' ({channel})")

        # Если пользовательское сообщение содержит '?' перед сообщением
        if user_message[0] == '?':
            user_message = user_message[1:]  # [1:] Удаляет [?]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    # Запоминаем персональный токен
    client.run(TOKEN)