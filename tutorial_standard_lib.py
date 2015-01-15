__author__ = 'Administrator'

if __name__ == '__main__':
    import  random
    fruit = ['apple','pear','banana']
    print(random.choice(fruit))
    ls =random.sample(range(100),10)
    print(ls)

    import zlib
    s = b'witch which has which withces writes watch'
    print('s len is :',len(s))
    t = zlib.compress(s)
    print(len(t))
    print(t)
    zlib.decompress(t)
    print(t)
    c = zlib.crc32(s)

    #thread
    import  threading,zipfile

    class AsyncZip(threading.Thread):
        def __init__(self,infile,outfile):
            threading.Thread.__init__(self)
            self.infile = infile
            self.outfile = outfile
        def run(self):
            f = zipfile.ZipFile(self.outfile,'w',zipfile.ZIP_DEFLATED)
            f.write(self.infile)
            f.close()
            print('finished backgroud zip of : ', self.infile)

    backgroud = AsyncZip('myfile.txt','myarchive.zip')
    backgroud.start()
    print('The main program continue to run in foregroud')
    backgroud.join()
    print('The program waited until backgroud was done')

    #log 日志
    import logging
    logging.debug('Debuging information')
    logging.info ( ' Informational ␣ message ' )
    logging.warning( ' Warning: config␣ file ␣%s ␣not ␣ found' , ' server.conf ' )
    logging.error( ' Error␣ occurred' )
    logging.critical ( ' Critical ␣ error␣ --␣ shutting␣ down' )

    #处理列表的工具
    from array import array
    a = array('H',[4000,10,700,2222])
    res = sum(a)
    print(res)
    print(a[1:3])
