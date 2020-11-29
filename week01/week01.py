def timeRecord():
    import logging
    logging.basicConfig(filename = '/var/log/python- 当前日期 /函数调用.log',
                        level = logging.DEBUG,
                        datefmt =  '%Y-%m-%d %H:%M:%S',
                        format = '%(asctime)s %(name)-8s %(levelname)-8s [Line: %(lineno)d] %(message)s') 
    logging.debug('显示为函数被调用时间')
if __name__ == '__main__':
    timeRecord()

