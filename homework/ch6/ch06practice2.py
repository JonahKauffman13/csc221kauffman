input_string = input("Input a string:")
results_dict = {}
# using ascii to set dictionary values
for xx in range(97,123):
    results_dict[chr(xx)] = 0

input_string.lower()
# loop through input string 1 char at a time 
for char in input_string:
    if char in results_dict:
        current_char_count = results_dict[char]
        current_char_count = current_char_count + 1
        results_dict[char] = current_char_count
        
for key, value in results_dict.items():
    print(f"{key}  {value}") 
