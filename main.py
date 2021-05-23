#                   Text Compression Project

import sys
import threading
import time
import concurrent
from concurrent.futures import ThreadPoolExecutor

# Number of lines for each thread to process
threshold = 500


def getwords(filepath):
    file = open(filepath, 'r')
    return file.read().split(" ")


def getwords_s(lines):
    s = ""
    for line in lines:
        s+=line
    return s


def compress(text_string):
    compressedWords = {}
    currWord = 0
    keys = ""
    text = ""
    words = text_string.split(" ")
    for word in words:
        if word in compressedWords:
            text = text + " " + compressedWords[word]
        else:
            if keys == "":
                keys = word + ":" + str(currWord)
            else:
                keys = keys + "`" + word + ":" + str(currWord)
            compressedWords[word] = str(currWord)
            if text == "":
                text = compressedWords[word]
            else:
                text = text + " " + compressedWords[word]
            currWord += 1
    keys = "{" + keys + "}"
    final_text = keys + "{}" + text
    return final_text


def decompress(path, dest_path):
    foo = open(path, 'r')
    foo.seek(0)
    textFile = foo.read().split("{}")
    foo.close()
    keys = textFile[0]
    text = textFile[1]
    keys = keys.split("{")[1]
    keys = keys.split("}")[0]
    keys = keys.split("`")
    tempKeys = {}
    for key in keys:
        tempKey = key.split(":")[1]
        tempValue = key.split(":")[0]
        tempKeys[tempKey] = tempValue
    keys = tempKeys
    decompressedText = ""
    for key in text.split(" "):
        if decompressedText == "":
            decompressedText += keys[key]
        else:
            decompressedText = decompressedText + " " + keys[key]
    foo = open(dest_path, "w")
    foo.write(decompressedText)
    foo.close()


def main():
    start_time = time.process_time()
    # Pass the path to the text file as a command-line  argument.
    filePath = sys.argv[1]
    # compressFilePath = sys.argv[2]
    # decompressFilePath = sys.argv[3]

    executor = ThreadPoolExecutor()

    # Open the file using read option.
    file = open(filePath, "r")
    threads = []
    lines = file.readlines()
    fo = open('testfile.txt', 'w')
    fo.write(compress(getwords_s(lines)))
    '''for i in range(1, int((len(lines)/threshold))+1):
        if i == int(len(lines)/threshold):
            # threads.append(threading.Thread(target=getwords_s(), args=(lines[threshold*i-1, len(lines)])))
            threads.append(executor.submit(getwords_s, lines[threshold*(i-1):len(lines)]))
            # print(str(threshold*(i-1)) + " : " + str(len(lines) + 1) + " last.")
        else:
            # threads.append(threading.Thread(target=getwords_s(), args=(lines[threshold*i-1:threshold*i])))
            threads.append(executor.submit(getwords_s, lines[threshold*(i-1):threshold*i]))
            # print(str(threshold * (i - 1)) + " : " + str(threshold*i + 1) + " Not last.")

    concurrent.futures.wait(threads)
    executor2 = ThreadPoolExecutor()
    threads2 = []

    for thread in threads:
        threads2.append(executor2.submit(compress, thread.result()))

    executor.shutdown(True)

    concurrent.futures.wait(threads2)

    keys = "{"
    text = ""

    for i in range(0, len(threads2)):
        tempStr = threads2[i].result()
        tempKey, tempText = tempStr.split('{}')
        tempKey = tempKey.split("{")[1]
        tempKey = tempKey.split("}")[0]
        keys += tempKey
        text += tempText
        if i != (len(threads2)-1):
            keys += '{}'
            text += '{}'

    keys += '}'

    fileOp = open('testingMultithreading.txt', 'w')
    fileOp.write(keys)
    fileOp2 = open('testingMultithreading1.txt', 'w')
    fileOp2.write(text)'''

    print("Time to process text file in seconds : %s" % (time.process_time()-start_time))
    # Split the file into a list of all the words.
    '''words1 = file.read().split(" ")

    file.close()

    compress(words1, compressFilePath)
    decompress(compressFilePath, decompressFilePath)'''


if __name__ == '__main__':
    main()




