## 配置文件说明

### 节点说明

| 节点名 |  节点描述 | 父节点 | 节点属性   |  属性描述 |
| ---- | ----- | ----- | ---- | ------ |
| ThreadGroups | 根节点 |  无 | 无 |  无 |
| ThreadGroup | 线程组节点| ThreadGroups | name | 线程组名 |
|  | |  | criteria | 任务进入该线程组的条件,定义格式:包路径.文件名.类名 |
|  | |  | strategy | 线程组内线程的任务分配策略,定义格式:包路径.文件名.类名 |
| Thread | 线程节点| ThreadGroup | name | 线程名 |
|  | |  | criteria | 任务进入该线程的条件,定义格式:包路径.文件名.类名 |

#### strategy 与 criteria 说明

##### 优先级
strategy > criteria

##### strategy
定义的线程内任务的分配策略，当一个任务来时，如何优先分配到哪些线程

##### criteria
如果不满足分配策略，则按定义的进入线程的条件，进入执行线程

##### DefaultStrategy策略流程图
[](https://github.com/thcpc/PyPackage/blob/main/flask_edk_threads/image.png)


### 例子
#### 定义 XML 文件 
```xml
<?xml version="1.0" encoding="UTF-8"?>
<ThreadGroups>
    <ThreadGroup name="1" criteria="example.criteria.dev1.Dev1" strategy="flask_threads.strategies.default_strategy.DefaultStrategy">
        <Thread name="1-1" criteria="example.criteria.small_file.SmallFile" />
        <Thread name="1-2" criteria="example.criteria.medium_file.MediumFile" />
        <Thread name="1-3" criteria="example.criteria.big_file.BigFile" />
    </ThreadGroup>
    <ThreadGroup name="2" criteria="example.criteria.dev2.Dev2" strategy="flask_threads.strategies.default_strategy.DefaultStrategy">
        <Thread name="2-1" criteria="example.criteria.small_file.SmallFile"/>
        <Thread name="2-2" criteria="example.criteria.medium_file.MediumFile"/>
        <Thread name="2-3" criteria="example.criteria.big_file.BigFile"/>
    </ThreadGroup>
    <ThreadGroup name="3" criteria="example.criteria.dev3.Dev3" strategy="flask_threads.strategies.default_strategy.DefaultStrategy">
        <Thread name="3-1" criteria="example.criteria.small_file.SmallFile"/>
        <Thread name="3-2" criteria="example.criteria.medium_file.MediumFile"/>
        <Thread name="3-3" criteria="example.criteria.big_file.BigFile"/>
    </ThreadGroup>
</ThreadGroups>
```
#### 定义 criteria
| 函数名 | 是否需要覆写 | 函数说明 |
| ---- | ----- | ------ |
| true | 必须 | 定义满足入组的条件 |

```python
# 继承 AbstractCriteria
class BigFile(AbstractCriteria):
	# 定义 为 真的条件 
    def true(self, criteria_desc):
        return criteria_desc.get("file_size") > 1024 * 800
```

#### 定义 strategy
| 函数名 | 是否需要覆写 | 函数说明 |
| ---- | ----- | ------ |
| distribute | 不需 | 定义分配任务的模板函数 |
| balance | 可选 | 定义分配任务的模板函数 |
| criteria | 可选 | 默认定义是按入组条件进入线程组和线程 |

```python
# 继承 AbstractStrategy
class DefaultStrategy(AbstractStrategy):

	# 制定线程组内，任务分配给线程的策略
    def balance(self, event: AbstractEvent) -> int:
        length = self.task_thread_group.thread_count()
        # 策略1. 优先使用空闲的线程, 处理任务
        for i in range(length):
            if self.task_thread_group.index(i).qsize() == 0: return i

        # 策略2. 找出任务数最先的线程，并且剩余任务数 < 2. 即将空闲的线程， 处理任务
        min_index = self.min()
        if self.task_thread_group.index(min_index).qsize() <= 2: return i

        # 没有满足策略的线程，任务按条件进入对应的线程
        return -1

    def min(self) -> int:
        min_index = 0
        for i in range(1, self.task_thread_group.thread_count()):
            if self.task_thread_group.index(i - 1).qsize() < self.task_thread_group.index(i).qsize():
                min_index = i
        return min_index
```



## 事件定义
### 函数说明
| 函数名 | 是否需要覆写 | 函数说明 |
| ---- | ----- | ------ |
| action | 必须 | 定义线程的执行内容 |
| call_back | 可选 | 定义线程的执行成功的回调内容 |
| fall_back | 可选 | 定义线程的执行失败的回调内容 |
| criteria_desc | 可选 | 进入线程和线程组的条件参数，默认为 空的字典 |

### 例子
```python
# 继承 AbstractEvent
class DBEvent(AbstractEvent):
    def __init__(self, host, file_size):
        super().__init__()
        self._host = host
        self._file_size = file_size
    #　覆写 action 函数，定义线程要执行的内容
    def action(self):
        with open(Path("D:\\github\\PyPackage\\flask_threads\\src\\example\\output").joinpath(self.event_id), 'w') as f:
            f.write(f'{self.task_thread.thread_name} {self.event_id} {self._host} {self._file_size}')

    # 定义进入线程组和线程要检测的条件
    def criteria_desc(self):
        return dict(host=self._host, file_size=self._file_size)
```

## Flask 引入
```python
app = Flask(__name__)
# 指定配置文件config_file 为绝对路径
fts = FlaskThreads(config_file=Path("D:\\github\\PyPackage\\flask_threads\\src\\example\\ThreadConfiguration.xml"))

# 注册FlaskThreads
fts.init_app(app)

#　指定　Flask　异常退出时，关闭线程组
def handle_sigint(sig, frame):
    fts.stop_ft()
    print('Close The Flask')
    sys.exit(0)

signal.signal(signal.SIGINT, handle_sigint)
if __name__ == '__main__':
	#　注册 Flask 非正常关闭处理
	#  不指定的话，可能会造成 Flask 非正常退出的时候，线程常驻内存.
    
    app.run(debug=True)

```

## 项目实例
[例子](https://github.com/thcpc/PyPackage/tree/main/flask_edk_threads/example)
```shell
flask --app app run
```

## 错误日志
FTErrorLog.txt

# Release 
## 1.0.0 
## 1.0.1
- 1.在失败的回调函数中捕获系统异常

## 1.0.2
- 1. event 增加 before_action,

## 1.0.3
- 1. 修复相同的event重复进线程