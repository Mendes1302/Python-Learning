from tkinter.messagebox import askyesno
from tld import parse_tld
from tkinter import ttk
from tqdm import tqdm
import tkinter as tk
import pandas as pd

# Settings of interface
root=tk.Tk()
root.title('Clean of Data')
root.geometry("600x400")

# Variables of control
dt_origin_var=tk.StringVar()
type_of_delimiter=tk.StringVar()
dt_beta_var=tk.StringVar()


def clear_ns(col, dt_origin,  new_table):
    '''
        Validation if it's a domain na library tld pelo Site
        Choise by if Site or Email
        Args:
            col:              Name of columns
            dt_origin:        Data source for cleaning
            new_table:        Data source for duplicate cleaning

        Kwargs:null

        Returns:null
    '''


    clean = ['!', ',','http://', 'www.', 'https://', 
             'Www.', '@', 'WWW', 'WWW.', 'www', 
             'www,', 'Www.', 'http', 'https', 
             'http:', 'https:', 'http:/', 'https:/']

    for indx in tqdm(range(dt_origin[col].shape[0]), desc='Limpando site'):
        try:
            txt = str(new_table['Domain'][indx])

            for cl in clean:
                txt = txt.replace(cl, "")
            indx1 = txt.find('/')

            if indx1 != -1:
                txt = txt[:indx1]
            domain = parse_tld('https://'+txt)

            if domain[1] != None:
                if len(str(domain[2])) > 0:
                    new_table.at[indx, 'Domain'] = domain[2]
                    new_table.at[indx, 'Complement'] = domain[2]+'.'+domain[1]+'.'+domain[0]
                else:
                    if domain[1] == 'wordpress' or domain[1] == 'wix' or domain[1] == 'wixsite':
                        new_table.at[indx, 'Domain'] = domain[2]
                        new_table.at[indx, 'Complement'] = domain[2]+'.'+domain[0]
                    else:
                        new_table.at[indx, 'Domain'] = domain[1]
                        new_table.at[indx, 'Complement'] = domain[1]+'.'+domain[0]
            if domain[0] == None or domain[1] == None or domain[2] == None:
                new_table.at[indx, 'Domain'] = 'NULL'+'_'+txt
                new_table.at[indx, 'Complement'] = 'NULL'+'_'+txt

        except Exception as error:
            print(error, indx, type(indx))


def clear_email(col, dt_origin, new_table):
    '''
        Validation if it's a domain na library tld pelo Email
        Choise by if Site or Email
        Args:
            col:              Name of columns
            dt_origin:        Data source for cleaning
            new_table:        Data source for duplicate cleaning

        Kwargs:null

        Returns:null
            obs=Call another function
    '''


    for indx in tqdm(range(dt_origin[col].shape[0]), desc= 'Get domain email'):
        
        try:
            txt = str(new_table['Domain'][indx])
            indx1 = txt.find('@')

            if indx1 != -1:
                txt = 'https://'+str(new_table['Domain'][indx])[indx1+1:]
            domain = parse_tld(txt)

            if domain[1] != None:
                new_table.at[indx, 'Domain'] = domain[1]
                new_table.at[indx, 'Complement'] = domain[1]+'.'+domain[0]

        except Exception as error:
            print(error, indx, type(indx))


def clear_email_personal(col, dt_origin, new_table):
    '''
        If choice email ,clean where is have email personal
        Choise by if Site or Email
        Args:
            col:              Name of columns
            dt_origin:        Data source for cleaning
            new_table:        Data source for duplicate cleaning

        Kwargs:null

        Returns: Number of @
    '''


    email_personal = ['@yahoo.', '@gmail.', '@hotmail.',
                  '@outlook.', '@bol.',  '@mail.',
                  '@uol.', '@terra.',  '@ig.',
                  '@r7.', '@zipmail.',  '@globo.',
                  '@globomail.', '@oi.']

    _is_email = _isnot_email = 0

    for value in email_personal:

        desc = 'Procurando por: '+value
        for indx in tqdm(range(dt_origin[col].shape[0]), desc= desc):

            try:

                if (str(new_table[col][indx]) != 'nan' and value in new_table[col][indx]) or str(new_table[col][indx]) == 'nan':
                    new_table.at[indx, 'Domain'] = 'NULL'+'_'+str(new_table[col][indx])
                    new_table.at[indx, 'Complement'] = 'NULL'+'_'+str(new_table[col][indx])

                if str(new_table[col][indx]) != 'nan' and '@' in new_table[col][indx]:
                    _is_email += 1

                if str(new_table[col][indx]) != 'nan' and '@' not in new_table[col][indx]:
                    _isnot_email += 1
                    
                if new_table['Domain'][indx] != 'NULL'+'_'+str(new_table[col][indx]):
                    new_table.at[indx, 'Domain'] = str(new_table[col][indx])
                    new_table.at[indx, 'Complement'] = str(new_table[col][indx])

            except Exception as error:
                print(error, indx, type(indx))

    return _is_email, _isnot_email


