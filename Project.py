import hashlib
import pyperclip


def main():
    match str(input("Input:String/File\n")).lower():
        case "file":
            pyperclip.copy(getattr(hashlib, input(f'{hashlib.algorithms_available}\n'))(
                open(f'{(str(input("Enter file path: ")))}', 'r').read().encode('utf-8')).hexdigest())
        case "string":
            pyperclip.copy(getattr(hashlib, input(f'{hashlib.algorithms_available}\n'))(
                str(input("Enter string: ")).encode('utf-8')).hexdigest())
    print("Hash succesfully copied to clipboard.")


if __name__ == '__main__':
    main()
