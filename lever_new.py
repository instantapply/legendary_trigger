from seleniumbase import SB
import json
import os
import sys
import logging
from datetime import datetime
import time

message = os.environ.get('MESSAGE_FROM_SQS')
message = json.loads(message)

# Configure logging

def download_resume(resume_url):
    import requests
    response = requests.get(resume_url)
    with open("/home/runner/work/legendary_trigger/legendary_trigger/resume.pdf", "wb") as f:
        f.write(response.content)

with SB(uc=True, test=True, locale="en") as sb:
    j = message
    url = j.get("application_url","")
    print("Application started successfully!")
    sb.activate_cdp_mode(url)
    print ("cdp mode activated")
    download_resume(j.get("user",{}).get("resumeData",{}).get("resumeUrl",""))
    sb.sleep(5)
    print ("resume downloaded successfully")
    sb.cdp.find_element('[id="resume-upload-input"]', best_match=False, timeout=10).send_file('/home/runner/work/legendary_trigger/legendary_trigger/resume.pdf')
    sb.sleep(10)
    print ("resume uploaded successfully")
    
    sb.cdp.find_element('[name="org"]', best_match=False, timeout=10).send_keys(j.get("user",{}).get("resumeData",{}).get("workExperience",[])[0].get("company","") or "NA") 
    print ("company filled")
    
    sb.cdp.find_element('[name="urls[LinkedIn]"]', best_match=False, timeout=10).send_keys(j.get("user",{}).get("personalDetails",{}).get("linkedin","") or "NA") 
    sb.cdp.find_element('[name="urls[Portfolio]"]', best_match=False, timeout=10).send_keys(j.get("user",{}).get("personalDetails",{}).get("portfolio","NA") or "NA" ) 
    sb.cdp.find_element('[name="urls[GitHub]"]', best_match=False, timeout=10).send_keys(j.get("user",{}).get("personalDetails",{}).get("github","NA") or "NA") 
    try:
        sb.cdp.find_element('[name="urls[Stack Overflow]"]', best_match=False, timeout=10).send_keys(j.get("user",{}).get("personalDetails",{}).get("other","NA") or "NA" ) 
    except:
      pass
    
    print ("social links")
    # questions_answers
    for q in j.get("application_questions",[]):
        if q.get("type","") == "text":
          sb.cdp.find_element(f'[name="{q.get("selector","")}"]', best_match=False, timeout=10).send_keys(q.get("answer","NA") or "NA")
        elif q.get("type","") == "select":
          pass
    print ("questions")
    # cover letter
    sb.cdp.find_element('[name="comments"]', best_match=False, timeout=10).send_keys(j.get("cover_letter","").replace("\n","\n\n") ) 
  
    sb.sleep(10)

    print ("coverletter")
    sb.cdp.scroll_into_view('[id="btn-submit"]')
    sb.cdp.find_element('[id="btn-submit"]', best_match=False, timeout=10).mouse_click()

    sb.sleep(10)
    print ("submitted")
    sb.cdp.save_screenshot('abc.png')
    sb.cdp.find_element('[data-qa="msg-submit-success"]', best_match=False, timeout=10)

    print("Application process completed successfully!")
  # [data-qa="msg-submit-success"]
    # sb.cdp.save_screenshot('abc1.png', folder=None, selector=None)
    # sb.cdp.find_element('[data-ui="lastname"]', best_match=False, timeout=10).send_keys('Narsingarh wala')
    # sb.sleep(5)
    # sb.cdp.scroll_into_view('[data-ui="apply-button"]')
    # sb.sleep(5)
    # sb.cdp.save_screenshot('abc2.png', folder=None, selector=None)
    # sb.cdp.find_element('[data-ui="apply-button"]', best_match=False, timeout=10).mouse_click()
    # sb.cdp.save_screenshot('abc3.png', folder=None, selector=None)
    # # sb.cdp.find_element('[data-ui="apply-button"]', best_match=False, timeout=10).mouse_click()
    # sb.sleep(3)
    # sb.cdp.save_screenshot('abc4.png', folder=None, selector=None)
    # sb.sleep(5)
    # try:
    #     # sb.uc_gui_handle_cf()
    #     sb.cdp.find_element('[id^="turnstile-container-"] div', best_match=False, timeout=5).mouse_click()
    #     sb.sleep(3)
    #     sb.cdp.find_element('[id^="turnstile-container-"] div', best_match=False, timeout=5).mouse_click()
    #     sb.sleep(3)
    #     sb.cdp.find_element('[id^="turnstile-container-"] div', best_match=False, timeout=5).mouse_click()
        
        
    # except Exception as e:
    #     print(f"Error clicking on reCAPTCHA: {e}")
    # sb.cdp.save_screenshot('abc5.png', folder=None, selector=None)
    # sb.sleep(20)
    # sb.cdp.save_screenshot('abc6.png', folder=None, selector=None)
    # sb.cdp.find_element('[data-ui="successful-submit"]', best_match=False, timeout=10)
