import openai
openai.api_key = "xxxxxx" # TODO replace to the real api key

class Model:
    def __init__(self):
        self.accumulated_content = ""

    async def _process_line(self, line):
        try:
            content = line['choices'][0]['delta']['content']
            self.accumulated_content += content
        except:
            pass

    # TODO replace openai to g4f
    async def ChatCompletion(self, messages):
        self.payload["messages"] = messages

        results = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
            stream=True,
        )
        for result in results:
            await self._process_line(result)

        return self.accumulated_content
