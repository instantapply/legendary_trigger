import asyncio
import logging
from typing import Optional

import zendriver as zd
import json


# message = os.environ.get('MESSAGE_FROM_SQS')
message = {"ats_name": "lever", "job_summary": "\ud83d\udc4b Greetings, future tech savant:\n\n\nEmbark on an exciting journey into the realm of software development with 3Pillar! We extend an invitation for you to join our team and gear up for a thrilling adventure. At 3Pillar, our focus is on leveraging cutting-edge technologies that revolutionize industries by enabling data driven decision making. As a Data Engineer, you will hold a crucial position within our dynamic team, actively contributing to thrilling projects that reshape data analytics for our clients, providing them with a competitive advantage in their respective industries. If your passion for data analytics solutions that make a real-world impact, consider this your pass to the captivating world of Data Science and Engineering! \ud83d\ude80\ud83d\udcbb\n\n\nWE ARE 3PILLAR GLOBAL\n\n\nAt 3Pillar, culture is more than a buzzword. The power of culture, teamwork, and open collaboration drives our commitment to building breakthrough software solutions that power digital businesses. Our passion for software development has gained us recognition in some of the industry\u2019s most innovative spaces, including a spot on the Inc. 5000 list ten years in a row, a three time winner of the Washington Post Top Workplaces Award, and notable features in Forbes, Fortune, and the Washington Business Journal.\n\n\nWe are an innovative software development partner whose solutions drive rapid revenue, market share, customer growth and employee efficiency for industry leaders in Media and Publishing, Information Services, Banking and Financial Services, Insurance and Healthcare.\nOur key differentiator is our Product Mindset. Our development teams focus on building for outcomes and all of our team members around the globe are trained on the Product Mindset\u2019s core values \u2013 Minimize Time to Value, Solve For Need, and Excel at Change. Our business-minded approach to agile development ensures that we align to client goals from the earliest conceptual stages through launch and beyond.\n\n\nWHAT WE BELIEVE\n\n\nAt 3Pillar, our core values \u2013 Intrinsic Dignity, Outsized Impact, Open Collaboration, and Continuous Improvement \u2013 drive our commitment to providing best-in-class software development services to high-growth businesses across the globe. We\u2019ve spent more than fifteen years building innovative software solutions. Our executive team has always held our values to the highest standard which has led to active participation on the Forbes Tech Council, a winner of the Ernst & Young Entrepreneur of the Year Award, and a spot on the Washington Business Journal\u2019s Women Who Mean Business list.\n\n\nKey Responsibilities\nFacilitate effective communication with client project stakeholders regarding project status and recommendations.\nCraft client code that is not just efficient but also performant, testable, scalable, secure, and of the highest quality.\nActively participate in accurate planning and estimation efforts, utilizing project methods and tools.\nProficiently gather requirements and organize/present developed features for clients.\nExecute complex activities within the current methodology and quality standards, showcasing success across diverse engagements.\nPromote client success across the team by collaborating with engineers, designers, and managers to understand user pain points, anticipate potential problems, and iterate on solutions that drive client success.\nEngage in agile software development, including daily stand-ups, sprint planning, team retrospectives, and other governance activities.\nActively participate in the Engineering Practice community, mentoring others through Communities of Practice (CoPs) or on project teams and supporting the growth of technical capabilities.\nIndependently drive project delivery within defined architecture, demonstrating autonomy and accountability in all stages from conceptualization to deployment.\n\n\nMinimum Qualifications\n6+ years of professional experience in software development\nStrong skills in organization, logical thinking, problem-solving, and task completion\nExpertise in the C#/.NET tech stack and a track record of building and maintaining distributed systems\nA knack for incrementally improving codebases with precision and care\nC#\nWpf\nWebApi\nMicrosoft Sql Server\nEntity Framework\n.NET 8 or 9\nGitHub\nExperience in Agile software development methodologies.\nExpertise in applying object-oriented programming principles (abstraction, encapsulation).\nExperience in creating and implementing well-tested, scalable, and performant enterprise-level systems.\nPractice and initiative mentoring other engineers and decision-makers throughout the organization.\nGood understanding of SOLID principles and Clean Code.\nFamiliarity with OWASP.\nProficiency in the English language.\nAdditional Experience Desired:\nWe\u2019re especially interested in you if you have:\nFull Stack Application Development: Experience in a collaborative environment\nSoftware Engineering Mastery: Deep understanding of modern software engineering principles and practices\nWillingness to Learn: Open to learning new development languages and tools\nMathematical Acumen: Proficiency in relevant mathematical concepts. Structural or civil engineering knowledge is a plus!\nLeadership Qualities: Ability to inspire, lead and mentor junior software engineers\nObject-Relational Mappers (ORMs)\nArchitectural (DDD, MVVM, etc) and Design Patterns (Factory, Singleton, Observer etc)\nUnit Testing (NUnit & Moq)\nContainers using Docker\nSpecific client-engagement technologies will be specified and vetted at the time of the interview.\n\n\nBenefits\nMedical insurance benefits as per company policy.\nLife Insurance as per company policy\n15 days of paid vacation, sick leave, and paid holidays as per local law\nPaternity and maternity leave as per as per local law\nMarriage, bereavement, and graduation leave as per company policy\nSick leave and paid holidays as per local law\nChristmas and mid-year bonuses as per local law\nMonthly productivity bonus as per local law\nDiscounts in local shops\nDirect deposit of payroll.\nPaid professional certifications\nWhat is it like working for 3Pillar Global?\nAt 3Pillar, we offer a world of opportunity:\n\n\nImagine a flexible work environment \u2013 whether it's the office, your home, or a blend of both. From interviews to onboarding, we embody a remote-first approach.\nYou will be part of a global team, learning from top talent around the world and across cultures, speaking English everyday. Our global workforce enables our team to leverage global resources to accomplish our work in efficient and effective teams.\nWe\u2019re big on your well-being \u2013 as a company, we spend a whole trimester in our annual cycle focused on wellbeing. Whether it is taking advantage of fitness offerings, mental health plans (country-dependent), or simply leveraging generous time off, we want all of our team members operating at their best.\nOur professional services model enables us to accelerate career growth and development opportunities - across projects, offerings, and industries.\nWe are an equal opportunity employer. It goes without saying that we live by values like Intrinsic Dignity and Open Collaboration to create cutting-edge technology AND reinforce our commitment to diversity - globally and locally.\n\n\nJoin us and be a part of a global tech community! \ud83c\udf0d\ud83d\udcbc\u00a0 Check out our LinkedIn site and Careers page to learn more about what it\u2019s like to be part of our #oneteam!", "application_url": "https://jobs.lever.co/3pillarglobal/35991ebd-5342-40e5-bef9-4c1dc94fa8f7/apply", "application_questions": [], "user": {"_id": "6830582669b330a5bf53c84a", "account": {"email": "talibmukadam@gmail.com", "passwordHash": "$2a$10$rFlp8e/9XKcbt/yrITlFIOYTOmzGCXjmL3h1aSuv3y5ew58suyNDi", "isVerified": True, "role": "user", "socialType": ["password"]}, "personalDetails": {"firstName": "Ishaque", "lastName": "Narsingarh Wala", "phone": "+91 7987931405, +91 9665784959", "linkedin": "https://www.linkedin.com/in/ishaque-narsingarh-wal", "github": "", "portfolio": "", "dateOfBirth": None, "gender": "Male", "location": {"city": "Pune, India", "state": "", "country": ""}, "summary": "", "profilePicture": None, "eeo": {"transgender": "No", "orientation": "", "disabilityStatus": "No", "veteranStatus": "No", "ethnicity": ""}}, "resumeData": {"skills": ["C# .NET", "Azure", "Microsoft Excel", "ASP.NET", "SolidWorks", "JIRA", "Python", "Postman", "SQL", "MySQL", "GitHub", "Microsoft SQL Server", "Web API", "MVC", "MVVM", "WPF", "VB.NET", "Design Patterns", "MongoDB", "RabbitMQ, SignalR"], "interests": [], "resumeUrl": "https://resumestalib.s3.us-east-2.amazonaws.com/resumes/6830582669b330a5bf53c84a-1747998806938.pdf", "workExperience": [{"jobTitle": "Principle Software Engineer", "company": "Arcserve", "location": "", "startDate": "2021-11-01", "endDate": "Present", "duration": "", "description": "Built plugins of client products and integrated with third party tools. Worked with software development and testing team members to design and develop robust solutions to meet client requirements for functionality, scalability and performance. Completed code debugging, software troubleshooting, root cause analysis and program reviews. Oversaw development and implementation of company-wide change controls, policies and standard operating procedures (SOPs).", "_id": "6830588569b330a5bf53c884"}, {"jobTitle": "Sr. Principle Development Engineer", "company": "Calsoft", "location": "", "startDate": "2017-08-01", "endDate": "2021-10-01", "duration": "", "description": "Used critical thinking to break down problems, evaluated solutions and made decisions. Carried out day-to-day duties accurately and efficiently. Participated in continuous improvement by generating suggestions, engaging in problem-solving activities to support teamwork. Developed and implemented performance improvement strategies and plans to promote continuous improvement. Worked with customers to understand needs and provide excellent service.", "_id": "6830588569b330a5bf53c885"}, {"jobTitle": "Programmer", "company": "Yardi Systems Pvt.Ltd", "location": "", "startDate": "2015-06-01", "endDate": "2017-07-01", "duration": "", "description": "Worked with software development and testing team members to design and develop robust solutions to meet client requirements for functionality, scalability and performance.", "_id": "6830588569b330a5bf53c886"}], "education": [{"degree": "B.Tech: Bioinformatics", "institution": "Dr. D.Y Patil University - Pune, MH", "location": "", "startYear": "", "endYear": "2012", "gpa": "", "_id": "6830588569b330a5bf53c887"}], "certifications": [{"name": "", "issuer": "", "year": "", "expirationDate": "", "credentialId": "", "verificationLink": "", "_id": "6830588569b330a5bf53c888"}], "projects": [{"description": "", "technologies": [], "link": "", "_id": "6830588569b330a5bf53c889"}], "publications": [], "awards": [], "languages": [], "volunteerExperience": []}, "jobPreferences": {"desiredJobTitles": [], "industries": [], "locations": [], "salaryRange": {"min": 0, "max": 0, "currency": "USD"}, "jobType": [], "relocationWillingness": False, "receiveJobAlerts": True, "_id": "6830588569b330a5bf53c88a"}}, "pdf_url": "", "first_name": "Ishaque", "last_name": "Narsingarh Wala", "full_name": "Ishaque Narsingarh Wala", "email": "talibmukadam@gmail.com", "phone": "+91 7987931405, +91 9665784959", "address": {"street": None, "city": "Pune, India", "state": "", "zip": None}, "date_of_birth": None, "current_location": "Pune, India", "current_company": None, "social_media": {"linkedin": "https://www.linkedin.com/in/ishaque-narsingarh-wal", "github": "", "twitter": None, "portfolio": ""}, "resume_url": "https://resumestalib.s3.us-east-2.amazonaws.com/resumes/6830582669b330a5bf53c84a-1747998806938.pdf", "cover_letter": "Dear Hiring Manager, \n\nI am writing to express my interest in the Data Engineer position at 3Pillar Global, as advertised. With over 6 years of professional experience in software development and a strong background in the C#/.NET tech stack, I am confident that I would be a valuable addition to your team. \n\nIn my previous roles, I have demonstrated my ability to craft client code that is not just efficient but also performant, testable, scalable, secure, and of the highest quality. I have also actively participated in accurate planning and estimation efforts, and have a knack for incrementally improving codebases with precision and care. \n\nI am excited about the opportunity to join 3Pillar Global and contribute to thrilling projects that reshape data analytics for clients, providing them with a competitive advantage in their respective industries. I am eager to bring my passion for data analytics solutions that make a real-world impact to your team. \n\nThank you for considering my application. I look forward to the opportunity to discuss my qualifications further. \n\nSincerely,\nIshaque Narsingarh Wala", "eeo": {"gender": "Male", "transgender": "No", "orientation": "", "disability_status": "No", "veteran_status": "No", "ethnicity": ""}}

