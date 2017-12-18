from Tkinter import *
import os
import time
import threading
from PIL import Image , ImageTk , ImageFilter
#Function For Code Implementation
def validate(cha_txt,path):
    global  root
    if(not os.path.exists(path)):
        t1=threading.Thread(target=change_text,args=(root,cha_txt,"Wrong path","Please Select Valid Image And Path","red","white",1))
        t1.start()
    else:
        img_pro(path)
#/home/zephyr/Downloads/dishonored-2.jpg
def func_undo():
    global image , imz
    if(len(imz)==1):
        pass
    else:
        image = imz[len(imz)-2]
        imz.pop()
        show_img()

def func_rotate(val,rt):
    global image , imz
    try:
        image = image.rotate(int(val.get()))
        rt.destroy()
        imz.append(image)
        show_img()
    except:
        pass

def func_save(sv,loc):
    global image
    try:
        image.save(loc.get())
        sv.destroy()
    except:
        pass
def func_merge(val):
    try:
        global  image,r,b,g, imz
        if(r==-1):
            r,g,b=image.split()
        if(val ==  "R G B"):
            image=Image.merge("RGB",(r,g,b))
        elif(val ==  "R B G"):
            #'yes'
            image = Image.merge("RGB",(r,b,g))
        elif(val ==  "B R G"):
            image=Image.merge("RGB",(b,r,g))
        elif(val ==  "B G R"):
            image=Image.merge("RGB",(b,g,r))
        elif(val ==  "G R B"):
            image=Image.merge("RGB",(g,r,b))
        elif(val ==  "G B R"):
            image=Image.merge("RGB",(g,b,r))
        flag=1
        imz.append(image)
        show_img()
    except:
        err=Tk()
        err.wm_title("Error Occured")
        err.geometry('%dx%d+%d+%d' % (530, 50, 600, 400))
        err.config(bg="#2b2b2b")
        err_la = Label(err,text="Image Is Not RGB, Can't Apply RGB Changes", font="Tahoma 15 bold",fg='Red',bg="#2b2b2b")
        err_la.grid(row=0,pady="10px",padx="10px")

def resiz(en_wid,en_hei,en_re):
    global image,imz,count
    try:
        image=image.resize((int(en_wid.get()),int(en_hei.get())))
        en_re.destroy()
        imz.append(image)
        show_img()
    except:
       pass

def func_conv(val):
    global image,r
    r=-1
    if(val=="RGB"):
        image=image.convert("RGB")
    elif(val=="1"):
        image=image.convert('1')
    elif(val=='L'):
        image=image.convert("L")
    imz.append(image)
    show_img()

def func_filter(val):
    global image
    if(val=='Blur'):
        image= image.filter(ImageFilter.BLUR)
    elif(val=='Contour'):
        image=image.filter(ImageFilter.CONTOUR)
    elif(val=='Detail'):
        image=image.filter(ImageFilter.DETAIL)
    elif(val=='Edge Enhance'):
        image=image.filter(ImageFilter.EDGE_ENHANCE)
    elif(val=='Edge Enhance More'):
        image=image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    elif(val=='Emboss'):
        image=image.filter(ImageFilter.EMBOSS)
    elif(val=='Find Edges'):
        image=image.filter(ImageFilter.FIND_EDGES)
    elif(val=='Smooth'):
        image=image.filter(ImageFilter.SMOOTH)
    elif(val=='Smooth More'):
        image=image.filter(ImageFilter.SMOOTH_MORE)
    elif(val=='Sharpen'):
        image=image.filter(ImageFilter.SHARPEN)
    global imz
    imz.append(image)
    show_img()

def blend(val,path):
    global image , imz, alpha,ima_c
    if(val=='+'):
        if(alpha<.9):
            alpha +=.1
    if(val=='-'):
        if(alpha>.1):
            alpha -=.1
    #alpha
    imagb = Image.open(path)

    image = Image.blend(ima_c,imagb,alpha)
    imz.append(image)
    show_img()

def func_flip(val):
    global image,imz
    if(val=='Left-Right'):
        image = image.transpose(Image.FLIP_LEFT_RIGHT)
    elif(val=='Top-Bottom'):
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
    imz.append(image)
    show_img()
#/home/zephyr/Pictures/boku_dake.jpg
x1=x2=y1=y2=0
def ini_crop(event):
    global x1,y1
    x1=event.x
    y1= event.y
    #x1,y1

def en_crop(event):
    global x2,y2
    x2=event.x
    y2= event.y
    #x2,y2

def crop_bind():
    global img
    img.bind('<Button-1>',ini_crop)
    img.bind('<Button-3>',en_crop)
