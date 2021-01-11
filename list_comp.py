sentence = "This is a sentence."

chars = [char for char in sentence]

print(chars)

two_by_two = [[1, 2, 3], [39, 4, 5], [6, 76, 8]]

print([max(row) for row in two_by_two])

char_name = ["Elric", "Red Sonja", "Conan", "Aelien"]

print([name for name in char_name if name.startswith('E') or len(name) > 5])
