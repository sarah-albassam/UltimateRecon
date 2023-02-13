import whois

def whoisLookup(url):
    try:

            print("****************************",url, "****************************")
            respone = whois.whois(url)

            experationDates = respone.expiration_date
            updatedDates = respone.updated_date
            creationDates = respone.creation_date

            print("[*] : Domain Name: ", respone.domain_name)
            print("[*] : registrar: ", respone.registrar)
            print("[*] : whois server: ", respone.whois_server)
            print("[*] : updated date: ")
            if (type(updatedDates) == list):
                print(updatedDates[0])
            else:
                print(updatedDates)
            print("[*] : creation date: ")
            if (type(creationDates) == list):
                print(creationDates[0])
            else:
                print(creationDates)
            print("[*] : experation date: ")
            if (type(experationDates) == list):
                print(experationDates[0])
            else:
                print(experationDates)
            print("[*] : name servers: ", respone.name_servers)
            print("[*] : status: ", respone.status)
            print("[*] : emails: ", respone.emails)
            print("[*] : dnssec: ", respone.dnssec)
            print("[*] : name: ", respone.name)
            print("[*] : Organization: ", respone.org)
            print("[*] : address: ", respone.address)
            print("[*] : city: ", respone.city)
            print("[*] : state: ", respone.state)
            print("[*] : registrant postal code: ", respone.registrant_postal_code)
            print("[*] : country: ", respone.country)

    except Exception as ex:
        print(ex)
