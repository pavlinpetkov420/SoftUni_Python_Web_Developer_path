class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


class Mailbox:
    def __init__(self):
        self.emails = []

    def add_email(self, mail):
        self.emails.append(mail)

    def send_emails(self, indices):
        for i in indices:
            self.emails[i].send()

    def print_mailbox(self):
        for mail in self.emails:
            print(mail.get_info())


mailbox = Mailbox()
# Read emails
while True:
    command = input()
    if command == "Stop":
        break

    sender, receiver, content = command.split()
    email = Email(sender, receiver, content)
    mailbox.add_email(email)

# Send emails
sent_indices = [int(x) for x in input().split(", ")]

# Mark mails as read
mailbox.send_emails(sent_indices)

# Print the mailbox
mailbox.print_mailbox()

