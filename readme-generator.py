import os, random

current_directory = os.getcwd()

code_folder = os.path.join(current_directory, 'code')

lst = []

with open("README.txt", "w") as file:
    if os.path.isdir(code_folder):
        files = os.listdir(code_folder)
        files = [f for f in files if os.path.isfile(os.path.join(code_folder, f))]
        
        if files:
            for term in files:
                lst.append(f"code/{term}\n")
        else:
            print("No files found in the 'code' folder.")

    question_folder = os.path.join(current_directory, 'question')

    if os.path.isdir(question_folder):
        files = os.listdir(question_folder)
        files = [f for f in files if os.path.isfile(os.path.join(question_folder, f))]
        
        if files:
            for term in files:
                lst.append(f"question/{term}\n")
        else:
            print("No files found in the 'question' folder.")

    random.shuffle(lst)

    for term in lst:
        file.write(term)

