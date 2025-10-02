from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    
    input_variables=["joke_type", "language_type"],
    template="""
        You are a witty joke generator. You prefer to tell adult joke with pun. 

        Generate a {joke_type} joke in {language_type}.

        Make sure the joke is short, funny, and hilarious,sarcastic.
        """
        )


template.save('template.json')