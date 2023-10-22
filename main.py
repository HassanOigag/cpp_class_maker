from sys import argv, exit
from datetime import datetime

def return_header(file_name, login="hoigag"):
    date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    return f"""/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   {file_name}                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: {login} <{login}@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: {date_time} by {login}            #+#    #+#             */
/*   Updated: {date_time} by {login}           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */"""


def get_class_name(str):
    words = str.split()
    name = ""
    for word in words:
        word = word[0].upper() + word[1:]
        name += word
    return name


def create_header_file(class_name):
    header_file_name = class_name + ".hpp"
    with open(header_file_name, "w") as f:
        # f.write(return_header(header_file_name))
        f.write("\n\n#ifndef " + class_name.upper() + "_HPP\n")
        f.write("#define " + class_name.upper() + "_HPP\n\n")
        f.write("class " + class_name + " {\n")
        f.write("\tpublic:\n")
        f.write("\t\t" + class_name + "();\n")
        f.write("\t\t~" + class_name + "();\n")
        f.write("\tprivate:\n")
        f.write("};\n\n")
        f.write("#endif\n")
    print(f"created: {header_file_name} successfully")

def create_source_file(class_name):
    source_file_name = class_name + ".cpp"
    header_file_name = class_name + ".hpp"
    with open(source_file_name, "w") as f:
        # f.write(return_header(source_file_name))
        f.write("\n\n#include \"" + header_file_name + "\"\n\n")
        f.write(class_name + "::" + class_name + "() {\n\n}\n\n")
        f.write(class_name + "::~" + class_name + "() {\n\n}\n\n")
    print(f"created: {source_file_name} successfully")

def create_main_file():
    main_file_name = "main.cpp"
    with open(main_file_name, "w") as f:
        # f.write(return_header(main_file_name))
        f.write("\n\n#include <iostream>\n\n");
        f.write("int main() {\n\treturn (0);\n}\n")
    print(f"created: {main_file_name} successfully")

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python main.py [class_name]")
        exit(1)
    
    if argv[1] == "help":
        print("Usage: python3 main.py [all calss names separated by space]")
        exit(0)

    for i in range(1, len(argv)):
        class_name = get_class_name(argv[i])
        if class_name == "":
            print("file not created, class name is empty")
            continue
        create_header_file(class_name)
        create_source_file(class_name)
    create_main_file()
