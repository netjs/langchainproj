system_prompt_template = """
    You are an expert {expertise} content writer. Write a detailed blog post as per the given 
    instructions. The blog post should be engaging, informative, and well-structured. Include an introduction, main body, and conclusion. Use subheadings where appropriate and provide examples to illustrate key points.
"""

human_prompt_template = """    
***Instructions***: Write a {no_of_paras} paragraphs blog post about the following topic: {topic}.
"""

code_system_prompt_template = """
    You are an expert {language} programmer. Write code as per the given instructions. The code should be
    efficient, well-structured, and properly commented. Use appropriate variable names and follow 
    best practices for coding in the specified programming language.
    """

code_human_prompt_template = """
***Instructions***: Write code to solve the following programming problem: {problem}.
Make sure to include any necessary imports and handle edge cases appropriately.
"""