hel=1
def func_crop():
    global image,imz,x1,x2,y1,y2,img,hel
    crop_bind()
    if(hel):
        err=Tk()
        err.wm_title("How To Use Crop")
        err.config(bg="#2b2b2b")
        err_la = Label(err,text="Left On the image to select starting point and right click for selecting end point then click in crop to crop image", wraplength=600,font="Tahoma 15 bold",fg='Red',bg="#2b2b2b")
        err_la.grid(row=0,pady="10px",padx="10px")
        hel=0
    if(x1 == x2 == y1 == y2 == 0):
        pass
    else:
        if(x1<x2):
            if(y1<y2):
                image=image.crop((x1,y1,x2,y2))
            else:
                image=image.crop((x1,y2,x2,y1))
        else:
            if(y1<y2):
                image=image.crop((x2,y1,x1,y2))
            else:
                image=image.crop((x2,y2,x1,y1))
        imz.append(image)
        show_img()
        img.unbind('<Button-1>')
        img.unbind('<Button-3>')
        x1=x2=y1=y2=0
    #"yes"

def blend_func(bl,bl_txt,path):
    global image , ima_c,alpha,t1
    alpha = .5
    if(not os.path.exists(path)):
        change_text(bl,bl_txt,"Wrong path","Please Select Valid Imge And Path","red","white",1)
    else:
        try:
            bl.destroy()
            ima_c = image
        except:
            pass
        blend(' ',path)
        bv = Tk()
        bv.wm_title("(-_-)")
        bv.config(bg="#2b2b2b")
        bv_add=Button(bv,text="+",relief=GROOVE,font="Tahoma 17 bold",width=2 ,fg="white",bg="#2b2b2b",command=lambda: blend('+',path)) #entry_img.get()
        bv_add.grid(row=0,column=0,padx=(20,10),pady=(5,20))
        bv_sub=Button(bv,text="-",relief=GROOVE,font="Tahoma 17 bold",fg="white",width=2,bg="#2b2b2b",command=lambda: blend('-',path)) #entry_img.get()
        bv_sub.grid(row=0,column=1,padx=(20,10),pady=(5,20))

def change_text(back,ch_txt,text,ftext,iclr,fclr,spd):
    ch_txt.config(text=text,fg=iclr);
    back.update()
    time.sleep(spd)
    ch_txt.config(text=ftext,fg=fclr);
    back.update()

                #GUI IMPLEMENTATION

