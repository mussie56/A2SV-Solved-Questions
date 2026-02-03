def split_and_join(line):
    # write your code here
    line = list(line.split())
    return "-".join(line)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
