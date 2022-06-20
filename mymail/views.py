from django.shortcuts import render

# Create your views here.
import imaplib, email


def Email(request):
    user = 'jitendrasharma'
    password = 'password'
    imap_url = 'sac.gov.in'
    # this is done to make SSL connection with GMAIL
    con = imaplib.IMAP4_SSL(imap_url, port=993)
    # # logging the user in
    con.login(user, password)
    # # calling function to check for email under this label
    con.select('Inbox')

    """
    # fetching emails from this user "tu**h*****1@gmail.com"
    key='FROM'
    value='san@sac.isro.gov.in'
    result, result_bytes = con.search(None, key, '"{}"'.format(value))
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.append(data)
    """
    msgs_subj=[]
    _, selected_mails = con.search(None, '(FROM "xscope@sac.isro.gov.in")')
    for num in selected_mails[0].split():
        _,data = con.fetch(num, '(RFC822)')
        _,bytes_data = data[0]
        email_msg = email.message_from_bytes(bytes_data)
        msgs_subj.append(email_msg["subject"])
        msgs_subj.append(email_msg["to"])
        
    
    return render(request, 'mymail/email.html', {'msgs':msgs_subj})
