import base64
import email
import imaplib
import quopri


def mail_read():
    mail_address = 'sea-of-max@yandex.ru'
    mail_pass = 'ppcmkhjkkxmmtmhj'

    imap_addr = 'imap.yandex.ru'

    connection = imaplib.IMAP4_SSL(imap_addr, 993)
    connection.login(mail_address, mail_pass)
    _, fldrs = connection.select('inbox')

    _, msgs = connection.uid('search', 'from', 'no-reply@sirius.online')

    latest_msg = msgs[0].split()[-1]

    _, data_msg = connection.uid('fetch', latest_msg, '(RFC822)')
    raw_msg = data_msg[0][1]
    # print(raw_msg)
    get_msg = email.message_from_bytes(raw_msg)
    # print('\n',get_msg)
    for part in get_msg.walk():
        if part.get_content_maintype() == 'text' and part.get_content_subtype() == 'plain':
            print(quopri.decodestring(part.get_payload()).decode('utf-8'))


mail_read()


# print('Agile' in str(mail_read()))
# print(str(mail_read()))