import os                                                                       
import argparse                                                                 
import sys 




if __name__ == '__main__':                                                      
                                                                               
                                                                               
   parser = argparse.ArgumentParser(description = 'Um programa de exemplo.')   
                                                                               
   parser.add_argument("-e", "--env", action="store", dest="pktio_env",        
                     default= '0', required = False,                           
                     help="Choose the pktio enviroment/s to compile with MACSAD core i.e 0=l2, 1=l3, 2=nat_ul, 3=nat_dl")
   arguments = parser.parse_args() 

   lst_psize= [128, 256, 512, 1024]
   #lst_psize= [256, 512]
   for i in range(1):                                                     
        print "round n: "+ str(i)
        for psize in lst_psize:
            cmd= "cat -n tcpdump_"+arguments.pktio_env+"_"+str(psize)+"_num_"+str(i)+" | grep -n ^ | grep ^302"
            print cmd
            os.system(cmd)
