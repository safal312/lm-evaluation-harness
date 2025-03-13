from functools import partial
from typing import Dict, List, Optional

try:
    from math_verify import parse, verify
except (ModuleNotFoundError, AssertionError) as e:
    raise type(e)(
        "`sympy`, `math_verify` and `antlr4-python3-runtime==4.11` are required for generating translation task prompt templates. "
        "Please install the required packages via pip install lm-eval[math] or pip install -e .[math]"
    ) from e


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


def format_cot_example(example, including_answer=True):
    prompt = "Question:\n"
    question = example["question"]
    options = example["options"]
    prompt += question + "\n"
    prompt += "Options:\n"
    for i, opt in enumerate(options):
        prompt += "{}. {}\n".format(choices[i], opt)
    if including_answer:
        cot_content = example["cot_content"].replace(
            "A: Let's think step by step.", "Answer: Let's think step by step."
        )
        prompt += cot_content + "\n\n"
    else:
        prompt += "Answer: Let's think step by step."
    return prompt

# def format_cot_example(example, including_answer=True):
#     options = ""
#     for i, opt in enumerate(example['options']):
#         options += "{}. {}\n".format(choices[i], opt)

#     prompt = f"""A conversation between User and Assistant. The user asks a question, and the Assistant solves it. The assistant first thinks about the reasoning process in the mind and then provides the user with the answer. The reasoning process and answer are enclosed within <think> </think> and <answer> </answer> tags, respectively, i.e., <think> reasoning process here </think><answer> answer here </answer>. 
#         User: You must put your answer inside <answer> </answer> tags, i.e.,<answer> answer here </answer>. And your final answer will be extracted automatically by the \\boxed{{}} tag.
#         {example['question']}
#         Options:
#         {options}
#         Assistant: <think>"""
    
#     return prompt
#     # prompt = "Question:\n"
#     # question = example["question"]
#     # options = example["options"]
#     # prompt += question + "\n"
#     # prompt += "Options:\n"
#     # for i, opt in enumerate(options):
#     #     prompt += "{}. {}\n".format(choices[i], opt)
#     # if including_answer:
#     #     cot_content = example["cot_content"].replace(
#     #         "A: Let's think step by step.", "Answer: Let's think step by step."
#     #     )
#     #     prompt += cot_content + "\n\n"
#     # else:
#     #     prompt += "Answer: Let's think step by step."
#     # return prompt

def process_results(doc: dict, results: List[str]) -> Dict[str, int]:
    candidates = results[0]

    # math_verify
    res = verify(parse(doc["response"].split('The answer is: ')[-1].strip()), parse(candidates))
    mathval = 1 if res else 0

    results = {
        "math_verify": mathval,
    }
    return results


doc_to_text = partial(format_cot_example, including_answer=False)
fewshot_to_text = partial(format_cot_example, including_answer=True)


def process_docs(dataset, type):
    return dataset.filter(lambda x: x["type"] == type)


process_gr = partial(process_docs, type="GSM_Rephrased")
process_gaa = partial(process_docs, type="GSM_AnsAug")
process_maa = partial(process_docs, type="MATH_AnsAug")
process_mr = partial(process_docs, type="MATH_Rephrased")
process_gfb = partial(process_docs, type="GSM_FOBAR")
process_gsv = partial(process_docs, type="GSM_SV")
process_msv = partial(process_docs, type="MATH_SV")
process_mfb = partial(process_docs, type="MATH_FOBAR")