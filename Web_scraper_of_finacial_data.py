import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime

# Linear regression
def find_k_b(a):
    n = len(a)
    a11 = (n * (n + 1) * (2 * n + 1)) / 6
    a12 = (n * (n + 1)) / 2
    delta = a11 * n - a12 * a12
    f1 = sum([(i + 1) * a[i] for i in range(len(a))])
    f2 = sum(a)
    delta1 = f1 * n - f2 * a12
    delta2 = a11 * f2 - a12 * f1
    k = delta1 / delta
    b = delta2 / delta
    return k, b

def get_and_store_data():
    first_date = input('Enter first date: ')
    last_date = input('Enter last date: ')
    first_date_list = first_date.split('.')
    last_date_list = last_date.split('.')

    date_1 = datetime.date(int(first_date_list[2]), int(first_date_list[1]), int(first_date_list[0]))
    date_last = datetime.date(int(last_date_list[2]), int(last_date_list[1]), int(last_date_list[0]))

    date_iter = date_1
    driver = webdriver.Chrome()
    data_file = open('curr_data.txt', 'a')
    data_file.truncate(0)

    date_list = []
    curr_usd_priv_list = []
    curr_usd_oshad_list = []
    #curr_usd_pumb_list = []

    data_file.write('Date \t\t PrivatBank\t OshadBank\t PUMB\n')
    data_file.write("=" * 60 + "\n")
    try:
        while date_iter <= date_last:
            driver.get("https://minfin.com.ua/ua/currency/banks/" + str(date_iter))
            date_list.append(date_iter)
            curr_usd_priv = driver.find_element(By.XPATH, '/html/body/main/div/div/div[1]/div/section[2]/div[2]/div[2]/table/tbody/tr[1]/td[2]')
            curr_usd_oshad = driver.find_element(By.XPATH, '/html/body/main/div/div/div[1]/div/section[2]/div[2]/div[2]/table/tbody/tr[2]/td[2]')
            #curr_usd_pumb = driver.find_element(By.XPATH,'/html/body/main/div/div/div[1]/div/section[2]/div[2]/div[2]/table/tbody/tr[6]/td[2]')
            curr_usd_priv_list.append(float(curr_usd_priv.text.replace(',', '.')))
            curr_usd_oshad_list.append(float(curr_usd_oshad.text.replace(',', '.')))
            #curr_usd_pumb_list.append(float(curr_usd_pumb.text.replace(',', '.')))

            data_file.write(f"{date_iter}:\t    {curr_usd_priv.text} \t{curr_usd_oshad.text} \n")

            date_iter = date_iter + datetime.timedelta(days=1)
        data_file.write("=" * 60 + "\n")
        data_file.close()
    except Exception as e:
        raise ValueError('Error occurred in get_and_store_data() by reading data from site')
    data = [date_list, curr_usd_priv_list, curr_usd_oshad_list]


    print('Saved data in curr_data.txt')
    return data

def graphic(data):
    plt.plot(data[0], data[1], label='PrivatBank USD', color='blue')
    plt.plot(data[0], data[2], label='OscadBank USD ', color='green')
    #plt.plot(data[0], data[3], label='PUMB', color='red')

    k_p, b_p = find_k_b(data[1])
    forecast_p = [k_p * (i + 1) + b_p for i in range(len(data[1]))]
    plt.plot(data[0], forecast_p, label='PrivatBank Forecast', linestyle='--', color='blue')

    k_o, b_o = find_k_b(data[2])
    forecast_o = [k_o * (i + 1) + b_o for i in range(len(data[2]))]
    plt.plot(data[0], forecast_o, label='OschadBank Forecast', linestyle='--', color='green')

    #k_pumb, b_pumb = find_k_b(data[3])
    #forecast_pumb = [k_pumb * (i + 1) + b_o for i in range(len(data[3]))]
    #plt.plot(data[0], forecast_pumb, label='PUMB Forecast', linestyle='--', color='red')

    plt.xlabel('Дата')
    plt.ylabel('Курс')
    plt.title(f'PrivatBank and OshadBank and PUMB USD')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

try:
    data = get_and_store_data()
except ValueError as e:
    print(e)
try:
    is_exit = False
    while not is_exit:
        print('''
        1.Forcast currency for bank
        2.Show graphic
        3.Update data
        4. Exit
        ''')
        inp = input('Enter your choice: ')
        if inp == '1':
            is_ok = False
            while not is_ok:
                forcast_inp = input('PrivatBank/OshadBank/PUMB: ')
                if forcast_inp == 'PrivatBank':
                    k_p, b_p = find_k_b(data[1])
                    next_curr = k_p * (len(data[1])+1) + b_p
                    print(f'PrivatBank next_curr: {next_curr}')
                    is_ok = True
                elif forcast_inp == 'OshadBank':
                    k_o, b_o = find_k_b(data[2])
                    next_curr = k_o * (len(data[2])+1) + b_o
                    print(f'OshadBank next_curr: {next_curr}')
                    is_ok = True
               # elif forcast_inp == 'PUMB':
                 #   k_pumb, b_pumb = find_k_b(data[3])
                   # next_curr = k_pumb * (len(data[3]) + 1) + b_pumb
                   # print(f'PUMB next_curr: {next_curr}')
                   # is_ok = True
                else:
                    print('Invalid input')
        elif inp == '2':
            graphic(data)
        elif inp == '3':
            data = get_and_store_data()
        elif inp == '4':
            is_exit = True
            break
        else:
            print('Invalid input')
except Exception as e:
    print('Error.')