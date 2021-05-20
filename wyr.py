# Name:  
# Student Number:  

# This file is provided to you as a starting point for the "wyr.py" program of Assignment 2
# of Programming Principles in Semester 1, 2021.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.

# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter file runs smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the required modules.
import tkinter
import tkinter.messagebox
import json


class ProgramGUI:

    def __init__(self):
        parent = tkinter.Tk()
        parent.geometry("500x500")
        try:
            parent.title("Would You Rather")
            file = open('data.txt','r')
            self.data = json.load(file)
            file.close()  
        except:
            tkinter.messagebox.showinfo("Missing/Invalid file","Missing/Invalid file")  
            parent.destroy
        self.question_num = 0
        self.show_mature = tkinter.messagebox.askyesno("want to see questions intended for a mature audience")
        button_1 = tkinter.Button(parent, command=lambda: self.record_vote('votes_1'))
        button_2 = tkinter.Button(parent, command=lambda: self.record_vote('votes_2'))
        button_1.pack(pady = 40)
        button_2.pack(pady = 40) 
        data = self.show_question()
        button_1.config(text=data['option_1'] + '?' )
        button_2.config(text=data['option_2'] + '?' )
        parent.mainloop()

    def show_question(self):
            try:
                if self.show_mature == self.data[self.question_num]['mature'] :
                    option_1 = self.data[self.question_num]['option_1']
                    option_2 = self.data[self.question_num]['option_2']
                    data = {
                        'option_1':option_1,
                        'option_2':option_2

                    }
                    return data
                else:
                    self.question_num = self.question_num + 1
                    self.show_question()
            except:
                tkinter.messagebox.showinfo("End OF File","End OF File")  
        
    def record_vote(self, vote):
        Votes_1 = self.data[self.question_num]['votes_1']
        Votes_2 = self.data[self.question_num]['votes_2'] 
        if vote == 'votes_1':
            Votes_1 = Votes_1 + 1
            print(Votes_1)
        else:
            Votes_2 = Votes_2 + 1
            print(Votes_2)
        self.question_num = self.question_num + 1
        self.show_question()
        with open('data.txt', 'w') as outfile:
            json.dump(self.data,outfile)
        outfile.close()            
        


# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()


# If you have been paid to write this program, please delete this comment.
