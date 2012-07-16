class book:

    def SetInfo(self,title,author,contents):
        self.Title=title
        self.Author=author
        self.Contents=contents
    def show(self):
        print("Title: %s"%(self.Title))
        print("Author: %s"%(self.Author))
        print("Contents: %s"%(self.Contents))

      
ListOfBooks=[]
BookInfo=book()
BookInfo.SetInfo("Red Phalt","Albert Watson","Road Runner")
ListOfBooks.append(BookInfo)

class Pamphet(book):
    pass

class Contents(book):
    pass

for book in ListOfBooks:
    BookInfo.show()
   
       
        
    
