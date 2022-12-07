class NumSysConvert:
    def __init__(self, num, count):
        if 0 > num or num >= 1 or count <= 0:
            raise Exception("Incorrect number!")

        self._num = num
        self._count = count
