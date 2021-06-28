import heapq
from weigh import weigh_sent
from preprocess import preproces
from qucikstart import getEmails
from split_sentences import split_sentences


def summarize(entry_email):
    summary_sentences = heapq.nlargest(7, entry_email, key=entry_email.get)
    summary = ' '.join(summary_sentences)
    entry_email = summary
    return entry_email


if __name__ == "__main__":
    email_data = getEmails()
    email_body = email_data['Body']
    email_sender = email_data['Sender']
    email_subject = email_data['Subject']
    body_preprocessed = preproces(entry_email=email_body)
    sentence_split = split_sentences(entry_email=body_preprocessed)
    sentence_weights = weigh_sent(entry_email=sentence_split)
    email_summary = summarize(sentence_weights)
    print(f"Subject: {email_subject}\nSender: {email_sender}\nSummary: {email_summary}")
    