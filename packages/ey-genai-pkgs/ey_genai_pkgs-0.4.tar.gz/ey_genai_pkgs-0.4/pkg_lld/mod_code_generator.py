from dotenv import load_dotenv
# from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate
# from langchain.chat_models import AzureChatOpenAI
from langchain_community.chat_models import AzureChatOpenAI
from langchain_community.llms import AzureOpenAI
from flask import Flask, request, jsonify
# from docx import Document
# from principle.BRD_Main.format_prompt import *
# from principle.BRD_Main.substitute import *

def create_code_val(use_case):
    system_template = '''
    I will be providing you with a task to generate code that validates email IDs and passwords.
    
    Task:
    Generate code that includes functions to validate email IDs and passwords. The code should pass the provided public tests.

    Prompt template: "Write a function `validateEmail` that takes an email ID as input and returns True if it's valid, otherwise False. Also, write a function `validatePassword` that takes a password as input and returns True if it's valid, otherwise False."

    Note: Each prompt should be different from the one generated before.
    
    
    {use_case}

    '''
    system_message_prompt = SystemMessagePromptTemplate.from_template(
        system_template)

    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt])
    formatted_chat_prompt = chat_prompt.format_messages(use_case=use_case)

    return formatted_chat_prompt


class ValidationResult:
    def __init__(self, passed, error_message):
        self.passed = passed
        self.error_message = error_message

def iterate_on_public_tests(code, public_tests):
    # Run the code on public tests and fix any failures
    for test in public_tests:
        result = run_code(code, test)
        if not result.passed:
            # Fix the code based on the error message
            code = fix_code(code, result.error_message)
    return code

def run_code(code_response, test):
    # Simulate running the code on a test and return the result
    # This is a placeholder and should be replaced with actual code execution logic
    try:
        # Simulate running the code on a test and return the result
        # This is a placeholder and should be replaced with actual code execution logic
        # exec_globals = {}
        # exec(code_response, exec_globals)
        # result = exec_globals['validate_email'](test)  # Assuming validate_email is the email validation function
        # return ValidationResult(passed=result, error_message=None)

        exec_globals = {}
        exec(code_response, exec_globals)
        validate_email = exec_globals.get('validateEmail')
        validate_password = exec_globals.get('validatePassword')
        result_email = validate_email(test[0]) if validate_email else False
        result_password = validate_password(test[1]) if validate_password else False
        return ValidationResult(passed=result_email and result_password, error_message=None)   
    except SyntaxError as syntax_error:
        return ValidationResult(passed=False, error_message=f"Syntax error in code: {str(syntax_error)}") 
    except Exception as e:
        # If an exception occurs during code execution, consider it a failure
        return ValidationResult(passed=False, error_message=f"Error running code: {str(e)}")   

def fix_code(code_response, error_message):
    # Simplified version: add a simple fix based on the error message
    # In practice, this might involve more complex logic

  fixed_code = f'''
try:
    {code_response}
except Exception as e:
    print("Validation failed:", str(e))
    result = False
'''
    # return fixed_code

    # return code + "\n# Fix: " + error_message

  return f'{fixed_code}\n# Error: {error_message}'



def create_chat_prompt(use_case):
    # Create a system message that sets the AI's role and purpose
    system_template = f'''
    I will be providing you with a LLD document which has number of use cases and for each use case review each one by one
    and provide me with a prompt for each use case with this prompt template -
    
    Prompt template-"Generate microservice code for the below use case.
    The microservice code should be based on necessary spring boot framework with Controller, Service, Entity, Repository etc. as needed.
    Additionally also generate the respective unit test cases using JUnit and Mockito wiremock"

    Generate the prompt based on this structure for each use case-

    ###Prompt(1):###
    ``prompt template:``
    ``Use Case(1):``
    ``Actions:``
    
    ###Prompt(2):###
    ``prompt template:``
    ``Use Case(1):``
    ``Actions:``
    
    ...
    
   
    Note: Each prompt should be different from the one that is generated before.
    {use_case}'''

    system_message_prompt = SystemMessagePromptTemplate.from_template(
        system_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt])
    formatted_chat_prompt = chat_prompt.format_messages(use_case=use_case)

    return formatted_chat_prompt