def download_resume(resume_url):
    import requests
    response = requests.get(resume_url)
    with open("/Users/runner/work/legendary_trigger/legendary_trigger/resume.pdf", "wb") as f:
        f.write(response.content)
from zendriver.cdp import fetch

PROXYHOST = "gw.dataimpulse.com"
PROXYPORT = "823"
PROXYUSERNAME = "e0af20643b6fe7cb3530"
PROXYPASSWORD = "da23d666a6336983"
PROXY = f"http://{PROXYHOST}:{PROXYPORT}"

async def setup_proxy(username, password, tab):
    async def auth_challenge_handler(event: fetch.AuthRequired):
        # Respond to the authentication challenge
        await tab.send(
            fetch.continue_with_auth(
                request_id=event.request_id,
                auth_challenge_response=fetch.AuthChallengeResponse(
                    response="ProvideCredentials",
                    username=username,
                    password=password,
                ),
            )
        )

    async def req_paused(event: fetch.RequestPaused):
        # Continue with the request
        await tab.send(fetch.continue_request(request_id=event.request_id))

    # Add handlers for fetch events
    tab.add_handler(
        fetch.RequestPaused, lambda event: asyncio.create_task(req_paused(event))
    )
    tab.add_handler(
        fetch.AuthRequired,
        lambda event: asyncio.create_task(auth_challenge_handler(event)),
    )

    # Enable fetch domain with auth requests handling
    await tab.send(fetch.enable(handle_auth_requests=True))

