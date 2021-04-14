import pyshark

file = pyshark.FileCapture('resources/WebApp.pcapng')

print(file[0])