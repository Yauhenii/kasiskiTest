import math
import string
import re

# Generate unigrams
def get_unigrams():
    return list(string.ascii_lowercase)

# Generate bigrams
def get_bigrams():
    return [i+j for i in string.ascii_lowercase for j in string.ascii_lowercase]

# Generate trigrams
def get_trigrams():
    return [i+j+k for i in string.ascii_lowercase for j in string.ascii_lowercase for k in string.ascii_lowercase]

# Generate fourgrams
def get_fourgrams():
    return [i+j+k+p for i in string.ascii_lowercase for j in string.ascii_lowercase for k in string.ascii_lowercase for p in string.ascii_lowercase]

# Generate fivegrams
def get_fivegrams():
    return [i+j+k+p+q for i in string.ascii_lowercase for j in string.ascii_lowercase for k in string.ascii_lowercase for p in string.ascii_lowercase for q in string.ascii_lowercase]

# Get letter frequence 
def get_letter_freq(text):
    
    freq_dict = dict.fromkeys(string.ascii_lowercase, 0)
    for ch in text:
        if ch in freq_dict:
            freq_dict[ch]+=1
    return freq_dict

# Get letter frequence in percentage
def get_letter_freq_percent(text):
    text_len=len(text)
    freq_dict=get_letter_freq(text)
    for key in freq_dict:
        freq_dict[key]=freq_dict[key]/text_len
    return freq_dict

# Get l-gram
def get_lgram_pos(lgrams, text):
    return [[lgram,[m.start() for m in re.finditer(lgram, text)]] for lgram in lgrams]

# Get rid of empty l-grams
def clear_lgram(lgram_pos):
    clrd_lgram_pos=[i for i in lgram_pos if len(i[1])>1]
    return clrd_lgram_pos

# Get rid of empty l-gram gcds
def clear_lgram_gcd(lgram_gcds):
    clrd_lgram_gcds=[i for i in lgram_gcds if len(i[1])>0]
    return clrd_lgram_gcds

# Get l-gram distances 
def get_lgram_dist(lgram_pos):
    lgram_dist=[[i[0],calc_dist(i[1])] for i in lgram_pos]
    return lgram_dist

# Calculate distances between the same l-grams 
def calc_dist(pos_list):
    dist_list=[]
    for j in range(len(pos_list)-1):
        dist_list+=[pos_list[j+1]-pos_list[j]]
    return dist_list

# Get l-gram gcds 
def get_lgram_gcd(lgram_dists):
    lgram_gcds=[[i[0],calc_gcd(i[1])] for i in lgram_dists]
    return lgram_gcds

# Calculate gcds ONLY between different l-grams and one time ONLY 
def calc_gcd(dist_list):
    gcd_list= [math.gcd(i,j) for i in dist_list for j in dist_list if i>j and math.gcd(i,j)!=1]
    return gcd_list

# Count total number of different gcds
def count_gcds(lgram_gcds):
    lgram_dict={}
    for i in lgram_gcds:
        for j in i[1]:
            if j in lgram_dict:
                lgram_dict[j]+=1
            else:
                lgram_dict[j]=1
    return lgram_dict

# Count total number of different gcds in percents 
def count_gcds_percent(lgram_gcds):
    lgram_percent_dict=count_gcds(lgram_gcds)
    total_num=sum(lgram_percent_dict.values())
    for key in lgram_percent_dict:
        lgram_percent_dict[key]=lgram_percent_dict[key]/total_num*100
    return lgram_percent_dict

# Sort dict by values 
def sort_dict(dict_to_sort):
    return {k: v for k, v in sorted(dict_to_sort.items(), key=lambda item: item[1],reverse=True)}

# Get average letter frequency occurrence 
def get_avg_letter_freq_percent():
    return {'a': 0.08167,'b': 0.01492,'c': 0.02782,'d': 0.04253,'e': 0.12702,'f': 0.0228,'g': 0.02015,
             'h': 0.06094,'i': 0.06966,'j': 0.00153,'k': 0.00772,'l': 0.04025,'m': 0.02406,'n': 0.06749,
             'o': 0.07507,'p': 0.01929,'q': 0.00095,'r': 0.05987,'s': 0.06327,'t': 0.09056,'u': 0.02758,
             'v': 0.00978,'w': 0.0236,'x': 0.0015,'y': 0.01974,'z': 0.00074 }

# Calculate possible shift between enc letter and dec letter
def get_shift(let_freq_dict, en_let_freq_dict):
    let_freqs=list(let_freq_dict.values())
    en_let_freqs=list(en_let_freq_dict.values())
    
    min=1
    shift=-1
    for i in range(26):
        norm=get_norm(let_freqs,en_let_freqs,i)
        if norm<min:
            min=norm
            shift=i
    return shift
            
# Calculate norm of two vectors with given shift 
def get_norm(list1,list2,shift):
    diff=[]
    for i in range(len(list1)):
        j=(i-shift)%len(list1)
        diff+=[list1[i]-list2[j]]
    sq_diff=[elem**2 for elem in diff]
    return sum(sq_diff)

def get_en_alphabet():
    return string.ascii_lowercase