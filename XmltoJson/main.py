""" This is The Internship Program Developer Exam 2019 """
import xmltodict, json, os

def main():
    """ This is MAin Function """
    print("Please input name of file XML: ", end="")
    name = input()
    for filename in os.listdir(): #loop to find file.XML in path directoy
        if filename.endswith(name+".xml"):
            f = open(filename) #Open file
            XML_content = f.read() #read XML file
            filename = filename.replace('.xml', '') #Tranform file name
            output_file = open(filename + '.json', 'w')
            #parse the content of each file using xmltodict
            x = xmltodict.parse(XML_content, attr_prefix='')
            j = json.dumps(x,indent=4)
            output_file.write(j)
            print("-- Convert XML to JSON Finished --")
main()