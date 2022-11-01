def greeting():
    print("This interest calculator will ask you to select an interest rate,\nfollowed by a principal value.  It will then calculate and display\nthe principal, interest rate, and balance after one year.  You will\nthen be invited to execute the process again or terminate.")


def getRate(choices):
    alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
    while True:
        print("\nPlease select an interest rate:")
        for i in range(len(choices)):
            print(alphabet[i]+") "+str(choices[i])+"%")
        temp = input("Enter A-"+alphabet[len(choices)-1]+": ").strip().upper()
        try:
            return choices[alphabet.index(temp)]
        except (IndexError, ValueError):
            print("That is not a valid selection.")


def getPrincipal(limit):
    while True:
        temp = input("Enter the principal (limit "+str(limit)+"): ")
        if "$" in temp:
            temp = [char for char in temp]
            temp.remove("$")
            temp = "".join(temp)
        try:
            temp = float(temp)
            if temp > limit:
                print("The principal can be at most "+str(limit)+".")
            elif temp <= 0:
                print("You must enter a positive amount.")
            elif len(str(temp).split(".")[1]) > 2:
                print("The principal must be specified in dollars and cents.")
            else:
                return temp
        except ValueError:
            print("Please enter a number")


def computeBalance(principal, rate):
    balance = principal + (principal * rate)
    return balance


def displayTable(principal, rate, balance):
    print("\nInitial Principal   Interest Rate   End of Year Balance\n=======================================================")
    print("$" +
          "{:.2f}".format(principal) +
          # ^ Initial Principal
          (" "*(len("Initial Principal   ")-len("$"+"{:.2f}".format(principal)))) +
          # ^ Spacing
          "{:.2f}".format(rate) +
          # ^ Interest Rate
          (" "*(len("Interest Rate   ")-len("{:.2f}".format(rate))))+"$" +
          # ^ Spacing
          "{:.2f}".format(balance)
          # ^ End of Year Balance
          )

    print("\nMonth   Starting Balance    APR     Ending Balance\n==================================================")
    [print(
        ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"][i] +
        "     $" + " "*(len("{:.2f}".format(round(computeBalance(principal, pow(1+rate, 11/12.)-1), 2)))-len("{:.2f}".format(round(computeBalance(principal, pow(1+rate, i/12.)-1), 2)))) +
        # ^ Spacing
        "{:.2f}".format(round(computeBalance(principal, pow(1+rate, i/12.)-1), 2)) +
        # ^ Starting Balance
        " "*(19-len(" "*(len("{:.2f}".format(round(computeBalance(principal, pow(1+rate, 11/12.)-1), 2)))-len("{:.2f}".format(round(computeBalance(principal, pow(1+rate, i/12.)-1), 2))))+"{:.2f}".format(round(computeBalance(principal, pow(1+rate, i/12.)-1), 2)))) +
        # ^ Spacing
        "{:.2f}".format(rate)+" "*(8-len("{:.2f}".format(rate))) +
        # ^ APR
        "$" + " "*(len("{:.2f}".format(round(computeBalance(principal, pow(1+rate, 11/12.)-1), 2)))-len("{:.2f}".format(round(computeBalance(principal, pow(1+rate, (i+1)/12.)-1), 2)))) +
        # ^ Spacing
        "{:.2f}".format(round(computeBalance(principal, pow(1+rate, (i+1)/12.)-1), 2))
        # ^ Ending Balance
    ) for i in range(12)]


def askYesNo(prompt="Another Computation [y/n]?"):
    if prompt is None:
        while True:
            temp = input("\n"+prompt+" ").upper()[0]
            if temp == "Y":
                return True
            elif temp == "N":
                return False
