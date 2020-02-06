# Program that reads input string, removes leading & trailing 'spaces',
# makes letters lowercase, also outputs the length of the inputted and outputted string.

raw_string = input("Enter string:")

normalized_string= raw_string.strip().lower()

len_raw_string = len(raw_string)
len_normalized_string = len(normalized_string)

print("Normalized string = {}".format(normalized_string) )
print("We have reduced the sting length from {} to {}".format(len_raw_string, len_normalized_string))
