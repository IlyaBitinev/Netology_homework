from func_reg import reader, change_names, duplicate_deleting, change_phone, writer

if __name__ == '__main__':
    writer(change_phone(duplicate_deleting(change_names(reader('phonebook_raw.csv')))))

