import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLearning:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver  # webdriver

    def run(self, num_d: int, word_d: list) -> None:  # 핸들러 실행
        driver = self.driver
        da_e, da_k, _ = word_d
        driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div"
        ).click()  # 세트 화면에서 테스트 학습 버튼 클릭
        time.sleep(1)

        # 테스트 학습 시작 버튼 클릭
        try:
            driver.find_element(
                By.CSS_SELECTOR,
                "#wrapper-test > div > div.quiz-start-div > div.layer.retry-layer.box > div.m-t-xl > a",
            ).click()
        except NoSuchElementException:
            print("테스트 학습 시작 버튼을 찾을 수 없습니다.")

        time.sleep(0.5)

        # 테스트 학습 시작 버튼 클릭
        try:
            driver.find_element(
                By.CSS_SELECTOR,
                "#wrapper-test > div > div.quiz-start-div > div.layer.prepare-layer.box.bg-gray.text-white > div.text-center.m-t-md > a",
            ).click()
        except NoSuchElementException:
            print("테스트 학습 시작 버튼을 찾을 수 없습니다.")

        time.sleep(0.5)

        # "테스트에 새로 응시하시겠습니까?" 모달 처리
        try:
            WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), '테스트에 새로 응시하시겠습니까?')]")))
            driver.find_element(By.XPATH, "/html/body/div[39]/div[2]/div/div[2]/a[3]").click()
        except (NoSuchElementException, TimeoutException):
            pass

        time.sleep(0.5)

        # "테스트를 다시 시작하면 기존 테스트는 무효화됩니다. 새로 시작할까요?" 모달 처리
        try:
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(text(), '테스트를 다시 시작하면 기존 테스트는 무효화됩니다. 새로 시작할까요?')]")))
            driver.find_element(By.XPATH, '//*[@id="confirmModal"]/div[2]/div/div[2]/a[3]').click()
        except (NoSuchElementException, TimeoutException):
            pass

        time.sleep(1.5)
        num_d = driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div[2]/div[1]/div/span[2]/span"
        ).text

        # 앞면 단어를 가져오고,
        for i in range(1, int(num_d) + 1):
            cash_d = driver.find_element(  # 카드 앞면 단어 가져오기
                By.XPATH,
                f"//*[@id='testForm']/div[{i}]/div/div[1]/div[2]/div[2]/div/div", # 맞음!
            ).text.split("\n")[0]
            time.sleep(1)

            # 앞면 카드 클릭
            driver.find_element(  # 카드 앞면 클릭
                By.XPATH,
                f"/html/body/div[2]/div/div[2]/div[2]/form/div[{i}]/div/div[1]/div[2]/div[2]/div/div",
            ).click()

            time.sleep(2)


            # 인풋이 카드 버튼일 경우
            try:
                if cash_d.upper() != cash_d.lower():
                    try:
                        text = da_k[da_e.index(cash_d)]
                    except ValueError:
                        text = da_e[da_k.index(cash_d)]
                else:
                    text = da_e[da_k.index(cash_d)]
            except ValueError:
                text = "모름"

            # 인풋이 입력해야 할 경우
            try:
                input_tag = driver.find_element(
                    By.XPATH,
                    f"//*[@id='testForm']/div[{i}]/div/div[2]/div/div[2]/div[1]/input",
                )
                submit_tag = driver.find_element(
                    By.XPATH,
                    f"//*[@id='testForm']/div[{i}]/div/div[2]/div/div[2]/div[2]/a",
                )
                # "테스트에 집중하세요" 모달 처리

                input_tag.click()  # 입력창 클릭
                input_tag.send_keys(text)  # 입력창에 단어 입력
                submit_tag.click()  # 제출 버튼 클릭
            except NoSuchElementException:  # 입력창이 없으면
                box_items = driver.find_element(  # 카드 뒷면 선택지 가져오기
                    By.XPATH,
                    f"/html/body/div[2]/div/div[2]/div[2]/form/div[{i}]/div/div[2]/div/div[1]",
                )
                box_items = box_items.find_elements(By.TAG_NAME, "div")
                if text == "모름":
                    print("모르는 단어 감지됨")
                    box_items[0].click()
                for box_item in box_items:
                    if box_item.text == text:
                        box_item.click()
                        break
            time.sleep(2)
