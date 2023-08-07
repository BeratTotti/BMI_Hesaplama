
from tkinter import *
import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(400,400)
window.config(bg="white", padx=50,pady=50)



def curculate_BMI():
    height = height_entry.get()
    weight = weight_entry.get()


    if height == "" or weight == "" :
        result_label.config(text="Lütfen Kilonuzu ve Boyunuzu Giriniz ")
    else:
        try:
            bmi = float(weight) / (float(height) / 100) ** 2
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Lütfen Geçerli rakam Giriniz")


def write_result(bmi):
    result_string  = f"BMI DEĞERİNİZ :  {bmi}. Siz "
    if 10<=bmi<18.5:
        result_string += "Zayıfsınız"
    elif 18.5<=bmi<25:
        result_string += "Sağlıklısınız"
    elif 25<=bmi<30:
        result_string += "Kilolusunuz"
    elif 30<=bmi<40:
        result_string += "Şişmansınız"
    elif 40<=bmi<=50:
        result_string += "Aşırı Şişmansınız"
    return  result_string








font = ("Arial",15,"bold")
# label
my_label = Label(text="Enter Your Weight (kg)",bg="white",fg="black",font=font)
my_label.config(padx=15,pady=15)
my_label.pack()



# Entry

weight_entry  = Entry(fg="black",bg="grey")
weight_entry.focus()
weight_entry.pack()

# label 2
my_label2 = Label(text="Enter Your Height (cm)",bg="white",fg="black",font=font)
my_label2.config(padx=15,pady=15)
my_label2.pack()

# entry 2




height_entry = Entry(bg="grey" )
height_entry.pack()

font2 = ("Arial",10,"bold")
#result label
result_label = Label(font=font,bg="white",fg="black",)
result_label.config(font=font2)
result_label.place(x=-15 , y = 210)









# button
my_button = Button(text="Curculate", bg="grey",fg="black",command=curculate_BMI)
my_button.config(width=10)
my_button.place(x =105 , y = 167)


window.mainloop()