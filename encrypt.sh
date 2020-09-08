function main {
    #consts
    a_pos=$(ord a)
    # 
    en_text=''
    # key
    key=$1
    key_len=${#key}
    # text
    text=$(tr A-Z a-z < $2)
    text_len=${#text}
    # algorithm
    i=0
    for j in $(seq 0 $(($text_len-1)))
    do
        text_let_pos=$(ord ${text:j:1})
        #space check
        if [[ $text_let_pos -ne 0 ]]
            then
            #lowercase letter check 
            if [[ ${text:j:1} =~ [a-z] ]] 
            then 
                start_sym_pos=$a_pos
            else
                echo 'Error, non-alphabetic value'
                break
            fi

            key_let_pos=$(($i % $key_len))
            key_let=${key:key_let_pos:1}

            let key_shift=$(ord $key_let)-$start_sym_pos
            let text_shift=$text_let_pos-$start_sym_pos 

            let shift=$text_shift+$key_shift
            let en_char_pos=$(($shift % 26))+$start_sym_pos
            en_char=$(chr $en_char_pos)
            en_text+=$en_char
            let i=i+1
        else
            en_text+=' '
        fi
    done

    echo $en_text

}

function ord {
    LC_CTYPE=C printf '%d' "'$1";
}

function chr {
  [ "$1" -lt 256 ] || return 1
  printf "\\$(printf '%03o' "$1")"
}

main $1 $2