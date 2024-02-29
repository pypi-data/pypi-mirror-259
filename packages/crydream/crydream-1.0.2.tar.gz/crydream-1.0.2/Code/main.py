import datetime
import os
import sys
import time

sys.path.append(os.path.dirname(__file__))

from em5822_sample.codeRun import em5822
from img_sample.codeRun import img
from .mount_sample.codeRun import mount


class Print_log:
    # 程序初始化
    def __init__(self):
        #   初始化
        self.em = em5822()
        self.img = img()
        self.mount = mount()
        #   文件保存标志，True保存，False不保存
        self.Print_Save = True

        print("_______________________________________________")
        #   创建文件夹目录
        createFloder_path = [
            './dataset/img_result',
            './dataset/img_result/img_cache',
            './dataset/img_result/img_history',
            './dataset/img_result/img_input',
            './dataset/img_result/img_out',
            './dataset/img_result/img_tem',
            './logs',
            './logs/log_mount',
            './logs/log_em5822Init',
            './logs/log_em5822Run',
            './logs/log_LedInit',
            './logs/log_process',
            './logs/log_CameraInit',
            './logs/log_AcqRun'
        ]
        #   创建文件夹
        for i in createFloder_path:
            if not os.path.exists("%s" % i):
                os.makedirs("%s" % i)
                print("%s文件夹已经创建成功！" % i)
            else:
                print("%s文件夹已存在！" % i)

    #   热转印打印机初始化日志
    def em5822_init_log(self):
        #   输出程序执行时间
        start = time.perf_counter()  # 开始时间点
        #   数据暂时存储
        temp = sys.stdout
        #   判断输出到控制台，还是日志中
        if self.Print_Save == True:
            # 初始化将print输出到文件中
            now_time = datetime.datetime.now()
            time_now = now_time.strftime("%Y-%m-%d_%H-%M-%S")
            # 把输出重定向文件
            Print_log = open("./logs/log_em5822Init/%s.log" % time_now, 'w')
            # 使用print函数，都将内容打印到日志文件中
            sys.stdout = Print_log
        else:
            pass

        #   调用需要保存日志的程序
        flag = self.em.emInit()

        end = time.perf_counter()  # 结束时间点
        print("时间消耗：%.2f s" % (end - start))

        #   上述print内容均已输出到文档
        if self.Print_Save == True:
            sys.stdout = temp
        else:
            pass

        return flag

    #   热转印打印机输出日志
    def em5822_out_log(self, Base, Nature, Data_Light):
        #   输出程序执行时间
        start = time.perf_counter()  # 开始时间点
        #   数据暂时存储
        temp = sys.stdout
        #   判断输出到控制台，还是日志中
        if self.Print_Save == True:
            # 初始化将print输出到文件中
            now_time = datetime.datetime.now()
            time_now = now_time.strftime("%Y-%m-%d_%H-%M-%S")
            # 把输出重定向文件
            Print_log = open("./logs/log_em5822Run/%s.log" % time_now, 'w')
            # 使用print函数，都将内容打印到日志文件中
            sys.stdout = Print_log
        else:
            pass

        #   调用需要保存日志的程序
        flag = self.em.emPrint(Base, Nature, Data_Light)

        end = time.perf_counter()  # 结束时间点
        print("时间消耗：%.2f s" % (end - start))

        #   上述print内容均已输出到文档
        if self.Print_Save == True:
            sys.stdout = temp
        else:
            pass

        return flag

    #   灯源控制器初始化日志
    def Led_init_log(self):
        #   输出程序执行时间
        start = time.perf_counter()  # 开始时间点
        #   数据暂时存储
        temp = sys.stdout
        #   判断输出到控制台，还是日志中
        if self.Print_Save == True:
            # 初始化将print输出到文件中
            now_time = datetime.datetime.now()
            time_now = now_time.strftime("%Y-%m-%d_%H-%M-%S")
            # 把输出重定向文件
            Print_log = open("../logs/log_LedInit/%s.log" % time_now, 'w')
            # 使用print函数，都将内容打印到日志文件中
            sys.stdout = Print_log
        else:
            pass

        #   调用需要保存日志的程序
        flag = self.img.ledInit()

        end = time.perf_counter()  # 结束时间点
        print("时间消耗：%.2f s" % (end - start))

        #   上述print内容均已输出到文档
        if self.Print_Save == True:
            sys.stdout = temp
        else:
            pass

        return flag

    #   摄像头初始化日志
    def Camera_init_log(self):
        #   输出程序执行时间
        start = time.perf_counter()  # 开始时间点
        #   数据暂时存储
        temp = sys.stdout
        #   判断输出到控制台，还是日志中
        if self.Print_Save == True:
            # 初始化将print输出到文件中
            now_time = datetime.datetime.now()
            time_now = now_time.strftime("%Y-%m-%d_%H-%M-%S")
            # 把输出重定向文件
            Print_log = open("./logs/log_CameraInit/%s.log" % time_now, 'w')
            # 使用print函数，都将内容打印到日志文件中
            sys.stdout = Print_log
        else:
            pass

        #   调用需要保存日志的程序
        flag = self.img.camInit()

        end = time.perf_counter()  # 结束时间点
        print("时间消耗：%.2f s" % (end - start))

        #   上述print内容均已输出到文档
        if self.Print_Save == True:
            sys.stdout = temp
        else:
            pass

        return flag

    #   图像获取日志
    def Img_acquire_log(self, path_chache, path_save, name):
        #   输出程序执行时间
        start = time.perf_counter()  # 开始时间点
        #   数据暂时存储
        temp = sys.stdout
        #   判断输出到控制台，还是日志中
        if self.Print_Save == True:
            # 初始化将print输出到文件中
            now_time = datetime.datetime.now()
            time_now = now_time.strftime("%Y-%m-%d_%H-%M-%S")
            # 把输出重定向文件
            Print_log = open("./logs/log_CameraInit/%s.log" % time_now, 'w')
            # 使用print函数，都将内容打印到日志文件中
            sys.stdout = Print_log
        else:
            pass

        #   调用需要保存日志的程序
        flag = self.img.imgA(path_chache, path_save, name)

        end = time.perf_counter()  # 结束时间点
        print("时间消耗：%.2f s" % (end - start))

        #   上述print内容均已输出到文档
        if self.Print_Save == True:
            sys.stdout = temp
        else:
            pass

        return flag

    #   图像处理日志
    def Img_process_log(self, path_read, path_write, combina, radius):
        #   输出程序执行时间
        start = time.perf_counter()  # 开始时间点
        #   数据暂时存储
        temp = sys.stdout
        #   判断输出到控制台，还是日志中
        if self.Print_Save == True:
            # 初始化将print输出到文件中
            now_time = datetime.datetime.now()
            time_now = now_time.strftime("%Y-%m-%d_%H-%M-%S")
            # 把输出重定向文件
            Print_log = open("./logs/log_process/%s.log" % time_now, 'w')
            # 使用print函数，都将内容打印到日志文件中
            sys.stdout = Print_log
        else:
            pass

        #   调用需要保存日志的程序
        flag, gray, nature = self.img.imgPro(path_read, path_write, combina, radius)

        end = time.perf_counter()  # 结束时间点
        print("时间消耗：%.2f s" % (end - start))

        #   上述print内容均已输出到文档
        if self.Print_Save == True:
            sys.stdout = temp
        else:
            pass

        return flag, gray, nature

    #   挂载移动日志
    def Move_log(self, original, final, identifier):
        #   输出程序执行时间
        start = time.perf_counter()  # 开始时间点
        #   数据暂时存储
        temp = sys.stdout
        #   判断输出到控制台，还是日志中
        if self.Print_Save == True:
            # 初始化将print输出到文件中
            now_time = datetime.datetime.now()
            time_now = now_time.strftime("%Y-%m-%d_%H-%M-%S")
            # 把输出重定向文件
            Print_log = open("./logs/log_mount/%s.log" % time_now, 'w')
            # 使用print函数，都将内容打印到日志文件中
            sys.stdout = Print_log
        else:
            pass

        #   调用需要保存日志的程序
        flag = self.mount.mount(original, final, identifier)

        end = time.perf_counter()  # 结束时间点
        print("时间消耗：%.2f s" % (end - start))

        #   上述print内容均已输出到文档
        if self.Print_Save == True:
            sys.stdout = temp
        else:
            pass
        return flag