def clear_network_social(col, dt_origin, new_table):
    '''
        If choice site clean where is have nerwork social
        Choise by if Site or Email
        Args:
            col:              Name of columns
            dt_origin:        Data source for cleaning
            new_table:        Data source for duplicate cleaning

        Kwargs:null

        Returns: Number of @
    '''


    network_social = ['facebook', 'instagram', 'linkedin']
    _is_email = _isnot_email = 0

    for value in network_social:

        desc = 'Procurando por: '+value
        for indx in tqdm(range(dt_origin[col].shape[0]), desc=desc):

            if str(new_table[col][indx]) != 'nan' and '@' in new_table[col][indx]:
                _is_email += 1

            if str(new_table[col][indx]) != 'nan' and '@' not in new_table[col][indx]:
                _isnot_email += 1

            if value == 'facebook':
                new_table.at[indx, 'Domain'] = str(new_table[col][indx])
                new_table.at[indx, 'Complement'] = str(new_table[col][indx])

            if value in str(new_table['Domain'][indx]):
                txt = str(new_table[col][indx])
                
                if value == 'linkedin':
                    txt = txt.replace('/in', '')

                txt = txt[txt.find('.com/')+5:]
                new_table.at[indx, 'Domain'] = str(txt[:txt.find('/')]+'.com.br')
                new_table.at[indx, 'Complement'] = str(txt[:txt.find('/')]+'.com.br')
               
    return _is_email, _isnot_email


def schodeler(column, col, dt_origin, dt_beta, new_table):
    '''
        Choise by if Site or Email
        Args:
            col:              Name of columns
            column:           Column choice for clean
            dt_beta:          Name of new file
            dt_origin:        Data source for cleaning
            new_table:        Data source for duplicate cleaning

        Kwargs:null

        Returns:null
            obs=Call another function
    '''

    
    col = str(col[0])
    _is_email = []

    def ctrl(is_mail):

        if is_mail[0] > is_mail[1]:
            return 1
        return 0

    if column[0] == '1 - Obter domain por Email':
        _is_email = clear_email_personal(col, dt_origin, new_table)

    if column[0] == '2 - Obter domain por Site':
        _is_email= clear_network_social(col, dt_origin, new_table)

    _is_email = ctrl(_is_email)
    if _is_email:
        clear_email(col, dt_origin, new_table)

    else:
        clear_ns(col, dt_origin, new_table)

    new_table.to_csv(dt_beta+'.csv')

 
def choice_clean(col, dt_origin, dt_beta, new_table):
    '''
        Second interface of user. 
        Args:
            col:              Name of columns
            dt_beta:          Name of new file
            dt_origin:        Data source for cleaning
            new_table:        Data source for duplicate cleaning

        Kwargs:null

        Returns:null
            obs=Call another function
    '''


    data = ['1 - Obter domain por Email',
            '2 - Obter domain por Site']

    rt=tk.Tk()
    rt.title('Clean of Data')
    rt.geometry("600x400")

    def showSelected():
        column = []
        cname = lb.curselection()

        for i in cname:
            op = lb.get(i)
            column.append(op)

        rt.destroy()
        schodeler(column, col, dt_origin, dt_beta, new_table)
    

    show = tk.Label(rt, text = "Seleciona como vai obter o dominio:", font = ("Times", 14), padx = 10, pady = 10)
    show.pack() 
    lb = tk.Listbox(rt, selectmode = "multiple", height=15)
    lb.pack(padx = 10, pady = 10, fill = "both") 

    for item in range(len(data)): 
        lb.insert(item, data[item]) 
        lb.itemconfig(item, bg="#ffaa00") 

    tk.Button(rt, text="Continuar", command=showSelected).pack()
    rt.mainloop()


