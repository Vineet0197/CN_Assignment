# CN_Assignment
BITS Pilani (SS ZC467) Computer Networks Assignment

# Topic
Implementation of HTTP Protocol Through Wireshark

# WireShark
Wireshark is the world's leading Network traffic Analyzer and open-source packet Analyzer, which is used for education, analysis, software development, commounication protocol development, and network troubleshooting. 

# Uses of Wireshark
1. It is used by network security engineers to examine security problems.
2. It allows the users to watch all the traffic being passed over the network.
3. It is used by network engineers to troubleshoot network issues.
4. It also helps to troubleshoot latency issues and malicious activities on your network.
5. It can also analyze dropped packets.
6. It helps us to know how all the devices like laptop, mobile phones, desktop, switch, routers, etc., communicate in a local network or the rest of the world.

# What is Packet?
A packet is a unit of data which is transmitted over a network between the origin and the destination. Network packets are small, i.e., maximum 1.5 Kilobytes for Ethernet packets and 64 Kilobytes for IP packets. The data packets in the Wireshark can be viewed online and can be analyzed offline.

# Steps to Capture Traffic through Wireshark
1. Make sure a simple Web application is running on the server.
2. This application can be started by running python code written in edu/bits/pilani/cnAssignment/WebApi.py
3. This application includes three pages i.e., Main page, and two subsequent pages.
4. After application is started, open Wireshark and start Capture packet using Adapter for Loopback traffic Capture.
5. Use the display filter "http" to capture HTTP packet.
