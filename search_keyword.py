import xml.etree.ElementTree as etree


def search(keyword):
    tree = etree.parse('entries.xml')
    root = tree.getroot()
    matches = []
    for child in root:
        if keyword in child.text:
            matches.append((child.text,len(child.text.split())))
    if len(matches) is 0:
        print("\nNo entries found\n")
    else:
        print("\n")
        sorted_matches = sorted(matches, key=lambda match: match[1])
        for m in sorted_matches:
            print( m[0] + "\n")

def main():
    keyword = input("please enter keyword:")
    search(keyword)

if __name__ == "__main__":
    main()
