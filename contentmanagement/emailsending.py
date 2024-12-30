from django.core.mail import EmailMessage
from email.mime.image import MIMEImage
import os
from django.conf import settings

def send_email(person_name, recipient_email_list):
    sender_mail = "yourstory@miccamerastories.com"
    subject = f"Story Submission Successful"
    
    # Email body with a placeholder for the image CID
    email_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Story Submission Confirmation</title>
    <style>
        body {{
            font-family: 'Verdana', sans-serif;
            color: #fff;
            background-color: #000;
            margin: 0;
            padding: 0;
        }}
        .container {{
            width: 100%;
            max-width: 650px;
            margin: 40px auto;
            padding: 30px;
            background-color: black;
            box-shadow: 0px 8px 25px rgba(0, 0, 0, 0.5);
            border-radius: 12px;
            text-align: center;
            border: 1px solid #333;
        }}
        .header img {{
            max-width: 120px;
            margin-bottom: 20px;
        }}
        .header h1 {{
            font-size: 28px;
            color: white;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 10px;
        }}
        .content {{
            padding: 20px;
            font-size: 18px;
            line-height: 1.8;
        }}
        .content h2 {{
            font-size: 24px;
            color: white;
            margin-bottom: 15px;
        }}
        .content p {{
            font-size: 16px;
            color: #ccc;
            margin-bottom: 20px;
        }}
        .content a {{
            color: #e50914;
            text-decoration: none;
            font-weight: bold;
            border-bottom: 1px solid #e50914;
            padding-bottom: 2px;
            transition: color 0.3s, border-color 0.3s;
        }}
        .content a:hover {{
            color: #fff;
            border-color: #fff;
        }}
        .footer {{
            font-size: 14px;
            color: #777;
            margin-top: 30px;
        }}
        .footer p {{
            margin: 5px 0;
        }}
        .footer a {{
            color: #e50914;
            text-decoration: none;
            font-weight: bold;
        }}
        .divider {{
            width: 80px;
            height: 3px;
            background-color: #e50914;
            margin: 20px auto;
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- Header with Logo -->
        <div class="header">
            <img src="cid:logo_image" name="Mic Camera Stories" alt="Mic Camera Stories Logo">
            <h1>Your Story, Your Voice</h1>
        </div>

        <div class="divider"></div>

        <!-- Content -->
        <div class="content">
            <h2>Hello, {person_name}!</h2>
            <p>Thank you for submitting your story to <strong>Mic Camera Stories</strong>! Your unique voice helps us grow a vibrant community of storytellers.</p>
            <p>Our team is reviewing your submission, and we'll get back to you shortly with updates. Stay tuned!</p>
            <p>If you have any questions, reach out to us anytime at <a href="mailto:miccamerastories@gmail.com">miccamerastories@gmail.com</a>.</p>
        </div>

        <div class="divider"></div>

        <!-- Footer -->
        <div class="footer">
            <p>Keep sharing your stories,</p>
            <p><strong>The Mic Camera Stories Team</strong></p>
            <p><a href="https://miccamerastories.com/" target="_blank">Visit Our Website</a></p>
        </div>
    </div>
</body>
</html>


    """

    # Prepare the email message
    email_message = EmailMessage(
        subject,
        email_html,
        sender_mail,
        recipient_email_list
    )

    # Attach the logo image saved in static files
    image_path = os.path.join(settings.BASE_DIR, 'static', 'img', 'logoforemail.png')
    with open(image_path, 'rb') as img_file:
        image = MIMEImage(img_file.read())
        image.add_header('Content-ID', '<logo_image>')  # The CID referenced in the HTML
        email_message.attach(image)

    # Set the email content type to HTML
    email_message.content_subtype = "html"

    try:
        # Send the email
        email_message.send(fail_silently=False)
    except Exception as e:
        print(f"Error sending email: {e}")