def img_pro(path):
    root.destroy()
    edit = Tk()
    edit.wm_title("ED-IT")

    '''LEFT FRAME FOR DISPLAYING IMAGE '''
    global leftframe , image
    leftframe=Frame(edit,width=1600,height=900)
    edit.configure(background="#2b2b2b")
    leftframe.pack(side="left",expand=True,fill='both')

    #LOADING AND CREATING IMAGE
    image = Image.open(path)
    imz.append(image)
    show_img()

    ''' RIGHT FRAME FOR BUTTONS AND COMMANDS '''
    rightframe=Frame(edit)
    rightframe.pack(side="right")
    rightframe.configure(background="#2b2b2b")

    save_btn=Button(rightframe,text="Save",relief='ridge',width=5,font="Tahoma 12 bold",fg="white",bg="#2b2b2b",command=lambda:save_box(path))
    save_btn.grid(row=1,column=0,padx="5px",pady="3px")

    open_btn=Button(rightframe,text="Open",relief='ridge',width=5,font="Tahoma 12 bold",fg="white",bg="#2b2b2b",command=lambda:imgsel(edit))
    open_btn.grid(row=1,column=1,padx="5px",pady="3px")

    undo_btn=Button(rightframe,text="Undo",relief='ridge',width=5,font="Tahoma 12 bold",fg="white",bg="#2b2b2b",command=func_undo)
    undo_btn.grid(row=2,column=1,padx="5px",pady="3px")



    crp_btn=Button(rightframe,text="Crop",relief='ridge',width=5,font="Tahoma 12 bold",fg="white",bg="#2b2b2b",command=func_crop)
    crp_btn.grid(row=3,column=0,padx="5px",pady="3px")

    res_btn=Button(rightframe,text="Resize",relief='ridge',width=5,font="Tahoma 12 bold",fg="white",bg="#2b2b2b",command=resize_box)
    res_btn.grid(row=3,column=1,padx="5px",pady="3px")

    ro_btn=Button(rightframe,text="Rotate",relief='ridge',width=5,font="Tahoma 12 bold",fg="white",bg="#2b2b2b",command=rotate_box)
    ro_btn.grid(row=4,column=0,padx="5px",pady="3px")

    blend_btn=Button(rightframe,text="Blend",relief='ridge',width=5,font="Tahoma 12 bold",fg="white",bg="#2b2b2b",command=blend_box)
    blend_btn.grid(row=2,padx="5px",pady="3px")

    #DETAILS MENU
    detv = StringVar(edit)
    detv.set("Image Details")
    details=OptionMenu(rightframe,detv,'Size: '+str(image.size),'Format: '+str(image.format),'Mode: '+str(image.mode))
    details.config(background="#2b2b2b",fg="white",font="Tahoma 12 bold")
    details['menu'].config(background="#2b2b2b",fg="white",font="Tahoma 12 bold")
    details['menu'].entryconfigure('Size: '+str(image.size),state="disabled")
    details['menu'].entryconfigure('Format: '+str(image.format),state="disabled")
    details['menu'].entryconfigure('Mode: '+str(image.mode),state="disabled")
    details.grid(row=0,column=0,columnspan=2,padx="5px",pady="3px")

    #FLIP MENU
    flv=StringVar(edit)
    flv.set("Flip")
    flips=['Left-Right','Top-Bottom']
    flip_list=OptionMenu(rightframe,flv,*flips,command=func_flip)
    flip_list.config(bg="#2b2b2b",fg='white',font="Tahoma 12 bold")
    flip_list['menu'].config(background="#2b2b2b",fg="white",font="Tahoma 12 bold")
    flip_list.grid(row=4,column=1,padx='5px',pady="3px")

    #MERGE MENU
    merv=StringVar(edit)
    merv.set("R G B")
    bands=['R G B','R B G','B R G','B G R','G R B','G B R']
    merge_band= OptionMenu(rightframe,merv,*bands,command=func_merge)
    merge_band.config(background="#2b2b2b",fg="white",font="Tahoma 12 bold")
    merge_band['menu'].config(background="#2b2b2b",fg="white",font="Tahoma 12 bold")
    merge_band.grid(row=5,column=1,padx="5px",pady="3px")

    #CONVERT MENU
    conv = StringVar(edit)
    conv.set("Convert")
    convr = ['RGB','1','L']
    con_list = OptionMenu(rightframe,conv,*convr,command=func_conv)
    con_list.config(background='#2b2b2b',fg='white',font='Tahoma 12 bold')
    con_list['menu'].config(background='#2b2b2b',fg='white',font='Tahoma 12 bold')
    con_list.grid(row=5,padx="5px",pady="3px")

    #FILTER MENU
    filv=StringVar(edit)
    filv.set('Image Filter')
    fil=['Blur','Contour','Detail','Edge Enhance','Edge Enhance More','Emboss','Find Edges','Smooth','Smooth More','Sharpen']
    img_fil=OptionMenu(rightframe,filv,*fil,command=func_filter)
    img_fil.config(background="#2b2b2b",fg="white",font="Tahoma 12 bold")
    img_fil['menu'].config(background="#2b2b2b",fg="white",font="Tahoma 12 bold")
    img_fil.grid(row=6,column=0,columnspan=2,padx="5px",pady="3px")

def show_img():
    global img
    photo=ImageTk.PhotoImage(image)
    try :
        for widget in leftframe.winfo_children():
            widget.destroy()
    except:
        pass
    leftframe.update_idletasks()
    #CREATING CANVAS FOR DISPLAYING IMAGE

    leftframe.config(background='#2b2b2b',width=1600 if image.width >1600 else image.width,height=900 if image.height>900 else image.height)
    leftframe.pack(side="left",expand=True,fill='both')
    img = Canvas(leftframe,width=1600 if image.width >1600 else image.width,height=900 if image.height>900 else image.height,scrollregion=(0,0,image.width,image.height))

    img.create_image(0,0,image=photo,anchor=NW)
    img.image=photo
    #HORIZONTAL BAR
    hbar = Scrollbar(leftframe,orient=HORIZONTAL)
    hbar.pack(side="bottom", fill=X)
    hbar.config(command=img.xview)
    #VERTICAL BAR
    vbar = Scrollbar(leftframe,orient=VERTICAL)
    vbar.pack(side="right",fill=Y)
    vbar.config(command=img.yview)
    # PACKING IMAGE TO LEFTFRAME
    img.config(xscrollcommand=hbar.set,yscrollcommand=vbar.set)
    img.pack(fill='both',expand=True)

