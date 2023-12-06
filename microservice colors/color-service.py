import time
Color_dict = {0:"#600080",1:"#8600b3",2:"#ac00e6",3:"#c61aff",4:"#d24dff",5:"#d966ff",6:"#df80ff",7:"#e699ff",8:"#ecb3ff"}
output_string=""
print("starting")
while(True):
    f=open("color-service-pipeline.txt","r")
    fcontents=f.read()
    if(fcontents.isdigit()):
        print("it's a digit")
        time.sleep(5)
        print("iterating")
        number_of_colors=int(fcontents)
        if(number_of_colors<10):
            for x in range(number_of_colors):
                print("adding color")
                output_string+= Color_dict[x]+" "
        f.close()
        f=open("color-service-pipeline.txt","w")
        f.write(output_string)
    f.close()

