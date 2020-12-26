# Designer PDF Viewer https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
import string


def designerPdfViewer(h, word):
    alphabet = list(string.ascii_lowercase)
    heights = 0
    for c in word:
        if h[alphabet.index(c)] > heights:
            heights = h[alphabet.index(c)]

    return len(word) * heights        

print designerPdfViewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,5, 7], 'zaba')   