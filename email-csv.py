To email a CSV file using Sendgrid in Python, you will need to install the SendGrid package, which you can do by running the following command:

Copy code
pip install sendgrid
Once you have installed the SendGrid package, you can use the following Python program to email a CSV file using SendGrid:

python
Copy code
import os
import csv
import sendgrid
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition

# Define the SendGrid API key
sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))

# Define the sender, recipient, subject, and message body
from_email = 'sender@example.com'
to_email = 'recipient@example.com'
subject = 'Emailing CSV file using SendGrid'
html_content = '<p>Hi, Please find attached the CSV file.</p>'

# Read the CSV file
with open('data.csv', 'r') as file:
    csv_data = file.read()

# Create the attachment
attachment = Attachment()
attachment.file_content = FileContent(csv_data)
attachment.file_name = FileName('data.csv')
attachment.file_type = FileType('text/csv')
attachment.disposition = Disposition('attachment')

# Create the email message and attach the file
message = Mail(
    from_email=from_email,
    to_emails=to_email,
    subject=subject,
    html_content=html_content)
message.attachment = attachment

# Send the email message
response = sg.send(message)

# Print the response status code and body
print(response.status_code)
print(response.body)


In the above program, you first import the required modules, including the SendGrid package. You then define the SendGrid API key, sender and recipient email addresses, subject, and message body.

Next, you read the CSV file and create an attachment object with the CSV data. You then create the email message and attach the file to it. Finally, you send the email message using the send method of the SendGrid API client and print the response status code and body.

Make sure to replace the SENDGRID_API_KEY, sender@example.com, recipient@example.com, and data.csv placeholders with your own values.


