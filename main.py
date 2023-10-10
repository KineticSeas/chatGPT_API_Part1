from fastapi import FastAPI, HTTPException
import openai

app = FastAPI()

#  Notes - End of Step 1 (Setup)
#  Download Python:     https://www.python.org/downloads/
#     -- Note:  Check version in terminal with >python3 --version
#  Download PyCharm:    https://www.jetbrains.com/pycharm/download/
#     -- Note:  You can use the free community edition with no problems.
#     -- Note:  I had problems with Python 3.12 with FastAPI, so I used Python 3.11.
#  Get OpenAI API Key:  https://platform.openai.com/account/api-keys
#  API Reference:  https://platform.openai.com/docs/api-reference/introduction


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/chat/")
async def chat():
    # Configure the OpenAI library with your API key
    # Create a file on your filesystem with the openai key.
    openai.api_key = open("/Users/user/openapi_key.txt", "r").read().strip('\n')

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Answer the question from the perspective of a chemical engineer"},
                {"role": "user", "content": "What is the moon made of?"},
                {"role": "assistant", "content": "The moon is primarily composed of rocks and minerals. The surface "
                                                 "of the moon is covered with a layer called regolith, which is "
                                                 "composed of fine dust, rocks, and boulders. The primary rock "
                                                 "type found on the moon is basalt, which is formed from solidified "
                                                 "lava. Additionally, there are traces of other elements and minerals "
                                                 "such as aluminum, calcium, potassium, iron, and magnesium. The moon "
                                                 "also has limited amounts of water ice in permanently shadowed regions"
                                                 " near its poles. Overall, the moon's composition is similar to the "
                                                 "Earth's crust, but with some variations."},
                {"role": "user", "content": "What minerals are there?"}
            ],
            max_tokens=300
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing POST data: {str(e)}")

    return {"response": completion}
