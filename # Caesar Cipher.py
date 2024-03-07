# Caesar Cipher - day 8

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(message, shift, direction):
  """Encrypts or decrypts a message using a Caesar cipher."""
  alphabet = alphabet * 2  # Doubled for wrapping convenience
  new_message = ""
  for char in message:
    if char in alphabet:
      index = alphabet.index(char)
      new_message += alphabet[index + shift % len(alphabet)]
    else:
      new_message += char
  if direction == "decode":
    shift *= -1
  print(f"Here's the {direction}d result: {new_message}")

while True:
  try:
    direction, message, shift_str = input("Choose 'encode' or 'decode', enter your message (lowercase), and input a shift number (mod 26):\n").lower().split(", ")
    shift = int(shift_str)
  except (ValueError, IndexError):
    print("Invalid input. Please try again.")
    continue

  caesar(message, shift, direction)

  restart = input("Type 'yes' to continue, 'no' to exit:\n").lower()
  if restart == "no":
    break

print("Goodbye!")