from tkinter import *
from tkinter import messagebox



window = Tk()

window.configure(background = "#e9e2a1")

window.title("ToDo App")
window.resizable(0, 0) 
window.geometry("550x600")


# global list is declare for storing all the task
tasks_list = []

# global variable is declare for counting the task
counter = 1

def inputError() :
	
	# check for enter task field is empty or not
	if name_entry.get() == "" :
		
		# show the error message
		messagebox.showerror("Input Error")
		
		return 0
	
	return 1

def submit_add_Task():

    global counter

    value = name_entry.get() + '\n'
    TextArea.insert('end -1 chars', " " + str(counter) + " -- " + value)
    tasks_list.append(value)
    counter += 1

def update_button():
	global counter
	
	# handling the empty task error
	if len(tasks_list) == 0 :
		messagebox.showerror("No task")
		return

	number = update_task_no_entry.get(1.0, END)
	update_text = update_TextArea.get()

	if (number == "\n" or number == '') and ( update_text == '' or update_text == '\n' ) :
		messagebox.showerror("Input error")
		return
	else :
		task_no = int(number)

	#tasks_list.pop(task_no - 1)

	tasks_list[task_no-1] = str(update_text) + '\n'

	#counter -= 1

	TextArea.delete(1.0, END)

	for i in range(len(tasks_list)) :
		TextArea.insert('end -1 chars', " " + str(i + 1) + " -- " + tasks_list[i])#.........doubt



#Top header
label_heading = Label(window, text = "ToDo List App", font=("Helvetica", 20,'bold'))


label = Label(window, text = "Enter the task:", font=("Helvetica", 15),background='#e9e2a1')
name_entry = Entry(window, font=('Helvetica',10,'normal'), width=20,)
Submit_button = Button(window, text = "Submit", fg = "Black", bg = "light blue", command = submit_add_Task)


label_text_area = Label(window, text = "Task list:", font=("Helvetica", 15),background='#e9e2a1')
TextArea = Text(window, height = 5, width = 25, font = "lucida 13")



update_label = Label(window, text = "Update Task No.:", font=("Helvetica", 15),background='#e9e2a1')
update_task_no_entry = Text(window, font=('Helvetica',10,'bold'), width=5,height=2)



update_label_text_area = Label(window, text = "Update Task Text:", font=("Helvetica", 15),background='#e9e2a1')
update_TextArea = Entry(window, width = 20,  font=('Helvetica',10,'normal'))


update_btn = Button(window, text = "Update", fg = "white", bg = "blue", command = update_button)


label_heading.grid(row = 1, column = 3,pady=20)
label.grid(row = 2, column = 2)
name_entry.grid(row = 2, column = 3,  ipadx = 30, ipady=5, pady=20)
Submit_button.grid(row = 2, column = 4,  ipadx = 20, ipady=5, pady=0, padx=10)
label_text_area.grid(row = 3, column = 2)
TextArea.grid(row = 3, column = 3,  sticky = W)



# update row
update_label.grid(row = 5, column = 2)
update_task_no_entry.grid(row = 5, column = 3,  ipadx = 1, ipady=1, pady=20)

update_label_text_area.grid(row = 6, column = 2,pady=10)
update_TextArea.grid(row = 6, column = 3)

update_btn.grid(row = 8, column = 3,  ipady=5, ipadx=8)

window.mainloop()
