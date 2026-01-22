from pixie.prompts import PromptVariables, create_prompt


simple_prompt = create_prompt(
    "simple_prompt", description="A simple prompt with no variables."
)


class Person(PromptVariables):
    name: str
    age: int


typed_prompt = create_prompt(
    "typed_prompt",
    Person,
    description="A typed prompt with specific variables.",
)


class Contact(PromptVariables):
    email: str
    phone: str
    person: Person


nested_typed_prompt = create_prompt(
    "nested_typed_prompt",
    Contact,
    description="A typed prompt with nested variable structures.",
)
