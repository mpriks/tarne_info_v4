from tkinter import *

root = Tk()
root.title("Tarne info v4.0")
root.geometry("600x400+750+150")
root.configure(highlightbackground="wheat")



# Päise pealkiri
tiitel_label = Label(root, text="TARNEINFO", fg="red")
tiitel_label.config(font=("Helvetica", 82))
tiitel_label.grid(row=50, column=100, columnspan=300)






# veergude pealkirjad
col_versioon = Label(root, text="VERSIOON")
col_versioon.grid(row=100, column=100)
col_olek = Label(root, text="OLEK")
col_olek.grid(row=100, column=200)
col_algus_kp = Label(root, text="ALGUS KP")
col_algus_kp.grid(row=100, column=300)
col_valjalaske_kp = Label(root, text="VÄLJALASKE KP")
col_valjalaske_kp.grid(row=100, column=400)
# padding kasutamine nt. col_olek.grid(padx=5, pady=2, row=3, column=3)







# sprindi info rida
sprint_label = Label(root, text="Käesolev sprint: ")
sprint_label.grid(row=200, column=100)

sprindi_spinbox = Spinbox(root, width=3, from_=0, to=9999)
sprindi_spinbox.grid(row=200, column=200)

# TODO: kp dünaamiline leidmine
algus_kp_label = Label(root, text="01.03.17")
algus_kp_label.grid(row=200, column=300)

# TODO: kp dünaamiline leidmine
lopp_kp_label = Label(root, text="15.03.17")
lopp_kp_label.grid(row=200, column=400)








root.mainloop()