async def main():

    # browser_args = ['--disable-web-security','--disable-site-isolation-trials']
    j = message
    url = j.get("application_url","")
    # browser = await zd.start()
    # page = await browser.get(url)

    browser = await zd.start(browser_args=[f"--proxy-server={PROXY}"])
    page = await browser.get("https://httpbin.io/ip")
    await setup_proxy(PROXYUSERNAME, PROXYPASSWORD, page)
    page = await browser.get(url)


    # await page.save_screenshot()
    # await page.get_content()
    # await page.scroll_down(150)
    # elems = await page.select_all('*[src]')
    # elems = await page.find('button[aria-haspopup="true"]')
    # await elems.click()
    download_resume(j.get("user",{}).get("resumeData",{}).get("resumeUrl",""))
    await asyncio.sleep(10)
    ele = await page.find('[id="resume-upload-input"]')
    await ele.send_file('/Users/runner/work/legendary_trigger/legendary_trigger/resume.pdf')

    await asyncio.sleep(20)

    ele = await page.find('[name="org"]')
    await ele.send_keys(j.get("user",{}).get("resumeData",{}).get("workExperience",[])[0].get("company","") or "NA")

    ele = await page.find('[id="btn-submit"]')
    await ele.scroll_into_view()
    await ele.click()
    await asyncio.sleep(10)
    await page.save_screenshot(filename='abc.jpeg', format='jpeg', full_page=True)

    ele = await page.find('[data-qa="msg-submit-success"]')
    # await ele.click()
    # await asyncio.sleep(10)
    # await browser.close()