def rotate_box():
    rt = Tk()
    rt.wm_title("Rotate")
    rt.config(bg="#2b2b2b")
    rt_la =Label(rt,text="Degree",fg="white",bg="#2b2b2b",font="Tahoma 12 bold")
    rt_la.grid(row=0,padx=(20,5),pady="20px")
    rt_vl = Entry(rt,width=7,fg="white",bg="#2b2b2b",borderwidth=3,font="Tahoma 12",insertbackground="white")
    rt_vl.grid(row=0,column=1,padx=(5,5),pady="20px")
    rt_bt=Button(rt,text='Rotate',bg="#2b2b2b",fg='white',relief="ridge",font="Tahoma 12 bold",width=4,command=lambda: func_rotate(rt_vl,rt))
    rt_bt.grid(row=0,column=2,padx=(5,20),pady="20px")


def save_box(path):
    sv = Tk()
    sv.wm_title("Save")
    sv.config(bg="#2b2b2b")
    sv_loc = StringVar(sv)
    sv_loc.set(path)
    sv_pt = Entry(sv,textvariable=sv_loc,width=50,fg="white",bg="#2b2b2b",borderwidth=3,font="Tahoma 12",insertbackground="white")
    sv_pt.grid(row=0,padx=(20,5),pady="20px")
    sv_bt=Button(sv,text='Save',bg="#2b2b2b",fg='white',relief="ridge",font="Tahoma 12 bold",width=8,command=lambda: func_save(sv,sv_loc))
    sv_bt.grid(row=0,column=1,padx=(5,20),pady="20px")


def resize_box():
    en_re = Tk()
    en_re.config(background="#2b2b2b")
    en_re.wm_title("Resize")
    tx_wid=Label(en_re,text="Width",font="Tahoma 12 bold",fg="white",bg='#2b2b2b')
    tx_wid.grid(row=0,pady=(10,4),padx=(20,4))
    en_wid=Entry(en_re,width=15,fg="white",bg="#2b2b2b",borderwidth=3,font="Tahoma 12",insertbackground="white")
    en_wid.grid(row=0,column=1,padx=(4,4),pady=(10,4))

    tx_hei=Label(en_re,text="Height",font="Tahoma 12 bold",fg="white",bg='#2b2b2b')
    tx_hei.grid(row=0,column=2,pady=(10,4),padx=(20,4))
    en_hei=Entry(en_re,width=15,fg="white",bg="#2b2b2b",borderwidth=3,font="Tahoma 12",insertbackground="white")
    en_hei.grid(row=0,column=3,padx=(4,20),pady=(10,4))

    en_btn=Button(en_re,text="Resize",relief='ridge',width=10,font="Tahoma 12 bold",fg="white",bg="#2b2b2b",command=lambda: resiz(en_wid,en_hei,en_re))
    en_btn.grid(row=1,columnspan=4,padx="5px",pady=(10,10))

def blend_box():
    bl = Tk()
    bl.wm_title("Select Image ")
    bl.config(bg="#2b2b2b")
    bl_txt=Label(bl,text='Select Image To Be Blended',fg="#ffffff",font="Tahoma 12 bold",bg="#2b2b2b")
    bl_txt.grid(row=0,columnspan=2,padx=(10,5),pady=5)
    bl_img=Entry(bl,width=60,fg="white",bg="#2b2b2b",borderwidth=3,font="Tahoma 12",insertbackground="white")
    bl_img.grid(row=1,padx=(10,10),pady=(5,20))
    bl_bt=Button(bl,text="Blend Image",relief=GROOVE,width=10,font="Tahoma 12 bold",fg="white",bg="#2b2b2b",command=lambda: blend_func(bl,bl_txt,bl_img.get())) #entry_img.get()
    bl_bt.grid(row=1,column=1,padx=(10,10),pady=(5,20))

def imgsel(*arg):
    global leftframe,img,flag,image,r,b,g,imz
    leftframe=img=flag=image=r=b=g=-1
    imz=[]
    try:
        arg[0].destroy()
    except:
        pass
    global root
    root=Tk()
    root.wm_title("Select Image")
    root.configure(background="#2b2b2b")
    cha_txt=Label(root,text='Please Select Valid Image And Path',fg="#ffffff",font="Tahoma 12 bold",bg="#2b2b2b")
    cha_txt.grid(row=0,columnspan=2,padx=(10,5),pady=5)
    entry_img=Entry(root,width=60,fg="white",bg="#2b2b2b",borderwidth=3,font="Tahoma 12",insertbackground="white")
    entry_img.grid(row=1,padx=(10,10),pady=(5,20))
    open_img=Button(root,text="Open Image",relief=GROOVE,width=10,font="Tahoma 12 bold",fg="white",bg="#2b2b2b",command=lambda: validate(cha_txt,entry_img.get())) #
    open_img.grid(row=1,column=1,padx=(10,10),pady=(5,20))
    root.mainloop()
