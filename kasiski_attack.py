import sys
import kasiskiutils as ku 

# Get predicted key length
pred_key_len=int(sys.argv[2])
# Read file to analyze
file_name=sys.argv[1]
with open(file_name) as file:
    text = file.read()
# Data cleaning
text=text.replace('\n',' ')
text=text.replace(' ','')
text=text.lower()
# Divide text into pred_key_len-parts
ch_texts_shifted=[]
for i in range(0,pred_key_len):
    ch_texts_shifted+=[text[i::pred_key_len]]
# Suggest key
suggested_key=''
en_alphabet=ku.get_en_alphabet()
en_letter_freq=ku.get_avg_letter_freq_percent()
for i in range(pred_key_len):
    suggested_key+=en_alphabet[ku.get_shift(ku.get_letter_freq_percent(ch_texts_shifted[i]),en_letter_freq)]
print(suggested_key)