from qucikstart import getEmails


def preproces(entry_email):
    email_en = entry_email
    lines = email_en.split()
    for j in reversed(range(len(lines))):
        lines[j] = lines[j].strip()
        if lines[j] == ' ':
            lines.pop(j)
    entry_email = ' '.join(lines)
    return entry_email


if __name__ == "__main__":
    email_data = getEmails()
    email_body = email_data['Body']
    print(preproces(entry_email=email_body))
