def most_common_words(filepath, number_of_words=6):
    
    with open(filepath, "r") as f:
        word_list = f.read().split()

    for ind, word in enumerate(word_list):
        if ',' in word or '.' in word:
            word = word[:len(word) - 1]
        word_list[ind] = word.lower()
        
    most_common_amount = [0 for i in range(number_of_words)]
    most_common_list = ['' for i in range(number_of_words)]
    for word in word_list:
        amount = word_list.count(word)
        if amount > min(most_common_amount):
            ind = most_common_amount.index(min(most_common_amount))
            most_common_amount[ind] = amount
            most_common_list[ind] = word
        for i in range(amount):
            word_list.remove(word)
    
    return most_common_list