from ftplib import FTP
ftp = FTP("172.30.1.23")
print('banner:',ftp.getwelcome())
print('login:',ftp.login())
print('LIST:',ftp.retrlines('LIST'))
print('RETR:',ftp.retrbinary('RETR boanproject.txt',
                     open('boan.txt', 'wb').write))

print('STOR:',ftp.storbinary('STOR boanproject2.txt',
                     open('boanproject2.txt', 'rb')))


