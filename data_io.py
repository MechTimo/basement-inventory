import pandas as pd


def open_db():
    data = pd.read_csv("data_template.csv")
    print('Database:')
    show_data(data)
    return data


def save_db(data):
    data.to_csv('data.csv')


def add_entry(data, e, t, c, q):  # data, ean, title, category, quantity
    s = pd.Series([e, t, c, q], index=data.columns)
    data = data.append(s, ignore_index=True)
    #pd.concat([data, s], ignore_index=True)
    return data


def del_entry(data, r, q):  # data, row, quantity
    data.loc[[r],['Menge']] = data.loc[[r],['Menge']] - q
    #print(data.loc[[r],['Menge']])
    if (data.loc[[r],['Menge']] <= 0).bool():
        data = data.drop([r])
    return data


def show_data(data, cat=''): # Was kann cat alles sein? Was als default wählen?
    if cat != '':
        data = data[data['Kategorie'] == cat]
    print(data)


if __name__ == '__main__':
    df = open_db()
    selection = 0
    while selection != 4:
        msg = 'Auswahl:\n1: Add\n2: Delete\n3: Show\n4: Quit\n'
        selection = int(input(msg))
        if selection == 1:  # Add
            ean = input("EAN: ")  # Int oder String?
            title = input("Titel: ")
            category = input("Kategorie: ")
            quantity = int(input("Menge: "))
            df = add_entry(df, ean, title, category, quantity)
        elif selection == 2:  # Delete
            show_data(df)
            row = int(input('Select item to drop: '))
            quantity = int(input('Enter quantity to drop: '))
            #print(type(quantity))
            df = del_entry(df, row, quantity)
        elif selection == 3:  # Show data
            # Filtern welche cat angezeigt werden soll
            categories = df['Kategorie'].drop_duplicates()
            print(categories)
            # hier try catch
            category = int(input('Welche Kategorie soll angezeigt werden?'))
            sc = categories.loc[category]
            #print('selected category: ', sc)
            show_data(df, sc)
        else:
            pass

    save_db(df)
