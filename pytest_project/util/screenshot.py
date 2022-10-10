from datetime import time, datetime

class ScreenShot:

    def take_screenshot(driver, nodeid):
        time.sleep(1)
        file_name = f'{nodeid}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace("/", "_").replace("::", "__")
        driver.save_screenshot(file_name)
