# DNS Enumeration

> The Domain Name System (DNS) is the hierarchical and decentralized naming system used to identify computers reachable through the Internet or other Internet Protocol (IP) networks. The resource records contained in the DNS associate domain names with other forms of information. These are most commonly used to map human-friendly domain names to the numerical IP addresses computers need to locate services and devices using the underlying network protocols, but have been extended over time to perform many other functions as well. The Domain Name System has been an essential component of the functionality of the Internet since 1985.  

Source : Wikipedia 

## DNS enumeration 
DNS enumeration is the process of locating all the DNS servers and their corresponding records for an organization. A company may have both internal and external DNS servers that can yield information such as usernames, computer names, and IP addresses of potential target systems. There are a lot of tools that can be used to gain information for performing DNS enumeration. The examples of tool that can be used for DNS enumeration are NSlookup, DNSstuff, American Registry for Internet Numbers (ARIN), and Whois. To enumerate DNS, you must have understanding about DNS and how it works.

You must have knowledge about DNS records. The list of DNS record provides an overview of types of resource records (database records) stored in the zone files of the Domain Name System (DNS). The DNS implements a distributed, hierarchical, and redundant database for information associated with Internet domain names and addresses. In these domain servers, different record types are used for different purposes. The following list describes the common DNS record types and their use:

|**DNS Record types**|methods|description|
|:-----------------------|:----------|:--------------|
|dns query|A|***Address record***, Returns a 32-bit IPv4 address, most commonly used to map hostnames to an IP address of the host, but it is also used for DNSBLs, storing subnet masks in RFC 1101, etc.|
|dns query|CNAME|***Canonical name record***, Alias of one name to another: the DNS lookup will continue by retrying the lookup with the new name.|
|dns query|AAAA|***IPv6 address record***, Returns a 128-bit IPv6 address, most commonly used to map hostnames to an IP address of the host.|
|dns query|MX|***Mail exchange record***, Maps a domain name to a list of message transfer agents for that domain|
|dns query|NS|***Name server record***, Delegates a DNS zone to use the given authoritative name servers|
|dns query|SOA|***zone of authority record***, Specifies authoritative information about a DNS zone, including the primary name server, the email of the domain administrator, the domain serial number, and several timers relating to refreshing the zone.|
|dns query|SPF|***Sender Policy Framework***, a simple email-validation system designed to detect email spoofing by providing a mechanism to allow receiving mail exchangers to check that incoming mail from a domain comes from a host authorized by that domain's administrators.|
|dns query|TXT|***Text record***, Originally for arbitrary human-readable text in a DNS record.|
|dns query|PTR|***Pointer record***, Pointer to a canonical name. Unlike a CNAME, DNS processing stops and just the name is returned. The most common use is for implementing reverse DNS lookups, but other uses include such things as DNS-SD.|
|dns query|SRV|***Service locator***, Generalized service location record, used for newer protocols instead of creating protocol-specific records such as MX.|
|dns query|NSEC|***Next Secure record***, Part of DNSSEC—used to prove a name does not exist. Uses the same format as the (obsolete) NXT record.|
|dns query|AXFR|***Authoritative Zone Transfer***, Transfer entire zone file from the master name server to secondary name servers. **DNS Zone Transfer** is typically used to replicate DNS data across a number of DNS servers, or to back up DNS files. A user or server will perform a specific zone transfer request from a ―name server.‖ If the name server allows zone transfers to occur, all the DNS names and IP addresses hosted by the name server will be returned in human-readable ASCII text.|
|dns query|IXFR|***Incremental Zone Transfer***, Transfer entire zone file from the master name server to secondary name servers.|
|dns query|DNS Wildcard|Check if nameserver enable wildcard query, or dns faked.|
|dns query|domain bruteforce|bruteforce subdomains with wordlists.|
|dns query|reverse bruteforce|reverse ip for domain|
|dns query|srv bruteforce|bruteforce srv records|
|dns query|gtld bruteforce|bruteforce gtld records|
|dns query|tld bruteforce|bruteforce tld records|

## Read the following documentation :

1. https://tryhackme.com/room/dnsindetail
1. https://securitytrails.com/blog/dns-enumeration
1. https://hackertarget.com/recon-ng-tutorial/
1. https://www.geeksforgeeks.org/python-theharvester-how-to-use-it/

## Exercices : 

Please save your answers. Your coaches may ask you for a copy of all your answers at the end of the challenge. 


1. What is the ip address of adlp-corp.com ?
    > Your response 52.51.133.160
    > Your command `nslookup adlp-corp.com`
    or `dig adlp-corp.com +short`

