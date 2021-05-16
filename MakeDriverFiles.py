import os
from datetime import date

def MakeDriverFiles():
  names =[ '_interface.h','_config.h','_private.h','_program.c']
  header=['_INTERFACE_H_','_CONFIH_H_','_PRIVATE_H_','_PROGRAM_C_']
  DriverName=input('What is your driver name : ')
  #Make dir
  os.mkdir(DriverName)
  #Enter dir 
  os.chdir(DriverName)
  
  #get date 
  today = date.today()
  d1 = today.strftime("%d/%m/%Y")
  
#Store the contents of the file that has your headers comments
  f0=open('../HeaderCommentsSourse.txt','r')
  contents=f0.readlines()
  contents[21] = '#include \"STD_TYPES.h\"\n'  
  contents[22] = '#include "BIT_MATH.h"\n' 
  for i in range (3):
      contents[25+i]='#include "'+DriverName+names[i]+"\"\n"
      
  #print(contents)
  f0.close()
  f1=open('../HeaderComments.txt','r')
  hcontents=f1.readlines()
  f1.close()
    #Start making .h files
  for i in range(4):
      f=open(DriverName+names[i],'w')
     	#insert header commentes
      hcontents[17]="#ifndef "+DriverName+header[i]+'\n'	#write header guards
      hcontents[18]='#define '+DriverName+header[i]+'\n'
      f.writelines(hcontents)
      f.close()
      f1=open(DriverName+names[i],'r')
      data =f1.read()
      f1.close()
      f1=open(DriverName+names[i],'w')
      data = data.replace('[File Name]' , DriverName+names[i])
      data = data.replace('[Date]' , d1)
      f1.write(data)
      #close file 
      f1.close()
  
  #Make .c file
  f=open(DriverName+names[3],'w')
  f.writelines(contents)	#insert header commentes
  #open xxxx_program.c to include librares and other files
  f=open(DriverName+'_program.c','r+')
  f.writelines(contents)	#insert header commentes
  f.close()
  f1=open(DriverName+names[3],'r')
  data =f1.read()
  f1.close()
  f1=open(DriverName+names[3],'w')
  data = data.replace('[File Name]' , DriverName+names[3])
  data = data.replace('[Date]' , d1)
  f1.write(data)
  #close file 
  f1.close()
  print('Done ... \n')


def main():
   MakeDriverFiles()

if __name__ == '__main__':
  main()
