def main():
    str = input()
    print(convert(str))

def convert(str):
    str = str.replace(':)', '\N{Slightly Smiling Face}')
    str = str.replace(':(', '\N{Slightly Frowning Face}')
    return str

main()

