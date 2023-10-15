from app.services.names import equipment as dic2
from app.services import get_all_names
names=get_all_names()
keys3=[]
for key in names:
    if len(key.split(" "))==2:
        keys3.append(key.split(" ")[0]+"-"+key.split(" ")[1]+" "+key.split(" ")[0]+key.split(" ")[1]+key)
    elif len(key.split(" "))==3:
        keys3.append((key.split(" ")[0]+"-"+key.split(" ")[1]+" "+key.split(" ")[0]+key.split(" ")[1]+" "+
                      key.split(" ")[1]+"-"+key.split(" ")[2]+" "+key.split(" ")[1]+key.split(" ")[2]+" "+
                      key.split(" ")[0] + "-" + key.split(" ")[2] + " " + key.split(" ")[0] + key.split(" ")[2] +" "+
                      key.replace("-","")  +
                      key))
    elif len(key.split(" "))==4:
        keys3.append((key.split(" ")[0] + "-" + key.split(" ")[1] + " " + key.split(" ")[0] + key.split(" ")[1] + " "+
                      key.split(" ")[1] + "-" + key.split(" ")[2] + " " + key.split(" ")[1] + key.split(" ")[2] +" "+
                      key.split(" ")[2] + "-" + key.split(" ")[3] + " " + key.split(" ")[2] + key.split(" ")[3] +" "+
                      key.split(" ")[0] + "-" + key.split(" ")[2] + " " + key.split(" ")[0] + key.split(" ")[2] +" "+
                      key.split(" ")[0] + "-" + key.split(" ")[3] + " " + key.split(" ")[0] + key.split(" ")[3] + " " +
                      key.replace("-", "") +
                      key))
    elif len(key.split(" "))==5:
        keys3.append((key.split(" ")[0] + "-" + key.split(" ")[1] + " " + key.split(" ")[0] + key.split(" ")[1] +" "+
                      key.split(" ")[1] + "-" + key.split(" ")[2] + " " + key.split(" ")[1] + key.split(" ")[2] +" "+
                      key.split(" ")[2] + "-" + key.split(" ")[3] + " " + key.split(" ")[2] + key.split(" ")[3] +" "+
                      key.split(" ")[0] + "-" + key.split(" ")[2] + " " + key.split(" ")[0] + key.split(" ")[2] +" "+
                      key.split(" ")[0] + "-" + key.split(" ")[3] + " " + key.split(" ")[0] + key.split(" ")[3] + " " +
                      key.replace("-", "") +
                      key))
