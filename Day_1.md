• Topics
o cData representation: Bits and Bytes, Storing text and numbers, Binary number
system.
o Basics of computer networks, IP addresses, Internet routing protocol
o UDP, TCP, HTTP, and The World Wide Web
o Programming basics: variables, strings, and numbers, if condition, loops
o Algorithm basis
Bit (বিট) কী?

Bit হলো কম্পিউটারের সবচেয়ে ছোট ডেটার একক।
এটা শুধু দুই রকম হতে পারে:

0

1

মানে একটা অন বা অফ সিগন্যালের মতো।
যেমন: 10110 — এখানে 5টি bit আছে।

🔹 Byte (বাইট) কী?

৮টা bit মিলে ১টা byte হয়।

1
 byte
=
8
 bits
1 byte=8 bits

উদাহরণ:

01010110 → এখানে 8 bit আছে → মানে 1 byte

সহজ উদাহরণ:

তুমি যদি দেখো 16-bit data, এর মানে:

16
 bits
=
2
 bytes
16 bits=2 bytes

আর 40-bit হলে:

40
 bits
=
5
 bytes
40 bits=5 bytes
📌 সারাংশ:
Unit	Value
1 bit	সবচেয়ে ছোট ডেটা (0 বা 1)
8 bits	= 1 byte
1 byte	কম্পিউটারে ছোট ডেটা স্টোরেজ ইউনিট
https://www.khanacademy.org/computing/ap-computer-science-principles/x2d2f703b37b450a3:digital-information/x2d2f703b37b450a3:binary-numbers/a/bits-and-binary




🔹 1) কম্পিউটার সরাসরি টেক্সট বা নাম্বার বোঝে না

কম্পিউটার শুধু বোঝে 0 এবং 1 (bit).

তাই টেক্সট আর নাম্বার—দুটোই প্রথমে binary (0/1) এ রূপান্তর করে তারপর মেমরিতে store করা হয়।

🔹 2) Text কীভাবে store হয়?

টেক্সট store করতে ASCII বা Unicode নামের standard ব্যবহার করা হয়।

উদাহরণ:

'A' → ASCII তে = 65

এই 65 আবার binary তে → 01000001

তারপর এটা 1 byte জায়গা নেয়।

আরেকটা উদাহরণ:

'a' → 97 → binary → 01100001

1 byte store হয়

একেকটা character = সাধারণত 1 byte বা 2 bytes (Unicode হলে)

🔹 3) Numbers কীভাবে store হয়?

নাম্বার দুইভাবে store হতে পারে:

(A) Integer (পূর্ণ সংখ্যা)

যেমন: 5, 100, -20
এসব binary তে রূপান্তর করে store হয়।

যেমন:

5 → binary → 00000101


ডেটা টাইপ অনুযায়ী জায়গা লাগে:

Type	Size
int (C/C++)	4 bytes
short	2 bytes
long long	8 bytes
(B) Floating point number (দশমিক সংখ্যা)

যেমন: 3.14, 9.81
এগুলো store হয় IEEE floating format অনুযায়ী।

float → 4 bytes

double → 8 bytes

এগুলো নাম্বারকে scientific format এ ভেঙে mantissa + exponent আকারে store করে।

🔹 সারাংশ (Easy Summary)
Data	কীভাবে store হয়?
Text	Character → number code (ASCII/Unicode) → binary
Number (int)	Binary তে রূপান্তর
Float	IEEE format (mantissa + exponent)
🔹 আরও সহজ কথায়:

টেক্সট: প্রতিটি অক্ষরকে একটা নাম্বারে রূপান্তর করে binary আকারে রাখা হয়।

নাম্বার: সরাসরি binary আকারে মেমরিতে রাখা হয়।




The Internet Protocol (IP) is one of the core protocols in the layers of the Internet, as you might guess from its name. It's used in all Internet communication to handle both addressing and routing.
The protocol describes the use of IP addresses to uniquely identify Internet-connected devices. Just like homes need mailing addresses to receive mail, Internet-connected devices need an IP address to receive messages.
When a computer sends a message to another computer, it must specify the recipient's IP address and also include its own IP address so that the second computer can reply.

IPv4 addresses
There are actually two versions of the Internet Protocol in use today:

IPv4, the first version ever used on the Internet

IPv6, a backwards-compatible successor

In the IPv4 protocol, IP addresses look like this:
74.125.20.113

Each IP address is split into 4 numbers, and each of those numbers can range from 0 to 255:
[0-255].[0-255].[0-255].[0-255]

We write those numbers in decimal, but the computer stores them in binary, like so:
01010101 01010101 01010101 01010101

Each number can represent 2^8 values, thanks to the 8 bits. That's also why we often call them "octets."
Overall, that's 2^32 possible values: 4,294,967,296 possible IPv4 addresses.

That's a lot! But remember, in the beginning, we said there are more than four billion devices connected to the Internet? Well, we're reaching the limit of possible IP addresses. It's time for plan B.

IP v6 addresses
Back when the Internet protocols were first invented, the creators didn't anticipate how popular it would become and that there would eventually be more than 2^32 devices wanting to connect to the Internet.
When it became obvious in the 1990s that the IPv4 addresses were running out, the IPv6 protocol was proposed with a much longer addressing scheme.

Here's an IPv6 address:
2001:0db8:0000:0042:0000:8a2e:0370:7334

Notice the letters in those numbers, like d and b in 0db8? Those are hexadecimal numbers, which means that the IPv6 address is much longer than it looks.

There are 8 hexadecimal numbers, and each number is 4 digits long. The highest value for each number is FFFF, since F is the highest digit in hexadecimal.

What's FFFF in decimal?

Each F represents 15 in decimal, so that's (15 × 4096) + (15 × 256) + (15 × 16) + (15 × 1) = 65,535.

Each 4-digit hexadecimal number can range between 0 and 65,535, so each number can represent 65,536 unique values—and there are 8 of them!
In total, each IPv6 address is represented by 128 bits, so there are 2^128 possible IP v6 addresses. That's 340 undecillion:
340,282,366,920,938,000,000,000,000,000,000,000,000,000

One way to find out your computer's IP address is by searching Google for "IP address". Google knows your IP address, since your computer sends a message to the Google computers as soon as it loads google.com.

Your IP address might be different tomorrow than it is today. Each ISP has a range of addresses they can assign, and they might give you a different one of those addresses each time they see your computer pop up on the network. That's called a dynamic IP address.

Switching to a different Wi-Fi network will definitely give you a new IP address, since each Wi-Fi provider has its own range of addresses that it can give out.

Computers that act as servers, like the computers that power Google.com, often have static IP addresses. That makes it easier for computers to quickly send search requests to the Google servers.

Check your understanding
Identify whether each address below is IPv4, IPv6, or invalid:

IP address	Address type?
119.67.44.86	IPv4 ✅
94.49.190.138	IPv4 ✅
258.151.50.253	Invalid ❌
e0f8:af58:eee6:52b	Invalid ❌
d938:2da7:b596:6d34:3970:6789:c941:2340	IPv6 ✅
d938:2da7:b596:6d3:3970:6789	Invalid ❌
