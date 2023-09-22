from g_calendar import event_parser

def main():
    cal_man = event_parser.calendar_man()
    cal_man.get_ten_events()
    pass

if __name__ == "__main__":
    main()