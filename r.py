# import re
# str = '3 for 200.99'
# p = r'\d+.\d'
# match = re.search(p, str)
#
# print(match.group())
from aspose.email import ImapClient
"""import base64
import email
import imaplib
from email.header import decode_header

mail_adress = 'sea-of-max@yandex.ru'
mail_pass = 'ppcmkhjkkxmmtmhj'

mail = imaplib.IMAP4_SSL('imap.yandex.ru')
mail.login(mail_adress, mail_pass)
mail.list()
mail.select('inbox')

result, data = mail.search(None, 'unseen')
ids = data[0]
ids_list = ids.split()
latest_mail = ids_list[-1]

res, data = mail.fetch(latest_mail, "(RFC822)")
msg_data = data[0][1]

text = ''
new_list = []
payload = msg_data.get_payload()
for part in payload:
  print(part.get_content_type())

# for part in msg.walk():
#     if part.get_content_maintype() == 'text' and part.get_content_subtype() == 'plain':
#         text += base64.b64decode(part.get_payload()).decode()


print(new_list)"""

with ImapClient("imap.gmail.com", 993, "username", "password") as client:

    # get list of folders
    folderInfoColl = client.list_folders()