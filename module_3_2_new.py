def send_email(message, recipient, *, sender='university.help@gmail.com'):
    for i in recipient:
        if '.com' in recipient and '@' in recipient or '.ru' in recipient and '@' in recipient or '.net' in recipient and '@' in recipient:
            continue
        else:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
            break
    for j in sender:
        if '@' in sender and '.com' in sender or '@' in sender and '.ru' in sender or '@' in sender and '.net' in sender:
            if sender == recipient:
                print('Нельзя отправить письмо самому себе!')
            elif sender == 'university.help@gmail.com':
                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}!')
            else:
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
            break
        else:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
            break


send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
