import socketserver
import dnslib
import threading
import dns.resolver


class MyDNSServer(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        dns_data = dnslib.DNSRecord.parse(data)

        p = dnslib.DNSRecord(dnslib.DNSHeader(id=dns_data.header.id, qr=1, aa=1, ra=1), q=dns_data.q)

        if dns_data.q.qtype == dnslib.QTYPE.A:
            if str(dns_data.q.qname) == 'www.example.com.':
                p.add_answer(
                    dnslib.RR(rname=dns_data.q.qname,
                              rtype=dnslib.QTYPE.A,
                              rdata=dnslib.A("93.184.216.34"),
                              ttl=60
                              )
                )
            elif str(dns_data.q.qname) == 'www.bing.com.':
                p.add_answer(
                    dnslib.RR(
                        rname=dns_data.q.qname,
                        rtype=dnslib.QTYPE.A,
                        rdata=dnslib.A("204.79.197.200"),
                        ttl=60
                    )
                )
        else:
            p.header.rcode = dnslib.RCODE.NXDOMAIN

        socket = self.request[1]
        socket.sendto(p.pack(), self.client_address)


def run_server():
    HOST, PORT = "127.0.0.10", 8053
    server = socketserver.UDPServer((HOST, PORT), MyDNSServer)
    server.serve_forever()


if __name__ == '__main__':

    # Start the DNS server in a new thread
    threading.Thread(target=run_server).start()

    # Query the DNS server
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ['127.0.0.10']  # IP of your local DNS server
    resolver.port = 8053

    for domain in ['www.example.com', 'www.bing.com']:
        answers = resolver.resolve(domain, 'A')
        for rdata in answers:
            print(f'IP for {domain}:', rdata.address)
