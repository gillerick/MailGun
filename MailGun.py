import requests

def send_complex_message(subject, address, content, attachment):
    return requests.post("https://api.mailgun.net/v3/mg.jkusdachurch.org/messages",
        auth=("api", "key-61cdc7861e0d1365aa4e91dafb5ba6b4"),
        files=[("attachment", ("Ganze Timeline.pdf", attachment))],
        data={"from": "JKUSDA Personal Ministries <pm@jkusdachurch.org>",
              "to": address,
              "subject": subject,
              "text": content})

def get_addresses():
    file = open("files/emails.txt","r")
    addresses = []
    for line in file:
        addresses.append(line.split()[0])
    file.close
    return addresses

def get_names():
    file = open("files/names.txt","r")
    names = []
    for line in file:
        names.append(line.split()[0])
    file.close
    return names

def cust_emails(names):
    file = open("files/content.txt","r")
    template = file.read()
    cust = []
    for name in names:
        cust.append(template.replace("{{name}}", name))
    file.close
    return cust

def get_attachment():
    file = open("files/Ganze_Timeline.pdf","rb")
    attachment = file.read()
    file.close
    return attachment

def send_emails(addresses, contents, attachment):
    responses = []
    for i in range(len(addresses)):
        if(addresses[i].find("students") == -1 & addresses[i].find("jkusda") == -1):
            responses.append(send_complex_message("Another", addresses[i],contents[i],attachment))
    return responses

def log_responses(responses):
    file = open("files/log.txt","a")
    for response in responses:
        file.write(str(response))
        file.write("\n")
    file.close
    return

addresses = get_addresses()
names = get_names()
emails = cust_emails(names)
attachment = get_attachment()
responses = send_emails(addresses, emails, attachment)
log_responses(responses)