def main(num=None):
    def validator(num=None):
        if num == None or not isinstance(num, int) or num < 0 or num > 100:
            return False
        return True

    return validator(num)
