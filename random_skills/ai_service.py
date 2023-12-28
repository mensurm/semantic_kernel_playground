import os
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import (
    OpenAITextCompletion,
)
from semantic_kernel.orchestration.context_variables import ContextVariables


class AIService:
    """
    This class encapsulates AI functions that are defined
    in the skills directory
    """

    def __init__(self):
        # initialize semantic kernel
        self.kernel = sk.Kernel()
        api_key, org_id = sk.openai_settings_from_dot_env()
        self.kernel.add_text_completion_service(
            "dv", OpenAITextCompletion("text-davinci-003", api_key, org_id)
        )

        # add skills
        self.skills_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'skills'))

        self.random_facts_skill = self.kernel.import_semantic_skill_from_directory(
            self.skills_directory, "RandomFacts"
        )
        self.fun_skills = self.kernel.import_semantic_skill_from_directory(self.skills_directory, "FunSkills")

        self.__init_skill_functions()

    def __init_skill_functions(self):
        self.random_country_facts = self.random_facts_skill["CountryRandomFact"]
        self.jokes = self.fun_skills["Joke"]

    def get_random_fact_about_a_country(self, country: str):
        """
        Generate a random fact for a country given as input
        Args:
            country: Name of a country

        Returns:

        """

        context_variables = ContextVariables(
            content=country
        )
        result = self.random_country_facts(variables=context_variables)

        # You can also invoke functions like this
        # result = await jokeFunction.invoke_async("time travel to dinosaur age")
        return str(result)

    def make_a_joke(self, topic: str):
        """
        Make a joke for a topic given as input
        Args:
            topic: Topic that should be the target of the joke

        Returns: A joke

        """
        context_variables = ContextVariables(
            content=topic
        )
        result = self.jokes(variables=context_variables)
        return str(result)
