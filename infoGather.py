def informationGathering():
    print("Getting Started On Website Penetration")
    answer = input("Do you want to know about information gathering websites?")
    if answer == "yes":
        websites = ["whois.domaintools.com","robtex.com"]
        print(websites)
    else:
         answer = input("Are You interested in Tools?")
         if answer == "yes":
             message = "Here are some tools"
             tools = ["Nmap","Maltego"]
             for tools in tools:
                 print(message + tools)
    
informationGathering()
