def maker(seconds_data):
    sidebar = [0,max(seconds_data)/3,(max(seconds_data)/3)*2,(max(seconds_data)/3)*3]
    print(sidebar)
    for a in seconds_data:
        temp = 600 * a
        print(temp/ max(seconds_data))
    pass                                                                             