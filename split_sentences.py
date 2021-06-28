from qucikstart import getEmails 
from preprocess import preproces
from nltk.tokenize import sent_tokenize 

def split_sentences(entry_email):
    """
    Splits the emails into individual sentences
    """

    sentences = sent_tokenize(entry_email)
        
    entry_email = sentences
    return entry_email

if __name__ == "__main__":
    email_data = getEmails()
    email_body = email_data['Body']
    ed = preproces(entry_email = email_body)
    print(split_sentences (ed))


