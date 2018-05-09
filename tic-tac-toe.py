from tkinter import *
def win():
      #only one row
      if list[0]["text"]==list[1]["text"]==list[2]["text"]!="     ":
            return 1
      if list[3]["text"]==list[4]["text"]==list[5]["text"]!="     ":
            return 1
      if list[6]["text"]==list[7]["text"]==list[8]["text"]!="     ":
            return 1
      #only one column
      if list[0]["text"]==list[3]["text"]==list[6]["text"]!="     ":
            return 1
      if list[1]["text"]==list[4]["text"]==list[7]["text"]!="     ":
            return 1
      if list[2]["text"]==list[5]["text"]==list[8]["text"]!="     ":
            return 1
      #diagonal
      if list[0]["text"]==list[4]["text"]==list[8]["text"]!="     ":
            return 1
      if list[2]["text"]==list[4]["text"]==list[6]["text"]!="     ":
            return 1
      else:
            return 0

def checked(i) :
      global player
      button = list[i]

      if button["text"] != "     " :
            return
      button["text"] = player 
      button["bg"] = "yellow"

      if player == "X" :
            if win()==1:
                  print("The winner is X")
                  sys.exit(1)
            player = "O"
            button["bg"] = "yellow"
      else :
            if win()==1:
                  print("The winner is O")
                  sys.exit(1)
            player = "X"
            button["bg"] = "lightgreen"
      
      
window = Tk()
player = "X"
list= []

for i in range(9) :
      b = Button(window, text="     ", command=lambda k=i: checked(k))
      b.grid(row=i//3, column=i%3)
      list.append(b)

window.mainloop()


