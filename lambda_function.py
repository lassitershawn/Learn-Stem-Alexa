# -*- coding: utf-8 -*-
#IMPORTS =================================================================================================================
import logging
import json
import ask_sdk_core.utils as ask_utils
import os
import random #for random questioning - Dalton

from ask_sdk_s3.adapter import S3Adapter
s3_adapter = S3Adapter(bucket_name=os.environ["S3_PERSISTENCE_BUCKET"]) #For storing information between intents - Dalton

from ask_sdk_core.skill_builder import CustomSkillBuilder
from ask_sdk_core.dispatch_components import (
    AbstractRequestHandler, AbstractExceptionHandler,
    AbstractRequestInterceptor, AbstractResponseInterceptor)
from ask_sdk_core.utils import is_request_type, is_intent_name, viewport
from ask_sdk_core.response_helper import get_plain_text_content #new
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model.ui import SimpleCard
from ask_sdk_model.ui import StandardCard
from ask_sdk_model import Response
from ask_sdk_model.interfaces.display import (ImageInstance, Image, RenderTemplateDirective, BackButtonBehavior, BodyTemplate1, BodyTemplate2) #new
from ask_sdk_model import ui # new

from ask_sdk_core.utils import get_supported_interfaces #new

from ask_sdk_model.interfaces.alexa.presentation.apl import (
    RenderDocumentDirective, ExecuteCommandsDirective, SpeakItemCommand,
    AutoPageCommand, HighlightMode)
from typing import Dict, Any

import data
#import questions
#from questions import *

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
#===========================================================================================================================

"""Receives APL for UI- Dalton
Load the apl json document at the path into a dict object."""
def _load_apl_document(file_path):
    # type: (str) -> Dict[str, Any]
    with open(file_path) as f:
        return json.load(f)

"""Handler for Skill Launch"""
#class LaunchRequestHandler(AbstractRequestHandler):
    #Decides if it's a Launch Request or not
    #If it is, it proceeds with the code in this class
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("LaunchRequest")(handler_input)
        
    def handle(self, handler_input):
        #*********DO NOT COMMENT OUT INSIDE RenderDocumentDirective************
        response_builder = handler_input.response_builder
        response_builder.set_card(
                ui.StandardCard(
                    title = "Welcome to Learn Stem!",
                    text= data.WELCOME_MESSAGE,
                    image = ui.Image(
                        small_image_url="https://upload.wikimedia.org/wikipedia/en/1/17/Stetson_Hatters_logo_%282018%29.png?download",
                        large_image_url="https://upload.wikimedia.org/wikipedia/en/1/17/Stetson_Hatters_logo_%282018%29.png?download"
                    )))
        if get_supported_interfaces(handler_input).alexa_presentation_apl is not None:
            response_builder.add_directive(
                RenderDocumentDirective(
                    token="learnSTEMToken",
                    document=_load_apl_document("./template.json")
                )
            )
        return response_builder.speak(data.WELCOME_MESSAGE).ask(data.SUBJECT_SPECIFICATION).response

def askQuestion(question_type, grade_level):
    methodName =  question_type + grade_level
    possibles = globals().copy()
    possibles.update(locals())
    method = possibles.get(methodName)
    return method()

def math5th():
    newq = random.choice(data.MATH_FIFTH_LIST)
    while data.LAST_QUESTION_ASKED == newq:
        newq = random.choice(data.MATH_FIFTH_LIST)
    return newq

def math4th():
    newq = random.choice(data.MATH_FOURTH_LIST)
    while data.LAST_QUESTION_ASKED == newq:
        newq = random.choice(data.MATH_FOURTH_LIST)
    return newq

def math3rd():
    newq = random.choice(data.MATH_THIRD_LIST)
    while data.LAST_QUESTION_ASKED == newq:
        newq = random.choice(data.MATH_THIRD_LIST)
    return newq

def mathsecond():
    newq = random.choice(data.MATH_SECOND_LIST)
    while data.LAST_QUESTION_ASKED == newq:
        newq = random.choice(data.MATH_SECOND_LIST)
    return newq

def math1st():
    newq = random.choice(data.MATH_FIRST_LIST)
    while data.LAST_QUESTION_ASKED == newq:
        newq = random.choice(data.MATH_FIRST_LIST)
    return newq

def coding5th():
    newq = random.choice(data.CODING_FIFTH_LIST)
    while data.LAST_QUESTION_ASKED == newq:
        newq = random.choice(data.CODING_FIFTH_LIST)
    return newq

def coding4th():
    newq = random.choice(data.CODING_FOURTH_LIST)
    while data.LAST_QUESTION_ASKED == newq:
        newq = random.choice(data.CODING_FOURTH_LIST)
    return newq

def coding3rd():
    newq = random.choice(data.CODING_THIRD_LIST)
    while data.LAST_QUESTION_ASKED == newq:
        newq = random.choice(data.CODING_THIRD_LIST)
    return newq

