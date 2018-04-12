##coding=utf-8
#Python对协程（Coroutine）的支持是通过generator实现的。
#https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432090171191d05dae6e129940518d1d6cf6eeaaa969000
'''
生成器理解要点: 
    1: 执行流程，执行时，遇到yield语句时，向调用者返回一个值（返回yield表达式后面的值，即 yield X 中的 X），且generator挂起，保留状态，再次执行时从离开的地方继续。
    2：理解send的作用, G.send(value), 作用1，恢复生成器的执行, 作用2，赋值，(yield X) = value
    3：理解赋值语句 ms = G.send(value), ms 接受的返回值就是generator函数的返回值即 yield X 中的 X    
    4：理解赋值语句 y = yield X +9 的意思，y = (yield X) + 9
    5：G.send(value)中的value是必需的参数，不能空，而且对a just-started generator只能send None
    6：next(G) 或 G.__next__ 等同于 G.send(None)
    7：generator函数中的return, 会引发StopIteration，return('str....')作用相当于Raise stopIteration（'str...')
'''

#生产者-消费者模型
def consumer():
    r = ''
    while True:
        nc = yield r   
        if not nc:
            return
        print('[CONSUMER] Consuming %s...' % nc)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        rms = c.send(n)
        print('[PRODUCER] Consumer return message: %s' % rms)
    c.close()

c = consumer()
produce(c)