2. What is the TXT record of adlp-corp.com? 
    > Your response  BC{DESCRIPTIVE-DOMAIN-TXT}
    > Your command ```dig adlp-corp.com TXT``
    or `dig -t txt adlp-corp.com +short`

3. What are the MX records of becode.org ?
    > Your response 1 aspmx.l.google.com.
                    10 alt3.aspmx.l.google.com.
                    5 alt1.aspmx.l.google.com.
                    10 alt4.aspmx.l.google.com.
                    5 alt2.aspmx.l.google.com.
    > Your command `dig becode.org MX`
    or `dig -t mx becode.org +short`

4. What are the MX records of adlp-corp.com ?
    > Your response 10 alt3.aspmx.l.google.com.
                	10 alt4.aspmx.l.google.com.
                    5 alt1.aspmx.l.google.com.
                	1 aspmx.l.google.com.
                    5 alt2.aspmx.l.google.com.
    > Your command `dig adlp-corp.com`
    or `dig -t mx adlp-corp.com +short`

5. What is the first NS name server of adlp-corp.com?
    > Your response ns-269.awsdns-33.com.
            2nd:    ns-1997.awsdns-57.co.uk.
            3rd:    ns-1185.awsdns-20.org.
            4th:    ns-588.awsdns-09.net.
    > Your command `dig adlp-corp.com NS`
    or `dig -t ns adlp-corp.com +short`

6. Uses a brute force tool to find subdomains of adlp-corp.com. How many did you find?
    > Your response 16 
    > Your command  ``python subnetter.py --address 52.51.133.160 --subnets 14 --range 4 ``
    tried a variety of tools but didn't work, ended up with a python script that did it for me. 

    -> use Burp


7. Use theHarvester tool at becode.org. How many Linkedin Users? 
    I used the Harvester but it doesn't provide this service anymore.
    -> doesn't work 

8. Use theHarvester tool at becode.org. How many ip addresses did you find? 
    > Your response 40
    > Your command theharvester -d becode.org -b all
9. Write a small script to attempt a zone transfer from adlp-corp.com using a higher-level
scripting language such as Python, Perl, or Ruby
    > Your Script 
you'll need dnspython for this-> install it 

```python
import dns.query
import dns.zone
import dns.resolver

def attempt_zone_transfer(domain):
    try:
        # Get the list of name servers for the domain
        ns_records = dns.resolver.resolve(domain, 'NS')
        for ns in ns_records:
            ns = str(ns)
            print(f'Trying zone transfer for {domain} from name server: {ns}')
            try:
                zone = dns.zone.from_xfr(dns.query.xfr(ns, domain))
                if zone:
                    print(f'Zone transfer successful from {ns}!\n')
                    for name, node in zone.nodes.items():
                        print(zone[name].to_text(name))
                    return
            except Exception as e:
                print(f'Zone transfer failed from {ns}: {e}')
    except Exception as e:
        print(f'Could not resolve NS records for {domain}: {e}')

if __name__ == '__main__':
    domain = 'adlp-corp.com'  # Replace with your target domain
    attempt_zone_transfer(domain)
```
10.  Write a small script to attempt a brute force search for subdomains using a higher level scripting language such as Python, Perl or Ruby.
    > Your Script 
    you'll need dnspython for this -> install it 
```python 
    import dns.resolver

def brute_force_subdomains(domain, wordlist):
    subdomains = []
    resolver = dns.resolver.Resolver()
    resolver.timeout = 1
    resolver.lifetime = 1

    try:
        with open(wordlist, 'r') as file:
            for line in file:
                subdomain = line.strip() + '.' + domain
                try:
                    answers = resolver.resolve(subdomain, 'A')
                    for answer in answers:
                        subdomains.append(subdomain)
                        print(f'Found: {subdomain} -> {answer}')
                except (dns.resolver.NXDOMAIN, dns.resolver.Timeout, dns.resolver.NoNameservers):
                    pass
    except FileNotFoundError:
        print(f'Wordlist file not found: {wordlist}')

    return subdomains

if __name__ == '__main__':
    domain = 'adlp-corp.com'  # Replace with your target domain
    wordlist = 'subdomains.txt'  # Replace with the path to your wordlist

    found_subdomains = brute_force_subdomains(domain, wordlist)
    print(f'Total subdomains found: {len(found_subdomains)}')
```
## Ressources 
- https://en.wikipedia.org/wiki/List_of_DNS_record_types
- https://www.exploit-db.com/docs/12389.pdf
- https://pentestlab.blog/tag/dns-enumeration/
- http://tools.kali.org/information-gathering/dnsrecon
- https://github.com/nixawk/ig/