alice_text = ("alice in wonder land land land")

with open("alice_in_wonderland.txt", "r", encoding="utf-8") as f:
   alice_text = f.read()
    
alice_words = alice_text.split()
words_count_results = {}
# counting each word in word_counts._results 
for word in alice_words:
    # makes lower/upper case not matter
    word = word.lower()
    word = word.replace("\"", "")
    word = word.replace(")", "")
    word = word.replace("(", "")
    word = word.replace("--", "")
    word = word.replace("`", "")
    word = word.replace(";", "")
    word = word.replace(".", "")
    word = word.replace(":", "")
    word = word.replace(",", "")
    word = word.replace("!", "")
    word = word.replace("[", "")
    word = word.replace("]", "")
    word = word.replace("\t", "")
    # word = word.replace("'", "")
    if word in words_count_results:
        words_count_results[word] = words_count_results[word] + 1
    else: 
        #the word was not it the map, so it will be 1 
        words_count_results[word] = 1 
        
words_count_results = {k: v for k, v in sorted(words_count_results.items())}
print("Word\t\t\tCount")
print("=============================")
for key, value in words_count_results.items():
    print(f"{key} \t\t\t {value}")
