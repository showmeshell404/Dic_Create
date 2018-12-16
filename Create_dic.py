# coding=utf-8

import exrex
import sys

'''
host=http://123.456.com or 123.456.com or https://123.456.com or  http://123.456.com/
'''

web_white = ['com', 'cn', 'gov', 'edu', 'org', 'www']


def host_para(host):
    if '://' in host:
        host = host.split('://')[1].replace('/', '')

    if '/' in host:
        host = host.replace('/', '')
    return host


# 结合常用字典创造新的dic
def dic_creat(hosts):
    web_dics = hosts.split('.')
    # 核心的生成规则，写入配置文件

    f_rule = open('rule.ini', 'r')
    for i in f_rule:
        if '#' != i[0]:
            rule = i

    f_pass_out = open('dictonary.txt', 'w')
    f_pass_out.close()

    for web_dic in web_dics:
        if web_dic not in web_white:
            f_pass = open('pass_0.txt', 'r')
            for dic_pass in f_pass:
                dics = list(exrex.generate(rule.format(web_dic=web_dic, dic_pass=dic_pass.strip('\n'))))

                for dic in dics:
                    if len(dic) > 4:
                        f_pass_out = open('dictonary.txt', 'a+')
                        f_pass_out.write(dic + '\n')
                        f_pass_out.close()
                        print dic


if __name__ == '__main__':
    if len(sys.argv) == 2:
        dic_creat(host_para(sys.argv[1]))
    else:
        print 'Usage:%s www.demo.com' % sys.argv[0]
        sys.exit(-1)
