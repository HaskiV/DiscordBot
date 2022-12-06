import random


def handle_response(message) -> str:
    p_message = message.lower()
    if p_message == 'Привет!':
        return 'Ну привет! Что будет делать?'

    if p_message == 'roll' or p_message == 'кости':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return "`Я тебе помогу!.`"