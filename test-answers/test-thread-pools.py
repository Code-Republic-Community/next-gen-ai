from concurrent.futures import ThreadPoolExecutor
 
 
def length_calculator(s):
    time.sleep(2)
    return len(s)
 
 
texts = ['Adam', 'This is a test!', 'Hey', 'Albert Camus']
 
with ThreadPoolExecutor(4) as executor:
    for text, length in zip(texts, executor.map(length_calculator, texts)):
        print(text + ' - ' + str(length))
