def main(num=None):
    def validator(num=None):
        return (
            "num" in vars()  # param defined
            and isinstance(num, int)  # param is list
            and 0 <= num <= 100  # list has at least 3 entries
        )

    return validator(num)
