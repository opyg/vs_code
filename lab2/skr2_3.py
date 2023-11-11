
import datetime
import calendar

def main():
    now = datetime.datetime.now()
    print("date and time:\n1 format: ",now.strftime("%b %d %Y %H:%M"),
          "\n 2 format: ",now.strftime("%Y-%m-%d %H:%M:%S"),
          "\n3 format: ",now.strftime("%m.%d.%Y  %I:%M"))
    pass
if __name__ == '__main__':
    main()