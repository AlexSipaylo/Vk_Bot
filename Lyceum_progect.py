import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import time
import json

vk_session = vk_api.VkApi(token='624cc7fe6f3e5a795a1c6a9cbfb599f02f109f532704fcd8e39eecf848c7ba09e7da19d7ce0321cb108e1',
                          api_version=5.95)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, '195803251')

keyboard1 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "START"
                },
                "color": "negative"
            }
        ]
    ]
}
print(json.dumps(keyboard1, ensure_ascii=False))

keyboard2 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "55 BC"
                },
                "color": "negative"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "60 AD"
                },
                "color": "primary"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": "409 AD"
                },
                "color": "positive"
            }
        ]
    ]
}
print(json.dumps(keyboard2, ensure_ascii=False))

keyboard3 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Next question"
                },
                "color": "positive"
            }
        ]
    ]
}
print(json.dumps(keyboard3, ensure_ascii=False))

keyboard4 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "1066 AD"
                },
                "color": "negative"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "in the 8th century"
                },
                "color": "primary"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": "409 AD"
                },
                "color": "positive"
            }
        ]
    ]
}
print(json.dumps(keyboard4, ensure_ascii=False))

keyboard5 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Harold Hardrada"
                },
                "color": "negative"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Harold of England"
                },
                "color": "primary"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": "William of Normandy"
                },
                "color": "positive"
            }
        ]
    ]
}
print(json.dumps(keyboard5, ensure_ascii=False))

keyboard6 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Oliver Cromwell"
                },
                "color": "negative"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "King John"
                },
                "color": "primary"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": "Charles I"
                },
                "color": "positive"
            }
        ]
    ]
}
print(json.dumps(keyboard6, ensure_ascii=False))

keyboard7 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Latin"
                },
                "color": "negative"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "French"
                },
                "color": "primary"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": "English"
                },
                "color": "positive"
            }
        ]
    ]
}
print(json.dumps(keyboard7, ensure_ascii=False))

keyboard8 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Stratford-upon-Avon"
                },
                "color": "negative"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "London"
                },
                "color": "primary"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": "Liverpool"
                },
                "color": "positive"
            }
        ]
    ]
}
print(json.dumps(keyboard8, ensure_ascii=False))

keyboard9 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "1603"
                },
                "color": "negative"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "1567"
                },
                "color": "primary"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": "1588"
                },
                "color": "positive"
            }
        ]
    ]
}
print(json.dumps(keyboard9, ensure_ascii=False))

keyboard10 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "1763"
                },
                "color": "negative"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "1620"
                },
                "color": "primary"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": "1805"
                },
                "color": "positive"
            }
        ]
    ]
}
print(json.dumps(keyboard10, ensure_ascii=False))

keyboard11 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Henry III"
                },
                "color": "negative"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Oliver Cromwell"
                },
                "color": "primary"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": "Edward I"
                },
                "color": "positive"
            }
        ]
    ]
}
print(json.dumps(keyboard11, ensure_ascii=False))

keyboard12 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "cloth"
                },
                "color": "negative"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "machines"
                },
                "color": "primary"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": "food products"
                },
                "color": "positive"
            }
        ]
    ]
}
print(json.dumps(keyboard12, ensure_ascii=False))

keyboard13 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Yes"
                },
                "color": "positive"
            },

            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "No"
                },
                "color": "negative"
            }
        ]
    ]
}
print(json.dumps(keyboard13, ensure_ascii=False))

keyboard14 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "1756"
                },
                "color": "negative"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "1788"
                },
                "color": "primary"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": "1763"
                },
                "color": "positive"
            }
        ]
    ]
}
print(json.dumps(keyboard14, ensure_ascii=False))

keyboard15 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "1776"
                },
                "color": "negative"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "1806"
                },
                "color": "primary"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": "1798"
                },
                "color": "positive"
            }
        ]
    ]
}
print(json.dumps(keyboard15, ensure_ascii=False))

