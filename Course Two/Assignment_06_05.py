text = "X-DSPAM-Confidence:    0.8475"
found = text.find(':')

heart = text.find('5', found)

final = text[found+1:heart+1]
print(float(final))

# print(float(text[-7:]))
