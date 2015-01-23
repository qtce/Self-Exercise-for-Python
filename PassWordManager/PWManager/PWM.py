from Tkinter import *
import tkMessageBox

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.grid()
		self.createWidgets()

	def createWidgets(self):
		"define the storage module"
		self.StorageLabel = Label(self, text = "Store PassWord")
		self.StorageLabel.grid(column = 0, row = 0, sticky = W)
		
		self.nameInputLabel = Label(self, text = "Web Address:")
		self.nameInputLabel.grid(column = 0, row = 1, sticky = W)
		self.nameInput = Entry(self)
		self.nameInput.grid(column = 1, row = 1, sticky = W)
		
		self.accountInputLabel = Label(self, text = "Account Name:")
		self.accountInputLabel.grid(column = 0, row = 2, sticky = W)
		self.accountInput = Entry(self)
		self.accountInput.grid(column = 1, row = 2, sticky = W)
		
		self.passwordInputLabel = Label(self, text = "PassWord:")
		self.passwordInputLabel.grid(column = 0, row = 3, sticky = W)
		self.passwordInput = Entry(self)
		self.passwordInput.grid(column = 1, row = 3, sticky = W)
		
		self.saveButton = Button(self, text = ' Save ', command = self.saveInformation)
		self.saveButton.grid(column = 2, row = 3, padx =5)
		
		"define the search module"
		self.SearchLabel = Label(self, text = "Search PassWord")
		self.SearchLabel.grid(column = 0, row = 4, sticky = W)
		
		self.WebnameLabel = Label(self, text = "Web Address:")
		self.WebnameLabel.grid(column = 0, row = 5, sticky = W)
		self.senameInput = Entry(self)
		self.senameInput.grid(column = 1, row = 5, sticky = W)
		self.seButton = Button(self, text = 'Search', command = self.saveInformation)
		self.seButton.grid(column = 2, row = 5, padx =5)


	def saveInformation(self):
	"define the save function"
		Webname = self.nameInput.get()
		Aconame = self.accountInput.get()
		PassWord = self.passwordInput.get()
		
		tkMessageBox.showinfo("Message", "Information Saved:\n Website: %s\n Account: %s\n PassWord: %s"
							% (Webname, Aconame, PassWord))


	def saveInformation(self):
	"define the search function"
		

app = Application()
# Set the title of the GUI
app.master.title('PassWordManager')
# Main information Loop
app.mainloop()