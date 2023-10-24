usage_message = '''
Welcome to the email system! What would you like to do?

s - send email.
l - list emails from a sender.
r - read email.
m - mark email as spam.
gu - get unread emails.
gs - get spam emails.
d - delete email.
e - exit this program.
'''
#An Email Simulation

user_choice = ""
class Email():
    def __init__(self, sender_address, subject_line, contents):
        self.sender_address = sender_address
        self.subject_line = subject_line
        self.contents = contents       
        self.has_been_read = False
        self.is_spam = False

    def __str__(self):
        return f"From: {self.sender_address}\nSubject: {self.subject_line}\nContent: {self.contents}\nRead status: {self.has_been_read}\nSpam status: {self.is_spam}\n"
    
    def mark_as_read(self):
           self.has_been_read =  True
    
    def mark_spam(self):
            self.is_spam = True

class Inbox(): 

    def __init__(self):
        self.emails = []

    def add_email(self, new_email):
        self.emails.append(new_email)
        pass

    def list_messages_from_sender(self, sender_address):
            for pos, obj in enumerate(self.emails):
                if sender_address == obj.sender_address:
                       output = f'\n' 
                       output = f' {pos} {obj.sender_address}'
                       output = f' {pos} {obj.subject_line}' 
                       print(output)
                                
    def get_email(self, sender_address, index):
        sender_emails = []
        for pos, obj in enumerate(self.emails):
           if obj.sender_address == sender_address and pos == index:
              obj.mark_as_read()
              sender_emails.append(obj)  
        return sender_emails[index]
    
    def mark_as_spam(self, sender_address, index):
        for pos, obj in enumerate(self.emails):
           if obj.sender_address == sender_address and pos == index:
                obj.is_spam = True
                
    def get_unread(self):
        for email in self.emails:
           if email.has_been_read == False :
               print(email.sender_address, email.subject_line, email.contents) 

    def get_spam (self):
        for email in self.emails:
           if email.is_spam == True:
              print(email.sender_address, email.subject_line, email.contents)  
    
    def delete(self,sender_address, index) : 
        for email in self.emails:
           if email.sender_address == sender_address and email_index == index:
                 self.emails.remove(email)

inbox_object = Inbox()

while True:
    user_choice = input(usage_message).strip().lower()
    if user_choice == "s":
        # Send an email (Create a new Email object)
        sender_address = input(str("Please enter the address of the sender\n:"))
        subject_line = input(str("Please enter the subject line of the email\n:"))
        contents = input(str("Please enter the contents of the email\n:"))
        new_email = Email(sender_address, subject_line, contents)

        # Now add the email to the Inbox
        inbox_object.add_email(new_email)

        # Print a success message
        print("Email has been added to inbox.")
        pass

    elif user_choice == "l":
        # List all emails from a sender_address
        sender_address = input(str("Please enter the address of the sender\n:"))
        # Now list all emails from this sender
        inbox_object.list_messages_from_sender(sender_address)
        pass

    elif user_choice == "r":
        # Read an email

        # Step 1: show emails from the sender
        sender_address = input("Please enter the address of the sender of the email\n:")
        
        # Step 2: show all emails from this sender (with indexes)
        inbox_object.list_messages_from_sender(sender_address)
        
        # Step 3: ask the user for the index of the email
        email_index = int(input("Please enter the index of the email that you would like to read\n:"))
        index = email_index
        # Step 4: display the email
        inbox_object.get_email(sender_address, index)
        pass
    
    elif user_choice == "m":
        # Mark an email as spam
        # Step 1: show emails from the sender
        sender_address = input("Please enter the address of the sender of the email\n:")

        # Step 2: show all emails from this sender (with indexes)
        inbox_object.list_messages_from_sender(sender_address)

        # Step 3: ask the user for the index of the email
        email_index = int(input("Please enter the index of the email that you would like to read\n:"))
        index = email_index

        # Step 4: mark the email as spam
        inbox_object.mark_as_spam(sender_address, index)

        # Step 5: print a success message
        print("Email has been marked as spam")
        pass

    elif user_choice == "gu":
        # List all unread emails
        inbox_object.get_unread()
        pass

    elif user_choice == "gs":
        # List all spam emails
        inbox_object.get_spam()
        pass

    elif user_choice == "e":
        print("Goodbye")
        break

    elif user_choice == "d":
        # Delete an email
        # Step 1: show emails from the sender
        sender_address = input("Please enter the address of the sender of the email\n:")

        # Step 2: show all emails from this sender (with indexes)
        inbox_object.list_messages_from_sender(sender_address)

        # Step 3: ask the user for the index of the email
        email_index = int(input("Please enter the index of the email to be deleted\n:"))
        index = email_index

        # Step 4: delete the email
        inbox_object.delete(sender_address, index)

        # Step 5: print a success message
        print("Email has been deleted")
        pass
    else:
        print("Oops - incorrect input")