keyboard16 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "1789"
                },
                "color": "negative"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "1804"
                },
                "color": "primary"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": "1825"
                },
                "color": "positive"
            }
        ]
    ]
}
print(json.dumps(keyboard16, ensure_ascii=False))

keyboard17 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "1815"
                },
                "color": "negative"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "1914"
                },
                "color": "primary"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": "1805"
                },
                "color": "positive"
            }
        ]
    ]
}
print(json.dumps(keyboard17, ensure_ascii=False))

keyboard18 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "1899"
                },
                "color": "negative"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "1825"
                },
                "color": "primary"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": "1832"
                },
                "color": "positive"
            }
        ]
    ]
}
print(json.dumps(keyboard18, ensure_ascii=False))

keyboard19 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Scotland"
                },
                "color": "negative"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Wales"
                },
                "color": "primary"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": "The Republic of Ireland"
                },
                "color": "positive"
            }
        ]
    ]
}
print(json.dumps(keyboard19, ensure_ascii=False))

keyboard20 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "1906"
                },
                "color": "negative"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "1832"
                },
                "color": "primary"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": "1928"
                },
                "color": "positive"
            }
        ]
    ]
}
print(json.dumps(keyboard20, ensure_ascii=False))

keyboard21 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "1947"
                },
                "color": "negative"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "1945"
                },
                "color": "primary"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": "1940"
                },
                "color": "positive"
            }
        ]
    ]
}
print(json.dumps(keyboard21, ensure_ascii=False))

keyboard22 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "1798"
                },
                "color": "negative"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "1990s"
                },
                "color": "primary"
            }
        ],

        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": "1603"
                },
                "color": "positive"
            }
        ]
    ]
}
print(json.dumps(keyboard22, ensure_ascii=False))

keyboard23 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "1837"
                },
                "color": "negative"
            }
        ],
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "1997"
                },
                "color": "primary"
            }
        ],
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": "1939"
                },
                "color": "positive"
            }
        ]
    ]
}
print(json.dumps(keyboard23, ensure_ascii=False))

keyboard24 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Quit"
                },
                "color": "negative"
            }
        ]
    ]
}
print(json.dumps(keyboard22, ensure_ascii=False))

