from playwright.sync_api import sync_playwright
import pandas as pd
import time

def main():
    with sync_playwright() as p:
        url = 'https://www.nike.com/id/w/new-mens-shoes-3n82yznik1zy7ok'
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_load_state("networkidle")
        # scroll down
        for x in range(1, 6):
            page.keyboard.press("End")
            print("scrolling", x)
            time.sleep(1)




        browser.close()







if __name__ == '__main__':
    main()