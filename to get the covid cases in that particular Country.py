from covid import Covid
cname=input("enter your country name: ")
c=Covid()
cases=c.get_status_by_country_name(cname)
for x in cases:
    print(x,":",cases[x])
