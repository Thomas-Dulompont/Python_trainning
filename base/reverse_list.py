
def inverse(elements):
    reverse_elements = []
    for element in elements:
        reverse_elements.insert(0, element)
    return reverse_elements

liste = [1, "test", 0.9867, "Python, c'est génial !"]
print(inverse(liste))
print(liste)