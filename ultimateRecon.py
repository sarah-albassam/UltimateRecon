import argparse
import whoisL as wh
import web_crawler as w
import portScanner as p


def thank_you():
    print("""

 _____ _   _   ___   _   _  _   __ __   _______ _   _ _ 
|_   _| | | | / _ \ | \ | || | / / \ \ / /  _  | | | | |
  | | | |_| |/ /_\ \|  \| || |/ /   \ V /| | | | | | | |
  | | |  _  ||  _  || . ` ||    \    \ / | | | | | | | |
  | | | | | || | | || |\  || |\  \   | | \ \_/ / |_| |_|
  \_/ \_| |_/\_| |_/\_| \_/\_| \_/   \_/  \___/ \___/(_)



    """)


print('''
██╗   ██╗██╗  ████████╗██╗███╗   ███╗ █████╗ ████████╗███████╗    ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
██║   ██║██║  ╚══██╔══╝██║████╗ ████║██╔══██╗╚══██╔══╝██╔════╝    ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
██║   ██║██║     ██║   ██║██╔████╔██║███████║   ██║   █████╗      ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
██║   ██║██║     ██║   ██║██║╚██╔╝██║██╔══██║   ██║   ██╔══╝      ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
╚██████╔╝███████╗██║   ██║██║ ╚═╝ ██║██║  ██║   ██║   ███████╗    ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
 ╚═════╝ ╚══════╝╚═╝   ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝    ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝

''')

print("--Credits: ")
print("[<3] Sarah Albassam")
print("[<3] Shahad AlGhareeb")
print("[<3] Shaima AlBaker")
print("[<3] Lama Almesned")
print("[<3] Maram Alnaim")

print("\n--> Instructor: Mr. Hussain Alattas\n\n")



def get_args():
    parser = argparse.ArgumentParser(prog='Ultimate Recon',
                                     description=f' All your recon needs in one tool!  \n->port scaning\n->whois\n->web crawler\n->subdomain enumeration ')
    parser.add_argument('-url', help='Target URL', type=str)
    parser.add_argument('-d','--domainName', help='Target URL', type=str)
    parser.add_argument('-w', '--whois', help='Performs a whois lookup on target url',action='store_true')
    parser.add_argument('-wl', '--wordlist',type=str, help='Performs subdomain enumeration with custom wordlist on target url (provide your own wordlist)')
    parser.add_argument('-Sw', '--short_wordlist', help='Performs subdomain enumeration with most common subdomains wordlist for subdomain enumeration on target url', action='store_true')
    parser.add_argument('-Lw', '--long_wordlist', help='Performs subdomain enumeration with all possible subdomains wordlist enumeration on target url (might take 20 min or more)', action='store_true')
    parser.add_argument('-c', '--crawler', help='Performs website crawling on target url',action='store_true')
    parser.add_argument('-ip', '--TargetIP',type=str, help='Performs port scanning on target IP')
    parser.add_argument('-a', '--allPorts', help='Scans all ports (1 to 65535) on target IP ',action='store_true')
    parser.add_argument('-r', '--custPorts', help='Scans custom ports (specified range) on target IP',nargs=2)
    parser.add_argument('-wp', '--wellKnownPorts', help='Scans well-known ports (specified range) on target IP',action='store_true')


    return parser.parse_args()



args = get_args()
if args.whois:
    wh.whoisLookup(args.url)
if args.wordlist:
    w.subdomain_test(args.domainName,args.wordlist)
if args.short_wordlist:
    w.subdomain_test(args.domainName,short=args.short_wordlist)
if args.long_wordlist:
    w.subdomain_test(args.domainName, long=args.long_wordlist)
if args.crawler:
    w.crawl(args.url)
if args.allPorts:
    p.threadsFunction1(1021,args.TargetIP)
if args.wellKnownPorts:
    p.threadsFunction2(1021,args.TargetIP)
if args.custPorts:
    p.threadsFunction3(1021,args.TargetIP,int(args.custPorts[0]),int(args.custPorts[1]))

thank_you()


