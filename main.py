#Stephany Jimenez
def encode(password):
  return ''.join([str((int(num) + 3) % 10) for num in password])


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