def codingsecond():
    newq = random.choice(data.CODING_SECOND_LIST)
    while data.LAST_QUESTION_ASKED == newq:
        newq = random.choice(data.CODING_SECOND_LIST)
    return newq

def coding1st():
    newq = random.choice(data.CODING_FIRST_LIST)
    while data.LAST_QUESTION_ASKED == newq:
        newq = random.choice(data.CODING_FIRST_LIST)
    return newq

"""Handler for what type of STEM question."""
class CaptureQuestionTypeIntentHandler(AbstractRequestHandler):
    #Decides if it's prompting for a question or not
    #If it is, it proceeds with the code in this class
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CaptureQuestionTypeIntent")(handler_input)
        
    #Determines values of each slot, question type and grade level, based on user indication
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        QType = slots["QType"].value
        GLevel = slots["GLevel"].value
        
        questionanswer_attributes = {
            "global_answer": data.GLOBAL_NULL,
            "global_question": data.GLOBAL_NULL,
            "last_question_asked": data.GLOBAL_NULL,
            "global_GLevel": data.GLOBAL_NULL,
            "global_QType": data.GLOBAL_NULL
        }
        
        #Calls askQuestion method, which pulls question and answer pair based on topic & grade
        #Result returned is split at the colon into a question and an answer
        #The split question and answer strings are stored in an array, qa_array
        qa_array = askQuestion(QType, GLevel).split(':')
        #Question and Answer are at spots 0 & 1, respectively, in the qa_array
        question_string = qa_array[0]
        question_answer = qa_array[1]
        #constants from data.py are overwritten by the new strings
        data.GLOBAL_ANSWER = question_answer
        data.GLOBAL_QUESTION = question_string
        data.LAST_QUESTION_ASKED = question_string + ":" + question_answer
        data.GLOBAL_GLEVEL = GLevel
        data.GLOBAL_QTYPE = QType
        attributes_manager = handler_input.attributes_manager
        
        #makes a persistent copy of important data
        #Testing for user re-asking questions - Dalton
        questionanswer_attributes = {
            "global_answer": data.GLOBAL_ANSWER,
            "global_question": data.GLOBAL_QUESTION,
            "last_question_asked": data.LAST_QUESTION_ASKED,
            "global_GLevel": data.GLOBAL_GLEVEL,
            "global_QType": data.GLOBAL_QTYPE
        }
        attributes_manager.persistent_attributes = questionanswer_attributes
        attributes_manager.save_persistent_attributes()
        #speaks the question
        #listens for the answer- if it's invalid and can't go on to the next method (e.g. doesn't include "what is")
        #the ANSWER_CLARIFICATION_REQUEST is asked
        
        questiontypedisplay = "placeholder string"
        if (data.GLOBAL_QTYPE) == "math":
            questiontypedisplay = "Math"
        else:
            questiontypedisplay = "Coding"
        
        response_builder = handler_input.response_builder
        response_builder.set_card(
                ui.StandardCard(
                    title = questiontypedisplay + " Question for " + data.GLOBAL_GLEVEL + " Grade",
                    text= data.GLOBAL_QUESTION,
                    image = ui.Image(
                        small_image_url="https://upload.wikimedia.org/wikipedia/en/1/17/Stetson_Hatters_logo_%282018%29.png?download",
                        large_image_url="https://upload.wikimedia.org/wikipedia/en/1/17/Stetson_Hatters_logo_%282018%29.png?download"
                    )))
        return handler_input.response_builder.speak(question_string).ask(data.ANSWER_CLARIFICATION_REQUEST).response

"""For repeating same question again - Dalton"""
class RepeatQIntentHandler(AbstractRequestHandler): 
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("RepeatQIntent")(handler_input)
        
    def handle(self, handler_input):
        slots = handler_input.request_envelope.request.intent.slots
        attr = handler_input.attributes_manager.persistent_attributes
        data.GLOBAL_QUESTION = attr['global_question']
        
        return handler_input.response_builder.speak(data.GLOBAL_QUESTION).ask(data.ANSWER_CLARIFICATION_REQUEST).response

class GetAnswerIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("GetAnswerIntent")(handler_input)
    
    def handle(self, handler_input):
        slots = handler_input.request_envelope.request.intent.slots
        attr = handler_input.attributes_manager.persistent_attributes
        data.GLOBAL_ANSWER = attr['global_answer']
        rightanswerstring = "The right answer is " + data.GLOBAL_ANSWER
        
        response_builder = handler_input.response_builder
        response_builder.set_card(
                ui.StandardCard(
                    title = "Correct Answer",
                    text= rightanswerstring,
                    image = ui.Image(
                        small_image_url="https://upload.wikimedia.org/wikipedia/en/1/17/Stetson_Hatters_logo_%282018%29.png?download",
                        large_image_url="https://upload.wikimedia.org/wikipedia/en/1/17/Stetson_Hatters_logo_%282018%29.png?download"
                    )))
        
        return response_builder.speak(rightanswerstring).ask(data.GLOBAL_ANSWER).response

