import dspy
from typer import Typer

from dspygen.utils.dspy_tools import init_dspy

app = Typer()


class PromptPep8PythonSourceCodeModule(dspy.Module):
    """Verbose Documentation for the DSPy Module"""

    def forward(self, prompt):
        pred = dspy.ChainOfThought("prompt -> pep8_python_source_code")
        result = pred(prompt=prompt).pep8_python_source_code
        return result


def python_source_code_call(prompt):
    prompt_pep8_python_source_code = PromptPep8PythonSourceCodeModule()
    return prompt_pep8_python_source_code.forward(prompt=prompt)


@app.command(name="call")
def module_test(prompt):
    """Verbose Documentation for the DSPy Module"""
    init_dspy()

    print(python_source_code_call(prompt=prompt))


def main():
    init_dspy()

    prompt = "Hello World def with print FastAPI call with import"
    print(python_source_code_call(prompt=prompt))


if __name__ == "__main__":
    main()
