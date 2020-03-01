def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
 
    # LEARNER CODE START HERE
    frequencies = {}

    file_contents = file_contents.lower()

    words = file_contents.split()

    for word in words:
        if word not in uninteresting_words:
            if word.isalpha():
                if word not in frequencies:
                    frequencies[word] = 1
                else:
                    frequencies[word] += 1
#wordcloud



    print(frequencies)

    



print(calculate_frequencies(["hello my world","1.how are you??","I am good!","You are good","When are you coming"]))
    

    #["hello my world","how are you??","I am good!","You are good","When are you coming"]