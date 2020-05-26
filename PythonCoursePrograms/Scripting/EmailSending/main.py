import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path # os.path

def main():
    html = Template(Path('index.html').read_text())
    email = EmailMessage()
    email['from'] = 'Ryan Rosiak'
    email['to'] = 'ryan@gmail.com'
    email['subject'] = 'You won 1,000,000 dollars!'
    email.set_content('I am a Python Master!')

    email.set_content(html.substitute({'name': 'TinTin'}), 'html')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('ryan@gmail.com', 'YouWillNeverKnowMyPassword')
        smtp.send_message(email)
        print('All good boss')


if __name__ == '__main__':
    main();
