def main(num=None):
    def validator(num=None):
        return (
            "num" in vars()  # param defined
            and isinstance(num, int)  # param is list
            and 0 <= num <= 100  # list has at least 3 entries
        )

    def digitsum(num):
        digitsum = 0
        for digit in str(num):
            digitsum += int(digit)
        return digitsum

    def calculate(num):
        total_digsum = 0
        multiple = num
        while multiple <= 100:
            total_digsum = total_digsum + digitsum(multiple)
            multiple = multiple + num
        return total_digsum

    if validator(num):
        if num == 0:
            return 0
        return calculate(num)
    return False
