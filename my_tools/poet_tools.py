from agents import function_tool
import json
from my_schema.blue_print import PoemSchema


@function_tool
def verses(lines:int):
    """
    Helps to generate a poem with the specified number of lines.
    
    Args:
        lines (int): The number of lines in the poem.
        
    Returns:
        str: A poem with the specified number of lines.


    This will be used when user ask how many lines following poem have.
    """
    return f"This poem has {lines} lines."



@function_tool
def save_poem_data(poem: str, title: str, summary: str):
    """
    Saves the poem with the given title and summary.
    
    Args:
        poem (str): The content of the poem.
        title (str): The title of the poem.
        summary (str): A short summary of the poem.
        
    Returns:
        str: Confirmation message that the poem has been saved.
    """
  
    saved_data:PoemSchema = {
           "title": title,
           "content": poem,
           "short_summary": summary
    }

    file_path = f"Saved_files/{title}.json"
    with open(file_path, "w") as file:
                json.dump(saved_data,file)

    

    return f"Poem titled '{title}' has been saved."






