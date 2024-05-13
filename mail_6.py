import smtplib
def mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('shramanjoardar@gmail.com','xxxxxxxxxxxxxx')
    
    subject = "PRICE DROP ALERT"
    body = " iPHONE 15  in Flipkart has a price drop , check it out Shraman"
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail('smtp.gmail.com', 'shramanjoardar@gmail.com', msg)
