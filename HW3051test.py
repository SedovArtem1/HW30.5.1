from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_petfriends():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get("https://petfriends.skillfactory.ru/")

    # нажимаем на кнопку "Зарегистрироваться"
    button_reqister = browser.find_element(By.CLASS_NAME, 'btn.btn-success')
    button_reqister.click()

    # нажимаем на кнопку "У меня уже есть аккаунт"
    button_akkount = browser.find_element(By.LINK_TEXT, u"У меня уже есть аккаунт")
    button_akkount.click()

    # чистим поле электронной почты и вводим свою электронную почту
    email_login = browser.find_element(By.ID, "email")
    email_login.clear()
    email_login.send_keys("pr1403@yandex.ru")

    # используем WebDriverWait для явного ожидания
    # чистим поле пароля и вводим пароль
    password = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.ID, "pass")))
    password.clear()
    password.send_keys("pr140381")

    # нажимаем на кнопку "Войти"
    button_enter = browser.find_element(By.CLASS_NAME, 'btn.btn-success')
    button_enter.click()

    # нажимаем на "Мои питомцы"
    button_my_pets = browser.find_element(By.CLASS_NAME, 'nav-link')
    button_my_pets.click()

    # проверяем, что мы оказались на главной странице пользователя
    assert browser.find_element(By.TAG_NAME, 'h2').text == "Надежда"
    print("Страница принадлежит Надежде")

    # проверяем, что карточек с питомцами на странице 8 штук
    all_cards = browser.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
    quantity = len(all_cards)
    print(f'Количество карточек с моими питомцами  =  {quantity}')
    assert quantity == 8
    # проверяем количество карточек по картинкам, почему-то карточки без картинок тоже считает
    all_images = browser.find_elements(By.CSS_SELECTOR, 'th>img')
    print(f'Количество питомцев на странице = {len(all_images)}')
    assert len(all_images) == 8
    print("_________________________________________________________________________")


    there_is_a_photo = []
    there_is_no_photo = []
    for a in range(len(all_images)):
        if all_images[a].get_attribute('src') != '':
            there_is_a_photo.append(a)
        else:
            there_is_no_photo.append(a)
    assert len(there_is_a_photo) + len(there_is_no_photo) == len(all_images)
    # проверяем, что хотя бы у половины питомцев есть фото
    assert len(there_is_a_photo) >= len(there_is_no_photo)
    print(f"Карточек с фото {len(there_is_a_photo)} из {len(all_images)} штук")
    print(f"Карточек без фото {len(there_is_no_photo)} из {len(all_images)} штук")
    print("_________________________________________________________________________")

    # "вытаскиваем" из текста на странице фразу "Питомцев: 8" и сравниваем вторую часть фразы с количеством фото не странице
    for number_of_pets in browser.find_elements(By.XPATH, 'html/body/div[1]/div/div[1]'):
        list_number = number_of_pets.text.split()
        num = list_number[2]
        assert int(num) == len(all_images)

    # проверка на наличие имени, породы и возраста у всех питомцев
    # проверка на уникальность имен питомцев
    for all_elements in browser.find_elements(By.CLASS_NAME, 'table.table-hover'):
        all_words = all_elements.text.split()
        all_names = all_words[4:35:4]
        assert len(all_names) == quantity # проверка, что у всех питомцев есть имена
        print("У всех карточек есть имена")
        unique_names = set(all_names)
        assert len(unique_names) != len(all_names) # проверка, что имена не уникальны
        print("К сожалению имена питомцев не уникальны")
        all_breeds = all_words[5:35:4]
        assert len(all_breeds) == quantity # проверка, что у всех питомцев есть породы
        print("У всех карточек есть породы")
        all_ages = all_words[6:35:4]
        assert len(all_ages) == quantity  # проверка, что у всех питомцев есть возрасты
        print("У всех карточек есть возрасты")
        print("_________________________________________________________")

    # проверка питомцев на уникальность
    pet_1 = all_words[4:7]
    pet_2 = all_words[8:11]
    pet_3 = all_words[12:15]
    pet_4 = all_words[16:19]
    pet_5 = all_words[20:23]
    pet_6 = all_words[24:27]
    pet_7 = all_words[28:31]
    pet_8 = all_words[32:35]
    if pet_1 != pet_2:
        print("Первый и второй питомец не совпадают")
    else:
        print('Первый и второй питомец СОВПАДАЮТ')
    if pet_1 != pet_3:
        print("Первый и третий питомец не совпадают")
    else:
        print('Первый и третий питомец СОВПАДАЮТ')
    if pet_1 != pet_4:
        print("Первый и четвертый питомец не совпадают")
    else:
        print('Первый и четвертый питомец СОВПАДАЮТ')
    if pet_1 != pet_5:
        print("Первый и пятый питомец не совпадают")
    else:
        print('Первый и пятый питомец СОВПАДАЮТ')
    if pet_1 != pet_6:
        print("Первый и шестой питомец не совпадают")
    else:
        print('Первый и шестой питомец СОВПАДАЮТ')
    if pet_1 != pet_7:
        print("Первый и седьмой питомец не совпадают")
    else:
        print('Первый и седьмой питомец СОВПАДАЮТ')
    if pet_1 != pet_8:
        print("Первый и восьмой питомец не совпадают")
    else:
        print('Первый и восьмой питомец СОВПАДАЮТ')
    if pet_2 != pet_3:
        print("Второй и третий питомец не совпадают")
    else:
        print('Второй и третий питомец СОВПАДАЮТ')
    if pet_2 != pet_4:
        print("Второй и четвёртый питомец не совпадают")
    else:
        print('Второй и четвёртый питомец СОВПАДАЮТ')
    if pet_2 != pet_5:
        print("Второй и пятый питомец не совпадают")
    else:
        print('Второй и пятый питомец СОВПАДАЮТ')
    if pet_2 != pet_6:
        print("Второй и шестой питомец не совпадают")
    else:
        print('Второй и шестой питомец СОВПАДАЮТ')
    if pet_2 != pet_7:
        print("Второй и седьмой питомец не совпадают")
    else:
        print('Второй и седьмой питомец СОВПАДАЮТ')
    if pet_2 != pet_8:
        print("Второй и восьмой питомец не совпадают")
    else:
        print('Второй и восьмой питомец СОВПАДАЮТ')
    if pet_3 != pet_4:
        print("Третий и четвёртый питомец не совпадают")
    else:
        print('Третий и четвёртый питомец СОВПАДАЮТ')
    if pet_3 != pet_5:
        print("Третий и пятый питомец не совпадают")
    else:
        print('Третий и пятый питомец СОВПАДАЮТ')
    if pet_3 != pet_6:
        print("Третий и шестой питомец не совпадают")
    else:
        print('Третий и шестой питомец СОВПАДАЮТ')
    if pet_3 != pet_7:
        print("Третий и седьмой питомец не совпадают")
    else:
        print('Третий и седьмой питомец СОВПАДАЮТ')
    if pet_3 != pet_8:
        print("Третий и восьмой питомец не совпадают")
    else:
        print('Третий и восьмой питомец СОВПАДАЮТ')
    if pet_4 != pet_5:
        print("Четвёртый и пятый питомец не совпадают")
    else:
        print('Четвёртый и пятый питомец СОВПАДАЮТ')
    if pet_4 != pet_6:
        print("Четвёртый и шестой питомец не совпадают")
    else:
        print('Четвёртый и шестой питомец СОВПАДАЮТ')
    if pet_4 != pet_7:
        print("Четвёртый и седьмой питомец не совпадают")
    else:
        print('Четвёртый и седьмой питомец СОВПАДАЮТ')
    if pet_4 != pet_8:
        print("Четвёртый и восьмой питомец не совпадают")
    else:
        print('Четвёртый и восьмой питомец СОВПАДАЮТ')
    if pet_5 != pet_6:
        print("Пятый и шестой питомец не совпадают")
    else:
        print('Пятый и шестой питомец СОВПАДАЮТ')
    if pet_5 != pet_7:
        print("Пятый и седьмой питомец не совпадают")
    else:
        print('Пятый и седьмой питомец СОВПАДАЮТ')
    if pet_5 != pet_8:
        print("Пятый и восьмой питомец не совпадают")
    else:
        print('Пятый и восьмой питомец СОВПАДАЮТ')
    if pet_6 != pet_7:
        print("Шестой и седьмой питомец не совпадают")
    else:
        print('Шестой и седьмой питомец СОВПАДАЮТ')
    if pet_6 != pet_8:
        print("Шестой и восьмой питомец не совпадают")
    else:
        print('Шестой и восьмой питомец СОВПАДАЮТ')
    if pet_7 != pet_8:
        print("Седьмой и восьмой питомец не совпадают")
    else:
        print('Седьмой и восьмой питомец СОВПАДАЮТ')