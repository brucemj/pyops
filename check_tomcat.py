# -*- coding: UTF-8 -*-

import os, time, datetime
import httplib
import urllib2 , urllib , json
import log

def time_txt():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
def time_ms():
    return  time.time()

ck_app = {
    'css-waixiao': {
        'http': 'http://10.11.12.185:9081',
        #'http': 'http://119.23.23.152:8080',
        'url': {
            'path' : '/userservice/odm/addodm.do',
            'time' : 8 ,
            'values' : {
                'odm' : r'{"cid":"13677741","flash":"KMR31000BA_B614","imei":"356451080300622","lac":"1445","lcm":"ili9881c_hd720_dsi_vdo","mainCamera":"s5k3h7yxdl_mipi_raw","mcc":"410","md5":"352891725f196f763e556a134f76c94d","mnc":"1","phoneModel":"QMobile+E1","platformModel":"MT6735P","softwareVersion":"QMobileE1_MP_11_26","subCamera":"ov5670_mipi_raw","totalRam":"3GB","totalRom":"16GB"}'
            }
        },
        'get_pid': " ps aux | grep java | grep '/konkacss/oversea/apache-tomcat-7.0.64' | grep -v ' grep '",
        'stop': "/konkacss/oversea/apache-tomcat-7.0.64/bin/shutdown.sh",
        'start': "/konkacss/oversea/apache-tomcat-7.0.64/bin/startup.sh"
    },
    'css-xiaob': {
        'http': 'http://119.23.23.152:8080',
        #'http': 'http://10.11.12.184:8080',
        'url': {
            'path' : '/userservice/electroniccardover/getServicePhone.do',
            'time' : 8 ,
            'values' : {
                #'odm' : r'{"cid":"13677741","flash":"KMR31000BA_B614","imei":"356451080300622","lac":"1445","lcm":"ili9881c_hd720_dsi_vdo","mainCamera":"s5k3h7yxdl_mipi_raw","mcc":"410","md5":"352891725f196f763e556a134f76c94d","mnc":"1","phoneModel":"QMobile+E1","platformModel":"MT6735P","softwareVersion":"QMobileE1_MP_11_26","subCamera":"ov5670_mipi_raw","totalRam":"3GB","totalRom":"16GB"}'
                'over': r'{"cell":{"cid":"146062593","lac":"28765","mcc":"505","mnc":"1"},"imei":"863385039835674","md5":"c9eca0340c3eaeb20a6693460c5b9a08"}'
            }
        },
        'get_pid': " ps aux | grep java | grep '/konkacss/oversea2/apache-tomcat-7.0.64' | grep -v ' grep '",
        'stop': "/konkacss/oversea2/apache-tomcat-7.0.64/bin/shutdown.sh",
        'start': "/konkacss/oversea2/apache-tomcat-7.0.64/bin/startup.sh"
    }
}

def get_pid(cmd_ck):
    css_tomcat = os.popen(cmd_ck).read()
    pid_arr = css_tomcat.split()
    if len(pid_arr)>2:
        css_pid = pid_arr[1]
    else:
        css_pid = ''
    return css_pid

def get_hostname():
    return os.popen('hostname').read()

def kill_pid(pid, arg=' -9 '):
    os.system(' kill %s %s '% (arg, pid) )

def run_cmd(path, arg=''):
    os.system( ' %s %s ' % (path, arg) )

def restart_tm(stop_cmd, pid, start_cmd, wait_time=100):
    logtm.info('stop tomcat: %s' % stop_cmd)
    run_cmd(stop_cmd)
    css_pid = get_pid(pid)
    logtm.info('kill -9 %s' % css_pid )
    kill_pid(css_pid, arg=' -9 ')
    logtm.info('start tomcat: %s' % start_cmd)
    run_cmd(start_cmd)
    ping_c(wait_time)

def ping_c(c=2):
    os.system(' ping 127.0.0.1 -c ' + str(c) + ' > /dev/null 2>&1')

def post_http(
    url = 'http://www.baidu.com/s',
    values = {'name': 'Michael Foord', 'location': 'Northampton', 'language': 'Python'},
    req_timeout = 8,
    retry = 2
):
    req_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome_ck', 'Content-Type': 'application/x-www-form-urlencoded'}
    postdata = urllib.urlencode(values)
    req = urllib2.Request(url, postdata, req_header)

    doc = False
    trynum = retry
    while retry > 0:
        try:
            t1 = time_ms()
            doc = urllib2.urlopen(req, None, timeout=req_timeout).read()
            logtm.info('%s open success, Response_time:%6.4f s; retry=%d/%d; doc=%s' %
                (url, time_ms()-t1, trynum-retry+1 , trynum, doc[0:13] )
            )
            #print doc
            return doc
        except Exception, e:
            logtm.error( '%s open fail in %d s ; retry=%d/%d;' % (url , req_timeout, trynum-retry+1 , trynum ) )
            retry -= 1

    return doc
    #return json.loads(doc)

def check_main(var_cnf , server='s_waixiao'):
    url = var_cnf[server]['http'] + var_cnf[server]['url']['path']
    values = var_cnf[server]['url']['values']
    req_timeout = var_cnf[server]['url']['time']

    httpreq = post_http(url=url, values=values, req_timeout=req_timeout)
    if httpreq == False:
        logtm.error('%s tomcat is crash ! check_url=%s' % (server, url))

        stop_cmd = var_cnf[server]['stop']
        start_cmd = var_cnf[server]['start']
        pid = var_cnf[server]['get_pid']
        restart_tm(stop_cmd, pid, start_cmd)

if __name__ == "__main__":
    hostname = get_hostname().strip()
    #hostname = 'css-xiaob'
    logfile = 'check_tm_' + hostname + '.log'
    logtm = log.console_set(logfile, lvl=1)

    if hostname == 'css-waixiao' or hostname == 'css-xiaob':
        r , t0 = 0 , time_txt()
        while True:
            print 'Start: %s ; Num: %d' % ( t0 , r )
            check_main(ck_app, server=hostname)
            r += 1
            ping_c( 306 )
