
import sys
import kasiskiutils as ku 

def analyze_lgram(lgram,text):
    # Search for l-grams in the given file
    lgram_pos=ku.get_lgram_pos(lgram,text)
    # Calculate distance between the same l-grams
    # Clear l-grams, if they are empty
    lgram_dists=ku.get_lgram_dist(ku.clear_lgram(lgram_pos))
    # Calculate gcds 
    lgram_gcds=ku.get_lgram_gcd(lgram_dists)
    # Clear l-grams, if they are empty
    lgram_gcds=ku.clear_lgram_gcd(lgram_gcds)
    # Count gcds occurrence percent
    # Sort dictionary 
    gcds_percent_dict=ku.sort_dict(ku.count_gcds_percent(lgram_gcds))
    return gcds_percent_dict
def print_top(dict_to_print, num=3):
    i=0
    for key in dict_to_print:
        if(i>=num):
            break
        i+=1
        print('{}: {}'.format(key,dict_to_print[key]))

# Check parameters
l=int(sys.argv[2])
if(l>3 or l<1):
    print('Invalid l-gram parametr. Use l=3 parametr by default')
    l=3
# Read file to analyze
file_name=sys.argv[1]
with open(file_name) as file:
    text = file.read()
# Data cleaning
text=text.replace('\n',' ')
text=text.replace(' ','')
text=text.lower()
# Generate l-grams
unigrams=ku.get_unigrams()
bigrams=ku.get_bigrams()
trigrams=ku.get_trigrams()
# Print possible key lengths
if(l==1):
    print_top(analyze_lgram(unigrams,text))
elif(l==2):
    print_top(analyze_lgram(bigrams,text))
elif(l==3):
    print_top(analyze_lgram(trigrams,text))


