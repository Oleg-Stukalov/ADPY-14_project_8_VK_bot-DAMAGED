from random import randrange
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

# API VK group key (VK_API_KEY)
#token = '4bb471afcdc67d358a9236856a96088364fa3e57b7d02bfbe6fe6f5cbff25a1c45b9130f8117d88b90c52'
token = input('Token: ')

# Authorization as group
vk = vk_api.VkApi(token=token)

# work with messages
longpoll = VkLongPoll(vk)


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message,  'random_id': randrange(10 ** 7),})

# main cycle
for event in longpoll.listen():
    # if we get new message
    if event.type == VkEventType.MESSAGE_NEW:

        # if message for bot
        if event.to_me:
            # message from user
            request = event.text

            # main bot algo
            if request == "привет":
                write_msg(event.user_id, f"Хай, {event.user_id}")
            elif request == "пока":
                write_msg(event.user_id, "Пока((")
            else:
                write_msg(event.user_id, "Не поняла вашего ответа...")