from base64 import decode


def get_ascii_equivalent(messege):
    """
        This function is responsible for : 
            converting a a given string to its ascii character representation form
    """
    encoded_messege=""
    index=0
    while(index<len(messege)):
        encoded_messege += " "+str(ord(messege[index]))
        index+=1
    return encoded_messege

def get_string_equivalent(encoded_message):
    decoded_message=""
    index=0
    numbers= list(map(int, encoded_message.split()))
    for number in  numbers:
        decoded_message += str(chr(number))
    return decoded_message

if __name__=="__main__":
    encoded_msg=get_ascii_equivalent("Hello this is demo program to understand pull and push in git hub")
    print(encoded_msg)
    print(get_string_equivalent(encoded_msg))