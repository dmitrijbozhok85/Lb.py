operation = input()
shift = int(input())
rotors = []
for i in range(3):
    rotor = input()
    rotors.append(rotor)
message = input()
result = ''
for i in range(len(message)):
    letter = message[i]
    if operation == 'ENCODE':
        shifted_letter = chr((ord(letter) - ord('A') + shift + i) % 26 + ord('A'))
        for rotor in rotors:
            shifted_letter = rotor[ord(shifted_letter) - ord('A')]
        result += shifted_letter
    elif operation == 'DECODE':
        for rotor in reversed(rotors):
            shifted_letter = chr(ord('A') + rotor.index(letter))
            letter = shifted_letter
        result += chr((ord(letter) - ord('A') - (shift + i)) % 26 + ord('A'))
print(result)
