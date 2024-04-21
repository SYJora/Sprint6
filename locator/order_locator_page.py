from selenium.webdriver.common.by import By


class OrderPageLocator:
    NAME = (By.XPATH, "//input[@placeholder = '* Имя']")
    LASTNAME = (By.XPATH, "//input[@placeholder = '* Фамилия']")
    ADRES = (By.XPATH, "//input[@placeholder = '* Адрес: куда привезти заказ']")
    PHONE = (By.XPATH, "//input[@placeholder = '* Телефон: на него позвонит курьер']")
    METRO = (By.XPATH, "//input[@placeholder = '* Станция метро']")
    STANTION = (By.XPATH, "//button/child::div[contains(text(), 'Бульвар Рокоссовского')]")

    DATA = (By.XPATH, "//input[@placeholder = '* Когда привезти самокат']")
    DATA_DELIVERY = (By.XPATH, "//div[@class = 'react-datepicker__day react-datepicker__day--016']")

    RENT_DATA_PLACEHOLDER = (By.XPATH, "//div[contains(text(), '* Срок аренды')]")
    RENT_DAY = (By.XPATH, "//div[@class = 'Dropdown-menu']/child::div[contains(text(), 'трое суток')]")

    COLOR_SELECT = (By.XPATH, "//label[contains(text(), 'чёрный жемчуг')]")
    COMMENT = (By.XPATH, "//input[@placeholder = 'Комментарий для курьера']")

    SUCCESSFUL_ORDER = (By.XPATH, "//div[@class = 'Order_Modal__YZ-d3']")

    BUTTON_YES = (By.XPATH, "//div[@class = 'Order_Buttons__1xGrp']/child::button[contains(text(), 'Да')]")
    BUTTON_NEXT = (By.XPATH, "//button[contains(text(), 'Далее')]")
    BUTTON_ORDER = (By.CLASS_NAME, "Button_Button__ra12g")
    BUTTON_ORDER_LAST_PAGE = (By.XPATH, "//div[@class = 'Order_Buttons__1xGrp']/child::button[contains(text(), 'Заказать')]")
    BUTTON_ORDER_BIG = (By.XPATH, "//div[@class = 'Home_FinishButton__1_cWm']/child::button")
    BUTTON_COOKES = (By.ID, 'rcc-confirm-button')