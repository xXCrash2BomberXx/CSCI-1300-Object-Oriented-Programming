''' # Version 01
def dna(sequence=None, pattern=None):
    sequence = (input("Enter a DNA sequence: ") if sequence is None else sequence)
    pattern = (input("Enter the pattern:  ") if pattern is None else pattern)
    prefix = sequence.split(pattern, 1)[0]
    marker = pattern
    middle = sequence.split(pattern, 1)[-1].split(''.join(reversed(pattern)), 1)[0]
    reversed_middle = ''.join(reversed(middle))
    reversed_marker = ''.join(reversed(marker))
    if len(middle) != 0:
        suffix = sequence.split(prefix, 1)[-1].split(marker, 1)[-1].split(middle, 1)[-1].split(reversed_marker, 1)[-1]
    else:
        suffix = sequence.split(prefix, 1)[-1].split(marker, 1)[-1].split(reversed_marker, 1)[-1]
    print("Prefix:", prefix)
    print("Marker:", marker)
    print("Middle:", middle)
    print("Reversed Middle:", reversed_middle)
    print("Reversed Marker:", reversed_marker)
    print("Suffix:", suffix)
    return "Result:", prefix+marker+reversed_middle+reversed_marker+suffix


if __name__ == "__main__":
    print(dna())
'''

''' # Version 02
def dna(sequence=None, pattern=None):
    sequence = (input("Enter a DNA sequence: ") if sequence is None else sequence)
    pattern = (input("Enter the pattern:  ") if pattern is None else pattern)
    if len(sequence.split(pattern, 1)[-1].split(''.join(reversed(pattern)), 1)[0]) != 0:
        suffix = sequence.split(sequence.split(pattern, 1)[0], 1)[-1].split(pattern, 1)[-1].split(sequence.split(pattern, 1)[-1].split(''.join(reversed(pattern)), 1)[0], 1)[-1].split(''.join(reversed(pattern)), 1)[-1]
    else:
        suffix = sequence.split(sequence.split(pattern, 1)[0], 1)[-1].split(pattern, 1)[-1].split(''.join(reversed(pattern)), 1)[-1]
    return(sequence.split(pattern, 1)[0]+pattern+''.join(reversed(sequence.split(pattern, 1)[-1].split(''.join(reversed(pattern)), 1)[0]))+''.join(reversed(pattern))+suffix)


if __name__ == "__main__":
    print(dna())
'''


print([sequence := input("Enter a DNA sequence: "), pattern := input("Enter the pattern:  "), sequence.split(pattern, 1)[0] + pattern + ''.join(reversed(sequence.split(pattern, 1)[-1].split(''.join(reversed(pattern)), 1)[0])) + ''.join(reversed(pattern)) + (sequence.split(sequence.split(pattern, 1)[0], 1)[-1].split(pattern, 1)[-1].split(sequence.split(pattern, 1)[-1].split(''.join(reversed(pattern)), 1)[0], 1)[-1].split(''.join(reversed(pattern)), 1)[-1] if len(sequence.split(pattern, 1)[-1].split(''.join(reversed(pattern)), 1)[0]) != 0 else sequence.split(sequence.split(pattern, 1)[0], 1)[-1].split(pattern, 1)[-1].split(''.join(reversed(pattern)), 1)[-1])][-1])
