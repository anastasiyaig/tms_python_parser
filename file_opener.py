import json


def my_parser():
    with open('parseMe.csv', 'r') as f:

        text_lines = []  # empty list to store lines from the csv file
        for line in f.readlines():
            text_lines.append(line.rstrip().split(";"))  # filling up the list with lines, separated by ;

        keys = list(text_lines[0])  # getting 1st line as keys for dictionary

        values = []  # empty list to create values that will be mapped to keys
        for i in range(1, len(text_lines)):  # starting from 1 to skip the header line
            values.append(dict(zip(keys, text_lines[i])))
        with open("sample.json", "w") as outfile:
            json.dump(values, outfile)
        return values


def main():
    print(my_parser())


if __name__ == "__main__":
    main()
