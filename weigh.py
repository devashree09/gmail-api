import nltk
from preprocess import preproces
from qucikstart import getEmails
from split_sentences import split_sentences

nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)


def weigh_sent(entry_email):
    stopwords = nltk.corpus.stopwords.words('english')
    word_frequencies = {}
    for sentence in entry_email:
        for word in nltk.word_tokenize(sentence):
            if word not in stopwords:
                if word not in word_frequencies.keys():
                    word_frequencies[word] = 1
                else:
                    word_frequencies[word] += 1
    
    maximum_frequncy = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
    
    sentence_scores = {}
    for sent in entry_email:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]
    entry_email = sentence_scores
    return entry_email


if __name__ == "__main__":
    email_data = getEmails()
    email_body = email_data['Body']
    ed = preproces(entry_email=email_body)
    sps = split_sentences(entry_email=ed)
    print(weigh_sent(sps))
