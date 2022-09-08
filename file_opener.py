import json


def my_parser():
    values = []  # empty list to create values that will be mapped to keys
    with open('parseMe.csv', 'r') as f:
        for index, line in enumerate(f.readlines()):
            text_line = line.rstrip().split(";")  #
            if index == 0:
                keys = text_line
            else:
                values.append(dict(zip(keys, text_line)))
    with open("sample.json", "w") as outfile:
        json.dump(values, outfile, indent=4)
    return values


def main():
    print(my_parser())


if __name__ == "__main__":
    main()
