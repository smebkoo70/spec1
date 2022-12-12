class Test_Data:
    seconds = None
    ratio = None

    def __init__(self):
        pass

    def __int__(self, seconds, ratio):
        self.seconds = seconds
        self.ratio = ratio


class Flag:
    copies = None
    test_list = []

    def setCopies(self, copies):
        self.copies = copies

    def addTestList(self, dataList: Test_Data):
        self.test_list.append(dataList)


class ResultMessage:
    benchmark = None
    base = None
    peak = None

    def __init__(self):
        pass

    def __int__(self, benchmark, base: Flag, peak: Flag):
        self.base = base
        self.peak = peak
        self.benchmark = benchmark

    def setBase(self, base="Flag"):
        self.base = base

    def setPeak(self, peak="Flag"):
        self.peak = peak

    def setBenchmark(self, benchmark):
        self.benchmark = benchmark

    def getBenchmark(self):
        return self.benchmark

    def getBase(self) -> Flag:
        return self.base

    def getPeak(self) -> Flag:
        return self.peak


class Cpu_Message:
    # 保存页面当中一些测试信息的实体类
    test_Message = None
    # 保存页面中关于硬件介绍信息的实体类
    hardware_Message = None
    # 保存页面接收软件信息的实体类
    software_Message = None
    # 保存页面介绍测试数据结果的信息的实体类
    result_Message = None
    # 保存介绍后面环境注意和要点的信息实体类
    note_Message = None
    # 保存基础信息标志信息的实体类
    baseFlag_Message = None
    # 保存Peak信息标志信息的实体类
    peakFlag_Message = None

    def setTest(self, testMessage):
        self.test_Message = testMessage

    def setHardware(self, hardwareMessage):
        self.hardware_Message = hardwareMessage

    def setSoftware(self, softwareMessage):
        self.software_Message = softwareMessage

    def setResult(self, resultMessage: ResultMessage):
        self.result_Message = resultMessage

    def setNote(self, noteMessage):
        self.note_Message = noteMessage

    def setBaseFlag(self, baseFlagMessage):
        self.baseFlag_Message = baseFlagMessage

    def setPeakFlag(self, peakFlagMessage):
        self.peakFlag_Message = peakFlagMessage


class Test_CPURates:
    sys_name = ''
    base_copies = 0
    enable_cores = 0
    enable_chip = 0
    thread_core = 0
    base = None
    peak = None

    # def __init__(self, sys_name, base_copies, enable_cores, enable_chip, thread_core, base, peak):
    #     self.sys_name = sys_name
    #     self.base_copies = base_copies
    #     self.enable_cores = enable_cores
    #     self.enable_chip = enable_chip
    #     self.thread_core = thread_core
    #     self.base = base
    #     self.peak = peak

    def setSys_name(self, sys_name: str):
        self.sys_name = sys_name

    def setBase_copies(self, base_copies: int):
        self.base_copies = base_copies

    def setEnable_cores(self, enable_cores: int):
        self.enable_cores = enable_cores

    def setEnable_chip(self, enable_chip: int):
        self.enable_chip = enable_chip

    def setThread_core(self, thread_core: int):
        self.thread_core = thread_core

    def setBase(self, base: str):
        self.base = base

    def setPeak(self, peak: str):
        self.peak = peak

    def __str__(self):
        return "sys_name: " + self.sys_name + " base_copies: " + str(self.base_copies) + " enable_cores: " \
               + str(self.enable_cores) \
               + " enable_chip: " + str(self.enable_chip) + " thread_core: " + str(self.thread_core) + " base:" \
               + str(self.base) + " peak: " + str(self.peak)


class Test_CPUSpeed:
    sys_name = ''
    parallel = 'no'
    base_threads = 0
    enable_cores = 0
    enable_chip = 0
    thread_core = 0
    base = None
    peak = None

    def setSys_name(self, sys_name: str):
        self.sys_name = sys_name

    def setParallel(self, parallel: str):
        self.parallel = parallel

    def setBase_threads(self, base_threads: int):
        self.base_threads = base_threads

    def setEnable_cores(self, enable_cores: int):
        self.enable_cores = enable_cores

    def setEnable_chip(self, enable_chip: int):
        self.enable_chip = enable_chip

    def setThread_core(self, thread_core: int):
        self.thread_core = thread_core

    def setBase(self, base: str):
        self.base = base

    def setPeak(self, peak: str):
        self.peak = peak

    def __str__(self):
        return "sys_name: " + self.sys_name + " parallel " + self.parallel + " base_threads: " + str(
            self.base_threads) + " enable_cores: " + str(
            self.enable_cores) \
               + " enable_chip: " + str(self.enable_chip) + " thread_core: " + str(self.thread_core) + " base:" \
               + str(self.base) + " peak: " + str(self.peak)


