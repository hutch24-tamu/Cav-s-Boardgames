from getXMLs import getXMLRequests
N = 10

for i in range(N):
    try:
        getXMLRequests()
    except:
        print("Try",i+1,"is finished")
print("Program end")
exit(0)