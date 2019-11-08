# -*- coding:utf-8 -*-
# @Author: 'XingXiaolei'
# @Time  : '2019-10-15 17:05'
import os
import unittest, time
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.application import MIMEApplication
from public import HTMLTestReportCN


curpath = os.path.dirname(os.path.realpath(__file__))
case_path = os.path.join(curpath)
now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))

currentDir = os.path.abspath(os.path.dirname(__file__))
proDir = os.path.split(currentDir)[0]
report_path = os.path.join(proDir, 'report')

dis = unittest.defaultTestLoader.discover(case_path,pattern="test*.py")

def send_mail(file_new,receivers,reportname,starttime,endtime,passge,fail,erro):
    mail_host = "smtp.ikang.com"  # 设置服务器
    mail_user = "xiaolei.xing@ikang.com"  # 用户名
    mail_pass = "Xxl51868,"  # 口令
    sender = "xiaolei.xing@ikang.com"   #发送邮件的邮箱
    if ',' in receivers:
        receivers = receivers.split(',')  # 字符串转化为列表，邮件接受者，取定时任务里的具体值
    else:
        receivers = receivers
    reportname = reportname  # 测试报告名称，取项目名称为测试报告名称

    # 定义正文
    msg = MIMEMultipart()  # 构造MIMEMultipart对象做为根容器
    msg['From'] = Header("自动化测试", 'utf-8')
    msg['To'] = Header("To相关收件人", 'utf-8')
    # 邮件正文内容
    msg.attach(MIMEText("<font color=black face=微软雅黑 size=5 style=line-height:3>【%s_PROD_UI_自动化测试报告】 </font><br>"
                        "<font color=black style=line-height:2 face=微软雅黑><strong>开始时间： </strong></font>%s<br>"
                        "<font color=black style=line-height:2 face=微软雅黑><strong>结束时间： </strong></font>%s<br>"
                        "<font color=black style=line-height:2 face=微软雅黑><strong>合计耗时： </strong></font>%s <br>"
                        "<font color=black style=line-height:2 face=微软雅黑><strong>用例总数： </strong></font>%s<br>"
                        "<font color=black style=line-height:2 face=微软雅黑><strong>执行结果：<font color=green >PASS： %s </font><font color=red >  FAIL：     %s</strong></font><font color=orange >  Erro： %s</strong></font>  <font color=#8a2be2 >  通过率=%.2f%%</font><br>"
                        "<font color=blue style=line-height:2 face=微软雅黑>详细内容请查看附件. </font><br>"
                        "<font color=#83838c style=line-height:2 face=微软雅黑>(--来自UI自动化测试--)</font>"
                        % (reportname, starttime, endtime, endtime - starttime,int(passge)+int(fail)+int(erro), passge, fail,erro,int(passge)*100/(int(passge)+int(fail)+int(erro))),"html", "utf-8"))

    # 构造附件
    att1 = MIMEText(open(file_new, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename=TJB_UI_TestReportDetails.html'
    msg.attach(att1)

    # 邮件正文内容
    # mail_body = f.read()
    # f.close()
    # msg.attach(MIMEText(mail_body, _subtype='html', _charset='utf-8'))

    # 定义标题
    msg['Subject'] = u"【%s_PROD_UI_自动化测试报告】"%reportname

    # 定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')


    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, msg.as_string().encode("utf-8"))
        # log_build.log("邮件发送成功")
        # log_build.log("邮件接收人：%s" % receivers)
    except smtplib.SMTPException:
        # log_build.log("Error: 邮件发送失败")
        pass

def create_report(all_case):
    fileName = "AutoTest_TJBUI_%s.html" % now
    file_path = os.path.join(report_path, fileName)
    fp = open(file_path, 'wb')
    runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                             title='AutoTest_TJBUI',
                                             description='体检宝ui自动化测试',
                                             tester='xiaolei.xing',
                                             verbosity=2)
    result, stopTime, startTime, Pass,fail,error = runner.run(all_case)
    fp.close()
    return stopTime, startTime, Pass,fail,error,file_path
if __name__ == '__main__':
    startTime, stopTime, Pass, fail, error, file_path = create_report(dis)
    send_mail(file_new=file_path, receivers='xiaolei.xing@ikang.com', reportname="TJB", starttime=startTime,
              endtime=stopTime,
              passge=Pass, fail=fail, erro=error)