# def create_use_case(BRD_Document_Content):
#      # Create a system message that sets the AI's role and purpose
#     system_template = f'''Consider yourself as an expert in prompt engineering.
#     I will be providing you with a document of user requirements to build the whole application with some 
#     microservice which is nothing but a BRD(Business Requirement Document), so review the whole content and based on the your analysis provide 
#     me Use Cases with its detailed description and action in this format-

#     ###Use Case:###
#     ###Description:###
#     ###Action:###

#     Note: Each Use Case should be different from the one that is generated before. 
#     {BRD_Document_Content}'''
#     system_message_prompt = SystemMessagePromptTemplate.from_template(
#         system_template)

#     # Create a user message with the user's requirements
#     # user_template = f'''Generate prompt in this format for the BRD doc:\n{BRD_Document_Content}
#     # The code should be generate in this way:
#     # ---PROMPT---
#     # THE PROMPT SHOULD BE GENERATED HERE
   
#     # ---DESCRIPTION---
#     # THE DESCRIPTION FOR EACH PROMPT SHOULD BE GENERATED HERE
#     # '''
#     # user_message_prompt = AIMessagePromptTemplate.from_template(user_template)

#     # Combine system and user messages in a chat prompt
#     chat_prompt = ChatPromptTemplate.from_messages(
#         [system_message_prompt])
#     formatted_chat_prompt = chat_prompt.format_messages()

#     return formatted_chat_prompt

def create_code(use_case):
     # Create a system message that sets the AI's role and purpose
    system_template = f'''Consider yourself as an expert in generating microservice spring-boot code-base.
    I will be providing you with some number of Prompts which includes 'prompt template,Use Case and Actions'.
    Process each and every prompt seperately and generate microservice spring-boot code-base based on the prompt for each and every use case seperatly.

    Note: Each use case should be different to generate code base from the one that is generated before.
    {use_case}'''

    system_message_prompt = SystemMessagePromptTemplate.from_template(
        system_template)
    
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt])
    formatted_chat_prompt = chat_prompt.format_messages()

    return formatted_chat_prompt

# def invoke_openai_chat_model(formatted_chat_prompt):
#     # chat_model = ChatOpenAI(
#     #     model_name="gpt-4",
#     #     temperature=0,
#         # max_tokens=1000
    
#     # )
#     azurechat= AzureChatOpenAI(model_name="text-davinci-003", deployment_name="gpt-4", temperature=0.7, max_tokens=1500)

#     response = azurechat(messages=formatted_chat_prompt)
#     return response.content

def invoke_openai_prompt(formatted_chat_prompt):
    # chat_model = ChatOpenAI(
    #     model_name="gpt-4",
    #     temperature=0,
        # max_tokens=1000
    
    # )
    azurechat= AzureChatOpenAI(model_name="text-davinci-003", deployment_name="gpt-4", temperature=0.7, max_tokens=2500)

    response = azurechat(messages=formatted_chat_prompt)
    return response.content

def invoke_openai_code_gen(formatted_chat_prompt):
    # chat_model = ChatOpenAI(
    #     model_name="gpt-4",
    #     temperature=0,
        # max_tokens=1000
    
    # )
    azurechat= AzureChatOpenAI(model_name="text-davinci-003", deployment_name="gpt-4", temperature=0.7, max_tokens=2500)

    response = azurechat(messages=formatted_chat_prompt)
    return response.content
    # generated_codes = []
    # for prompt in formatted_chat_prompt:
    #     response = azurechat(messages=prompt)
    #     generated_codes.append(response.content)
# 
    # return generated_codes

def invoke_openai_code_val(formatted_chat_prompt):
    # chat_model = ChatOpenAI(
    #     model_name="gpt-4",
    #     temperature=0,
        # max_tokens=1000
    
    # )
    azurechat= AzureChatOpenAI(model_name="text-davinci-003", deployment_name="gpt-4", temperature=0.7, max_tokens=2500)

    response = azurechat(messages=formatted_chat_prompt)
    return response.content