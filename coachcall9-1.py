li_string = "This is a long string with a lot of random words in it that don't mean anything"
li_list = li_string.split()

def check_list_for_string(s, l, case_sensitive = False):
    if (not case_sensitive):
        s = s.strip().lower()
        l = [st.strip().lower() for st in l]
  
    if (s in l):
        print(s + " is in")      
    else:
        print(s + " is not in")
        
check_list_for_string("long", li_list, case_sensitive = False)