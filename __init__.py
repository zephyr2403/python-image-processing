import start
import threading
#GLOBAL VARIABLES
leftframe=img=flag=image=ima_c=r=b=g=t1=-1
imz=[]
alpha =.5
# EXECUTION STARTS FROM HERE
root=0
t2=threading.Thread(target=start.imgsel())
t2.start()
t2.join()
