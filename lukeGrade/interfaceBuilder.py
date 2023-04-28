import streamlit as stl


def IB_HeadingsViewer():
    stl.title(":blue[Turing Checker Machine]")


def IB_Languages_Radio():
    languages = ['python', 'c', 'cpp', 'cshtml', 'css', 'javascript', 'csharp', 'java']
    language_choice = stl.radio("**:green[Choose your language]**", (languages), horizontal=True)
    return language_choice


def IB_AutoTestCases() -> bool:
    checkBox = stl.checkbox("Check with random test cases")
    return checkBox


def IB_LanguageModelQuery(language: str, code: str, testCase: bool = None) -> str:
    # print(f"Language : {language}")
    # print(f"Code : {code}")
    # print(f"TestCases : {testCase}")

    if testCase:
        return \
            f"""
        Hey, I will send you my {language} code and test cases. Test my code with those test cases 
        and check how many test cases it passed and how many it failed. My code is,
        {code}
        
        My test cases are {testCase}.
        
        Just give me the output in a nicely formatted list form.And don't give anything else,
        Example test case,
        Test Case 1: n = some value
        Expected Output: "Correct" or "Incorrect"
        Result: Passed or Failed
        """
    else:
        return \
            f"""
        Hey, I will send you my {language} code. Analyse the code and test the code with multiple test cases
        of your choice and check how many test cases it passed and how many it failed. 
        My code is,
        {code}

        Total test cases is 5
        Test the code with 5 different inputs of your choice and give me how many it passed and how many it failed
        Choose 5 random test cases inputs, based on the code.

        Just give me the output in a nicely formatted list form.And don't give anything else,
        Example test case,
        Test Case 1: n = some value
        Expected Output: "Correct" or "Incorrect"
        Result: Passed or Failed
        """