if __name__ == '__main__':

    # since asyncio.run never worked (for me)
    asyncio.run(main())

# with SB(uc=True, locale="en") as sb:
#     j = message
#     url = j.get("application_url","")
#     print("Application started successfully!")
#     sb.activate_cdp_mode(url)
#     print ("cdp mode activated")
#     download_resume(j.get("user",{}).get("resumeData",{}).get("resumeUrl",""))
#     sb.sleep(5)
#     print ("resume downloaded successfully")
#     sb.cdp.find_element('[id="resume-upload-input"]', best_match=False, timeout=10).send_file('/Users/talib/resume.pdf')
#     sb.sleep(10)
#     print ("resume uploaded successfully")
    
#     sb.cdp.find_element('[name="org"]', best_match=False, timeout=10).send_keys(j.get("user",{}).get("resumeData",{}).get("workExperience",[])[0].get("company","") or "NA") 
#     print ("company filled")
    
#     sb.cdp.find_element('[name="urls[LinkedIn]"]', best_match=False, timeout=10).send_keys(j.get("user",{}).get("personalDetails",{}).get("linkedin","") or "NA") 
#     sb.cdp.find_element('[name="urls[Portfolio]"]', best_match=False, timeout=10).send_keys(j.get("user",{}).get("personalDetails",{}).get("portfolio","NA") or "NA" ) 
#     sb.cdp.find_element('[name="urls[GitHub]"]', best_match=False, timeout=10).send_keys(j.get("user",{}).get("personalDetails",{}).get("github","NA") or "NA") 
#     try:
#       sb.cdp.find_element('[name="urls[Stack Overflow]"]', best_match=False, timeout=10).send_keys(j.get("user",{}).get("personalDetails",{}).get("other","NA") or "NA" ) 
#     except:
#       pass

#     print ("social links")
#     # questions_answers
#     for q in j.get("application_questions",[]):
#         if q.get("type","") == "text":
#           sb.cdp.find_element(f'[name="{q.get("selector","")}"]', best_match=False, timeout=10).send_keys(q.get("answer","NA") or "NA")
#         elif q.get("type","") == "select":
#           pass
#     print ("questions")
#     # cover letter
#     sb.cdp.find_element('[name="comments"]', best_match=False, timeout=10).send_keys(j.get("cover_letter","").replace("\n","\n\n") ) 
  
#     sb.sleep(10)

#     print ("coverletter")
#     sb.cdp.scroll_into_view('[id="btn-submit"]')
#     sb.cdp.find_element('[id="btn-submit"]', best_match=False, timeout=10).mouse_click()

#     sb.sleep(10)
#     print ("submitted")
#     sb.cdp.find_element('[data-qa="msg-submit-success"]', best_match=False, timeout=10)

#     print("Application process completed successfully!")
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
