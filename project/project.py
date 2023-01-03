from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from pandas import DataFrame
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np



def main():
    stock = input("what's stock you looking for: ")
    crl = crawler(stock)
    reg = regular(stock)
    drawing_and_save(stock) 

def crawler(stock):
    url = "https://finance.yahoo.com"
    #啟用瀏覽器的服務
    PATH="YOUR PATH YOU SAVE CHROME DRIVER" 
    driver = webdriver.Chrome(PATH)

    driver.get(url)

    #等跑完，發現廣告ready最晚
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "darla")))

    #在search欄位中打入要搜的股票代碼
    search = driver.find_element_by_css_selector("#Col2-1-SymbolLookupV2-Proxy > div > form > input")
    search.clear()
    search.send_keys(stock)
    search.send_keys(Keys.RETURN)
    
    #針對跳出小視窗(詢問是否login)按x取消
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH , '//*[@id="myLightboxContainer"]/section')))
    #signinlater = driver.find_element_by_css_selector('#myLightboxContainer > section > button.Mx(a).Fz(16px).Fw(600).Mt(20px).D(n)--mobp')
    signinlater = driver.find_element_by_css_selector('#myLightboxContainer > section > button.Mx\(a\).Fz\(16px\).Fw\(600\).Mt\(20px\).D\(n\)--mobp')
    signinlater.click()

    #穩定再等~~~
    time.sleep(10)

    #按歷史來叫出數據
    history = driver.find_element_by_css_selector("#quote-nav > ul > li:nth-child(4) > a")
    history.click()

    #等跑完，發現廣告ready最晚
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "darla")))

    #捲動到底(15次每次間隔0.1)是測試後的數據，穩定到底
    for i in range(15):
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
        time.sleep(0.1)
    
    #爬表格數據
    items = driver.find_elements(By.CLASS_NAME , "BdT")
    path = 'THE PATH YOU WANT TO SAVE'+stock+'-'+'items.txt'
    f = open(path, 'w')
    for item in items:
        f.writelines(item.text+"\n")
    f.close()

    #關頁面  
    driver.quit()

def regular(stock):
    path = 'THE PATH YOU ALREADY SAVE'+stock+'-'+'items.txt'
    df = pd.DataFrame(columns=['Month','Day','Year','Open','High','Low','Close','Adj,Close','Volume'])
    df = pd.read_csv(path, sep=' ', header=None, names=['Month','Day','Year','Open','High','Low','Close','Adj,Close','Volume'], error_bad_lines=False)

    # Remove the commas from the DAY column
    df['Day'] = df['Day'].str.replace(',', '')

    # 合併首3個欄位，並將它們存為新欄位
    df['Date'] = df['Month'].map(str) + '-' + df['Day'].map(str) + '-' + df['Year'].map(str)

    # Drop the columns 'Month', 'Day', 'Year', last row
    df = df.drop(columns=['Month', 'Day', 'Year'])
    df = df.drop(df.index[-1])

    # 把新的Date欄位放在第一個欄位
    df = df[['Date'] + [col for col in df.columns if col != 'Date']]

    # 另存新檔
    df.to_csv(stock+'.csv', index=False)
    
def drawing_and_save(stock):
    # 下面這一行是要啟用matplotlib
    mpl.use('TkAgg')
    # 讀取csv檔案的數據
    df = pd.read_csv('THE PATH YOU ALREADY SAVE'+stock+'.csv')

    # 將dataframe轉換為numpy陣列，否則不接受
    data = df.to_numpy()
    # 取出x和y的資料
    x = data[:, 0]
    y = data[:, 5]

    # Create a subplot經試驗，要將x軸反向
    fig ,ax = plt.subplots()
    # Plot the data
    ax.plot(x, y)
    # Invert the x-axis
    ax.invert_xaxis()

    # 添加標題和標籤
    plt.title('Stock Index of '+stock)
    plt.xlabel('Date')
    plt.ylabel('Price')

    # 保存圖片
    plt.savefig('Stock Index of '+stock+'.png')
    
if __name__ == "__main__":
    main()
