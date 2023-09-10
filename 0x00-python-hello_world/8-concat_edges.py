#!/usr/bin/python3

# Define the original sentence with a meaningful variable name
original_sentence = (
    "Python is an interpreted, interactive, object-oriented programming "
    "language that combines remarkable power with very clear syntax"
)

# Extract and concatenate the desired parts of the sentence
substring1 = original_sentence[39:67]
substring2 = original_sentence[107:112]
substring3 = original_sentence[:6]

result = f"{substring1}{substring2}{substring3}"

# Print the resulting string
print(result)
