import requests

def send_complex_message(subject, address, content, attachment, api_key):
    return requests.post("https://api.mailgun.net/v3/mg.jkusdachurch.org/messages",
        auth=("api", api_key),
        files=[("attachment", ("Ganze Timeline.pdf", attachment))],
        data={"from": "JKUSDA Personal Ministries <pm@jkusdachurch.org>",
              "to": address,
              "subject": subject,
              "text": content})

def send_emails(addresses, contents, attachment):
    file = open("files/config.txt", "r")
    api_key = file.read()
    file.close
    responses = []
    for i in range(len(addresses)):
        if(addresses[i].find("students") == -1 & addresses[i].find("jkusda") == -1):
            print("Sending to " + addresses[i])
            response = send_complex_message("Another", addresses[i], contents[i], attachment, api_key)
            print("Sent!")
            responses.append(response)
    return responses

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