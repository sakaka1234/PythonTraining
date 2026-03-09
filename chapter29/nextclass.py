class NextClass:
    def printer(self,text):
        self.message = text
        print(self.message)

x = NextClass()
NextClass.printer(x,'class call')
