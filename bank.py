def main():
    greeting = input("Приветствие: ").lower()
    check_greeting(greeting.split(' '))

def check_greeting(list):
    match list:
        case "здравствуйте", *name:
            print("$0")
            exit()
    if list[0].startswith("з"):
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()