flag = True
while flag is True:
    count = 0
    while flag is True:
        count = 0
        for event in longpoll.listen():
            time.sleep(1.5)
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.object.text.lower() == 'hello' or event.object.text.lower() == 'hi' or \
                        event.object.text == 'Quit':
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message='Hello! 👋👋👋 Welcome to "The Quiz Bot".🇬🇧 In our quiz we will test your '
                                             'knowledge of the history of Great Britain. To start the quiz click START',
                                     keyboard=json.dumps(keyboard1, ensure_ascii=False), random_id=0)
                elif event.object.text.upper() == 'START':
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message='Question 1:\nWhen did Julius Caesar arrive in Britain?',
                                     keyboard=json.dumps(keyboard2, ensure_ascii=False),
                                     attachment="photo543376821_457239039", random_id=0)
                elif event.object.text == '55 BC':
                    vk.messages.send(peer_id=event.object.peer_id, message='Right',
                                     keyboard=json.dumps(keyboard3, ensure_ascii=False),
                                     attachment="audio649036550_456239017", random_id=0)
                    count += 1
                    break
                else:
                    vk.messages.send(peer_id=event.object.peer_id, message='Wrong.\nThe correct answer is 55 BC',
                                     keyboard=json.dumps(keyboard3, ensure_ascii=False),
                                     attachment="audio649036550_456239017", random_id=0)
                    break

        for event in longpoll.listen():
            time.sleep(1.5)
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.object.text == 'Next question':
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message='Question 2:\nWhen did the Roman army leave Britain?',
                                     keyboard=json.dumps(keyboard4, ensure_ascii=False),
                                     attachment="photo543376821_457239040", random_id=0)
                elif event.object.text == '409 AD':
                    vk.messages.send(peer_id=event.object.peer_id, message='Right',
                                     keyboard=json.dumps(keyboard3, ensure_ascii=False),
                                     attachment="audio649036550_456239018", random_id=0)
                    count += 1
                    break
                else:
                    vk.messages.send(peer_id=event.object.peer_id, message='Wrong.\nThe correct answer is 409 AD',
                                     keyboard=json.dumps(keyboard3, ensure_ascii=False),
                                     attachment="audio649036550_456239018", random_id=0)
                    break

        for event in longpoll.listen():
            time.sleep(1.5)
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.object.text == 'Next question':
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message='Question 3:\nWho won the Battle of Hastings?',
                                     keyboard=json.dumps(keyboard5, ensure_ascii=False),
                                     attachment="photo543376821_457239041", random_id=0)
                elif event.object.text == 'William of Normandy':
                    vk.messages.send(peer_id=event.object.peer_id, message='Right',
                                     keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=0)
                    count += 1
                    break
                else:
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message='Wrong.\nThe correct answer is William of Normandy',
                                     keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=0)
                    break

        for event in longpoll.listen():
            time.sleep(1.5)
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.object.text == 'Next question':
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message='Question 4:\nWhich ruler signed the Magna Carta?',
                                     keyboard=json.dumps(keyboard6, ensure_ascii=False),
                                     attachment="photo543376821_457239042", random_id=0)
                elif event.object.text == 'King John':
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message='Right', keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=0)
                    count += 1
                    break
                else:
                    vk.messages.send(peer_id=event.object.peer_id, message='Wrong.\nThe correct answer is King John',
                                     keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=0)
                    break

        for event in longpoll.listen():
            time.sleep(1.5)
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.object.text == 'Next question':
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message='Question 5:\n'
                                             'What language was the Bible read in during the rule of Henry VIII?',
                                     keyboard=json.dumps(keyboard7, ensure_ascii=False),
                                     attachment="photo543376821_457239043", random_id=0)
                elif event.object.text == 'English':
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message='Right', keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=0)
                    count += 1
                    break
                else:
                    vk.messages.send(peer_id=event.object.peer_id, message='Wrong.\nThe correct answer is English',
                                     keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=0)
                    break

        for event in longpoll.listen():
            time.sleep(1.5)
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.object.text == 'Next question':
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message='Question 6:\nWhere was William Shakespeare born?',
                                     keyboard=json.dumps(keyboard8, ensure_ascii=False),
                                     attachment="photo543376821_457239044", random_id=0)
                elif event.object.text == 'Stratford-upon-Avon':
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message='Right', keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=0)
                    count += 1
                    break
                else:
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message='Wrong.\nThe correct answer is Stratford-upon-Avon',
                                     keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=0)
                    break

        for event in longpoll.listen():
            time.sleep(1.5)
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.object.text == 'Next question':
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message='Question 7:\nWhen did Spanish ships try to attack England?',
                                     keyboard=json.dumps(keyboard9, ensure_ascii=False),
                                     attachment="photo543376821_457239045", random_id=0)
                elif event.object.text == '1588':
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message='Right', keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=0)
                    count += 1
                    break
                else:
                    vk.messages.send(peer_id=event.object.peer_id, message='Wrong.\nThe correct answer is 1588',
                                     keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=0)
                    break

        for event in longpoll.listen():
            time.sleep(1.5)
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.object.text == 'Next question':
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message='Question 8:\nWhen did a group of English Puritans sail '
                                             'to America in a boat called the Mayflower?',
                                     keyboard=json.dumps(keyboard10, ensure_ascii=False),
                                     attachment="photo543376821_457239046", random_id=0)
                elif event.object.text == '1620':
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message='Right', keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=0)
                    count += 1
                    break
                else:
                    vk.messages.send(peer_id=event.object.peer_id, message='Wrong.\nThe correct answer is 1620',
                                     keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=0)
                    break

        for event in longpoll.listen():
            time.sleep(1.5)
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.object.text == 'Next question':
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message='Question 9:\nWhich ruler was called ‘Lord Protector’?',
                                     keyboard=json.dumps(keyboard11, ensure_ascii=False),
                                     attachment="photo543376821_457239047", random_id=0)
                elif event.object.text == 'Oliver Cromwell':
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message='Right', keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=0)
                    count += 1
                    break
                else:
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message='Wrong.\nThe correct answer is Oliver Cromwell',
                                     keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=0)
                    break

        for event in longpoll.listen():
            time.sleep(1.5)
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.object.text == 'Next question':
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message='Question 10:\nWhat did the world’s first factories produce?',
                                     keyboard=json.dumps(keyboard12, ensure_ascii=False),
                                     attachment="photo543376821_457239048", random_id=0)
                elif event.object.text == 'cloth':
                    vk.messages.send(peer_id=event.object.peer_id, message='Right', random_id=0)
                    count += 1
                    vk.messages.send(peer_id=event.object.peer_id, message='Would you like to continue?',
                                     keyboard=json.dumps(keyboard13, ensure_ascii=False), random_id=0)
                    break
                else:
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message='Wrong.\nThe correct answer is cloth', random_id=0)
                    vk.messages.send(peer_id=event.object.peer_id, message='Would you like to continue?',
                                     keyboard=json.dumps(keyboard13, ensure_ascii=False), random_id=0)
                    break

        for event in longpoll.listen():
            time.sleep(1.5)
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.object.text == 'No':
                    score = count / 10 * 100
                    score = int(score)
                    Wrong_answers = 10 - count
                    if score == 100:
                        vk.messages.send(peer_id=event.object.peer_id,
                                         message=f'SCORE: {score}%  Congratulations! Perfect!\n'
                                                 'Total questions: 10\n'
                                                 f'Correct answers: {count}\n'
                                                 f'Wrong answers: {Wrong_answers}',
                                         keyboard=json.dumps(keyboard24, ensure_ascii=False), random_id=0)
                        break

                    elif score in range(90, 96):
                        vk.messages.send(peer_id=event.object.peer_id,
                                         message=f'SCORE: {score}%  Excellent but not perfect:)\n'
                                                 'Total questions: 10\n'
                                                 f'Correct answers: {count}\n'
                                                 f'Wrong answers: {Wrong_answers}',
                                         keyboard=json.dumps(keyboard24, ensure_ascii=False), random_id=0)
                        break

                    elif score in range(80, 86):
                        vk.messages.send(peer_id=event.object.peer_id,
                                         message=f'SCORE: {score}%  Very Good!\n'
                                                 'Total questions: 10\n'
                                                 f'Correct answers: {count}\n'
                                                 f'Wrong answers: {Wrong_answers}',
                                         keyboard=json.dumps(keyboard24, ensure_ascii=False), random_id=0)
                        break

                    elif score in range(60, 76):
                        vk.messages.send(peer_id=event.object.peer_id,
                                         message=f'SCORE: {score}%  Good!\n'
                                                 'Total questions: 10\n'
                                                 f'Correct answers: {count}\n'
                                                 f'Wrong answers: {Wrong_answers}',
                                         keyboard=json.dumps(keyboard24, ensure_ascii=False), random_id=0)
                        break

                    elif score in range(50, 56):
                        vk.messages.send(peer_id=event.object.peer_id,
                                         message=f'SCORE: {score}%  Satisfactory\n'
                                                 'Total questions: 10\n'
                                                 f'Correct answers: {count}\n'
                                                 f'Wrong answers: {Wrong_answers}',
                                         keyboard=json.dumps(keyboard24, ensure_ascii=False), random_id=0)
                        break

                    elif score in range(25, 36):
                        vk.messages.send(peer_id=event.object.peer_id,
                                         message=f'SCORE: {score}%  Near Fail\n'
                                                 'Total questions: 10\n'
                                                 f'Correct answers: {count}\n'
                                                 f'Wrong answers: {Wrong_answers}',
                                         keyboard=json.dumps(keyboard24, ensure_ascii=False), random_id=0)
                        break

                    elif score in range(0, 21):
                        vk.messages.send(peer_id=event.object.peer_id,
                                         message=f'SCORE: {score}%  Fail\n'
                                                 'Total questions: 10\n'
                                                 f'Correct answers: {count}\n'
                                                 f'Wrong answers: {Wrong_answers}',
                                         keyboard=json.dumps(keyboard24, ensure_ascii=False), random_id=0)
                        break

                elif event.object.text == 'Yes':
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message='Question 11:\nWhen did Britain defeat France in the Seven Years’ War?',
                                     keyboard=json.dumps(keyboard14, ensure_ascii=False), random_id=0)
                elif event.object.text == '1763':
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message='Right', keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=0)
                    count += 1
                    flag = False
                    break
                else:
                    vk.messages.send(peer_id=event.object.peer_id, message='Wrong.\nThe correct answer is 1763',
                                     keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=0)
                    flag = False
                    break
    flag = True
    for event in longpoll.listen():
        time.sleep(1.5)
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.object.text == 'Next question':
                vk.messages.send(peer_id=event.object.peer_id,
                                 message='Question 12:\nWhen did America become independent from Britain?',
                                 keyboard=json.dumps(keyboard15, ensure_ascii=False), random_id=0)
            elif event.object.text == '1776':
                vk.messages.send(peer_id=event.object.peer_id,
                                 message='Right', keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=0)
                count += 1
                break
            else:
                vk.messages.send(peer_id=event.object.peer_id, message='Wrong.\nThe correct answer is 1776',
                                 keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=0)
                break

    for event in longpoll.listen():
        time.sleep(1.5)
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.object.text == 'Next question':
                vk.messages.send(peer_id=event.object.peer_id,
                                 message='Question 13:\nWhen was the world’s first railway built?',
                                 keyboard=json.dumps(keyboard16, ensure_ascii=False), random_id=0)
            elif event.object.text == '1804':
                vk.messages.send(peer_id=event.object.peer_id,
                                 message='Right', keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=0)
                count += 1
                break
            else:
                vk.messages.send(peer_id=event.object.peer_id, message='Wrong.\nThe correct answer is 1804',
                                 keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=0)
                break

    for event in longpoll.listen():
        time.sleep(1.5)
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.object.text == 'Next question':
                vk.messages.send(peer_id=event.object.peer_id,
                                 message='Question 14:\nWhen did the Battle of Trafalgar take place?',
                                 keyboard=json.dumps(keyboard17, ensure_ascii=False), random_id=0)
            elif event.object.text == '1805':
                vk.messages.send(peer_id=event.object.peer_id,
                                 message='Right', keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=0)
                count += 1
                break
            else:
                vk.messages.send(peer_id=event.object.peer_id, message='Wrong.\nThe correct answer is 1805',
                                 keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=0)
                break

    for event in longpoll.listen():
        time.sleep(1.5)
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.object.text == 'Next question':
                vk.messages.send(peer_id=event.object.peer_id,
                                 message='Question 15:\nWhen did workers form their first trade union?',
                                 keyboard=json.dumps(keyboard18, ensure_ascii=False), random_id=0)
            elif event.object.text == '1825':
                vk.messages.send(peer_id=event.object.peer_id,
                                 message='Right', keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=0)
                count += 1
                break
            else:
                vk.messages.send(peer_id=event.object.peer_id, message='Wrong.\nThe correct answer is 1825',
                                 keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=0)
                break

    for event in longpoll.listen():
        time.sleep(1.5)
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.object.text == 'Next question':
                vk.messages.send(peer_id=event.object.peer_id,
                                 message='Question 16:\nWhich is not a part of the United Kingdom?',
                                 keyboard=json.dumps(keyboard19, ensure_ascii=False), random_id=0)
            elif event.object.text == 'The Republic of Ireland':
                vk.messages.send(peer_id=event.object.peer_id,
                                 message='Right', keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=0)
                count += 1
                break
            else:
                vk.messages.send(peer_id=event.object.peer_id,
                                 message='Wrong.\nThe correct answer is The Republic of Ireland',
                                 keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=0)
                break

    for event in longpoll.listen():
        time.sleep(1.5)
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.object.text == 'Next question':
                vk.messages.send(peer_id=event.object.peer_id,
                                 message='Question 17:\nWhen did rules for women and men become the same?',
                                 keyboard=json.dumps(keyboard20, ensure_ascii=False), random_id=0)
            elif event.object.text == '1928':
                vk.messages.send(peer_id=event.object.peer_id,
                                 message='Right', keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=0)
                count += 1
                break
            else:
                vk.messages.send(peer_id=event.object.peer_id, message='Wrong.\nThe correct answer is 1928',
                                 keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=0)
                break

    for event in longpoll.listen():
        time.sleep(1.5)
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.object.text == 'Next question':
                vk.messages.send(peer_id=event.object.peer_id,
                                 message='Question 18:\nWhen did India and Pakistan become independent from Britain?',
                                 keyboard=json.dumps(keyboard21, ensure_ascii=False), random_id=0)
            elif event.object.text == '1947':
                vk.messages.send(peer_id=event.object.peer_id,
                                 message='Right', keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=0)
                count += 1
                break
            else:
                vk.messages.send(peer_id=event.object.peer_id, message='Wrong.\nThe correct answer is 1947',
                                 keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=0)
                break

    for event in longpoll.listen():
        time.sleep(1.5)
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.object.text == 'Next question':
                vk.messages.send(peer_id=event.object.peer_id, message='Question 19:\nWhen were the Scots, Welsh and '
                                                                       'Northern Irish given their own parliaments?',
                                 keyboard=json.dumps(keyboard22, ensure_ascii=False), random_id=0)
            elif event.object.text == '1990s':
                vk.messages.send(peer_id=event.object.peer_id,
                                 message='Right', keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=0)
                count += 1
                break
            else:
                vk.messages.send(peer_id=event.object.peer_id, message='Wrong.\nThe correct answer is 1990s',
                                 keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=0)
                break

    for event in longpoll.listen():
        time.sleep(1.5)
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.object.text == 'Next question':
                vk.messages.send(peer_id=event.object.peer_id,
                                 message='Question 20:\nWhen did Hong Kong become part of China?',
                                 keyboard=json.dumps(keyboard23, ensure_ascii=False), random_id=0)
            elif event.object.text == '1997':
                vk.messages.send(peer_id=event.object.peer_id, message='Right', random_id=0)
                count += 1
                score1 = count / 20 * 100
                score1 = int(score1)
                Wrong_answers1 = 20 - count
                if score1 == 100:
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message=f'SCORE: {score1}%  Congratulations! Perfect!'
                                             'Total questions : 20'
                                             f'Correct answers: {count}'
                                             f'Wrong answers : {Wrong_answers1}',
                                     keyboard=json.dumps(keyboard24, ensure_ascii=False), random_id=0)
                    break

                elif score1 in range(90, 96):
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message=f'SCORE: {score1}%  Excellent but not perfect:)'
                                             'Total questions: 20'
                                             f'Correct answers: {count}'
                                             f'Wrong answers: {Wrong_answers1}',
                                     keyboard=json.dumps(keyboard24, ensure_ascii=False), random_id=0)
                    break

                elif score1 in range(80, 86):
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message=f'SCORE: {score1}%  Very Good!'
                                             'Total questions: 20'
                                             f'Correct answers: {count}'
                                             f'Wrong answers: {Wrong_answers1}',
                                     keyboard=json.dumps(keyboard24, ensure_ascii=False), random_id=0)
                    break

                elif score1 in range(60, 76):
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message=f'SCORE: {score1}%  Good!'
                                             'Total questions: 20'
                                             f'Correct answers: {count}'
                                             f'Wrong answers: {Wrong_answers1}',
                                     keyboard=json.dumps(keyboard24, ensure_ascii=False), random_id=0)
                    break

                elif score1 in range(50, 56):
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message=f'SCORE: {score1}%  Satisfactory'
                                             'Total questions: 20'
                                             f'Correct answers: {count}'
                                             f'Wrong answers: {Wrong_answers1}',
                                     keyboard=json.dumps(keyboard24, ensure_ascii=False), random_id=0)
                    break

                elif score1 in range(25, 36):
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message=f'SCORE: {score1}%  Near Fail'
                                             'Total questions: 20'
                                             f'Correct answers: {count}'
                                             f'Wrong answers: {Wrong_answers1}',
                                     keyboard=json.dumps(keyboard24, ensure_ascii=False), random_id=0)
                    break

                elif score1 in range(0, 21):
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message=f'SCORE: {score1}%  Fail'
                                             'Total questions: 20'
                                             f'Correct answers: {count}'
                                             f'Wrong answers: {Wrong_answers1}',
                                     keyboard=json.dumps(keyboard24, ensure_ascii=False), random_id=0)
                    break
            else:
                vk.messages.send(peer_id=event.object.peer_id,
                                 message='Wrong.                                                                    '
                                         'The correct answer is 1997', random_id=0)
                score1 = count / 20 * 100
                score1 = int(score1)
                Wrong_answers1 = 20 - count
                if score1 == 100:
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message=f'SCORE: {score1}%  Congratulations! Perfect!'
                                             'Total questions : 20'
                                             f'Correct answers: {count}'
                                             f'Wrong answers : {Wrong_answers1}',
                                     keyboard=json.dumps(keyboard24, ensure_ascii=False), random_id=0)
                    break

                elif score1 in range(90, 96):
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message=f'SCORE: {score1}%  Excellent but not perfect:)'
                                             'Total questions: 20'
                                             f'Correct answers: {count}'
                                             f'Wrong answers: {Wrong_answers1}',
                                     keyboard=json.dumps(keyboard24, ensure_ascii=False), random_id=0)
                    break

                elif score1 in range(80, 86):
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message=f'SCORE: {score1}%  Very Good!'
                                             'Total questions: 20'
                                             f'Correct answers: {count}'
                                             f'Wrong answers: {Wrong_answers1}',
                                     keyboard=json.dumps(keyboard24, ensure_ascii=False), random_id=0)
                    break

                elif score1 in range(60, 76):
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message=f'SCORE: {score1}%  Good!'
                                             'Total questions: 20'
                                             f'Correct answers: {count}'
                                             f'Wrong answers: {Wrong_answers1}',
                                     keyboard=json.dumps(keyboard24, ensure_ascii=False), random_id=0)
                    break

                elif score1 in range(50, 56):
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message=f'SCORE: {score1}%  Satisfactory'
                                             'Total questions: 20'
                                             f'Correct answers: {count}'
                                             f'Wrong answers: {Wrong_answers1}',
                                     keyboard=json.dumps(keyboard24, ensure_ascii=False), random_id=0)
                    break

                elif score1 in range(25, 36):
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message=f'SCORE: {score1}%  Near Fail'
                                             'Total questions: 20'
                                             f'Correct answers: {count}'
                                             f'Wrong answers: {Wrong_answers1}',
                                     keyboard=json.dumps(keyboard24, ensure_ascii=False), random_id=0)
                    break

                elif score1 in range(0, 21):
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message=f'SCORE: {score1}%  Fail'
                                             'Total questions: 20'
                                             f'Correct answers: {count}'
                                             f'Wrong answers: {Wrong_answers1}',
                                     keyboard=json.dumps(keyboard24, ensure_ascii=False), random_id=0)
                    break
