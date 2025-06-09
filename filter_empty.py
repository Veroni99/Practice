def remove_empty_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file: 
        lines = file.readlines()

    non_empty_lines = [line for line in lines if line.strip() != '']

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(non_empty_lines)


def main():
    file_path = "C:/Users/Veronika/Desktop/ху/1.txt"
    remove_empty_lines(file_path)

if __name__ == '__main__':
    main()