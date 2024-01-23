freqs = [8.08, 1.67, 3.18, 3.99, 12.56, 2.17, 1.80, 5.27, 7.24, 0.14, 0.63, 4.04, 2.60, 7.38, 7.47, 1.91, 0.09, 6.42, 6.59, 9.15, 2.79, 1.00, 1.89, 0.21, 1.65, 0.07]

def find_shift(letter_freq):
    best_shift = 0
    min_diff = float('inf')

    for shift in range(26):
        diff = 0
        for i in range(26):
            diff += abs(letter_freq[(i + shift) % 26] - freqs[i])
        if diff < min_diff:
            min_diff = diff
            best_shift = shift

    return best_shift

def shift_char(c, shift):
    if not c.isalpha():
        return c

    is_lower = c.islower()
    if is_lower:
        c = c.upper()

    idx = (ord(c) - ord('A') - shift + 26) % 26
    shifted_char = chr(ord('A') + idx)

    if is_lower:
        shifted_char = shifted_char.lower()

    return shifted_char

msg = input()

count = [0] * 26
total = 0

for c in msg:
    if c.isalpha():
        total += 1
        index = ord(c.lower()) - ord('a')
        count[index] = count[index] + 1

freq = []
for x in count:
    if total > 0:
        frequency = (x * 100.0) / total
    else:
        frequency = 0
    freq.append(frequency)

shift = find_shift(freq)

result = ''
for c in msg:
    result += shift_char(c, shift)

print(result)
