from functools import partial


choices = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
]


# def format_cot_example(example, including_answer=True):
#     prompt = "Question:\n"
#     question = example["question"]
#     options = example["options"]
#     prompt += question + "\n"
#     prompt += "Options:\n"
#     for i, opt in enumerate(options):
#         prompt += "{}. {}\n".format(choices[i], opt)
#     if including_answer:
#         cot_content = example["cot_content"].replace(
#             "A: Let's think step by step.", "Answer: Let's think step by step."
#         )
#         prompt += cot_content + "\n\n"
#     else:
#         prompt += "Answer: Let's think step by step."
#     return prompt

def format_cot_example(example, including_answer=True):
    options = ""
    for i, opt in enumerate(example['options']):
        options += "{}. {}\n".format(choices[i], opt)

    prompt = f"""A conversation between User and Assistant. The user asks a question, and the Assistant solves it. The assistant first thinks about the reasoning process in the mind and then provides the user with the answer. The reasoning process and answer are enclosed within <think> </think> and <answer> </answer> tags, respectively, i.e., <think> reasoning process here </think><answer> answer here </answer>. 
        User: You must put your answer inside <answer> </answer> tags, i.e.,<answer> answer here </answer>. And your final answer will be extracted automatically by the \\boxed{{}} tag.
        {example['question']}
        Options:
        {options}

        Assistant: <think>""",
    
    return prompt
    # prompt = "Question:\n"
    # question = example["question"]
    # options = example["options"]
    # prompt += question + "\n"
    # prompt += "Options:\n"
    # for i, opt in enumerate(options):
    #     prompt += "{}. {}\n".format(choices[i], opt)
    # if including_answer:
    #     cot_content = example["cot_content"].replace(
    #         "A: Let's think step by step.", "Answer: Let's think step by step."
    #     )
    #     prompt += cot_content + "\n\n"
    # else:
    #     prompt += "Answer: Let's think step by step."
    # return prompt


doc_to_text = partial(format_cot_example, including_answer=False)
fewshot_to_text = partial(format_cot_example, including_answer=True)


def process_docs(dataset, subject):
    return dataset.filter(lambda x: x["category"] == subject)


process_biology = partial(process_docs, subject="biology")
process_business = partial(process_docs, subject="business")
process_chemistry = partial(process_docs, subject="chemistry")
process_computer_science = partial(process_docs, subject="computer science")
process_economics = partial(process_docs, subject="economics")
process_engineering = partial(process_docs, subject="engineering")
process_health = partial(process_docs, subject="health")
process_history = partial(process_docs, subject="history")
process_law = partial(process_docs, subject="law")
process_math = partial(process_docs, subject="math")
process_other = partial(process_docs, subject="other")
process_philosophy = partial(process_docs, subject="philosophy")
process_physics = partial(process_docs, subject="physics")
process_psychology = partial(process_docs, subject="psychology")
