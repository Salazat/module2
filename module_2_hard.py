def generate_pass(n):
    numbers = list(range(1, 21))
    if n in numbers:
        numbers.remove(n)
    else:
        print("Правила очень просты, число должно быть от 3 до 20")
        return ""
    user_pass = []
    result = ""
    for a in numbers:
        for b in numbers:
            if a != b:
                para_found = False
                for para in user_pass:
                    if para[0] == a and para[1] == b:
                        para_found = True
                        break
                if para_found == False:
                    sum_pass = a + b
                    if n % sum_pass == 0:
                        result += str(a) + str(b)
                        user_pass.append((a, b))
                        user_pass.append((b, a))
    return result

n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    password = generate_pass(n)
    print("Получившийся результат:", password)
else:
    print("Ошибка: число должно быть в диапазоне от 3 до 20!")


