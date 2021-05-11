from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import imaplib
import smtplib
import email
import os

class harpo:

    def __init__(self, email, password, server):
        """
            @brief Config of email

            @param [email]:    (String) User name.\n
            @param [password]: (String) Key of email.\n
            @param [server]:   (String) Server of email.\n
               index 0 = SMTP // index 1 = IMAP
        """
        self.email = email
        self.password = password
        self.server = server


    def send(self, destiny, subject, context, send_image=False, img=""):
        """
            @brief Send email for N destinations

            @param [destiny]: (List) User of destiny.\n
            @param [subject]: (String) Email subject.\n
            @param [context]: (String) Email context.\n
            @param [send_image]: (Bool) Send image.\n
               send_image = True // send_image = False (default)
            @param [img]: (String) Name image in "/home/rpasistel/RPA/".\n

            @return False/True
        """

        try:
            if len(self.server) > 1:
                server = self.server[1]
            if len(self.server) == 0:
                server = self.server[0]
            if send_image:
                img_data = open(img, 'rb').read()

                message = MIMEMultipart()
                message['subject'] = subject
                message['from'] = self.email
                message['to'] = destiny

                text = MIMEText(context)
                message.attach(text)
                image = MIMEImage(img_data, name=os.path.basename(img))
                message.attach(image)

            if send_image == False:
                message = MIMEText(context)
                message['subject'] = subject
                message['from'] = self.email
                message['to'] = destiny
            
            mail = smtplib.SMTP(server, 587)
            mail.login(self.email, self.password)
            mail.sendmail(self.email, destiny, message.as_string())
            mail.quit()
            
        
        

        except Exception as error:
            return error
        
        else:
            return True
    

    def __clean(self, mail_ids, mail):
        """
            @brief Internal method, clean inbox after obtained

            @param [mail_ids]: (List) Email received.\n
            @param [mail]:     (Class) Class of type IMAP4_SSL.\n
        """
        try:
            start = mail_ids[0].decode()
            end = mail_ids[-1].decode()
            print(end, start, "\n\n\n\n\n")
            mail.store(f'{start}:{end}'.encode(), 'FLAGS', '\\Deleted')
            mail.close()
            mail.logout()

        except Exception as error:
            print(error)
    

    def receive(self, filters="ALL"):
        """
            @brief Receive email of N destinations and delete it.

            @param [filters]: (String) Filter by time, from, text, ...
                filters = ALL (default)
            
            @return False/True
        """

        try:
            mail = imaplib.IMAP4(self.server[0])
            mail.login(self.email, self.password)
            mail.select('inbox')

            status, data = mail.search(None, filters.upper())
            mail_ids = []

            for block in data:

                mail_ids += block.split()

            for i in mail_ids:
                status, data = mail.fetch(i, '(RFC822)')

                for response_part in data:
                    if isinstance(response_part, tuple):

                        message = email.message_from_bytes(response_part[1])

                        mail_from = message['from']
                        mail_subject = message['subject']

                        if message.is_multipart():
                            mail_content = ''
                            
                            for part in message.get_payload():
                                

                                if part.get_content_type() == 'text/plain':
                                    mail_content += part.get_payload()
                        else:
                            mail_content = message.get_payload()


                        print(f'From: {mail_from}')
                        print(f'Subject: {mail_subject}')
                        print(f'Content: {mail_content}')
        except Exception as error:
            return error
        
        else:
            self.__clean(mail_ids, mail)
            return True
