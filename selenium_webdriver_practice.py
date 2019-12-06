import selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from AutomatiomFWsep.utilities.customlogger import customLogger as cl


class seleniumwebdriver:

    log  = cl.customlogger(loglevel=logging.INFO)

    def __init__(self,driver):
        self.driver=driver


    def gettype(self,locator):
        if locator == 'name':
            return By.NAME
        elif locator == 'id':
            return By.ID
        elif locator == 'xpath':
            return By.XPATH
        elif locator == 'class name':
            return By.CLASS_NAME
        elif locator == 'partial link text':
            return By.PARTIAL_LINK_TEXT
        elif locator == 'tag name':
            return By.TAG_NAME
        elif locator == 'link text':
            return By.LINK_TEXT
        elif locator == 'css selector':
            return By.CSS_SELECTOR
        else:
            self.log.error("Provided locator is wrong "+locator+" Plea"
                           "se provide valid one")
            return False

    def getwebelement(self,locatorvalue,locator='id'):
        element = None
        try:
            Bytype = self.gettype(locator)
            element =self.driver.find_element(Bytype,locatorvalue)
            self.log.info("Identified webelement with locator "+locator+ "and locatorvalue" +locatorvalue)
        except Exception as e:
            self.log.error("Unable to identify the webelement with locator "
                           ""+locator+"and locator value "+locatorvalue+e)
            return element


    def getwebelements(self,locator,locatorvalues):
        elements=None
        try:
            Bytype=self.gettype(locator)
            elements=self.driver.find_element(Bytype,locatorvalues)
            self.log.info("identified we elements with locator "+locator+"and locator values"+locatorvalues)
        except Exception as e:
            self.log.error("unable to identifie the elements"+locator+"and"+locatorvalues+e)
            return False

    def iselementpresent(self,locatorvalue,locator='id'):
        element=self.getwebelement(locator,locatorvalue)
        if element is not None:
            self.log.info("element found with"+locator+locatorvalue)
        else:
            self.log.error("element not found with"+locatorvalue+locator)
            return False

    def sendurl(self,url):
        self.driver.get(url)


    def browsernavigation(self,action='back'):
        if action == 'back':
            self.log.info("clicked on back")
            self.driver.back()
        elif action == 'forward':
            self.log.info("clicked on forward")
            self.driver.forward()
        elif action == "refresh":
            self.log.info("clicked on refresh")
        else:
            self.log.error("Provide wrong navigation action,please provide valid action")
        return False

    def setbrowsersize(self,width=500,height=500):
        self.driver.set_window_size(width,height)

    def setbrowserposition(self,width=500,height=500):
        self.driver.set_window_position(width,height)

    def browsermaxormin(self,action='max'):
        if action == "max":
            self.log.info("maximized the windows")
            self.driver.maximize_window()
        elif action == "Min":
            self.log.info("clicked on minimized window")
            self.driver.minimized_window()

    def gettitle(self):
        return self.driver.title()

    def geturl(self):
        return self.driver.current_url()

    def senddata(self,data,locatorvalues,locator):
        element=self.getwebelement(locator,locatorvalues)
        if element is not None :
            element.send.keys(data)
            self.log.info("entered text data"+data+"into element"+locatorvalues)
        else:
            self.log.error("unable to send data")
            return False

    def click(self,locatorvalues,locator='id'):
        element= self.getwebelement(locatorvalues,locator)
        if element is not None:
            element.click()
            self.log.info("Clicked on web element "+locatorvalues)
        else:
            self.log.error("unable to click on the element"+locatorvalues)
            return False

    def clear(self,locatorvalues,locator='id'):
        element = self.getwebelement(locatorvalues,locator)
        if element is not None:
            element.clear()
            self.log.info("cleared the text from element"+locatorvalues)
        else:
            self.log.error("unable to clear the text"+locatorvalues)
            return False

    def gettext(self,locatorvalues,locator='id'):
         element = self.getwebelement(locatorvalues,locator)
         text=None
         if element is not None:
             text = element.text
             self.log.info("got text"+text+"from"+locatorvalues)
         else:
             self.log.error("unable to get text from"+locatorvalues)
             return False

    def selectoptionfrmdrpdwn(self,option,locatorvalues,locator='id'):
        element = self.getwebelement(locator,locatorvalues)
        if element is not None:
            s1=Select(element)
            s1.select_by_visible_text(option)
            self.log.info("Selected " + option + " from drp dwn " + locatorvalues)
        else:
            self.log.error("Unable to select option from web element " + locatorvalues)
            return False

    def selectoptionfrmdrpdwnbyvalue(self,value,locatorvalues,locator='id'):
        element = self.getwebelement(locator,locatorvalues)
        if element is not None :
           s1 =  Select(element)
           s1.select_by_value(value)
           self.log.info("Selected " + value + " from drp dwn " + locatorvalues)
        else:
           self.log.error("Unable to select option from web element " + locatorvalues)
           return False

    def selectbyindexdrpdwn(self,locatorvalue,locator='id',index='0'):
        element=self.getwebelement(locator,locatorvalue)
        if element is not None:
            s1=Select(element)
            s1.select_by_index(index)
            self.log.info("Selected " + index + " from drp dwn " + locatorvalue)
        else:
            self.log.error("Unable to select option from web element " + locatorvalue)
            return False

    def deselectallaoption(self,locatorvalues,locator='id'):
        element = self.getwebelement(locatorvalues,locator)
        if element is not None:
            s1=Select(element)
            s1.deselect_all()
            self.log.info("De Selected all options from drp dwn " + locatorvalues)
        else:
            self.log.error("Unable to de select option from web element " + locatorvalues)
            return False

    def deselectbyvaluefrmddrpdwn(self,value,locatorvalues,locator):
        element = self.getwebelement(locatorvalues,locator)
        if element is not None:
            s1= Select(element)
            s1.deselect_by_value(value)
            self.log.info("De Selected "+value+"option from drp dwn " + locatorvalues)
        else:
            self.log.error("Unable to de select "+value+"option from web element " + locatorvalues)
            return False

    def handlefframe(self,id=''):
        try:
            self.driver.switch_to.frame(id)
            self.log.info("switched to frame"+id)
        except Exception as e:
            self.log.error("error in frames"+id+e)

    def switchparentframe(self):
        self.driver.switch_to.parent_frame()

    def switchtodefaultcontentframe(self):
        self.driver.switch_to.default_content()

    def jsonpopups(self,action="accept"):
        if action == "accept":
            self.driver.switch_to.alert.accept()
        elif action == "dismiss":
            self.driver.switch_to.alert.dismiss()
        else:
            self.log.error("unable to do jsonpopups action with provided ")

    def getcurrentwindowid(self):
        wh = self.driver.current_window_handle
        return wh

    def getcurrentwinodwhandles(self):
        wh = self.driver.window_handles
        return wh

    def switchtowindow(self,windowid):
        self.driver.switch_to.window(windowid)

    def webdrivers_elementclicable(self,locatorvalue,locator='id',waittime=20, poll_freq=2):
        bytype=self.gettype()
        try:
            wait = WebDriverWait(self.driver,waittime,poll_freq,ElementNotSelectableException,ElementNotInteractableException)
            wait.until(Ec.element_to_be_clickable(bytype,locatorvalue))
            self.log.info("Waited for element "+str(waittime))
        except Exception as e:
            self.log.error("Unable to wait for element "+str(e))

    def wedriverwait_titlecontains(self,locatorvalue,title,locator='id',waittime=30,poll_freq=3):
        bytype=self.gettype(locator)
        try:
            wait = WebDriverWait(self.driver,waittime,poll_freq,ElementNotInteractableException,ElementNotSelectableException)
            wait.until(Ec.title_contains(title))
            title.sleep(10)
            self.log.info("Waited for title "+str(waittime))
        except Exception as e:
            self.log.error("Unable to wait for element "+str(e))

    def webdriver_urlcontains(self,url,waittime=30,poll_freq=3):
        try:
            wait = WebDriverWait(self.driver,waittime,poll_freq,ElementNotInteractableException,ElementNotVisibleException,ElementNotSelectableException)
            wait.until(Ec.url_contains(url))
            self.log.info("Waited for url " + str(waittime))
        except Exception as e:
            self.log.error("Unable to wait for url " + str(e))

    def mouseover(self,locatorvalue,locator):
        try:
            element=self.getwebelement(locator,locatorvalue)
            ac=ActionChains(self.driver)
            ac.move_to_element(element).perform()
        except Exception as e:
            self.log.error("Unable to mouse over on element "+locatorvalue)

    def mouserover_click(self,locatorvalues,locator='id'):
        try:
            element=self.getwebelement(locator,locatorvalues)
            ac = ActionChains(self.driver)
            ac.move_to_element(element).click().perform()
        except Exception as e:
            self.log.error("Unable to mouse over on element "+locatorvalues)

    def scrollpage(self,x=500,y=500):
        self.driver.execute_script("window.scrollBy("+x+""+y+");")


