# Marah McCaffery lab 3 03/27/23

def analyzeBook():
    file = open('h.txt', 'r', encoding="utf8")
    count = {}
    for line in file:
        for word in line.split():
            word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
            word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
            word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
            word = word.replace(']', '').replace(';', '')
            word = word.lower()
            if word.isalpha():
                if word in count:
                    count[word] = count[word] + 1
                else:
                    count[word] = 1
    file.close()
    return count

def outputAnalysis(count):
    keys = list(count.keys())
    keys.sort()
    out = open('analysis.txt', 'w')
    for word in keys:
        out.write(word + " " + str(count[word]))
        out.write('\n')
    out.close()
    if not count:
        return False
    else:
        return True

def main():
    count = analyzeBook()
    success = outputAnalysis(count)
    if success:
        print("Analysis completed successfully!")
    else:
        print("An error occurred during analysis.")

if __name__ == "__main__":
    main()
