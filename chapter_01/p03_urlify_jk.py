def urlify(data):
    return data[0][:data[1]].replace(" ","%20")

if __name__ == "__main__":
    data = ("Mr John Smith         ", 13)
    delim = "%20"
    print(urlify(data))
