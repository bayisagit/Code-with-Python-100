bids={}
istr=True
def fma(birrsfor):
    firs=0
    for k in birrsfor:
        amoun=birrsfor[k]
        if amoun>firs:
            firs=amoun
            winner=k
    print(f"the winner is {k} with a bids of ${firs}")

while istr:
    name=input("what is your name? ")
    price=int(input("what is your bid: $ "))
    bids[name]=price
    choi=input("are there other bidders? Type 'Yes' or 'No'. ").lower()
    if choi=="no":
        fma(bids)
        istr=False
