with open(r"C:\Users\smjai\Documents\shelflife_result.txt", "w") as f:
    f.write("Python is running!\n")
    try:
        import bcrypt
        f.write("bcrypt OK\n")
    except Exception as e:
        f.write(f"bcrypt FAIL: {e}\n")
    try:
        import customtkinter
        f.write("customtkinter OK\n")
    except Exception as e:
        f.write(f"customtkinter FAIL: {e}\n")
    try:
        import sqlite3
        f.write("sqlite3 OK\n")
    except Exception as e:
        f.write(f"sqlite3 FAIL: {e}\n")
    f.write("DONE\n")
