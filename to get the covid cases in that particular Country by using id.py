from covid import Covid
cid=input("enter your countryId: ")
c=Covid()
cases=c.get_status_by_country_id(cid)
for x in cases:
    print(x,":",cases[x])