"""This class is only called if the user input, answering a question, is valid
Handles Answers- determines if they're correct or not"""
class CaptureUserAnswerIntent(AbstractRequestHandler):
    #Decides if it's a Answer Intent or not
    #If it is, it proceeds with the code in this class
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("CaptureUserAnswerIntent")(handler_input)
    
    #compares user-given answer and correct answer
    def handle(self, handler_input):
        slots = handler_input.request_envelope.request.intent.slots
        #User-given answer
        Answer = slots["Answer"].value
        attr = handler_input.attributes_manager.persistent_attributes
        #Correct answer
        data.GLOBAL_ANSWER = attr['global_answer']
        #want to add in:
            #hints
            #limited number of attempts
        #add missing phrasing response?
        
        response_builder = handler_input.response_builder
        #if the user-given answer contains the correct answer, give the correct answer response
        if Answer.find(data.GLOBAL_ANSWER) == 0:
            response_builder.set_card(
                ui.StandardCard(
                    title = "Correct!",
                    text= data.CORRECT_ANSWER_RESPONSE + " The answer is " + data.GLOBAL_ANSWER + ".",
                    image = ui.Image(
                        small_image_url="https://upload.wikimedia.org/wikipedia/en/1/17/Stetson_Hatters_logo_%282018%29.png?download",
                        large_image_url="https://upload.wikimedia.org/wikipedia/en/1/17/Stetson_Hatters_logo_%282018%29.png?download"
                    )))
            return response_builder.speak(data.CORRECT_ANSWER_RESPONSE).response
        #if the user-given answer contains the incorrect answer, give the incorrect answer response
        elif Answer.find(data.GLOBAL_ANSWER) != 0:
            response_builder.set_card(
                ui.StandardCard(
                    title = "Incorrect Answer",
                    text= data.WRONG_ANSWER_RESPONSE,
                    image = ui.Image(
                        small_image_url="https://upload.wikimedia.org/wikipedia/en/1/17/Stetson_Hatters_logo_%282018%29.png?download",
                        large_image_url="https://upload.wikimedia.org/wikipedia/en/1/17/Stetson_Hatters_logo_%282018%29.png?download"
                    )))
            return response_builder.speak(data.WRONG_ANSWER_RESPONSE).response

"""Offers a guide for users"""
class HelpIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        #speaks help message and listens for a response to navigate to different spot in the program
        response_builder = handler_input.response_builder
        response_builder.set_card(
                ui.StandardCard(
                    title = "Help",
                    text= data.HELP_MESSAGE,
                    image = ui.Image(
                        small_image_url="https://upload.wikimedia.org/wikipedia/en/1/17/Stetson_Hatters_logo_%282018%29.png?download",
                        large_image_url="https://upload.wikimedia.org/wikipedia/en/1/17/Stetson_Hatters_logo_%282018%29.png?download"
                    )))
        return handler_input.response_builder.speak(data.HELP_MESSAGE).ask(data.HELP_MESSAGE).response

"""Exits program"""
class CancelOrStopIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        response_builder.set_card(
                ui.StandardCard(
                    title = "See you next time!",
                    text= data.STOP_CANCEL_OUTPUT,
                    image = ui.Image(
                        small_image_url="https://upload.wikimedia.org/wikipedia/en/1/17/Stetson_Hatters_logo_%282018%29.png?download",
                        large_image_url="https://upload.wikimedia.org/wikipedia/en/1/17/Stetson_Hatters_logo_%282018%29.png?download"
                    )))
        return handler_input.response_builder.speak(data.STOP_CANCEL_OUTPUT).response

"""Handler for Session End"""
class SessionEndedRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # Any cleanup logic goes here.
        return handler_input.response_builder.response #///

"""The intent reflector is used for interaction model testing and debugging. It will simply repeat the intent the user said. You can create custom handlers
for your intents by defining them above, then also adding them to the request handler chain below."""
class IntentReflectorHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return handler_input.response_builder.speak(speak_output).response
                # .ask("add a reprompt if you want to keep the session open for the user to respond")

"""Generic error handling to capture any syntax or routing errors. If you receive an error stating the request handler chain is 
not found, you have not implemented a handler for the intent being invoked or included it in the skill builder below."""
class CatchAllExceptionHandler(AbstractExceptionHandler):
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)
        return handler_input.response_builder.speak(data.ISSUE_MESSAGE).ask(data.ISSUE_MESSAGE).response

#Processed top to bottom

sb = CustomSkillBuilder(persistence_adapter=s3_adapter)#SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(CaptureQuestionTypeIntentHandler())
sb.add_request_handler(RepeatQIntentHandler())
sb.add_request_handler(GetAnswerIntentHandler())
sb.add_request_handler(CaptureUserAnswerIntent())
#sb.add_request_handler(CaptureGradeLevelIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
