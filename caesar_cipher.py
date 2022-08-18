
from art import logo
print(logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue=True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift%26

    def caesar(start_text,shift_amount,cipher_direction):
        list=[]
        for letter in start_text:
            list.append(letter)
            
        new_list=[]  
        if cipher_direction == 'encode':
            
            for char in list:
                if char in alphabet:
                    ind=alphabet.index(char)
                    index_num=ind+shift_amount
                    new_list.append(alphabet[index_num])
                else:
                    new_list.append(char)
                    
            # print(new_list)
            print(f"The encoded text is","".join(new_list))

        elif direction == 'decode':
            for char in list:
                if char in alphabet:
                    ind=alphabet.index(char)
                    index_num=ind-shift
                    new_list.append(alphabet[index_num])
                else:
                    new_list.append(char)
        # print(new_list)
            print(f"The decoded text is :","".join(new_list))
            
            
    caesar(start_text=text,shift_amount=shift,cipher_direction=direction)


    result=input("\nType 'yes' if you want to continue. Otherwise type'no'.\n").lower()
    if result=='no':
        should_continue=False
        print("\nGoodbye! Have a good day ahead.")
# def caesar(start_text,shift_amount,cipher_direction):
#     if direction == 'encode':
#         encrypt(plain_text=text, shift=shift)
    
#     elif direction == 'decode':
#         decrypt(dec_text=text, shift=shift)
        
# def encrypt(plain_text, shift):
#     list=[]
#     for letter in plain_text:
#         list.append(letter)

#     new_list=[]
#     for char in list:
#         ind=alphabet.index(char)
#         index_num=ind+shift
#         new_list.append(alphabet[index_num])
            
#     # print(new_list)
#     print(f"The encoded text is","".join(new_list))

# def decrypt(dec_text,shift):
#     list=[]
#     for letter in dec_text:
#         list.append(letter)

#     new_list=[]
#     for char in list:
#         ind=alphabet.index(char)
#         index_num=ind-shift
#         new_list.append(alphabet[index_num])
            
#     # print(new_list)
#     print(f"The decoded text is :","".join(new_list))
    
    
