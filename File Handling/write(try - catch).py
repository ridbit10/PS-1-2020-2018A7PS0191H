try:
    f=open("text.txt",'w',encoding='utf-8')
    f.write("Messi is the best player\n")
    f.write("Messi plays for barca\n")
    f.write("Messi wears jersey no.10")
except:
    print ((sys.exc_info()[0]),"occured")
finally:
    f.close()
