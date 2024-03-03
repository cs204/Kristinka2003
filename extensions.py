def main():
    file_extension(input("File name: "))

def file_extension(file_name):
    file_name = file_name.split(".")
    match file_name[1]:
        case "gif" | "png" as extension:
            print(f"image/{extension}")
        case "jpg" | "jpeg":
            print(f"image/jpeg")
        case "pdf" | "txt" | "zip" as extension:
            print(f"application/{extension}")
        case _:
            print("application/octet-stream")

if __name__ == "__main__":
    main()
