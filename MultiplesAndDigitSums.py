def main(num=None):
    def validator(num=None):
        return (
            "num" in vars()  # param defined
            and isinstance(num, int)  # param is list
            and 0 <= num <= 100  # list has at least 3 entries
        )

    def calculate(num):
        multiples = []
        current = num
        while current <= 100:
            multiples.append(current)
            current = current + num
        print("".join(str(multiples)))
        digsums = []
        for thisnum in multiples:
            summa = 0
            for digit in str(thisnum):
                summa += int(digit)
            digsums.append(summa)
        print("".join(str(digsums)))
        print(sum(digsums))
        return sum(digsums)

    if validator(num):
        if num == 0:
            return 0
        return calculate(num)
    return False
