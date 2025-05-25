import os
import sys
import logging
from datetime import datetime
from seleniumbase import SB
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)
logger = logging.getLogger(__name__)

def main():
    try:
        with SB(uc=True, test=True, locale="en") as sb:  # Removed headless=True
            url = "https://apply.workable.com/two95-international-inc-3/j/E91B0F3F46/apply/"
            logger.info(f"Navigating to URL: {url}")
            sb.activate_cdp_mode(url)
            
            # Handle cookie consent
            try:
                sb.cdp.find_element('[data-ui="cookie-consent-accept"]', best_match=False, timeout=10).mouse_click()
                logger.info("Cookie consent accepted")
            except Exception as e:
                logger.warning(f"Cookie consent handling failed: {e}")

            # Upload resume
            sb.cdp.find_element('button[aria-haspopup="true"]', best_match=False, timeout=10).mouse_click()
            sb.cdp.find_element('[id="file-upload"]', best_match=False, timeout=10).send_file('/app/resume.pdf')
            logger.info("Resume uploaded successfully")
            sb.sleep(10)  # Longer wait after upload

            # Fill form
            sb.cdp.find_element('[data-ui="lastname"]', best_match=False, timeout=10).send_keys('Narsingarh wala')
            logger.info("Form filled successfully")
            sb.sleep(5)

            # Submit application
            sb.cdp.scroll_into_view('[data-ui="apply-button"]')
            sb.sleep(5)
            sb.cdp.find_element('[data-ui="apply-button"]', best_match=False, timeout=10).mouse_click()
            logger.info("Application submitted")
            sb.sleep(10)  # Longer wait before CAPTCHA

            # Handle CAPTCHA
            try:
                sb.cdp.find_element('[id^="turnstile-container-"] div', best_match=False, timeout=5).mouse_click()
                logger.info("CAPTCHA clicked successfully")
            except Exception as e:
                logger.warning(f"CAPTCHA click failed: {e}")

            # Final verification
            sb.sleep(15)  # Longer wait for verification
            sb.cdp.save_screenshot('submission_final.png')
            sb.cdp.find_element('[data-ui="successful-submit"]', best_match=False, timeout=10)
            logger.info("Application process completed successfully!")

    except Exception as e:
        logger.error(f"Script execution failed: {e}")
        raise

if __name__ == "__main__":
    main()