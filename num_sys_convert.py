class NumSysConvert:
    def __init__(self, num, count):
        if 0 > num or num >= 1 or count <= 0:
            raise Exception("Incorrect number!")

        self._num = num
        self._count = count

    def binary(self):
        converted = "0,"
        num = self._num

        for _ in range(1, self._count):
            converted += "1" if num >= 1/2 else "0"
            num *= 2

            if num >= 1:
                num -= 1

        return converted

    def ternary(self):
        converted = "0,"

        num = self._num

        for _ in range(1, self._count):
            if num >= 2/3:
                converted += "2"
            elif num >= 1/3:
                converted += "1"
            else:
                converted += "0"

            num *= 3

            if num >= 2:
                num -= 2
            elif num >= 1:
                num -= 1

        return converted