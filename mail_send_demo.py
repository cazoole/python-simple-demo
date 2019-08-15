from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import urllib


def main():
    # 创建一个带有附件的邮件消息对象
    message = MIMEMultipart()

    sender = 'xxx@qq.com'
    receivers = ['xxxx@qq.com']

    text_content = MIMEText('附件中有文本和图片，请查收!', 'plain', 'utf-8')
    message['Subjext'] = Header('带附件的测试邮件', 'utf-8')
    message.attach(text_content)
    print('开始处理附件')

    with open('xxxxx/Test.txt', 'rb') as f:
        txt = MIMEText(f.read(), 'base64', 'utf-8')
        txt['Context-Type'] = 'text/plain'
        txt['Content-Disposition'] = 'attachment; filename=hello.txt'
        message.attach(txt)
        print("附件文本处理完毕")

    with open('xxxx/picture.jpg', 'rb') as f:
        ctype = 'application/octet-stream'
        mainType, subtype = ctype.split('/', 1)
        picture = MIMEImage(f.read(), _subtype=subtype)
        picture['Content-Disposition'] = 'attachment; filename=picture.jpg'
        message.attach(picture)
        print("图片附件处理完毕")

    message['From'] = Header(sender, 'utf-8')
    message['To'] = Header('xx，xxx，xxx', 'utf-8')
    message['Subject'] = Header('这个是测试的实验邮件，有图片和文本附件，看到了阔以回复哈', 'utf-8')
    print("开始准备发送邮件")
    smtper = SMTP('smtp.qq.com')
    smtper.login(sender, '')
    smtper.sendmail(sender, receivers, message.as_string())
    print(message['From'])
    print("邮件发送完毕")


if __name__ == '__main__':
    main()
