import requests, json, traceback, openai
from flask import request
import loggerutility as logger
import commonutility as common
import os
from datetime import datetime

class InvokeIntent:
    userId = ""
    def getInvokeIntent(self):
        try:
            logger.log(f"\n\nInside getInvokeIntent()","0")
            jsonData = request.get_data('jsonData', None)
            intentJson = json.loads(jsonData[9:])
            logger.log(f"\njsonData openAI class::: {jsonData}","0")
            
            finalResult     =  {}
            openAI_APIKey   =  intentJson['openAI_APIKey'] 
            intent_input    =  intentJson['intent_input']
            enterprise      =  intentJson['enterprise']  

            if 'userId' in intentJson.keys():
                self.userId = intentJson['userId']

            fileName        = "intent_Instructions.txt"
            openai.api_key  = openAI_APIKey
            
            logger.log(f"\n\njsonData getIntentService fileName::: \t{fileName}\n","0")
            
            # Get the current date and time
            current_datetime = datetime.now()
            logger.log(f"\n\current_datetime datatype ::: \t{type(current_datetime)} \t {current_datetime}\n","0")
            # Format the date and time as required
            formatted_datetime = current_datetime.strftime("%d-%b-%Y, %H:%M:%S")
            logger.log(f"\n\ndateteme datatype ::: \t{type(formatted_datetime)}\n","0")
   
            logger.log(f"\n\njsonData openAI class datetime::: \t{formatted_datetime}\n","0")
            
            if os.path.exists(fileName):
                intent_trainingData = open(fileName,"r").read()
            else:
                logger.log(f"\n\n{fileName}  does not exist.\n","0")  
                message = f"The Intent API service could not be requested due to missing '{fileName}' file. "
                return message
                
            logger.log(f"\n\ngetIntentService before conversion :::::: {type(intent_trainingData)} \n{intent_trainingData}\n","0")
            replaced_trainingData = intent_trainingData.replace("<intent_input>", intent_input)
            logger.log(f"\n\ngetIntentService after replacing <intent_input> :::::: \n{replaced_trainingData} \n{type(replaced_trainingData)}","0")
            
            logger.log(f"\n\nopenAI_trainingData before conversion date:::::: {type(intent_trainingData)} \n{intent_trainingData}\n","0")
            replaced_trainingData = replaced_trainingData.replace("<Current_date_time>", formatted_datetime)
            logger.log(f"\n\nopenAI_trainingData after replacing date <Current_date_time> :::::: \n{replaced_trainingData} \n{type(replaced_trainingData)}","0")
            
            messageList = json.loads(replaced_trainingData)
            logger.log(f"\n\nmessageList after conversion :::::: {messageList} \n{type(messageList)}","0")
            
            logger.log(f"\n\nfinal messageList :::::: {messageList}","0")

            if self.userId and self.userId != "":
                response = openai.ChatCompletion.create(
                                                        model="gpt-3.5-turbo",
                                                        messages=messageList,
                                                        temperature=0,
                                                        max_tokens=1800,
                                                        top_p=1,
                                                        frequency_penalty=0,
                                                        presence_penalty=0,
                                                        user=self.userId,
                                                    )
            else:
                response = openai.ChatCompletion.create(
                                                        model="gpt-3.5-turbo",
                                                        messages=messageList,
                                                        temperature=0,
                                                        max_tokens=1800,
                                                        top_p=1,
                                                        frequency_penalty=0,
                                                        presence_penalty=0,
                                                    )
            logger.log(f"\n\nResponse openAI endpoint::::: {response} \n{type(response)}","0")
            finalResult=str(response["choices"][0]["message"]["content"])
            logger.log(f"\n\nOpenAI endpoint finalResult ::::: {finalResult} \n{type(finalResult)}","0")
            return finalResult
        
        except Exception as e:
            logger.log(f'\n In getIntentService exception stacktrace : ', "1")
            trace = traceback.format_exc()
            descr = str(e)
            returnErr = common.getErrorXml(descr, trace)
            logger.log(f'\n Exception ::: {returnErr}', "0")
            return str(returnErr)
        

