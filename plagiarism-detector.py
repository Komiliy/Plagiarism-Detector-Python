from difflib import SequenceMatcher

with open  ('demo1.txt') as one_file, open('demo2.txt') as two_file:
    data_file = one_file.read()
    data_file2 = two_file.read()

    document = SequenceMatcher(None, data_file, data_file2).ratio()
    print(f"The Plagiarized content is {document*100}")



    