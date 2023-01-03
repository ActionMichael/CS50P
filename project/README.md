# crawler yahoo finance in python
#### Video Demo:  https://youtu.be/KcqyETxZagM

####Description:

        SETTING:
            pip install selenium
            pip install matplotlib

            prepare selenium.webdriver
                # check your Chrome Version is?(in about Chrome)
                # search "ChromeDriver" in your browser and download that mach version in your filder
                PATH="C:/"YOUR-PATH"/chromedriver.exe" 
                # AND REMANBER CHANGE "\" TO "/"
                driver = webdriver.Chrome(PATH)

            look spec of selenium.webdriver and select function what you need 
                #https://selenium-python.readthedocs.io/waits.html
                from selenium.webdriver.common.by import By
                from selenium.webdriver.common.keys import Keys
                from selenium.webdriver.support.wait import WebDriverWait
                from selenium.webdriver.support import expected_conditions as EC

            for dataset can be visualized in python and output that 
                # pip install matplotlib
                import matplotlib as mpl
                import matplotlib.pyplot as plt
                # AND ADD "mpl.use('TkAgg')" IN THE PYTHON CODE
                ## TO PRIVENT ISSUE #UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.% get_backend()

        We use three functions to build this project
        CRAWLER:
            I highly recommend using selenium library to realize the dynamic function of web pages
            I use the F12 key to observe "https://finance.yahoo.com" and found that the advertisement is the last READY ELEMENT, 
            so I start executing after this is completed, and then need to enter the stock code that we want to query in the SEARCH space and press the ENTER key , 
            after the window jumps, 
            press x to cancel the small window (asking whether to log in), 
            call the TIME function and wait for 10 seconds, 
            then press the history page to call out the data, wait for the screen to jump stably, 
            scroll to the end (15 times, each interval is 0.1 ) is the data after the test can stabilize the screen to the end, 
            and start of CLAWLER table data, save then to .txt file, then close the window.
        REGULAR:
            Regularization is an extremely important point in data science. 
            A good data regularization will be the key to data analysis and statistical calculation. 
            After we observed the .txt files from CRAWLER, we found that the first ROW to the 48th ROW are all blank. 
            In addition The last ROW is not what we want, and each column of the data has no title. 
            After regularization, 
            I Remove the commas from the DAY column, 
            merge the first 3 fields, and save them as a new field as Date , 
            Drop the columns 'Month', 'Day', 'Year', last row, 
            put the new Date field in the first field, and save a new .csv file
        DRAWING_AND_SAVE:
            Visualization is a process of converting huge amounts of data into graphics. 
            For the stock market, line charts are common
            The most common visualization library in python is matplotlib. 
            The things encountered in this call except the above-mentioned ADD " In addition to mpl.use('TkAgg')", 
            there is also the need to call the Numpy library and find that the x-axis data is reversed after plotting.
            so I am performing related corrections here

        TESTING:
            Here I implement the output file test of CRAWLER, REGULAR, DRAWING_AND_SAVE 3 functions

    ~~~~THE END~~~


        


        

        
        