def checkbox(data, dt_origin, dt_beta, new_table):
    '''
        Show columns of data reveived. And enables choice.
        Args:
            data:             Name of columns
            dt_beta:          Name of new file
            dt_origin:        Data source for cleaning
            new_table:        Data source for duplicate cleaning

        Kwargs:null

        Returns:null
            obs=Call another function
    '''


    rt=tk.Tk()
    rt.title('Clean of Data')
    rt.geometry("600x400")

    def showSelected():
        column = []
        cname = lb.curselection()

        for i in cname:
            op = lb.get(i)
            column.append(op)

        rt.destroy()
        choice_clean(column, dt_origin, dt_beta, new_table)

    show = tk.Label(rt, text = "Selecione as colunas", font = ("Times", 14), padx = 10, pady = 10)
    show.pack() 
    lb = tk.Listbox(rt, selectmode = "multiple", height=15)
    lb.pack(padx = 10, pady = 10, fill = "both") 
    
    for item in range(len(data)): 
        lb.insert(item, data[item]) 
        lb.itemconfig(item, bg="#ffaa00") 

    tk.Button(rt, text="Continuar", command=showSelected).pack()
    rt.mainloop() 


def management_of_file(dt_origin, type_delimiter, dt_beta):
    '''
        Prepare data for continue (DataFrame).
        Args:
            dt_beta:          Name of new file
            dt_origin:        Data source for cleaning
            type_delimiter:   Type delimiter of data origin.

        Kwargs:null

        Returns:null
            obs=Call another function

    '''


    try:

        new_table = pd.read_csv(dt_origin+'.csv', delimiter=type_delimiter, encoding='latin-1')
        new_table['Domain'] = list(range(new_table.shape[0]))
        new_table['Complement'] = list(range(new_table.shape[0]))
        new_table = new_table.astype({'Domain': 'object', 'Complement': 'object'})
        dt_origin = pd.read_csv(dt_origin+'.csv', delimiter=type_delimiter, encoding='latin-1')

        checkbox(dt_origin.columns, dt_origin, dt_beta, new_table)
            
        
    except Exception as error:
        print(error)


def submit():
    '''
        If true continue Elif Back to first interface.

        Args:    null

        Kwargs:  null

        Returns: null 
            obs=Call another function
    '''


    dt_origin=dt_origin_var.get()
    type_delimiter=type_of_delimiter.get()
    dt_beta=dt_beta_var.get()
     
    dt_origin_var.set("")
    type_of_delimiter.set("")
    dt_beta_var.set("")

    txt = 'Confirma essas informações:'+'\n'+dt_origin+'\n'+type_delimiter+'\n'+dt_beta
    answer = askyesno(title='confirmation', message=txt)

    if answer:
        root.destroy()
        management_of_file(dt_origin, type_delimiter, dt_beta)

     
def main():
    '''
        First interface of user. 
        
        Args:    null

        Kwargs:  null

        Returns: null
    '''


    dt_origin = tk.Label(root, text = 'Nome do arquivo original:', font=('calibre',10, 'bold'))
    dt_origin_answer = tk.Entry(root,textvariable = dt_origin_var, font=('calibre',10,'normal'))

    type = tk.Label(root, text = 'Tipo do separador:', font=('calibre',10, 'bold'))
    type_answer = tk.Entry(root,textvariable = type_of_delimiter, font=('calibre',10,'normal'))

    dt_beta = tk.Label(root, text = 'Nome do novo arquivo:\0', font=('calibre',10, 'bold'))
    dt_beta_answer = tk.Entry(root,textvariable = dt_beta_var, font=('calibre',10,'normal'))

    sub_btn=tk.Button(root,text = 'Submit', command = submit)
    dt_origin.grid(row=0,column=0)
    dt_origin_answer.grid(row=0,column=1)
    

    type.grid(row=1,column=0, sticky="w")
    type_answer.grid(row=1,column=1)

    dt_beta.grid(row=2, sticky="w")
    dt_beta_answer.grid(row=2,column=1)
    sub_btn.grid(row=3,column=1)


    root.mainloop()


if __name__ == '__main__':
    main()
