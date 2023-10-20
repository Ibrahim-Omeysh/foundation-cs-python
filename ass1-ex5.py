def main():

  def strongPass(code):
    c = 0
    a = 0
    h = 0
    u = 0
    for i in range(len(code)):
      if code[i].isupper():
        u = 1
      elif code[i].isdigit():
        c = 1
      elif code[i].isalpha():
        a = 1
      elif code[i] in ['@', '#', '$', '%', '&', '*']:
        h = 1
    if (c == 1 and a == 1 and h == 1 and len(code) >= 8):
      return True
    else:
      return False

  ps = input('Enter the password:')
  if strongPass(ps):
    print('Strong Password')
  else:
    print('Weak Password')


main()
    