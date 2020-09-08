function main {
    #consts
    a_pos=$(ord a)
    z_pos=$(ord z)
    # 
    dec_key=''
    dec_text=''
    # key
    key=$1
    key_len=${#key}
    # text
    text=$(tr A-Z a-z < $2)
    text_len=${#text}
    # algorithm
    for j in $(seq 0 $(($key_len-1)))
    do
        key_let_pos=$(ord ${key:j:1})    # 'z'-(char-'a-1')
        let dec_key_let_pos=$z_pos-$key_let_pos+$a_pos+1
        dec_char=$(chr $dec_key_let_pos)
        dec_key+=$dec_char
    done
    dec_text=$(./encrypt.sh $dec_key $2)
    echo $dec_text

}

function ord {
    LC_CTYPE=C printf '%d' "'$1";
}

function chr {
  [ "$1" -lt 256 ] || return 1
  printf "\\$(printf '%03o' "$1")"
}

main $1 $2