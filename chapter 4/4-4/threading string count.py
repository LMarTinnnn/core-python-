import timeit
import threading


def single_thread_main(filename, string_to_count):
    with open(filename, 'r', encoding='GBK') as file:
        data = file.read()
    return data.count(string_to_count)


class multi_thread_main(object):
    def __init__(self, filename, string_to_count, thread_num):
        self.filename = filename
        self. string_to_count = string_to_count
        self.all_count = 0
        self.thread_list = []
        self.thread_num = thread_num

    def split(self, length, data):
        length_part = length // self.thread_num
        part_list = []
        now_index = 0
        for i in range(self.thread_num):
            try:
                part_list.append(data[now_index:now_index + length_part])
                now_index += length_part
            except IndexError:
                part_list.append(data[now_index:])
        return part_list

    def count(self, string_to_count, part):
        self.all_count += part.count(string_to_count)

    def run(self):
        #  work start here
        with open(filename, 'r', encoding='GBK') as file:
            data = file.read()
        length = len(data)

        parts = self.split(length, data)

        for part in parts:
            t = threading.Thread(target=self.count, args=(string_to_count, part))
            self.thread_list.append(t)

        for t in self.thread_list:
            t.start()

        for t in self.thread_list:
            t.join()

        return self.all_count


filename = '280.txt'
string_to_count = input('你要查什么: ')
print(single_thread_main(filename, string_to_count))
str_func = 'single_thread_main(%s, %s)' % (filename, string_to_count)
print('单线程总用时: ' + str(timeit.timeit('str_func', globals=globals())))

time_dic = {}
for i in range(2, 10):
    str_func2 = 'multi_thread_main(%s, %s, %s).run()' % (filename, string_to_count, i)
    time_dic[i] = timeit.timeit('str_func2', globals=globals())


least_id = 2
t_min = 1

for t_id, time in time_dic.items():
    if time < t_min:
        least_id = t_id
        t_min = time

print(least_id, time_dic[least_id])
