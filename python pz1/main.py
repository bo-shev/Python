birth = " "
home = " "

def infoCut():
    pib = Say()
    surname = pib[0]
    name = pib[1]
    fathername = pib[2]
    print("Вивід ПІБ, року народження та місця проживання: ")
    print(surname + " " + name[0:1] + "." + fathername[0:1] + " " + birth + ", " + home)





def cv():


    pib = Say()

    print("Рік народження: ")
    global birth
    birth = input()
    print("Освіта: ")
    education = input()
    print("Хобі: ")
    hobbi = input()
    print("Місце проживання: ")
    global home
    home = input()
    print("Зарплатня: ")
    salary = input()

    work()


    expList = experience_skill()
    for key, value in expList.items():
        print(key, value)


    print("Піб:" + pib[0] + " " + pib[1] + " " + pib[2])
    print("\nРік народження: {0}\nОсвіта: {1}\nХобі: {2}\nМісце проживання: {3}\nЗарплатня: {4}\n".format(
        birth, education, hobbi, home, salary))


def experience_skill():
    expSkillsList = {}  # створення словника
    print("При введені 0 або return функція закінчується")
    print("Увага! Команда 'q' завершує поточний ввід")
    # досвід
    iterator = 1
    print("Наявність опиту в сфері IT:")
    while 1:
        print(f"Досвід у {iterator} справі:")
        exp = input()
        if exp == '0' or exp == 'return':
            return
        elif exp == 'q':
            break;
        else:
            expSkillsList[f'Exp{iterator} :'] = exp
            iterator += 1

    # вміння
    iterator = 1
    print("Наявність вмінь в сфері IT:")
    while 1:
        print(f"Вміння {iterator}:")
        skill = input()
        if skill == '0' or skill == 'return':
            return
        elif skill == 'q':
            break;
        else:
            expSkillsList[f'Skill_{iterator}: '] = skill
            iterator += 1

    # вивід інформації
    for key, value in expSkillsList.items():
        print(key, value)
    return expSkillsList


def work():
    print("Ввести посади, які відповідають Вашим професійним навичкам: ")
    print("Програма завершить роботу про вводі 0 або return, якщо кількість посад менше ніж три")
    print("Увага! Команда 'q' виводить введені посади")
    posts = []
    iteration = 1
    while 1:
        print(f"Посада {iteration}")
        tempInput = input();
        if len(posts) < 3:
            if tempInput == '0' or tempInput == 'return':
                print("Завершення роботи");
                return
        if tempInput == 'q':
            print("Ваші посади:")
            for post in posts:
                print(post)
            break;

        posts.append(tempInput)
        iteration += 1
    return  posts;



def Say():
    pib = [];
    print("Вітаю, введіть наступну інформацію");
    print("Прізвище: ");
    surname=input();
    pib.append(surname);
    print("Ім'я: ");
    name=input();
    pib.append(name);
    print("По батькові: ");
    fathername=input();
    pib.append(fathername);
    print("Вивід персональних даних: " + surname + " " + name + " " + fathername);
    return  pib;

import math

def formula(x, y):
    F = (1+x)**y+(y*x/math.factorial(1))+(y*(y-1)*x**2)/math.factorial(2)+math.sqrt(1+4*(x/y))/math.sqrt(20*y);
    print(F);

def main():

    formula(22, 24);
    #infoCut();
    #experience_skill();

    #work();
    #Say() ;

main();