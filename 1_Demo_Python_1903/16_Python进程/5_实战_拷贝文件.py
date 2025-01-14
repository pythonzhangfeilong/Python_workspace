import os
import shutil
import multiprocessing
# import time
# 文件拷贝任务
def copy_work(src_dir, dst_dir, file_name):
    # 查看进程对象
    pid = multiprocessing.current_process().pid
    print(pid)
    # 拼接源文件的路径
    src_file_path = src_dir + "/" + file_name
    # 拼接目标文件的路径
    dst_file_path = dst_dir + "/" + file_name
    with open(dst_file_path, "wb") as dst_file:
        # 打源文件读取文件中的数据
        with open(src_file_path, "rb") as src_file:
            while True:
                # 读取数据
                src_file_data = src_file.read(1024)
                if src_file_data:
                    # 写入到目标文件里面
                    dst_file.write(src_file_data)
                else:
                    break
if __name__ == '__main__':
    # 源目录
    src_dir = "./copy/"
    # 目标目录
    dst_dir = "./copy_in/"
    # 判断文件夹是否存在
    if os.path.exists(dst_dir):
        # 存在则删除文件夹及文件夹里面的所有文件
        shutil.rmtree(dst_dir)
    # 创建目标文件夹
    os.mkdir(dst_dir)
    # 获取源目录里面文件的列表
    file_name_list = os.listdir(src_dir)
    # 创建进程池
    pool = multiprocessing.Pool(3)
    # 遍历文件里面获取文件名
    for file_name in file_name_list:
        # 使用进程池执行拷贝任务
        pool.apply_async(copy_work, (src_dir, dst_dir, file_name))
    # 关闭进程池
    pool.close()
    # 主进程等待进程池执行完成以后程序再退出
    pool.join()
