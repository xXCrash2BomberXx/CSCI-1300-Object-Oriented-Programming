''' # Version 01
def dna(sequence=None, pattern=None):
    sequence = (input("Enter a DNA sequence: ") if sequence is None else sequence)
    pattern = (input("Enter the pattern:  ") if pattern is None else pattern)
    prefix = sequence[:sequence.index(pattern)]
    marker = pattern
    middle = sequence[sequence.index(pattern)+len(pattern):sequence.index(pattern[::-1], sequence.index(pattern)+len(pattern))]
    reversed_middle = middle[::-1]
    reversed_marker = marker[::-1]
    suffix = sequence[sequence.index(reversed_marker, sequence.index(pattern)+len(pattern))+len(reversed_marker):]
    print("Prefix:", prefix)
    print("Marker:", marker)
    print("Middle:", middle)
    print("Reversed Middle:", reversed_middle)
    print("Reversed Marker:", reversed_marker)
    print("Suffix:", suffix)
    return(prefix+marker+reversed_middle+reversed_marker+suffix)


if __name__ == "__main__":
    print(dna())
'''

''' # Version 02
def dna(sequence=None, pattern=None):
    return [sequence := (input("Enter a DNA sequence: ") if sequence is None else sequence), pattern := (input("Enter the pattern:  ") if pattern is None else pattern), sequence[:sequence.index(pattern)] + pattern + sequence[sequence.index(pattern)+len(pattern):sequence.index(pattern[::-1], sequence.index(pattern)+len(pattern))][::-1] + pattern[::-1] + sequence[sequence.index(pattern[::-1], sequence.index(pattern)+len(pattern))+len(pattern[::-1]):]][-1]


if __name__ == "__main__":
    print(dna())
'''


print([sequence := input("Enter a DNA sequence: "), pattern := input("Enter the pattern:  "), sequence[:sequence.index(pattern)] + pattern + sequence[sequence.index(pattern)+len(pattern):sequence.index(pattern[::-1], sequence.index(pattern)+len(pattern))][::-1] + pattern[::-1] + sequence[sequence.index(pattern[::-1], sequence.index(pattern)+len(pattern))+len(pattern[::-1]):]][-1])
