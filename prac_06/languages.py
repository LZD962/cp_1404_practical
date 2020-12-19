from prac_06.programming_language import ProgrammingLanguage

if __name__ == '__main__':
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    language_list = [ruby, python, visual_basic]

    print("The dynamically typed languages are:")
    for lang in language_list:
        if lang.is_dynamic():
            print(lang.name)
