import os
import re
def safe_open(filename,mode='r',*rubbish_args,**rubbish_keywords):
	try:
		if mode == 'r':
			open(filename,mode,encoding='utf8').read()
		return open(filename,mode,encoding='utf8')
	except:
		return open(filename,mode,encoding='gbk')

# 遍历指定目录，显示目录下的所有文件名
def listFileName(filepath):
    pathDir =  os.listdir(filepath)
    with safe_open(imageNames,"w",encoding='utf8') as f:
	    for eachDir in pathDir:
	    	f.write("%s%s" % (eachDir,"\r\n"))
	    #    child = os.path.join(filepath, allDir)
	    #    print(eachDir) 
	    

def search(pattern,string):
	#return re.search(pattern,string,re.MULTILINE|re.DOTALL)
	res = string.find(pattern)
	if res <0:
		return None
	else:
		return 1     

filepath='E:\\defense\\image'
imageNames='C:\\Users\\dell\\Desktop\\imgnames.txt'
latexFilename='E:\\defense\\Danping_thesisDefenseslides.tex'


listFileName(filepath) # read all the filenames in the designate filepath and save them to a txt file


origin_text=safe_open(latexFilename).read() # read Latex file and find eps names
text = origin_text
current_start_pos = 0
pos=[]

filenames=safe_open(imageNames)
while 1:
	line=filenames.readline()
	if not line:
		break
	else:
		line=line[0:len(line)-1]
		search_pattern = line
	
		res=search(search_pattern,text)
		if res==None:
			imgfilename = os.path.join(filepath, line)
			os.remove(imgfilename)
		##delete the file 