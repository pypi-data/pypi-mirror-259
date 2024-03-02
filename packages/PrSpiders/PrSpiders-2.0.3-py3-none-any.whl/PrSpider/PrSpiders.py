import time, os
import requests
import inspect
import traceback
import threading
import multiprocessing
from .log import *
from .utils import *
from .pipelines import *
from .pyconn import PrMysql
from .Request import Request
from collections.abc import Iterator
from .settion import _IT, settions, filter_settions
from concurrent.futures import ThreadPoolExecutor, as_completed

author = """
 ____
|  _ \ ___ _ __  _ __
| |_) / _ \ '_ \| '__|
|  __/  __/ | | | |
|_|   \___|_| |_|_|
"""


class PrSpiders(settions):

    def __init__(self, **kwargs):
        self.start_preparation()
        self.spider_run()

    def start_preparation(self):
        """初始化工作"""
        self.start_time = time.time()
        if self.custom_settings:
            for key, value in self.custom_settings.items():
                key = key.lower()
                if key in filter_settions:
                    continue
                if isinstance(value, str):
                    if value.isdigit():
                        value = int(value)
                setattr(settions, key, value)
        assert self.thread_num > 0, 'thread_num must be > 0'
        settions.init += 1
        if settions.init <= 1:
            Log(self).loggering()
        self.loging = loging(loguercor)
        self.executor = ThreadPoolExecutor(self.thread_num)
        self.Request = requests.session() if self.session else requests
        self.pipelines = dict_sort(self.pipelines)
        pipelines_msg = str(self.pipelines).replace(',', ',\n')
        loguercor.log('Start', Start % (self.thread_num, self.retry, self.pid, self.download_delay, self.download_num,
                                        self.log_level.upper()))
        loguercor.log('Pipelines', f'Used Pipelines:\n{pipelines_msg}')

    def spider_run(self):
        """
        线程一: 爬虫业务代码（请求入队列）
        线程二: 监听队列
        """
        self.thread_requests = threading.Thread(target=self.start_call)
        self.thread_queue = threading.Thread(target=self.start_queue)

        # 启动线程
        self.thread_requests.start()
        self.thread_queue.start()

        # 等待线程结束
        self.thread_requests.join()
        self.thread_queue.join()

    def start_queue(self):
        while True:
            qlist = []
            qsize = self.Queues.qsize()
            # 检查队列是否为空
            if not self.Queues.empty():
                queue_list = []
                num_to_download = min(self.download_num, qsize)
                for _ in range(num_to_download):
                    data = settions.Queues.get().data
                    wait = data.get('wait')
                    queue_list.append(data)
                    del data['wait']
                    if wait:
                        break
                qlist.append(queue_list)
                for qdata in qlist:
                    for item in qdata:
                        task = self.executor.submit(self.make_request, **item)
                        self.futures.add(task)
                for future in as_completed(self.futures):
                    result = future.result()
                    worker_exception = future.exception()
                    result_class_name = result.__class__.__name__
                    self.futures.remove(future)
                    if isinstance(result, Iterator) and result_class_name != 'None':
                        try:
                            for item in result:
                                self.loging.yie(item)
                                pipeline_process_item(item, self)
                        except Exception as e:
                            self.trace(e)
                    else:
                        pass

                    if worker_exception:
                        self.trace(worker_exception)

                time.sleep(self.download_delay)
            else:
                if self.thread_requests.is_alive():
                    pass
                else:
                    break

    def trace(self, worker_exception, msg=""):
        formatted_traceback = traceback.format_exception(type(worker_exception),
                                                         worker_exception,
                                                         worker_exception.__traceback__)
        formatted_traceback = f'{msg}'.join(formatted_traceback)
        if self.traceback:
            self.loging.exception(worker_exception)
        else:
            self.loging.error(formatted_traceback)

    def start_call(self, *args, **kwargs):
        self.open()
        pipeline_start(self)
        self.start_requests(*args, **kwargs)
        while True:
            if not settions.futures and not self.Queues.qsize():
                break
            time.sleep(self.schedule_time)
        self.close()
        pipeline_close(self)

    def open(self):
        """爬虫启动前执行函数"""
        pass

    def close(self):
        """爬虫关闭后执行函数"""
        pass

    def start_requests(self, *args, **kwargs):
        if self.start_urls is None:
            raise AttributeError("Crawling could not start: 'start_urls' not found ")
        if isinstance(self.start_urls, list):
            for url in self.start_urls:
                self.Requests(url=url, callback=self.parse)
        else:
            self.Requests(url=self.start_urls, callback=self.parse)

    def parse(self, response):
        pass

    @staticmethod
    def Requests(url, headers=None, method="GET", meta=None, retry=True, callback=None, retry_num=3,
                 encoding="utf-8", retry_time=3, timeout=30, priority=0, wait=False, retry_xpath=None, **kwargs):
        if isinstance(url, str):
            query = {
                "url": url,
                "headers": headers,
                "method": method,
                "meta": meta,
                "retry": retry,
                "callback": callback,
                "retry_num": retry_num,
                "encoding": encoding,
                "retry_time": retry_time,
                "timeout": timeout,
                "wait": wait,
                "retry_xpath": retry_xpath,
            }
            frame = inspect.currentframe().f_back
            caller_name = frame.f_code.co_name
            if caller_name == 'start_requests':
                deep = priority
            else:
                if priority != 0:
                    deep = priority
                else:
                    if caller_name not in settions.deep_func:
                        settions.deep_func.append(caller_name)
                    deep = -(settions.deep_func.index(caller_name)) - 1
            query.update(**kwargs)
            item = _IT(deep, query)
            settions.Queues.put(item)
        elif isinstance(url, list):
            for url in url:
                PrSpiders.Requests(url, headers=headers, method=method, meta=meta, retry=retry, callback=callback,
                                   retry_num=retry_num, encoding=encoding, retry_time=retry_time, timeout=timeout,
                                   priority=priority, retry_xpath=retry_xpath, wait=wait, **kwargs)
        else:
            raise TypeError("url must be str or list")

    def make_request(self, url, callback, headers=None, retry_num=3, method="GET", meta=None, retry=True,
                     encoding="utf-8", retry_time=3, timeout=30, **kwargs):
        try:
            self.request_num += 1
            response = self.download(url=url, headers=headers, retry_time=retry_num, method=method,
                                     meta=meta, retry=retry, encoding=encoding, retry_interval=retry_time,
                                     timeout=timeout, settion=settions, **kwargs)
            self.loging.crawl(f"Response ({response.code}) <{method.upper()} {url}>")
            self.retry_num += int(response.meta.get("retry_num"))
            if response and response.ok:
                self.success_num += 1
            else:
                self.false_num += 1
            return callback(response)
        except Exception as e:
            self.trace(e)

    def download(self, **kwargs):
        response = Request(self, self.Request).get(**kwargs)
        return response

    def error(self, response):
        pass

    def process_timestamp(self, t):
        timeArray = time.localtime(int(t))
        formatTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        return formatTime

    def __del__(self):
        """
         类销毁时执行的函数
         """
        end_time = time.time()
        spend_time = end_time - self.start_time
        try:
            average_time = spend_time / self.request_num
        except ZeroDivisionError:
            average_time = 0
        data = [
            ('Thread Num', self.thread_num),
            ('Download Delay', self.download_delay),
            ('Download Num', self.download_num),
            ('Request Num', self.request_num),
            ('Success Num', self.success_num),
            ('False Num', self.false_num),
            ('Retry Num', self.retry_num),
            ('Spend Time', '%.3fs' % spend_time),
            ('Average Time', '%.3fs' % average_time),
            ('Start Time', self.process_timestamp(self.start_time)),
            ('End Time', self.process_timestamp(end_time)),
        ]
        m = close_sign(data)
        loguercor.log('Close', m)


def run_spider(spider: list or object, pool=10):
    """
    爬虫任务启动调度, 采用进程池方式.
    """
    pool = multiprocessing.Pool(pool)
    if isinstance(spider, list):
        for spider_class in spider:
            pool.apply_async(spider_class)
    else:
        pool.apply_async(spider)
    pool.close()
    pool.join()
