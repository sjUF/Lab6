#Stephany Jimenez
def encode(password):
  return ''.join([str((int(num) + 3) % 10) for num in password])


# Isaiah Tanon (Decode addition)
def decode(password):
    x = password
    final_list2 = []
    for i in range(len(x)):
      y = int(x[i])
      final_list2 += [str(y - 3)]
    original_password = ''.join(final_list2)
    return original_password

def main():
  while True:
    print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
    option = input('\nPlease enter an option: ')
    if option == '1':
      password = encode(input('Please enter your password to encode: '))
      print('Your password has been encoded and stored!\n')
    elif option == '2':
      print(f'The encoded password is {password}, '
            f'and the original password is {decode(password)}.\n')
    else:
      break
    
main()
